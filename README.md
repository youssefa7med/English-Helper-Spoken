# English Spoken Evaluation System 🗣️

![English Speaking](https://gifs.cackhanded.net/invader-zim/career-day/the-machine-has-spoken.gif)

An intelligent English speaking evaluation system that uses advanced AI vision models to analyze images and evaluate your spoken English descriptions based on CEFR standards. Get detailed feedback on pronunciation, fluency, vocabulary, and grammar through image description tasks.

## 🚀 Live Demo

**Try it now:** [English Helper Spoken - Live Demo](https://huggingface.co/spaces/YoussefA7med/English_Helper_Spoken)

Experience the full functionality of the English Spoken Evaluation System directly in your browser! No installation required.

## 🌟 Features

### 🖼️ **AI-Powered Image Analysis**
- Advanced Vision-Language Models (VLM) for detailed image description
- Support for Meta LLaMA 3.2 and Google Gemini 2.0 Flash models
- Comprehensive scene understanding and context analysis

### 🎙️ **Advanced Speech Recognition**
- Real-time audio recording and transcription
- Accurate speech-to-text conversion using Google Speech Recognition
- Support for various audio formats with automatic conversion

### 📊 **Comprehensive Speaking Assessment**
- **Relevance Score**: How well your description matches the image content
- **Fluency Score**: Evaluation of speech smoothness and rhythm
- **Pronunciation Feedback**: Identification of specific pronunciation issues
- **Grammar Analysis**: Detection of grammatical errors and improvements
- **CEFR Level Assessment**: Automatic proficiency level determination (A1-C2)

### 🎓 **Detailed Feedback System**
- **Corrected Transcript**: Your speech with proper grammar and punctuation
- **Mistake Analysis**: Specific vocabulary and grammar issues identified
- **Learning Tips**: Actionable advice tailored to your weaknesses
- **Strengths Highlighting**: Recognition of impressive phrases or word choices
- **Motivational Comments**: Encouraging feedback to boost confidence

### 🔄 **Multi-Model Support**
- **Meta LLaMA 3.2 11B Vision**: Advanced vision understanding
- **Google Gemini 2.0 Flash**: Fast and accurate image analysis
- **OpenRouter Integration**: Reliable API access with fallback support

## 🚀 Getting Started

### Try Online First
Before setting up locally, test the system using our **[Live Demo](https://huggingface.co/spaces/YoussefA7med/English_Helper_Spoken)** to see if it meets your needs!

### Prerequisites

Before running the application locally, ensure you have the following:

- Python 3.8 or higher
- Required Python packages (see [Installation](#installation))
- API keys for the required services
- Microphone access for audio recording

### Required API Keys

You'll need to obtain the following API keys:

1. **DeepSeek API Key**: For AI-powered evaluation and feedback
   - Sign up at [DeepSeek Platform](https://platform.deepseek.com/)

2. **OpenRouter API Keys**: For vision-language model access
   - Sign up at [OpenRouter](https://openrouter.ai/)
   - The system supports multiple API keys for reliability

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/youssefa7med/english-spoken-evaluation.git
   cd english-spoken-evaluation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   OPENROUTER_API_KEY_1=your_first_openrouter_key
   OPENROUTER_API_KEY_2=your_second_openrouter_key
   OPENROUTER_API_KEY_3=your_third_openrouter_key
   OPENROUTER_API_KEY_4=your_fourth_openrouter_key
   ```

4. **Run the application**
   ```bash
   python spoken_evaluation.py
   ```

5. **Access the interface**
   
   Open your browser and navigate to the URL displayed in the terminal (typically `http://localhost:7860`)

## 📋 Requirements

Create a `requirements.txt` file with the following dependencies:

```txt
gradio>=4.0.0
requests>=2.31.0
python-dotenv>=1.0.0
pydub>=0.25.1
SpeechRecognition>=3.10.0
PyAudio>=0.2.11
```

## 🎮 How to Use

### Step 1: Provide Image URL
- Enter a URL of any image you want to describe
- The system supports various image formats (JPG, PNG, GIF, etc.)
- Choose images with clear, interesting content for better evaluation

### Step 2: Select Vision Model
- **Meta LLaMA 3.2**: Advanced vision understanding with detailed analysis
- **Google Gemini 2.0 Flash**: Fast processing with accurate image description

### Step 3: Record Your Description
- **Look at the image**: Take time to observe all details
- **Speak naturally**: Describe what you see in your own words
- **Be detailed**: Include objects, people, actions, colors, and context
- **Record clearly**: Speak at a moderate pace with clear pronunciation

### Step 4: Get Comprehensive Evaluation
- **Relevance Assessment**: How well your description matches the image
- **Fluency Analysis**: Evaluation of speech smoothness and rhythm
- **Error Correction**: See your transcript with proper grammar and punctuation
- **Personalized Tips**: Get specific advice for improvement
- **CEFR Level**: Understand your current proficiency level

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Image URL     │───▶│  Vision Model    │───▶│ Image Analysis  │
└─────────────────┘    │   (LLaMA/Gemini) │    │  Description    │
                       └──────────────────┘    └─────────────────┘
                                                        │
                                                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Evaluation    │◀───│ Speech-to-Text   │◀───│ Audio Recording │
│   (DeepSeek)    │    │    (Google)      │    │   (Gradio)      │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🎯 Learning Benefits

### For Language Learners
- **Visual Context Learning**: Practice describing real-world scenarios
- **Pronunciation Improvement**: Get specific feedback on speech patterns
- **Vocabulary Expansion**: Learn descriptive words through image analysis
- **Fluency Development**: Practice natural speaking rhythm and pace
- **Grammar Enhancement**: See corrected versions of your speech

### For Educators
- **Speaking Assessment Tool**: Objectively evaluate student oral skills
- **Visual Learning Support**: Use images to prompt speaking practice
- **Progress Tracking**: Monitor improvement in speaking proficiency
- **CEFR Alignment**: Standards-based evaluation system
- **Engaging Activities**: Make speaking practice more interactive and fun

## 📊 Evaluation Metrics

### Core Scores
- **Relevance Score (0-100)**: How accurately your description matches the image content
- **Fluency Score (0-100)**: Assessment of speech smoothness, rhythm, and natural flow

### Detailed Analysis
- **Pronunciation Feedback**: Specific sounds, stress patterns, or words needing improvement
- **Grammar Mistakes**: Identification of structural and vocabulary errors
- **Corrected Transcript**: Your speech with proper grammar, punctuation, and vocabulary
- **Learning Level**: CEFR proficiency assessment (A1-C2)
- **Strengths**: Recognition of good vocabulary choices or natural expressions
- **Learning Tips**: Personalized advice for targeted improvement areas

## 🔧 Customization

### Adding New Vision Models
Modify the model dropdown in the Gradio interface to include additional vision-language models available through OpenRouter.

### Changing Speech Recognition Settings
Update the `transcribe_audio()` function to use different languages or recognition services.

### Custom Evaluation Criteria
Extend the evaluation system by modifying the `evaluate_spoken_english()` function to include additional speaking assessment metrics.

## 📊 Technical Details

### AI Models Used
- **Vision Models**: Meta LLaMA 3.2 11B Vision, Google Gemini 2.0 Flash for image analysis
- **Evaluation Engine**: DeepSeek Chat API for comprehensive speaking assessment
- **Speech Recognition**: Google Speech Recognition API for accurate transcription

### Supported Languages
- Primary: English (US)
- Speech recognition and evaluation optimized for English pronunciation assessment

### Audio Processing
- **Input formats**: Various audio formats supported through PyDub
- **Output format**: WAV for optimal speech recognition
- **Quality**: Optimized for clear speech recognition and analysis

### Image Support
- **Formats**: JPG, PNG, GIF, WebP, and other common image formats
- **Source**: Any publicly accessible image URL
- **Processing**: Advanced computer vision analysis through state-of-the-art VLM models

## 🤝 Contributing

We welcome contributions to improve the English Spoken Evaluation System!

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- Additional vision model integrations
- Multi-language speech evaluation
- New evaluation metrics
- UI/UX improvements
- Performance optimizations
- Offline processing capabilities

## 🐛 Troubleshooting

### Common Issues

**Issue: Vision model not responding**
- Solution: Check OpenRouter API keys and ensure they have sufficient credits
- Try switching between LLaMA and Gemini models

**Issue: Image not loading**
- Solution: Ensure the image URL is publicly accessible and properly formatted
- Check if the image format is supported

**Issue: Speech recognition fails**
- Solution: Check internet connection (Google Speech Recognition requires internet)
- Speak clearly and at moderate pace
- Ensure microphone permissions are granted

**Issue: Audio conversion errors**
- Solution: Ensure PyDub and ffmpeg are properly installed
- Check audio file format compatibility

### Getting Help
- Check the [Issues](https://github.com/youssefa7med/english-spoken-evaluation/issues) page
- Create a new issue with detailed error descriptions
- Include system information and error logs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **DeepSeek**: For providing advanced language AI capabilities
- **OpenRouter**: For seamless access to multiple vision-language models
- **Meta**: For the powerful LLaMA 3.2 Vision model
- **Google**: For Gemini 2.0 Flash and Speech Recognition services
- **Gradio**: For the intuitive web interface framework
- **CEFR Framework**: For standardized language proficiency guidelines

## 📞 Contact

- **Project Maintainer**: [Youssef Ahmed](mailto:youssef111ahmed111@gmail.com)
- **GitHub**: [@youssefa7med](https://github.com/youssefa7med)
  
---

### 🌟 Star this repository if it helped you improve your English speaking skills!

**Made with ❤️ for English language learners worldwide**
