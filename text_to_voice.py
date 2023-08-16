import gtts
import playsound
text = input("Enter Something Text: ")
sound = gtts.gTTS (text, lang="ur")
a = input("Enter the file name to save: ")
sound.save(a + ".mp3")
