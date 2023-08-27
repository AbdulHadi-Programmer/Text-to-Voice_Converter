# Text-to-Voice_Converter
# Simple Text-to-Voice Converter using gTTS

## Introduction:
The Simple Text-to-Voice Converter project is a basic application that utilizes the Google Text-to-Speech (gTTS) library to convert user-input text into spoken audio. This project provides a user-friendly interface for inputting text and generating corresponding speech output in the English language.

## Code Overview:
The project code is written in Python and consists of a few simple steps:

## Importing Libraries:
The necessary libraries, gtts and playsound, are imported at the beginning of the code. gtts is used for converting text to speech, and playsound is used for playing the generated audio.

## User Input:
The program prompts the user to enter the text they want to convert to speech. The entered text is stored in the text variable.

## Text-to-Speech Conversion:
The gTTS library is used to convert the input text (text) into speech. The gTTS function takes the text and language (in this case, English) as arguments to generate the speech audio.

## Saving the Audio:
The user is prompted to enter a desired file name to save the generated speech as an MP3 audio file. The sound.save() method is used to save the generated speech as an MP3 file with the provided file name.

## Usage:
Run the script.
Enter the text you want to convert to speech when prompted.
Enter a desired file name (without extension) to save the generated audio.



## Conclusion:
The Simple Text-to-Voice Converter project provides a basic example of text-to-speech conversion using the gTTS library. While the current implementation requires users to manually input both the text to convert and the desired file name for audio storage, it can be enhanced through features like improved error handling, language selection, GUI integration, and support for multiple audio formats. These enhancements would collectively make the application more user-friendly, accessible, and versatile, meeting a wider range of user needs and preferences.

