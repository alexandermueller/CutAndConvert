#!/usr/bin/env python

import sys
from pydub import AudioSegment
from File import fetchItemsFromDir
from Constants import INPUTS_PATH, OUTPUTS_PATH

def main(argc, argv):
    files = fetchItemsFromDir(INPUTS_PATH)['files']        

    for filename in files:
        segments  = filename.split('.')
        name      = ' '.join(segments[:-1])
        bpm       = int(name.split(' ')[-1])
        name      = ' '.join(name.split(' ')[:-1])
        audio     = AudioSegment.from_file('%s/%s' % (INPUTS_PATH, filename))

        # print name + " = " + str(bpm)
        # audio.export('%s/%s.mp3' % (OUTPUTS_PATH, name))

if __name__ == '__main__':
   main(len(sys.argv) - 1, sys.argv[1:])
