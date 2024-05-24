#!/bin/bash 

# volume name: user_code_files

# main volume mount where the code in the volume has been saved. 
volume_mount="/user-codes-data"

# in the judge container, the files is stored under: /app/user-files/user_codes/lang/uuid/  (see the docker compose file for volume mount of judge container.)

# user_file_parent_dir= is the full path of the file inside the volume: $volume_mount/user_codes/lang/uuid

g++ $volume_mount$user_file_parent_dir/main.cpp -o $volume_mount$user_file_parent_dir/main 
compile_status=$?

if [ $compile_status -ne 0 ]; then 
    echo "Compile Failed"
    exit $compile_status 
fi

# run the binary 
$volume_mount$user_file_parent_dir/main < $volume_mount$user_file_parent_dir/input.txt > $volume_mount$user_file_parent_dir/output.txt 