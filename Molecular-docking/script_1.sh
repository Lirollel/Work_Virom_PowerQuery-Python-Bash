#!/bin/bash

find . -type f -name "*f.txt"  -exec smina --config "{}" \; 
