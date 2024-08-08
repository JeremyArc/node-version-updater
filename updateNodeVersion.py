import subprocess
import sys

# Replace this value on your usecase.
NODE_VERSION = "20"
NVM_PATH = "~/.nvm/nvm.sh"

def runCommand(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}\n{result.stderr}")
        sys.exit(1)
    return result.stdout

def checkNVMInstalled():
    try:
        runCommand(f"source {NVM_PATH} nvm -v")
        return True
    except:
        return False

def installNVM():
    print("Installing NVM...")
    runCommand("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash")
    nvmVersion = runCommand(f"source {NVM_PATH} nvm -v")
    print(f"nvm version: {nvmVersion}")

def installNode(version):
    print(f"Installing Node.js version {version}...")
    runCommand(f"brew install node@{version}")

def createNVMRC(version):
    print("Creating .nvmrc file...")
    with open(".nvmrc", "w") as file:
        file.write(version)

def useNode(version):
    print(f"Switching to Node.js version {version}...")
    runCommand(f"source {NVM_PATH} nvm use")

def printNodeVersion():
    version = runCommand("node -v")
    print(f"Current Nodejs version: {version}")

def main():
    if not checkNVMInstalled():
        installNVM()

    installNode(NODE_VERSION)
    createNVMRC(NODE_VERSION)
    useNode(NODE_VERSION)
    printNodeVersion()

if __name__ == "__main__":
    main()