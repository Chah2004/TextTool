from django.shortcuts import render,redirect
from TextTech.models import Blog
from TextTech.models import ContentCreator
from TextTech.models import MyReview
from TextTech.models import Help
from TextTech.models import ContactDetails
from TextTech.models import UserRegister
from django.conf import settings
from django.core.mail import send_mail
import datetime
from datetime import date
from newsapi.newsapi_client import NewsApiClient
from gtts import gTTS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import speech_recognition as sr
import pyttsx3 
from textblob import TextBlob
from langdetect import detect
from langcodes import Language
from googletrans import Translator
from googletrans import LANGUAGES
import googletrans
from fpdf import FPDF
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import pyqrcode
import png
from pyqrcode import QRCode
import spacy
import spacy.cli
from spellchecker import SpellChecker
import PyPDF2
from PyPDF2 import PdfReader
from translate import Translator
import os
import random



# Create your views here.
def navbar(request):
	return render(request,'navbar.html')

def sidebar(request):
	return render(request,'sidebar.html')


def footer(request):
	return render(request,'footer.html')

def login(request):
	if request.method=='POST':
		email=request.POST.get('email')
		password=request.POST.get('password')
		x=UserRegister.objects.filter(email = email ,password = password)
		k=len(x)
		if k>0:
			request.session['email']=email
			return redirect('/dashboard')
		else:
			return render(request,"login.html",{'msg':1})

	else:
		return render(request,'login.html')

def userprofil(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=UserRegister.objects.get(email=request.session['email'])
	if request.method=="POST":
		print("yes")
		if 'image' in request.FILES:
			user.image=request.FILES['image']
		else:
			nothing = "nothing"
		user.save()
		return render(request,'userprofil.html',{'user':user,'msg':'success'})
	else:
		return render(request,'userprofil.html',{'user':user})

def register(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		confirm_password=request.POST.get('c_password')
		if UserRegister.objects.filter(email=email).exists():
			return render(request,'register.html',{'msg':1})
		else:
			if password==confirm_password:
				length = 4
				otp = ''.join(str(random.randint(0, 9)) for _ in range(length))
				print("Your OTP is:", otp)
				subject="OTP"
				message="Welcome to TextTech....Your OTP is " + otp
				email_from=settings.EMAIL_HOST_USER
				recipient_list=[email,]
				send_mail(subject,message,email_from,recipient_list)
				rest="Your OTP sent to your respective Email Account. Please check your email box."
				return render(request,'register2.html',{'rest':rest,'otp':otp,'name':name,'email':email,'password':password})
			else:
				return render(request,'register.html',{'msg':3})
	else:
		return render(request,'register.html')
	return render(request,'register.html')



def register2(request):
	if request.method=='POST':
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		otp=request.POST.get('otp')
		original_otp=request.POST.get('original_otp')
		print(otp)
		print(original_otp)
		if otp == original_otp:
			x=UserRegister()
			x.name=request.POST.get('name')
			x.email=request.POST.get('email')
			x.password=request.POST.get('password')
			x.save()
			
			return render(request,'register.html',{'msg':2})
		else:
			
			return render(request,'register2.html',{'msg2':2})
	else:
		return render(request,'register2.html')

def forgot(request):
	if request.method=="POST":
		email=request.POST.get('email')
		user=UserRegister.objects.filter(email=email)
		if(len(user)>0):
			pw=user[0].password
			subject="password"
			message="Welcome to TextTech....Your password is " + pw
			email_from=settings.EMAIL_HOST_USER
			recipient_list=[email,]
			send_mail(subject,message,email_from,recipient_list)
			rest="Your password sent to your respective Email Account. Please check your email box."
			return render(request,'forgot.html',{'rest':rest})
		else:
			res="This Email ID is not register"
			return render(request,'forgot.html',{'rest':res})
	else:
		return render(request,'forgot.html')

def contact(request):
	if request.method=="POST":
		x=ContactDetails()
		x.name=request.POST.get('name')
		x.number=request.POST.get('number')
		x.email=request.POST.get('email')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'contact.html',{'message':1})

	else:
		return render(request,'contact.html')

def index(request):
	res=MyReview.objects.all()
	return render(request,'index.html',{'data':res})
	  
def base(request):
	return render(request,'base.html')

def allblog(request):
	res=Blog.objects.all()
	return render(request, 'allblog.html',{'data':res})

def detail_blog(request,id):
	res=Blog.objects.get(id=id)
	return render(request,'detail_blog.html',{'i':res})

def allcontentcreator(request):
	res=ContentCreator.objects.all()
	return render(request, 'allcontentcreator.html',{'data':res})

def about_us(request):
	return render(request,'about_us.html')

def dashboard(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'dashboard.html')

def review(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		x=MyReview()
		x.title=request.POST.get('txt')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'review.html',{'msg':1})

	else:
		return render(request,'review.html')

def changepw(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		o=request.POST.get("o_password")
		n=request.POST.get("n_password")
		c=request.POST.get("c_password")
		if n==c:
			user=UserRegister.objects.get(email=request.session['email'])
			p=user.password
			print(p)
			if o == p:
				user.password=n
				user.save()
				msg="successfully changed"
				return render(request,'changepw.html',{'msg':msg})
			else:
				msg="invalid current password"
				return render(request,'changepw.html',{'msg':msg})
		else:
			msg="password and confir password does not match"
			return render(request,'changepw.html',{'msg':msg})
	else:
		return render(request,'changepw.html')

def help(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		x=Help()
		x.title=request.POST.get('txt')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'help.html',{'msg':1})

	else:
		return render(request,'help.html')

def editprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	user=UserRegister.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.name=request.POST.get('name')
		user.birthday=request.POST.get('birthday')
		user.state=request.POST.get('state')
		user.country=request.POST.get('country')
		user.pincode=request.POST.get('pincode')
		user.number=request.POST.get('number')
		user.gender=request.POST.get('gender')
		user.age=request.POST.get('age')
		user.address=request.POST.get('address')
		if 'image' in request.FILES:
			user.image=request.FILES['image']
		else:
			nothing = "nothing"
		user.save()
		msg = 1
		return render(request,'editprofile.html',{'user':user,'msg':msg})
	else:
		return render(request,'editprofile.html',{'user':user})

def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	del request.session['email']
	return redirect('/login')

def livenews(request):
	newsapi=NewsApiClient(api_key='your api key')
	json_data=newsapi.get_everything(q='nlp',language='en',
		from_param=str(date.today()-datetime.timedelta(days=29)),
		to=str(date.today()),page_size=18,page=1,sort_by='relevancy')
	k=json_data['articles']
	return render(request,'livenews.html',{'k':k})


from gtts import gTTS, lang
def text_to_speech(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		data=request.POST.get('text')
		language = 'en'
		x = gTTS(text=data, lang=language, slow=False)
		x.save("./statics/images/output1.mp3")
		languages = lang.tts_langs()
		return render(request,'tts_output.html',{'data':data,'languages':languages})
	else:
		return render(request,'text_to_speech.html')

'''def tts_output(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	return render(request,'tts_output.html')'''

from translate import Translator
from gtts import gTTS, lang
def tts_output2(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		from gtts import gTTS, lang
		languages = lang.tts_langs()
		data=request.POST.get('text')
		lang1=request.POST.get('lang')
		if lang1 == 'Select Language':
			msg = 1
			return render(request,'tts_output.html',{'data':data,'msg':msg,'languages':languages})
		else:
			translator=Translator(to_lang=lang1)
			Translation = translator.translate(data)
			language = lang1
			myobj = gTTS(text=Translation, lang=language, slow=False)
			myobj.save("./statics/welcome.mp3")
			return render(request,'tts_output2.html',{'data':Translation})




def speech_to_text(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		r = sr.Recognizer()
		MyText=""
		try:
			with sr.Microphone() as source2:
				r.adjust_for_ambient_noise(source2, duration=0.2)
				audio2 = r.listen(source2)
				MyText = r.recognize_google(audio2)
				MyText = MyText.capitalize()
				print("Did you say ",MyText)	
		except sr.RequestError as e:
			print("Could not request results; {0}".format(e))
		except sr.UnknownValueError:
			print("unknown error occurred")
		return render(request,'speech_to_text.html',{'mytext':MyText})
	else:
		return render(request,'speech_to_text.html')

def word_cloud(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		data=request.POST.get('text')
		if data.isdigit():
			msg = 1
			return render(request,'word_cloud.html',{'msg':msg,'data':data})
		if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 2
			return render(request,'word_cloud.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 3
			return render(request,'word_cloud.html',{'data':data,'msg':msg})
		comment_words=data
		wordcloud = WordCloud(background_color = 'white').generate(comment_words)
		plt.figure()
		plt.imshow(wordcloud, interpolation='bilinear')
		plt.axis("off")
		plt.tight_layout(pad=0)
		plt.savefig('statics/wordcloud.png')
		return render(request,'wc_output.html',{'data':comment_words})

	else:
		return render(request,'word_cloud.html')

def sentiment_analysis(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		data=request.POST.get('text')
		if data.isdigit():
			msg = 0
			return render(request,'sentiment_analysis.html',{'msg':msg,'data':data})
		if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 2
			return render(request,'sentiment_analysis.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 3
			return render(request,'sentiment_analysis.html',{'data':data,'msg':msg})
		sa=TextBlob(data)
		sa.sentiment
		p=sa.sentiment.polarity
		msg=""
		if p==0:
			print("comment is neutral")
			msg="neutral"
		elif p<0:
			print("comment is negative")
			msg="negative"
		else:
			print("comment is positive")
			msg="positive"
		return render(request,'sa_output.html',{'data':data,'msg':msg})
	else:
		return render(request,'sentiment_analysis.html')

def language_detection(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		data=request.POST.get('text')
		if data.isdigit():
			msg = 1
			return render(request,'language_detection.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 2
			return render(request,'language_detection.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 3
			return render(request,'language_detection.html',{'data':data,'msg':msg})
		language_code=detect(data)
		language_name=Language.get(language_code).language_name().title()
		return render(request,'ld_output.html',{'msg':language_name,'data':data})
	else:
		return render(request,'language_detection.html')

def language_converter(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		from gtts import gTTS, lang
		result = lang.tts_langs()
		data=request.POST.get('text')
		target_language=request.POST.get('lang')
		if target_language == 'Select Language':
			msg = 1
			return render(request,'language_converter.html',{'data':data,'msg':msg,'result':result})
		else:
			translator= Translator(to_lang=target_language)
			translation= translator.translate(data)
			res=translation
			return render(request,'lc_output.html',{'data':data, 'res':res})
	else:
		result= googletrans.LANGUAGES
		return render(request,'language_converter.html',{'result':result})

def text_to_pdf(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		text_content=request.POST.get('text')
		output_example='./statics/output.pdf'
		pdf= FPDF()
		pdf.add_page()
		pdf.set_font("Arial",size=12)
		paragraphs = text_content.split('\n\n')
		for paragraph in paragraphs:
			pdf.multi_cell(0, 10, txt=paragraph)
		pdf.output(output_example)
		return render(request,'ttp_output.html',{'data':text_content})
	else:
		return render(request,'text_to_pdf.html')

def text_summarization(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		data=request.POST.get('text')
		if data.isdigit():
			msg = 1
			return render(request,'text_summarization.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 2
			return render(request,'text_summarization.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 3
			return render(request,'text_summarization.html',{'data':data,'msg':msg})
		language="english"
		parser=PlaintextParser.from_string(data, Tokenizer(language))
		summarizer = LsaSummarizer()
		summary = summarizer(parser.document, 3)
		for sentence in summary:
			print(sentence)
		return render(request, 'ts_output.html', {'msg': sentence, 'data': data})
	else:
		return render(request,'text_summarization.html')

def count(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		data=request.POST.get('text')
		target=request.POST.get('count')
		if target=="Choose one option":
			msg=1
			return render(request,'count.html',{'msg':msg,'data':data})
		else:
			if target=="paragraphs":
				if data.isdigit():
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				paragraphs = data.split('\n')
				paragraphs = [p for p in paragraphs if p.strip()]
				paragraph_count = len(paragraphs)
				print("Number of paragraphs:", paragraph_count)
				msg=paragraph_count
			elif target=="words":
				if data.isdigit():
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				words = data.split()
				word_count = len(words)
				print("Number of words:", word_count)
				msg=word_count
			elif target=="sentences":
				if data.isdigit():
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				sentence_count=0
				for char in data:
					if char in ('.', '!', '?'):
						sentence_count += 1
				print("Number of sentences:", sentence_count)
				msg=sentence_count
			elif target=="characters":
				if data.isdigit():
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
					msg = 0
					return render(request,'c_output.html',{'data':data,'msg':msg})
				char_count=0
				for char in data:
					if char != ' ':
						char_count += 1
				print("Number of characters:", char_count)
				msg=char_count
			elif target=="spaces":
				space_count = 0
				for char in data:
					if char == ' ':
						space_count += 1
				print("Number of spaces:", space_count)
				msg=space_count
			elif target=="vowels":
				vowel_count = 0
				vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
				for char in data:
					if char in vowels:
						vowel_count += 1
				print("Number of vowels:", vowel_count)
				msg=vowel_count
			elif target=="consonants":
				consonant_count = 0
				vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
				for char in data:
					if char.isalpha() and char not in vowels:
						consonant_count += 1
				print("Number of consonants:", consonant_count)
				msg=consonant_count
			elif target=="digits":
				digit_count = 0
				for char in data:
					if char.isdigit():
						digit_count += 1
				print("Number of digits:", digit_count)
				msg=digit_count
			else:
				msg="invalid input"
			return render(request,'c_output.html',{'data':data,'msg':msg})
	else:
		return render(request,'count.html')

def transform_text(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=="POST":
		data=request.POST.get('text')
		transform=request.POST.get('convert')
		if data.isdigit():
			msg = 0
			return render(request,'transform_text.html',{'msg':msg})
		if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 2
			return render(request,'transform_text.html',{'msg':msg})
		if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 3
			return render(request,'transform_text.html',{'msg':msg})
		result = ""
		if transform == "Choose one option":
			msg=1
			return render(request,'transform_text.html',{'msg':msg,'data':data})
		else:
			if transform == 'Upper':
				msg = data.upper()
			elif transform == 'Lower':
				msg = data.lower()
			elif transform == 'Capitalize':
				capitalize_next = True
				for char in data:
					if capitalize_next and char.isalpha():
						char = char.upper()
						capitalize_next = False
					elif char in ['.', '!', '?',' ']:
						capitalize_next = True
					result += char
				msg= result
			elif transform == 'Sentence':
				capitalize_next = True
				for char in data:
					if capitalize_next and char.isalpha():
						char = char.upper()
						capitalize_next = False
					elif char in ['.', '!', '?']:
						capitalize_next = True
					result += char
				msg= result
			elif transform == 'Toggle':
				toggle_state = True
				for char in data:
					if char.isalpha():
						if toggle_state:
							char = char.upper() 
						else:
							char = char.lower()
						toggle_state = not toggle_state
					result += char
				msg = result
			else:
				msg="Choose the options"
			return render(request,'tt_output.html',{'data':data,'msg':msg})
	else:
		return render(request,'transform_text.html')

def text_to_qr(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('text')
		qrcode=pyqrcode.create(data)
		file='statics/myqr.png'
		qrcode.png(file,scale=8)
		return render(request,'ttqr_output.html',{'data':data})
	else:
		return render(request,'text_to_qr.html')


def ttqr_output(request):
	return render(request,'ttqr_output.html')

def linguistic_analysis(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('text')
		if data.isdigit():
			msg = 0
			return render(request,'linguistic_analysis.html',{'msg':msg})
		if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 2
			return render(request,'linguistic_analysis.html',{'msg':msg})
		if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 3
			return render(request,'linguistic_analysis.html',{'msg':msg})
		linguistic=request.POST.get('linguistic')
		if linguistic == "Choose one option":
			msg = 1
			return render(request,'linguistic_analysis.html',{'msg':msg,'data':data})
		else:
			msg1 = "no"
			name = spacy.explain(linguistic)
			nlp=spacy.load("en_core_web_sm")
			doc=nlp(data)
			for i in doc:
				if linguistic == i.pos_ : 
					msg1="yes"

			print("part of speech tagging")
			return render(request,'la_output.html',{'msg1':msg1,'data':data,'doc':doc,'linguistic':linguistic,'name':name})
	else:
		return render(request,'linguistic_analysis.html')


def spelling_checker(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('text')
		if data.isdigit():
			msg = 1
			return render(request,'spelling_checker.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 2
			return render(request,'spelling_checker.html',{'data':data,'msg':msg})
		if all(char in '!"#$%&\'()*+,1234567890-./:;<=>?@[\\]^_`{|}~' for char in data):
			msg = 3
			return render(request,'spelling_checker.html',{'data':data,'msg':msg})
		spell=SpellChecker()
		words=data.split()
		misspelled = spell.unknown(words)
		corrected_text=[]
		for word in words:
			if word in misspelled:
				corrected_text.append(spell.correction(word))
			else:
				corrected_text.append(word)
		res=' '.join(corrected_text)
		return render(request,'sc_output.html',{'msg':res,'data':data})
	else:
		return render(request,'spelling_checker.html')

def pdf_to_text(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		pdf_file = request.FILES['pdf']
		with open('./statics/uploaded_pdf.pdf', 'wb') as f:
			f.write(pdf_file.read())
		reader = PdfReader('statics/uploaded_pdf.pdf')
		number_of_pages = len(reader.pages)
		return render(request, 'ptt_output.html', {'pages':number_of_pages,'pdf_file':pdf_file})
	else:
		return render(request, 'pdf_to_text.html')

def ptt_output(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		file = open('./statics/uploaded_pdf.pdf','rb')
		pdfReader = PyPDF2.PdfReader(file)
		pgno = int(request.POST.get('pageno'))
		page = pdfReader.pages[pgno - 1]
		k=page.extract_text().strip()
		print(k)
		pages=request.POST.get('pages')
		pdf_file=request.POST.get('pdf_file')
		return render(request,'ptt_output.html',{'pages':pages,'k':k, 'pdf_file':pdf_file ,'pgno':pgno}) 


def pdf_to_audio(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		pdf_file = request.FILES['pdf']
		with open('./statics/uploaded_pdf.pdf', 'wb') as f:
			f.write(pdf_file.read())
		reader = PdfReader('statics/uploaded_pdf.pdf')
		number_of_pages = len(reader.pages)
		return render(request, 'pta_output.html', {'pages':number_of_pages,'pdf_file':pdf_file})
	else:
		return render(request, 'pdf_to_audio.html')


def pta_output(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		file = open('./statics/uploaded_pdf.pdf','rb')
		pdfReader = PyPDF2.PdfReader(file)
		pgno = int(request.POST.get('pageno'))
		page = pdfReader.pages[pgno - 1]
		k=page.extract_text().strip()
		pages=request.POST.get('pages')
		pdf_file=request.POST.get('pdf_file')
		print(k,type(k))
		if k is None or k=='':
			msg = 2
			print("hello")
			return render(request,'pta_output.html',{'msg':msg,'pages':pages,'k':k, 'pdf_file':pdf_file ,'pgno':pgno})
		print("hii")
		
		language = 'en'
		myobj = gTTS(text=k, lang=language, slow=False)
		myobj.save("./statics/pdfread.mp3")
		yes=1
		return render(request,'pta_output.html',{'pages':pages,'k':k, 'pdf_file':pdf_file ,'pgno':pgno,'msg':yes})

def word_transformation(request):
	if not request.session.has_key('email'):
		return redirect('/login')
	if request.method=='POST':
		data=request.POST.get('text')
		w1=request.POST.get('word')
		w2=request.POST.get('subtitute')
		transformed_text = data.replace(w1, w2)
		yes=1
		return render(request,'word_transformation.html',{'data':data,'tt':transformed_text,'w1':w1,'w2':w2,'msg':yes})
	else:
		return render(request,'word_transformation.html')


