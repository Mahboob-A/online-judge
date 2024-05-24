#!/bin/bash 


# main volume mount where the code in the volume has been saved. 
volume_mount="/user-codes"

# user_file_parent_dir= is the full path of the file inside the volume: base-dir/user_codes/lang/uuid

g++ $volume_mount$user_file_parent_dir/main.cpp -o $volume_mount$user_file_parent_dir/main 
compile_status=$?

if [ $compile_status -ne 0 ]; then 
    echo "Compile Failed"
    exit $compile_status 
fi

# run the binary 
$volume_mount$user_file_parent_dir/main < $volume_mount$user_file_parent_dir/input.txt > $volume_mount$user_file_parent_dir/output.txt 