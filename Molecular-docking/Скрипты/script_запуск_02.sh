#!/bin/bash

read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1
echo "The program has started"

for d in */ ; 
do
	cd "$d"
	echo "Walking to the $d ..."
	array_check=($(ls | grep conf.txt))
	
	for conf_file in ${array_check[@]}
	do
		echo "Working with $conf_file in $d." 
		log_file_name=""
		number="${conf_file:0:2}"
		log_file_name="$(ls | grep "${number}_log.txt")"
		if test -f "$log_file_name"; then
			echo "$log_file_name in $d exists."
		else
			smina --config "$conf_file"
			log_file_name="$(ls | grep "${number}_log.txt")"
			cat "$conf_file" "$log_file_name" > "out_$log_file_name"
		fi
	done
	echo "Smina finished in the $d"
	cd ..
done

echo "The program is finished"