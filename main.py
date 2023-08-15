from youtube import YT

# Youtube to mp3
yt = YT()
youtube_url = "https://youtu.be/JgnbwKnHMZQ?t=1233"
output_path = ".\\RNN vid 3"

yt.download_audio(youtube_url, output_path)

#check the path of the downloaded audio file
'''audio_file_path = '.\\Example\\Magic Methods & Dunder - Advanced Python Tutorial 1.mp4'
dest = ".\\Example\\transcript.txt"
yt.generate_transcript(audio_file_path, dest )'''


'''
#generating english subtitles + transcript for hindi video
hindi_audio = "audio path"
dest = "path of transcript file"

yt.hindi_to_english(hindi_audio, dest)
'''