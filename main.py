from flask import Flask, render_template, request
import json

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')


def in_file(string):
    with open("static/users.json", "r") as fo:
        data = fo.read()
        return string in data


with open('static/users.json', 'r') as file:
    json_object = json.load(file)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('prvni_stranka.html', len=len(json_object), file_users=json_object), 200


@app.route('/druha_stranka', methods=['GET', 'POST'])
def druha_stranka():
    return render_template('druha_stranka.html', zprava="Tajná zpráva.."), 200


@app.route('/api/name/<name>', methods=['GET'])
def api_check(name):
    if in_file(name):
        res = ["True"]
        return res
    else:
        res = ["False"]
        return res


@app.route('/form_handler', methods=['GET', 'POST'])
def script():
    test_name = request.form['nick']
    je_plavec = request.form['je_plavec']
    if je_plavec:
        je_plavec = "Plavec"
    else:
        je_plavec = "Neplavec"
    test_friend_name = request.form['kanoe_kamarad']
    surname = request.form['jmeno']
    lastname = request.form['prijmeni']

    if in_file(test_name):
        return render_template('druha_stranka.html', zprava="Uzivatel se stejnym jmenem jiz existuje")
    else:
        data = {
            "Jmeno": surname,
            "Prijmeni": lastname,
            "Prezdivka": test_name,
            "Plave": je_plavec,
            "Kamarad": test_friend_name
        }
        data_json = json.dumps(data, indent=5)

        with open("static/users.json", "a") as fo:
            fo.write(data_json)

        return render_template('druha_stranka.html'), 200


@app.route('/feedback', methods=['GET', 'POST'])
def feedback_page():
    return render_template('feedback.html'), 200


@app.route('/feedback/send', methods=['GET', 'POST'])
def feedback_script():
    text = request.form['feedback']
    with open('static/feedbacks.txt', 'a') as fi:
        fi.write(text + "\n")
    return render_template('feedback.html', zprava="Feedback uspesne ulozen"), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
