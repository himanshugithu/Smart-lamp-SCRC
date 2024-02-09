from gtts import gTTS
import os
au = "Hello, how are you?"

# Create a gTTS object
tts = gTTS(text=au, lang='en')

# Save the audio file
tts.save("output1.mp3")

# Play the audio file
os.system("mpg321 output1.mp3")


# You may need to adjust the command based on your audio player

    