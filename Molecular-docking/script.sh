#!/bin/bash

read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

for d in */ ; 
do
	cd "$d"
	config_file_name="$(ls | grep *f.txt)"
	smina --config "$config_file_name"
	sleep 30m
	cd ..

done

echo "Done"