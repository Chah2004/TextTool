# 🧠 TextTool

**TextTool** is a Django-based web application that provides a collection of useful **text processing, analysis, transformation, NLP, speech, and PDF utilities** in one platform.

The application is designed to make common text-related operations simple and accessible through a user-friendly web interface. It combines **Python, Django, Natural Language Processing, speech processing, PDF utilities, and frontend technologies** to provide multiple productivity tools for working with text.

---

## ✨ Features

TextTool provides a wide range of text-processing utilities:

### 📝 Text Processing & Transformation

* 🔠 **Text Transformation**

  * Uppercase
  * Lowercase
  * Capitalize
  * Sentence case
  * Toggle case

* 🔄 **Word Transformation**

  * Find and replace words or phrases

* 🔢 **Text Counter**

  * Words
  * Characters
  * Sentences
  * Paragraphs
  * Spaces
  * Vowels
  * Consonants
  * Digits

* ✍️ **Spelling Checker**

  * Detects misspelled words
  * Suggests corrected words

---

### 🤖 NLP & Text Analysis

* ❤️ **Sentiment Analysis**

  * Positive
  * Negative
  * Neutral

* 🌍 **Language Detection**

  * Detects the language of entered text

* 🌐 **Language Converter**

  * Translates text into a selected language

* 📄 **Text Summarization**

  * Generates a concise summary from longer text

* 🔤 **Linguistic Analysis**

  * Part-of-speech analysis
  * NLP-based text processing using spaCy

* ☁️ **Word Cloud Generator**

  * Generates a visual representation of frequently occurring words

---

### 🔊 Speech & Audio Tools

* 🗣️ **Text to Speech**

  * Converts written text into speech

* 🎙️ **Speech to Text**

  * Converts spoken input into text

* 🔊 **PDF to Audio**

  * Extracts text from a selected PDF page
  * Converts extracted text into speech

---

### 📄 PDF & Document Tools

* 📄 **Text to PDF**

  * Converts entered text into a PDF document

* 📖 **PDF to Text**

  * Uploads a PDF
  * Extracts text from selected pages

* 🔊 **PDF to Audio**

  * Extracts text from PDF pages
  * Converts the extracted text into audio

---

### 📱 Other Utilities

* 📱 **Text to QR Code**

  * Converts text into a QR code

* 📰 **Live News**

  * Fetches NLP-related news using the News API

---

### 👤 User Features

TextTool also includes basic user-management functionality:

* 🔐 User registration
* 📧 OTP-based registration verification
* 🔑 Login and logout
* 🔄 Password change
* 📩 Forgot-password functionality
* 👤 User profile
* 🖼️ Profile image upload
* ✏️ Edit profile
* ⭐ Submit reviews
* ❓ Help/support section
* 📬 Contact form

---

### 📰 Content Features

* 📝 Blog listing
* 📖 Individual blog details
* 👨‍💻 Content creator listing
* ⭐ User reviews

---

## 🛠️ Tech Stack

### Backend

* 🐍 **Python**
* 🌐 **Django**

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Database

* SQLite

### NLP & Text Processing

* TextBlob
* spaCy
* langdetect
* langcodes
* Sumy
* pyspellchecker
* googletrans
* translate

### Speech & Audio

* gTTS
* SpeechRecognition
* PyAudio / microphone input

### PDF Processing

* FPDF
* PyPDF2

### Visualization & Utilities

* WordCloud
* Matplotlib
* PyQRCode
* pypng

### APIs

* News API

---

## 📂 Project Structure

The repository contains the Django project configuration in `TextTool` and the main application logic in `TextTech`.

```text
TextTool/
│
├── TextTool/                    # Django project configuration
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── TextTech/                   # Main Django application
│   ├── migrations/             # Database migrations
│   ├── __init__.py
│   ├── admin.py                # Django admin configuration
│   ├── apps.py                 # Application configuration
│   ├── models.py               # Database models
│   ├── views.py                # Application logic
│   └── tests.py                # Tests
│
├── media/                      # User-uploaded media
│
├── statics/                    # Static assets and generated files
│
├── templates/                  # HTML templates
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── sentiment_analysis.html
│   ├── word_cloud.html
│   ├── text_summarization.html
│   ├── language_detection.html
│   ├── language_converter.html
│   ├── linguistic_analysis.html
│   ├── spelling_checker.html
│   ├── text_to_speech.html
│   ├── speech_to_text.html
│   ├── text_to_pdf.html
│   ├── pdf_to_text.html
│   ├── pdf_to_audio.html
│   ├── text_to_qr.html
│   └── ...
│
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
└── README.md
```

The repository currently contains separate folders for the Django project configuration and application, so keeping `TextTool` and `TextTech` distinct in the documentation is important.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Chah2004/TextTool.git
cd TextTool
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

Install Django and the Python libraries used by the project:

```bash
pip install django
pip install gTTS
pip install wordcloud
pip install matplotlib
pip install SpeechRecognition
pip install pyttsx3
pip install textblob
pip install langdetect
pip install langcodes
pip install googletrans
pip install fpdf
pip install sumy
pip install PyQRCode
pip install pypng
pip install spacy
pip install pyspellchecker
pip install PyPDF2
pip install translate
pip install newsapi-python
```

You can also generate a dependency file after installing the required packages:

```bash
pip freeze > requirements.txt
```

---

## 🧠 spaCy Model Setup

The linguistic-analysis functionality uses the **`en_core_web_sm`** spaCy model.

Install it with:

```bash
python -m spacy download en_core_web_sm
```

Without this model, the linguistic-analysis feature will not work correctly.

---

## 🗄️ Database Setup

Run Django migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👨‍💻 Create a Superuser

To access the Django administration panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

---

## ▶️ Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 🔑 Configuration

Some features require external services or local configuration.

### News API

The live-news functionality uses the **News API** to retrieve articles. The API key should be configured before using the live-news feature.

Instead of committing API keys directly to the repository, it is recommended to store them in environment variables.

Example:

```env
NEWS_API_KEY=your_api_key_here
```

---

## 📌 How It Works

TextTool follows a simple workflow:

```text
User
  │
  ▼
Django Web Interface
  │
  ├── Text Processing
  ├── NLP Analysis
  ├── Speech Processing
  ├── PDF Processing
  ├── Translation
  ├── QR Generation
  └── Text Transformation
  │
  ▼
Processed Result
```

Most text-processing features accept user input through Django forms, process that input using Python libraries, and display the resulting output through dedicated HTML templates. The implementation is handled primarily through Django views.

---

## 🎯 Purpose of the Project

TextTool was developed as an integrated platform for experimenting with and implementing different **text-processing and NLP techniques** within a Django web application.

The project demonstrates practical usage of:

* Django web development
* Python programming
* Natural Language Processing
* Text analysis
* Speech recognition
* Text-to-speech systems
* PDF processing
* Language detection and translation
* Data visualization
* API integration
* User authentication and profile management

---

## 🔮 Future Improvements

Possible future enhancements include:

* 🔐 Secure password hashing and authentication
* 🔑 Environment-based configuration for API keys
* 📦 Add a complete `requirements.txt`
* 🎨 Improved responsive UI/UX
* ⚡ AJAX-based processing for faster interactions
* 🤖 AI-powered summarization and text generation
* 🧠 More advanced NLP models
* 📊 Detailed text analytics and statistics
* ☁️ Cloud deployment
* 🗂️ User history for processed documents
* 📥 Downloadable results for all tools
* 🔒 Improved security and input validation

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

```bash
git clone https://github.com/Chah2004/TextTool.git
cd TextTool
```

Create a new branch:

```bash
git checkout -b feature/your-feature
```

Make your changes, commit them, and push the branch:

```bash
git add .
git commit -m "Add new feature"
git push origin feature/your-feature
```

Then open a Pull Request.

---




