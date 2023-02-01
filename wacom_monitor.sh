#!/bin/bash
if [[ $(xrandr -q | grep 'DP1 connected 1920') ]]; then
#	xsetwacom set 9 MapToOutput 1920x1296+0+0
#	xsetwacom set 14 MapToOutput 1920x1296+0+0
#	xsetwacom set xsetwacom list devices | cut -d : -f 2 | cut -d   -f 2 | cut -c 1-2
	pen_id=$( xsetwacom list devices | cut -d : -f 2 | cut -d ' ' -f 2 | cut -c 1-2 | cut -d ' ' -f 2 | cut -d$'\n' -f 1
)
	eraser_id=$( xsetwacom list devices | cut -d : -f 2 | cut -d ' ' -f 2 | cut -c 1-2 | cut -d ' ' -f 2 | cut -d$'\n' -f 2
)

	xsetwacom set $pen_id MapToOutput 1920x1296+0+0
	xsetwacom set $eraser_id MapToOutput 1920x1296+0+0
fi