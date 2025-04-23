from flask import Flask, render_template, request, send_file
import pandas as pd
from gerador_cnab import gerar_cnab
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar', methods=['POST'])
def gerar():
    arquivo = request.files['arquivo_csv']
    if not arquivo:
        return 'Nenhum arquivo enviado', 400

    df = pd.read_csv(arquivo)
    conteudo_cnab = gerar_cnab(df)

    buffer = io.BytesIO()
    buffer.write(conteudo_cnab.encode('utf-8'))
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name='cnab240.txt',
        mimetype='text/plain'
    )

if __name__ == '__main__':
    app.run(debug=True)
