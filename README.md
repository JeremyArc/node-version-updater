# Node Version Updater

This Python script checks if Node.js is installed, installs it if necessary, creates a `.nvmrc` file with the specified Node.js version, and switches to that version using `nvm`.


## Overview

This script are going to do the following:
1. Check if nvm is installed and install it if necessary.
2. Install the specified Node.js version.
3. Create a .nvmrc file with the specified Node.js version.
4. Use nvm to switch to the specified Node.js version.
5. Print the current Node.js version to the terminal.

## Disclaimer

This project assume you are using macOS machine.

## Prerequisite

1. install Python on your machine.

    ```bash
    brew install python
    ```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/JeremyArc/node-version-updater.git
   cd node-version-updater
   ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

1. Run the script:

    ```bash
    python updateNodeVersion.py
    ```
