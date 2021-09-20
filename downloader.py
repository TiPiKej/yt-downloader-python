from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def downloader(url):
	try:
		yt = YouTube(url)
		yt.streams.filter(only_audio=True, file_extension='mp4').order_by("abr").desc().first().download("./out")
	except VideoUnavailable:
		return f"Cannot find video : {url}"
	return ''


def downloader_catcher(urls):
	file_mode = 'w'

	for url in urls:
		err = downloader(url)

		if len(err) > 0:
			try:
				print(err)
				with open("err.txt", file_mode) as f:
					f.write(err)
					file_mode = 'a'
			except (IOError, OSError) as e:
				print("Cannot create error log file")


u = input("Podaj adres url do filmu yt")
downloader_catcher([u])
