#!/usr/bin/zsh

rclone mount furnarius-drive-rclone: ~/furnarius-drive-rclone
sleep(10)
st -e vifm ~/furnarius-drive-rclone
