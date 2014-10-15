"""
Utilities powered by the magnificent me.
"""

import os, glob, re, subprocess

def getFilenames(path, byNewest):
        
    files = filter(os.path.isfile, glob.glob(path + "*"))
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

# returns [width, height]
def getImageSize(path):
    if path:
        image_size_as_string = subprocess.Popen(["identify","-format","\"%w,%h\"",path], stdout=subprocess.PIPE).communicate()[0]
        return [ int(x) for x in re.sub('[\t\r\n"]', '', image_size_as_string).split(',') ]

