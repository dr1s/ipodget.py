#!/usr/bin/env python
import sys
import os
import eyed3
import shutil

eyed3.log.setLevel('ERROR')

def usage():
    print("usage: ipodget $ipod_dir $output_dir")

def replace_characters(input):
    output = input.replace(u'/',u'-')
    return output

def get_id3(file_name):
    song = {}
    audiofile = eyed3.load(file_name)
    song['artist'] = replace_characters(audiofile.tag.artist)
    song['title'] = replace_characters(audiofile.tag.title)
    song['album'] = replace_characters(audiofile.tag.album)
    song['track_num'] = audiofile.tag.track_num[0]
    if audiofile.tag.album_artist is None:
            song['album_artist'] = replace_characters(audiofile.tag.artist)
    else:
        song['album_artist'] = replace_characters(audiofile.tag.album_artist)

    return song


def get_filename(song):
    file_name = unicode(song['track_num']) + u" - " + song['artist']
    file_name += u" - " + song['title'] + u".mp3"
    return file_name


def main():
    if not len(sys.argv) > 2:
        usage()
        sys.exit()

    ipod_dir = sys.argv[1]
    ipod_dir = os.path.abspath(ipod_dir)
    output_dir = sys.argv[2]
    output_dir = os.path.abspath(output_dir)
    music_dir = os.path.join(ipod_dir, "iPod_Control")
    music_dir = os.path.join(music_dir, "Music")
    for root, dirs, files in os.walk(music_dir):
        for file_name in files:
            if file_name.endswith(".mp3"):
                audiofile = os.path.join(music_dir, root)
                audiofile = os.path.join(audiofile, file_name)
                song_meta = get_id3(audiofile)
                filename = get_filename(song_meta)
                print(filename)

                artist_dir = os.path.join(output_dir, song_meta['album_artist'])
                album_dir = os.path.join(artist_dir, song_meta['album'])
                if not (os.path.exists(album_dir)):
                    os.makedirs(album_dir)

                file_path = os.path.join(album_dir, filename)
                print(file_path)

                shutil.copy(audiofile, file_path)




if __name__ == "__main__":
    main()
