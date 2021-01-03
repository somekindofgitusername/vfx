#!/usr/bin/python

import sys
import os
import re
import glob
import fnmatch
import argparse
import itertools 
import subprocess

class Color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

def parse_args():
    """Parse arguments.
    """
    parser = argparse.ArgumentParser(description="Show filepatterns of numbered files")
    parser.add_argument("-s", "--size", help="display size of file patterns", action="store_true")
    parser.add_argument("-m", "--minimal", help="only show file patterns", action="store_true")
    parser.add_argument("-v", "--verbose", type=int, nargs="?", const=1,
                        help="display elements of file patterns with | (present) and . (not present) ")

    args = parser.parse_args()
    return args

def condensed_string(maskString, n):
    """Take a string like |||.|||..... and rewrite in
    in such a way that characters appearing n times contigously
    are reduced to one occurance 
    """
    resultList = []
    for grouping_value, group_items in itertools.groupby(maskString):
        grp = "".join(list(group_items))
        grpLen = len(grp)
        multiple = (grpLen / n)
        remainder = grpLen%n
        itemType = grouping_value
        condensedItemType = Color.UNDERLINE + Color.BOLD + Color.RED + str(itemType) + Color.END
        condensedValue = condensedItemType*multiple + itemType*remainder
        resultList.append(condensedValue)

    return " verbosity on ("+str(n)+"s):"+"".join(resultList)

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r"(\d+)", text) ]

def contains_digit(s):
    """Find all files that contain a number and store their patterns.
    """
    isdigit = str.isdigit
    return any(map(isdigit,s))

def frames_ascii(minFrameNum, maxFrameNum, frames):
    """Loop over file patterns and compute ranges.
    """
    framesRepresentation = []
    for i in  range(minFrameNum, maxFrameNum):
        if i in frames:
            framesRepresentation.append("|")
        else:
            framesRepresentation.append(".")
    return framesRepresentation

def get_work_items(cwd):
    """Return work items aka the list of files to process.
    """
    items = filter(lambda f: not f.startswith("."), os.listdir(cwd) ) 
    items = filter(lambda f: not os.path.isdir(f), items)
    items = filter(contains_digit, items)
    filePatterns = {}
    for item in items:
        m = re.search(r"\d+(?=\D*$)", item) #search for a number starting at the string"s back
        
        frameNum = int(m.group(0))
        fileItem = item.rsplit(str(frameNum), 1) #split only once from back
        filePatterns[fileItem[0]]=[fileItem[0], fileItem[-1]]
    return(filePatterns, items)


#===== MAIN =======================================================================

def main():
    """ Loop over relevant files (work items) in current directory and
    extract their number terminated patterns. Give additional 
    information according to command options.
    """
    cwd = os.getcwd()

    args = parse_args()
    workItems = get_work_items(cwd)
    filePatterns = workItems[0]
    items = workItems[1]

    result = []
    for k,v in filePatterns.items():
        filePattern = "*".join(v)
        filePatternMatches = fnmatch.filter(items, filePattern)
        
        minFrameNum = None
        maxFrameNum = None
        currentFrameNum = None
        
        frames = []
        for fileName in filePatternMatches:
            m = re.search(r"\d+(?=\D*$)", fileName)
            currentFrameNum = int(m.group(0))
            frames.append(currentFrameNum) #list of all frames
            if minFrameNum==None:
                minFrameNum = currentFrameNum
                maxFrameNum = currentFrameNum
            else:    
                minFrameNum = min(minFrameNum, currentFrameNum)
                maxFrameNum = max(maxFrameNum, currentFrameNum)

        #------ arguments and options ------------------------------
        if args.minimal:
            message = filePattern
        else:
            message = filePattern + "\t----> has range: "+ str(minFrameNum) +"..."
            message += str(maxFrameNum) +"\tcompleted( "+ str(len(filePatternMatches)) + " )"

        #adds ASCII representation of frames
        if args.verbose:
            verboseMessage = "\nframes: " + "".join( frames_ascii(minFrameNum, maxFrameNum, frames) ) 
            if args.verbose>1:
                verboseMessage = condensed_string(verboseMessage, args.verbose)

            message += verboseMessage

        #add total filesize per filepattern
        if args.size:
            cmd = "du -h -c "+filePattern+" | tail -1"
            cmdOut = subprocess.check_output(cmd, shell=True).split()[0]
            message += " total size: "+ str(cmdOut)
        #------/arguments and options -----------------------------
        
        result.append(message)


    result.sort(key=natural_keys)   
    for thing in result:
        print thing

#===== /MAIN ========================================================================

if __name__ == "__main__":
    sys.exit(main())
