#!/bin/bash

read -p "Continue? (Y/N): " confirm && [[ $confirm == [yY] || $confirm == [yY][eE][sS] ]] || exit 1

for d in */ ; 
do
	cd "$d"
	check=""
	check="$(ls | grep out*)"
	if test -f "$check"; then
		echo "$check exist."
		cd ..
	else
		echo "$check does not exist."
		cd ..
	fi
done

echo "Done"