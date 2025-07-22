import os
import uuid
import requests
import json
import random
import re
from pydub import AudioSegment
import gradio as gr
import speech_recognition as sr

def log_step(msg):
    print(f"[EVAL_SPOKEN] {msg}")

def convert_to_wav(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.join("uploads", f"converted_{uuid.uuid4()}.wav")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    log_step(f"Converting audio from {input_path} to WAV format")
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        log_step(f"Audio successfully converted to {output_path}")
        return output_path
    except Exception as e:
        error_msg = f"Failed to convert audio: {e}"
        log_step(f"ERROR in audio conversion: {error_msg}")
        raise RuntimeError(error_msg)

def img_detector(model, url):
    api_keys = [
        os.getenv("OPENROUTER_API_KEY_1"),
        os.getenv("OPENROUTER_API_KEY_2"),
        os.getenv("OPENROUTER_API_KEY_3"),
        os.getenv("OPENROUTER_API_KEY_4"),
    ]
    api_keys = [k for k in api_keys if k]
    errors = []
    for api_key in api_keys:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": model,
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "What is appear in this image? Please provide a detailed description."},
                                {"type": "image_url", "image_url": {"url": url}}
                            ]
                        }
                    ]
                })
            )
            if response.status_code == 200:
                data = response.json()
                if 'choices' in data and len(data['choices']) > 0:
                    return data['choices'][0]['message']['content']
                else:
                    errors.append(f"API key {api_key[:8]}...: No choices in response.")
            else:
                errors.append(f"API key {api_key[:8]}...: Status {response.status_code}")
        except Exception as e:
            errors.append(f"API key {api_key[:8]}...: Exception {e}")
    return f"All VLM API requests failed: {' | '.join(errors)}"

def transcribe_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

def evaluate_spoken_english(vlm_description, transcript_input, lang="english"):
    """
    Evaluate spoken English based on a VLM image description and a transcript.
    Returns a dict with feedback and scores.
    """
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    if not DEEPSEEK_API_KEY:
        raise EnvironmentError("Missing DEEPSEEK_API_KEY in environment.")

    prompt = f"""
      You are an expert spoken English tutor evaluating learners' spoken English skills based on CEFR (Common European Framework of Reference for Languages) standards. Your evaluation must consider key criteria such as:

      - Pronunciation and stress
      - Fluency and rhythm
      - Vocabulary range and appropriateness
      - Coherence and structure
      - Grammar (as inferred from the transcript)

      Important: The transcript below has **no punctuation**, as it is auto-generated from speech. Focus on what can be evaluated reliably based on the content and structure.

      The learner was shown the following image (described by a vision-language model):
      ---
      {vlm_description}
      ---

      Then the learner described the image by voice. This is the auto-generated transcript:
      ---
      {transcript_input}
      ---

      Please evaluate the learner’s spoken English and return a JSON response including:
      1. "relevance_score": Score out of 100 for how relevant the speech was to the image.
      2. "fluency_score": Score out of 100 for fluency and smoothness of speech.
      3. "pronunciation_feedback": Identify any pronunciation issues or common errors.
      4. "mistakes": A list of grammar or vocabulary issues inferred from the transcript.
      5. "corrected_transcript": A corrected version of the transcript with appropriate punctuation and grammar.
      6. "learning_level": Estimated CEFR level (A1–C2).
      7. "tips": Actionable learning advice tailored to the learner’s weaknesses.
      8. "highlight": Something strong or impressive in the learner’s speaking (e.g., good phrasing or word choice).
      9. "motivational_comment": A short, encouraging note to boost the learner’s confidence.

      Respond in clean JSON format only.
      """

    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a certified spoken English tutor helping learners improve pronunciation, fluency, and confidence. You follow CEFR guidelines and speak warmly to encourage learners."
                    },
                    {
                        "role": "user",
                        "content": prompt.strip()
                    }
                ],
                "temperature": random.uniform(0.9, 1),
                "max_tokens": 1500
            }
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"]["content"]
                clean_json_text = re.sub(r"```json|```", "", content).strip()

                try:
                    return json.loads(clean_json_text)
                except json.JSONDecodeError as decode_err:
                    return {
                        "relevance_score": 0,
                        "fluency_score": 0,
                        "pronunciation_feedback": "N/A",
                        "mistakes": [],
                        "corrected_transcript": "N/A",
                        "learning_level": "Unknown",
                        "highlight": "N/A",
                        "motivational_comment": "N/A",
                        "tips": [f"Invalid JSON format: {str(decode_err)}", "Raw content:", clean_json_text]
                    }
        else:
            return {
                "relevance_score": 0,
                "fluency_score": 0,
                "pronunciation_feedback": "N/A",
                "mistakes": [],
                "corrected_transcript": "N/A",
                "learning_level": "Unknown",
                "highlight": "N/A",
                "motivational_comment": "N/A",
                "tips": [f"API Error: {response.status_code}"]
            }

    except Exception as e:
        return {
            "relevance_score": 0,
            "fluency_score": 0,
            "pronunciation_feedback": "N/A",
            "mistakes": [],
            "corrected_transcript": "N/A",
            "learning_level": "Unknown",
            "highlight": "N/A",
            "motivational_comment": "N/A",
            "tips": [f"Exception occurred: {str(e)}"]
        }

def gradio_spoken_eval(image_url, audio_file, model="meta-llama/llama-3.2-11b-vision-instruct:free"):
    log_step(f"Received image_url={image_url}, audio_file={audio_file}")
    wav_path = convert_to_wav(audio_file)
    transcript = transcribe_audio(wav_path)
    log_step(f"Transcript: {transcript}")
    vlm_desc = img_detector(model, image_url)
    log_step(f"VLM Description: {vlm_desc}")
    result = evaluate_spoken_english(vlm_desc, transcript)
    return json.dumps(result, indent=2, ensure_ascii=False)

iface = gr.Interface(
    fn=gradio_spoken_eval,
    inputs=[
        gr.Textbox(label="Image URL"),
        gr.Audio(type="filepath", label="Audio File (any format)"),
        gr.Dropdown(choices=["meta-llama/llama-3.2-11b-vision-instruct:free", "google/gemini-2.0-flash-exp:free"], value="meta-llama/llama-3.2-11b-vision-instruct:free", label="Vision Model")
    ],
    outputs=gr.Code(label="Evaluation JSON", language="json"),
    title="Spoken English Evaluation",
    description="Upload an image URL and an audio file describing the image. The system will transcribe your speech, analyze it, and return a detailed evaluation."
)

if __name__ == "__main__":
    iface.launch()
