#!/usr/bin/env python

import sys
from pydub import AudioSegment
from File import fetchItemsFromDir
from Constants import INPUTS_PATH, OUTPUTS_PATH, SONG_BARS_AVAIL

def main(argc, argv):
    totalSongBars = len(SONG_BARS_AVAIL)
    files         = fetchItemsFromDir(INPUTS_PATH)['files']        


    for filename in files:
        segments  = filename.split('.')
        name      = ' '.join(segments[:-1])
        bpm       = int(name.split(' ')[-1])
        name      = ' '.join(name.split(' ')[:-1])
        audio     = AudioSegment.from_file('%s/%s' % (INPUTS_PATH, filename))
        songLen   = audio.duration_seconds
        barLength = 60 / float(bpm)
        audioBars = songLen / barLength / 2
        
        for i in xrange(1, totalSongBars):
            if audioBars % SONG_BARS_AVAIL[totalSongBars - i] != audioBars:
                songLen = SONG_BARS_AVAIL[totalSongBars - i] * barLength
                break

        audio[:songLen * 1000].export('%s/%s.mp3' % (OUTPUTS_PATH, name))

        print 'Finished Editing : ' + name

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])
