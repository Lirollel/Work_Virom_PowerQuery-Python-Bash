#!/bin/bash

read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
echo "The program has started"

for d in */ ; 
do
	cd "$d"
	echo "Walking to the $d ..."
	check=""
	check="$(ls | grep out*)"
	if test -f "$check"; then
		echo "$check in $d exists."
		cd ..
	else
		config_file_name="$(ls | grep *conf.txt)"
		smina --config "$config_file_name"
		log_file_name="$(ls | grep *log.log)"
		cat "$config_file_name" "$log_file_name" > "out_$log_file_name"
		echo "Smina finished in the $d"
		cd ..
	fi
done

echo "The program is finished"