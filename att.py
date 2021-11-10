import speech_recognition as sr
#importing module 
import logging 

#Create and configure logger 
logging.basicConfig(filename="transcribe.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w')

logger=logging.getLogger() 
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG)

class Transcribe():

    # def __init__(self,):
    #     file = 'greetings_1.wav'

    def audio_to_text(self,file):
        try:
            recog = sr.Recognizer()
            audio_file = sr.AudioFile(file)
            with audio_file as source:        
                audio = recog.record(source)
                data = recog.recognize_google(audio)
            # print(data)
            logger.info(data)

            return data

        except Exception as e:
            print(e)

if __name__ == "__main__":
    audio_file = 'greetings_1.wav' # use WAV format only
    trans = Transcribe()
    text = trans.audio_to_text(audio_file)
    print(text)
