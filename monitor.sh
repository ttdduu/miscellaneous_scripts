#!/bin/bash

external_monitor=HDMI1
main_monitor=eDP1

pen_id=$( xsetwacom list devices | cut -d : -f 2 | cut -d ' ' -f 2 | cut -c 1-2 | cut -d ' ' -f 2 | cut -d$'\n' -f 1
)
eraser_id=$( xsetwacom list devices | cut -d : -f 2 | cut -d ' ' -f 2 | cut -c 1-2 | cut -d ' ' -f 2 | cut -d$'\n' -f 2
)

if [[ $1 = off ]]
then

	bspc monitor $main_monitor -a Desktop # Temp desktop because one desktop required per monitor
	bspc wm -O $main_monitor $external_monitor
	# Move everything to $external monitor to reorder desktops

	for desktop in $(bspc query -D -m $main_monitor)
	do
		bspc desktop $desktop --to-monitor $external_monitor
	done

	# Now move everything back to internal monitor
	bspc monitor $external_monitor -a Desktop # Temp desktop

	for desktop in $(bspc query -D -m $external_monitor)
	do
		bspc desktop $desktop --to-monitor $main_monitor
	done

	bspc desktop Desktop --remove # Remove temp desktops

	xrandr --output $external_monitor --off &
	bspc config border_width         2
	bspc config window_gap         8

	xsetwacom set $pen_id MapToOutput 2189x1459+0+0
	xsetwacom set $eraser_id MapToOutput 2189x1459+0+0
	#son 2736x1824 multiplicados por el scale que
	#pongo en bsprc
	feh --bg-fill ~/media/Pictures/bosque_sur.jpg
fi

if [[ $1 = on ]]
then

	desktops=5 # How many desktops to move to the second monitor

	for desktop in $(bspc query -D -m $main_monitor | sed "$desktops"q)
	do
		bspc desktop $desktop --to-monitor $external_monitor
	done

  # Remove "Desktop" created by bspwm
  	bspc desktop Desktop --remove

	feh --bg-fill ~/media/Pictures/bosque_sur.jpg
 fi
