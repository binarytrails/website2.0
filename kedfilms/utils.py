"""
    Utilities powered by the magnificent me.
"""

import os, glob, re, subprocess, markdown2

# get_image_info()
import struct, StringIO

def getFilenames(folderpath, byNewest):
    files = filter(os.path.isfile, glob.glob(folderpath + "*"))
    files.sort(key=lambda x: os.path.getmtime(x))
    
    if byNewest:
            files.reverse()
    
    names = []
    for f in files:
        fidx = f.rfind("/") + 1
        name = f[fidx:]
        names.append(name)    

    return names

def getMostRecentFileRecursively(rootfolder, extension=""):
    files = []
    for dirname, dirnames, filenames in os.walk(rootfolder):
        for filename in filenames:
            if filename.endswith(extension):
                st_mtime = os.stat(os.path.join(dirname, filename)).st_mtime
                files.append((st_mtime, os.path.join(dirname, filename)))

    files.sort(key=lambda files: files[0])
    return max(files)[1]

def markdownToHtml(filepath):
    try:
        mdfile = open(filepath, "r")
        text = mdfile.read()
    finally:
        if mdfile:
            mdfile.close()
    return markdown2.markdown(text)

"""
    Make two dimentional dict from list with last & next as sub-dict.
"""
def get_list_next_previous_as_two_dimentional_dict(alist=None):
    if not alist:
        return None

    adict = {}

    for index in range(len(alist)):
        item = alist[index][0]

        if len(alist) == 1:
            last = ""
            next = ""
        else:
            if index == 0:
                last = alist[len(alist) - 1][0]
                next = alist[index + 1][0]

            elif index == len(alist) - 1:
                last =  alist[index - 1][0]
                next = alist[0][0]

            else:
                last = alist[index - 1][0]
                next = alist[index + 1][0]

        adict[item] = {'last': last, 'next': next}

    return adict

"""
    Returns (content_type, width, height) for a given img file content
    without using external libraries. GIF, PNG, JPEG are supported.
    http://markasread.net/post/17551554979/get-image-size-info-using-pure-python-code
"""
def get_image_info(data):
    data = str(data)
    size = len(data)
    height = -1
    width = -1
    content_type = ''

    # handle GIFs
    if (size >= 10) and data[:6] in ('GIF87a', 'GIF89a'):
        # Check to see if content_type is correct
        content_type = 'image/gif'
        w, h = struct.unpack("<HH", data[6:10])
        width = int(w)
        height = int(h)

    # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
    # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
    # and finally the 4-byte width, height
    elif ((size >= 24) and data.startswith('\211PNG\r\n\032\n')
          and (data[12:16] == 'IHDR')):
        content_type = 'image/png'
        w, h = struct.unpack(">LL", data[16:24])
        width = int(w)
        height = int(h)

    # Maybe this is for an older PNG version.
    elif (size >= 16) and data.startswith('\211PNG\r\n\032\n'):
        # Check to see if we have the right content type
        content_type = 'image/png'
        w, h = struct.unpack(">LL", data[8:16])
        width = int(w)
        height = int(h)

    # handle JPEGs
    elif (size >= 2) and data.startswith('\377\330'):
        content_type = 'image/jpeg'
        jpeg = StringIO.StringIO(data)
        jpeg.read(2)
        b = jpeg.read(1)
        try:
            while (b and ord(b) != 0xDA):
                while (ord(b) != 0xFF): b = jpeg.read
                while (ord(b) == 0xFF): b = jpeg.read(1)
                if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                    jpeg.read(3)
                    h, w = struct.unpack(">HH", jpeg.read(4))
                    break
                else:
                    jpeg.read(int(struct.unpack(">H", jpeg.read(2))[0])-2)
                b = jpeg.read(1)
            width = int(w)
            height = int(h)
        except struct.error:
            pass
        except ValueError:
            pass

    return content_type, width, height
