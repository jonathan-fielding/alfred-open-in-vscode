# -*- coding: utf-8 -*-

# Copy Paths to Clipboard
# Workflow For Alfred 2
# Jonathan Fielding 2017
# https://github.com/jonathan-fielding/alfred-open-in-vscode
# based on http://github.com/franzheidl/copy-paths-to-clipboard Franz Heidl 2013 - 2014 
# MIT license.


import sys
import subprocess
from CopyAllPaths import CopyAllPaths
from AlFeedback import Feedback
from urllib import unquote

def main(q=False):

  paths = ((subprocess.check_output(['osascript', 'allpaths.applescript'])).strip()) # returns file urls string
  f_icon_name = "copypaths"

  if paths != "":
    p = CopyAllPaths(paths) #--> file ulrs array
    f_title = "File to open in Visual Studio:"
    posixPaths = ((subprocess.check_output(['osascript', 'fileurl_to_posix.applescript', paths])).strip())
    
    f_icon_name += "_posix"
    paths = unquote(posixPaths).decode('utf-8')

    f_sub = paths
    f_valid = "yes"

  else:
    f_icon_name += "_error"
    f_title = "Copy Paths:"
    f_sub = "Couldn't get any the file path"
    f_valid = "no"
  f_icon = f_icon_name + ".png"

  feedback = Feedback()
  feedback.addItem(title=f_title, subtitle=f_sub, valid=f_valid, arg=paths, icon=f_icon)
  print feedback

if  __name__ =="__main__":
  main(sys.argv[1:])
