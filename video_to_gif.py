from __future__ import print_function
from moviepy.editor import VideoFileClip
import sys
import os
import time
import datetime

if __name__ == '__main__':
    source = sys.argv[1]
    dest = sys.argv[2]
    print('Source: {}'.format(source))
    print('Destination: {}'.format(dest))
    assert os.path.isfile(source)
    assert os.path.exists(dest)
    output_filename = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H.%M.%S')
    output_filename = os.path.join(dest, output_filename+".gif")
    print('OutputFile: {}'.format(output_filename))
    clip = VideoFileClip(source)
    clip.write_gif(output_filename)
