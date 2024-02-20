import subprocess

def install_dependencies():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def run_batch_script():
    try:
        subprocess.run(['requirements.txt'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    install_dependencies()
    run_batch_script()
