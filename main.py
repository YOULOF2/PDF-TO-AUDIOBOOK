import textract
from gtts import gTTS
from playsound import playsound

from progress_bar import progress_bar

progress_gen = progress_bar()
next(progress_gen)

MP3_FILENAME = "temp/file.mp3"
PDF_FILENAME = "advs_removed.pdf"

text = textract.process(PDF_FILENAME, method="pdfminer", encoding="ascii").decode('utf-8')
next(progress_gen)

tts = gTTS(text)
next(progress_gen)

tts.save(MP3_FILENAME)
next(progress_gen)

playsound(MP3_FILENAME)
