#!/bin/sh

current_dir=$(basename "$PWD")

    cd ..
    rm -rf "$current_dir"
    
    git clone https://www.github.com/NugGETforFREE/kejunwan
    cd
    cd kejunwan
    bash req.sh
    python3 main.py
else
    echo "取消。"
fi