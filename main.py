# -*- coding: utf8 -*-


import os


def removeTorrent(folderPath=None):

    if folderPath == None:
        folderPath = os.getcwd()

    pathList = os.listdir(folderPath)

    for path in pathList:
        if os.path.splitext(path)[-1] == ".torrent":
            os.remove(os.path.join(folderPath, path))


def test():

    #folderPath = os.getcwd()
    folderPath = "C:\Users\Han\Downloads"
    
    pathList = os.listdir(folderPath)

    torrentCount = 0

    for path in pathList:
        if path[-8:] == ".torrent":
            torrentCount += 1

    removeTorrent(folderPath)

    assert len(os.listdir(folderPath)) == len(pathList) - torrentCount
    
    
    print "Success"


def main():

    if len(os.sys.argv) > 1:
        folderPath = os.sys.argv[1]
    else:
        folderPath = None

    removeTorrent(folderPath)

    print "Complete"


if __name__ == "__main__":
    #test()
    main()
