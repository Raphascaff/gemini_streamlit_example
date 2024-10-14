import subprocess

if __name__ == "__main__":
    process = subprocess.Popen(
        ["streamlit", "run", "main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    for line in iter(process.stdout.readline, b''):
        print(line.decode().strip())

    process.wait()