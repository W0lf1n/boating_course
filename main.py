from flask import Flask, render_template, request
import re

trida = {
    "Jmeno": [],
    "Je_plavec": [],
    "Jmeno_kamarada": []
}

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('prvni_stranka.html'), 200


@app.route('/druha_stranka', methods=['GET', 'POST'])
def druha_stranka():
    return render_template('druha_stranka.html', zprava="Tajná zpráva.."), 200

@app.route('/api/name/<name>', methods=['GET'])
def api_check(name):
    if name in trida["Jmeno"]:
        res = ["True"]
        return res
    else:
        res = ["False"]
        return res

@app.route('/form_handler', methods=['GET', 'POST'])
def script():
    test_name = request.form['nick']
    je_plavec = request.form['je_plavec']
    test_friend_name = request.form['kanoe_kamarad']
    surname = request.form['jmeno']
    lastname = request.form['prijmeni']

    if test_name in trida["Jmeno"]:
        return render_template('druha_stranka.html', zprava = "Uzivatel se stejnym jmenem jiz existuje")
    else:
        trida["Jmeno"].append(test_name)
        trida["Je_plavec"].append(je_plavec)
        trida["Jmeno_kamarada"].append(test_friend_name)
        return render_template('prvni_stranka.html') + str(trida)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
