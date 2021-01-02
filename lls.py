#!/usr/bin/python
import sys, os, re, glob, fnmatch

#======argparse===================================================================
import argparse

parser = argparse.ArgumentParser(description='Show filepatterns of numbered files')
parser.add_argument('-s', '--size', help='display size of file patterns', action='store_true')
parser.add_argument('-v', '--verbose', type=int, nargs="?", const=1, help='display elements of file patterns with | (present) and . (not present) ')#, action='store_true')

args = parser.parse_args()
#=======/argparse==================================================================


def condensedString(l, n):
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

    resultList = []
    import itertools
    for grouping_value, group_items in itertools.groupby(l):
        grp = ''.join(list(group_items))
        grpLen = len(grp)
        multiple = (grpLen / n)
        remainder = grpLen%n
        itemType = grouping_value
        condensedItemType = color.UNDERLINE + color.BOLD + color.RED + str(itemType) + color.END
        condensedValue = condensedItemType*multiple + itemType*remainder
        #print itemType, grpLen, multiple, remainder, " --->", condensedValue
        resultList.append(condensedValue)
        
    return " verbosity on ("+str(n)+"s):"+''.join(resultList)

cwd = os.getcwd()
#==================================================================================

#Find all files that contain a number and store their patterns
def contains_digit(s):
    isdigit = str.isdigit
    return any(map(isdigit,s))

items = filter(lambda f: not f.startswith('.'), os.listdir(cwd) ) 
items = filter(lambda f: not os.path.isdir(f), items)
items = filter(contains_digit, items)

filePatterns = {}
for item in items:
    m = re.search(r'\d+(?=\D*$)', item) #search for a number starting at the string's back
    
    frameNum = int(m.group(0))
    fileItem = item.rsplit(str(frameNum), 1) #split only once from back
    fileList = [fileItem[0], frameNum, fileItem[1]]
    filePatterns[fileItem[0]]=[fileItem[0], fileItem[-1]]


#Loop over file patterns and compute ranges
def framesAscii(minFrameNum, maxFrameNum, frames):
    framesRepresentation = []
    for i in  range(minFrameNum, maxFrameNum):
        if i in frames:
            framesRepresentation.append("|")
        else:
            framesRepresentation.append(".")
    return framesRepresentation

result = []
for k,v in filePatterns.items():
    filePattern = "*".join(v)
    filePatternMatches = fnmatch.filter(items, filePattern)
    
    minFrameNum = None
    maxFrameNum = None
    currentFrameNum = None
    frames = []
    for fileName in filePatternMatches:
        m = re.search(r'\d+(?=\D*$)', fileName)
        currentFrameNum = int(m.group(0))
        frames.append(currentFrameNum) #list of all frames
        if minFrameNum==None:
            minFrameNum = currentFrameNum
            maxFrameNum = currentFrameNum
        else:    
            minFrameNum = min(minFrameNum, currentFrameNum)
            maxFrameNum = max(maxFrameNum, currentFrameNum)

    message = filePattern + "\t----> has range: "+ str(minFrameNum) +"..." + str(maxFrameNum) +"\tcompleted( "+ str(len(filePatternMatches)) + " )"

    #adds ASCII representation of frames
    if args.verbose:
        visualMessage = "\nframes: " + "".join( framesAscii(minFrameNum, maxFrameNum, frames) ) 
        if args.verbose>1:
            visualMessage = condensedString(visualMessage, args.verbose)
        message += visualMessage

    #add total filesize per filepattern
    if args.size:
        import subprocess
        cmd = "du -h -c "+filePattern+" | tail -1"
        cmdOut = subprocess.check_output(cmd, shell=True).split()[0]
        message += " total size: "+ str(cmdOut)
        
    result.append(message)

#==================================================================================
#print sorted file patterns with ranges
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

result.sort(key=natural_keys)   

for thing in result:
    print thing

