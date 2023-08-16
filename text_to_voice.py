import gtts
import playsound
text = input("Enter Something Text: ")
sound = gtts.gTTS (text, lang="ur")
a = input("Enter the file name to save: ")
sound.save(a + ".mp3")
'''
# "20 سال پھنسا 9 بجے سے 5 بجے کی جیل میں
چکی پیسی، یہ سمجھے بچوں کا کھیل ہے
ایمنگ ہائی، اور اوپر میرے مقاصد بھی
سنگت کری کم، لیکن کام میرے دوست نہیں
پریشان سب کے سوچے جاتا میں کدھر؟
صبح 8 جاتا، رات 12 آتا گھر
رشتوں کی دور میں نے کاٹے سارے دھاگے
دغا جو کرتے میں نے توڑے انسے ناتے
#'''
