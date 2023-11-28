#!/bin/bash

read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

for d in */ ; 
do
	cd "$d"
	config_file_name="$(ls | grep *conf.txt)"
	smina --config "$config_file_name"
	log_file_name="$(ls | grep *log.log)"
	cat "$config_file_name" "$log_file_name" > "out_$log_file_name"
	cd ..

done

echo "Done"