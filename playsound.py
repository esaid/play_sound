import subprocess
import os

def play_sound(file_path):
    """Plays a WAV file using the system's aplay utility."""
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return

    try:
        # aplay is a standard ALSA command-line sound player on Linux
        subprocess.run(["aplay", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error playing sound: {e}")
    except FileNotFoundError:
        print("Error: 'aplay' command not found. Please ensure alsa-utils is installed.")

if __name__ == "__main__":
    play_sound("coq.wav")
