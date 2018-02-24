from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from config import CLOUDINARY
from cloudinary import uploader
import cloudinary

class DbConnect:
	target = "temp.mp4"

	def clip(self, filename, title, timestamp, start, end):
		ffmpeg_extract_subclip(filename, start, end, targetname = self.target)
		self.title = title
		self.timestamp = timestamp

	def push_to_db(self):
		cloudinary.config(
          cloud_name = CLOUDINARY['cloud_name'],  
          api_key = CLOUDINARY['api_key'],  
          api_secret = CLOUDINARY['api_secret']
        )
		cloudinary.uploader.upload(self.target, resource_type = "video")
