from flask import Flask, render_template, jsonify
import subprocess
from pathlib import Path

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/rebuild/<secret>")
def rebuild(secret):
    if secret != "supersecretpassword":
        return jsonify({"error": "incorrect password"})

    file_path = Path(
        "/home/pierre/Projects/Codativity/strapi/scripts/rebuild-frontend.sh"
    )

    # If your shell script has shebang,
    # you can omit shell=True argument.
    output = subprocess.run([file_path.absolute()], capture_output=True)
    stdout = output.stdout.decode("utf-8")
    stderr = output.stderr.decode("utf-8")
    print(f"stdout: {stdout} \n stderr: {stderr}")
    return jsonify({"stderr": stderr, "stdout": stdout})


if __name__ == "__main__":
    app.run("127.0.0.1", 8001)
