#!C:\Python34\python

__author__ = 'Alexander'

import os
import re
import shutil

def main():

    #input from user:
    #path, show = map(str, input("Enter path and TV show. format = path,show: ").split(','))
    #print('Entered path: ', path)
    #print('Entered show ', show)

    splitter = re.compile(r'[.-]+')     #input splitter

    #input:
    path = 'downloads'
    show = 'house'

    show = ' '.join(splitter.split(show))

    #regular expressions:
    ignore   = re.compile(r'[^nfo$|sfv$]')  #files we want to ignore
    #aviFiles = re.compile(r'.*\.avi$')  #.avi files
    season   = re.compile(r's(\d{1,2})', re.I)          #format: House.S08E03.HDTV.XviD-LOL
    season2  = re.compile(r'([1-9])\d\d')               #format:  house.805.hdtv-lol
    title    = re.compile(r'(^%s)[ -.]' % show, re.I)   #Title of show

    #creates folder with incoming name if it does not exist:
    folder = os.path.join(path, show)
    if not os.path.exists(folder):
        os.mkdir(folder)
        print('%s was created' % folder)
    else:
        print('%s exists!' % folder)

    #sort by title:
    for root, dirs, files in os.walk(path):
        for name in files:
            splittedName = ' '.join(splitter.split(name))

            if title.search(splittedName):
                src = os.path.join(root, name)
                des = os.path.join(folder, name)
                shutil.move(src, des)
            else:
                continue

    #sort by season:
    for root, dirs, files in os.walk(folder):
        for name in files:

            if season.search(name):
                snum = int(season.search(name).group(1))
            elif season2.search(name):
                snum = int(season2.search(name).group(1))
            else:
                continue

            seasondir = 'Season ' + str(snum)
            seasondir = os.path.join(folder, seasondir)

            src = os.path.join(root, name)
            des = os.path.join(seasondir, name)

            if not os.path.exists(seasondir):
                os.mkdir(seasondir)
                shutil.move(src, des)

            else:
                shutil.move(src, des)



if __name__ == "__main__":
    main()

