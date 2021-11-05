#pip install PyPDF2
import PyPDF2
import pyttsx3

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)
#o nome do arquivo pdf recomendo colocar no mesmo diretorio do código
pdfReader = PyPDF2.PdfFileReader(open('LivroAlvo.pdf', 'rb'))

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

speaker.save_to_file(text, 'audiobook.mp3')
speaker.runAndWait()