# run_app.py

import subprocess
import webbrowser
import time
import sys
import os

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_path = os.path.join(current_dir, 'app', 'main.py')

    streamlit_cmd = [sys.executable, '-m', 'streamlit', 'run', app_path, '--server.port=8501', '--server.address=localhost']

    process = subprocess.Popen(streamlit_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    time.sleep(5)

    webbrowser.open('http://localhost:8501')

    try:
        process.communicate()
    except KeyboardInterrupt:
        process.terminate()
        print("\nStreamlit app terminated.")

if __name__ == '__main__':
    main()
