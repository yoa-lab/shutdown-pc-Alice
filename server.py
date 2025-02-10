import subprocess
import logging

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/shutdown', methods=['GET'])
def shutdown_server():
    try:
        subprocess.call('D:/shutdown_alice/shutdown.bat', stdout=logging.sys.stdout, stderr=logging.sys.stderr)
        return 'Script executed successfully', 200
    except Exception as e:
        return f'Error: {str(e)}', 500

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host='0.0.0.0', port=8000)
