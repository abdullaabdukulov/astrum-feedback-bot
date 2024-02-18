#!/bin/bash

# Function to generate .env file
generate_env_file() {
    echo "Generating .env file..."
    echo "BOT_TOKEN=\"YOUR BOT TOKEN\"" > .env
    echo "ADMINS=\"YOUR ID\"" >> .env
    echo "ip=\"localhost\"" >> .env
    echo "Done."
}

if [ -f .env]; then
    echo ".env file already exists."
else
    generate_env_file
fi
