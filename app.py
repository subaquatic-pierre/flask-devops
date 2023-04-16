from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import subprocess
from pathlib import Path
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

app = Flask(__name__)
CORS(app, origins=["*"], methods=["*"])


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, "static"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )


@app.route("/rebuild", methods=["POST"])
def rebuild():
    data = request.get_json()

    # Set project envs for script
    os.environ["PROJECT_DIR"] = data.get("projectDir")
    root_password = os.environ.get("ROOT_PASSWORD")
    os.environ["ROOT_PASSWORD"] = root_password

    secret = data.get("password")
    project_dir = data.get("projectDir")
    build_script = data.get("buildScript")

    api_password = os.environ.get("API_PASSWORD")

    if secret != api_password:
        return jsonify({"stderr": "Incorrect password", "stdout": ""})

    file_path = Path(project_dir, build_script)

    output = subprocess.run([file_path.absolute()], capture_output=True)
    stdout = output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    print(f"stdout: {stdout} \n stderr: {stderr}")
    sleep(2)

    return jsonify({"stderr": stderr, "stdout": stdout})


if __name__ == "__main__":
    app.run("127.0.0.1", 8001, debug=True)
    # serve(app, host='127.0.0.1', port=8001, url_scheme='https')
