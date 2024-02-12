#!/bin/bash

# Define commands to run
commands=(
    "help"
    "all MyModel"
    "show BaseModel"
    "show BaseModel My_First_Model"
    "create BaseModel"
    "all BaseModel"
    "show BaseModel 49faff9a-6318-451f-87b6-910505c55907"
    "destroy"
    "update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name 'Betty'"
    "update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name Betty salim"
    "show BaseModel 49faff9a-6318-451f-87b6-910505c55907"
    "create BaseModel"
    "all BaseModel"
    "destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907"
    "show BaseModel 49faff9a-6318-451f-87b6-910505c55907"
)

# Run each command
for cmd in "${commands[@]}"; do
    output=$(echo "$cmd" | ./console.py)
    if [[ $output == *"FAIL"* ]]; then
        echo "$cmd: FAIL"
    else
        echo "$cmd: OK"
    fi
done
