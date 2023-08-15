from pytube import YouTube
import whisper
from googletrans import Translator #translate hindi to english
		
		

class YT:
    def __init__(self) -> None:
        pass
    
    # Youtube to mp3
        #dest = path of th folder in which the audio file will be saved
    def download_audio(self, youtube_url, dest):
        try:
            #get the Youtube video
            yt = YouTube(youtube_url)

            #extract the audio
            audio_stream = yt.streams.filter(only_audio=True).first()

            #if audio is available, then download the audio file
            if audio_stream:
                audio_stream.download(dest)
                print("Audio file downloaded.\n")
            else:
                print("No audio stream available for the provided video.\nDownload failed.\n")

        except Exception as e:
            print(f"Error: {e}")


    #generate video transcript
        #english transcript foer english videos
    def generate_transcript(self, audio_file, dest_file):
        model = whisper.load_model("tiny.en")
        result = model.transcribe(audio_file)
        transcript = result["text"]
		
		#write the transcript to the output file
        with open(dest_file, "w") as file:
            file.write(transcript)

        #print(result)

    
    #english transcript for a hindi audio file
    def hindi_to_english(self, audio_file, dest_file):
        def translate_to_english(hindi_text):
            translator = Translator()
            translated = translator.translate(hindi_text, src='hi', dest='en')
            return translated.text

        #generate the hindi transcript
        model = whisper.load_model("tiny.hi")
        result = model.transcribe(audio_file)
        hindi_ts = result["text"]

        # Translate the Hindi transcript to English
        translated_ts = translate_to_english(hindi_ts)

        #write the transcript to the output file
        with open(dest_file, "w") as file:
            file.write(translated_ts)


        # Print the translated text in English
        print("Translated Transcript in English:", translated_ts)

    





