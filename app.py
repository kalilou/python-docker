from flask import Flask, jsonify 



app = Flask(__name__) 


@app.route("/")
def main():
    return jsonify({
            'name': 'Kalilou',
            'lastname': 'Diaby',
            'age': 28,
            'tutorial': 'tetsing ansible'
        })

@app.route("/health")
def health():
    return jsonify({
        'status': '200',
        'message': 'Application up and running'
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
