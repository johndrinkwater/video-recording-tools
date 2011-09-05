#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Toggle the active window’s window decoration

Author:
	John Drinkwater	<john@nextraweb.com>
"""

from gtk.gdk import *

# TODO supply window ID / program ID via command line

w=window_foreign_new((get_default_root_window().property_get("_NET_ACTIVE_WINDOW")[2][0]))
state = w.property_get("_NET_WM_STATE")[2]
maximized='_NET_WM_STATE_MAXIMIZED_HORZ' in state and '_NET_WM_STATE_MAXIMIZED_VERT' in state
if maximized: w.unmaximize()
if w.get_decorations() == 0 :
    w.set_decorations(DECOR_ALL)
else:
    w.set_decorations(0)

if maximized: w.maximize()
window_process_all_updates()
