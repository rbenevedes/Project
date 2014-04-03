from flask import Flask, render_template, request
import base64
import dynamic
import analysis_2
import os
import tempfile

app = Flask(__name__)

@app.route("/")
def front_page():
    return render_template("recorder.html")

@app.route("/authorized", methods=["POST"])
def authorization():
    audio_data_base64 = request.form.get("audio", "not found")

    with open('test.raw', 'wb+') as f:
        f.write(audio_data_base64)

    # Strip out header crap until the comma
    audio_data_base64 = audio_data_base64[audio_data_base64.index(',')+1:]
    audio_data = base64.b64decode(audio_data_base64)


    with open('test.wav', 'wb+') as f:
        f.write(audio_data)
        
        seqx = analysis_2.master(os.path.abspath("audios/Alohamora_3.wav"))
        seqy = analysis_2.master('test.wav')

        cost = dynamic.dynamicTimeWarp(seqx, seqy)

        match = dynamic.match_test(cost)

    return "hello %r" % cost

if __name__=="__main__":
    app.run(debug=True)