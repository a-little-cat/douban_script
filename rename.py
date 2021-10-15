import os


class song_info():
    def __init__(self, song: str, album: str, singer: str) -> None:
        self.song = song
        self.album = album
        self.singer = singer


song_infos = []
with open("musicList.txt") as f:
    lines = f.readlines()
    for line in lines:
        song, album, singer = line.strip().split("	")
        song_infos.append(song_info(song, album, singer))

file_names = []
with open("DoubanMusicLinks.txt") as f:
    lines = f.readlines()
    for line in lines:
        file_name = line.split("/")[-1].strip()
        file_names.append(file_name.replace("/", "-"))

mp3_path = "mp3/"
out_path = "out/"
for song_info, file_name in zip(song_infos, file_names):
    src_file = mp3_path+file_name
    dst_file = out_path+song_info.song.replace("/", "-")+"_" + \
        song_info.singer.replace("/", "-")+"_" + \
        song_info.album.replace("/", "-")+".mp3"
    os.system("cp {} \"{}\"".format(src_file, dst_file))
