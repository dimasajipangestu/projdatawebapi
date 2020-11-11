from flask import Flask, request, jsonify
import json

app = Flask(__name__)

def read_file(country_code):
    with open("./dataset2/"+country_code+".json", "r") as read_file:
        data = json.load(read_file)
        return(data)

@app.route('/<country_code>', methods=['GET'])
def country(country_code):
    data = read_file(country_code)
    return jsonify(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        waktu = datetime.now(indonesia)
        new_presensi = Presensi(nama=nama, nim=nim, waktu=waktu)

        try:
            db.session.add(new_presensi)
            db.session.commit()
            return redirect('/')
        except:
            return "Error"

    else:
        presensi = Presensi.query.order_by(Presensi.waktu.desc(), Presensi.nim).all()
        return render_template('index.html', presensi=presensi)

@app.route('/delete/<int:id>')
def delete(id):
    presensi = Presensi.query.get_or_404(id)

    try:
        db.session.delete(presensi)
        db.session.commit()
        return redirect('/')
    except:
        return "Error"

if __name__ == '__main__':
    app.run(debug=True)
