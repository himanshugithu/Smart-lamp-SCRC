from datetime import datetime
from gtts import gTTS
import os

current_datetime = datetime.now()
formated_datetime=current_datetime.strftime("%Y-%m-%d %A %H:%M:%S")


def text_to_speech(text, language='en', filename='dt.mp3', play=True):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(filename)
    if play:
        os.system("mpg321 dt.mp3")

text_to_speech(formated_datetime)
print("Current date and time:",formated_datetime)


