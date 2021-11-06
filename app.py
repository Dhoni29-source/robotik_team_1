from flask import Flask, render_template, request, redirect
import pickle
import sklearn
import numpy as np                        # numpy==1.19.3

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':

        with open('rfc', 'rb') as r:
            model = pickle.load(r)

        suhu = float(request.form['suhu'])
        kelembapan = float(request.form['kelembapan'])
        co = float(request.form['Karbon Monoksida'])
        pm10 = float(request.form['Partikulate matter (PM10)'])

        datas = np.array((suhu,kelembapan,co,pm10))
        datas = np.reshape(datas, (1, -1))

        isDiabetes = model.predict(datas)

        return render_template('hasil.html', finalData=isDiabetes)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
