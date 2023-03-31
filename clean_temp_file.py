# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from moviepy.editor import *
import shutil
import time


def removeFile(file):
    if os.path.exists(file):
        os.remove(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    removeFile('in_sub.mp4')
    removeFile('out.mp4')
    removeFile('out_sub.mp4')
    removeFile('output0.mp3')
    removeFile('test.mp3')
    removeFile('BGM.mp3')
    removeFile('BGM_volume.mp3')
    removeFile('nosound.mp4')
    for i in range(8):
        removeFile('people{}.mp3'.format(i))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
