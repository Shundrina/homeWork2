from flask import Flask, render_template
from flask import request
from cryptography.fernet import Fernet

app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)


@app.route('/encrypt')
def encrypt():
    """Function gets parameter in string and encrypts it."""
    string = request.args.get('string', '')
    result = f.encrypt(string.encode())
    res_string = result.decode()
    return render_template('index.html', string='Encrypted string:', value=res_string)


@app.route('/decrypt')
def decrypt():
    """Function gets parameter in string and decrypts it."""
    string = request.args.get('string', '')
    result = f.decrypt(string.encode())
    res_string = result.decode()
    return render_template('index.html', string='Encrypted string:', value=res_string)


app.run(debug=True)
