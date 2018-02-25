from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from config import CLOUDINARY
from cloudinary import uploader
import cloudinary
import datetime

class DbConnect:
    target = "temp.mp4"

    def clip(self, filename,  start, end):
        ffmpeg_extract_subclip(filename, start, end, targetname = self.target)

    def push_to_db(self, title):
        cloudinary.config(
          cloud_name = CLOUDINARY['cloud_name'],  
          api_key = CLOUDINARY['api_key'],  
          api_secret = CLOUDINARY['api_secret']
        )
        id = title + ", " + datetime.datetime.now().strftime("%H:%M:%S %m-%d-%Y")
        cloudinary.uploader.upload(self.target, resource_type="video", public_id=id)
