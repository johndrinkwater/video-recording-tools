#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Sets the active window’s window size to 720p

Author:
	John Drinkwater	<john@nextraweb.com>
"""

from gtk.gdk import *

# TODO take --metrics or something to set via command line
# TODO supply window ID / program ID via command line

newwidth = 1280
newheight = 720

# get window
ourwindow = window_foreign_new((get_default_root_window().property_get("_NET_ACTIVE_WINDOW")[2][0]))
currentpos = ourwindow.get_frame_extents()

# get desktop
desktop = get_default_root_window()
desktopsize = desktop.get_frame_extents()

# find new top left
x,y,w,h = desktopsize 
w -= newwidth
h -= newheight
w /= 2
h /= 2 

# resize and move to central position
ourwindow.move_resize(w, h, newwidth, newheight)

# push update
window_process_all_updates()
