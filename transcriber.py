from youtube_transcript_api import YouTubeTranscriptApi
import re
import transformers


def get_video_id_from_url(url):
    video_id = re.search(r'(?<=v=)[^&#]+', url)
    if video_id:
        return video_id.group()
    else:
        return None



def transcribe(url='https://www.youtube.com/watch?v=Ywec1MbeQDk'):
    video_id = get_video_id_from_url(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ' '.join([line['text'] for line in transcript])
    return transcript_text


