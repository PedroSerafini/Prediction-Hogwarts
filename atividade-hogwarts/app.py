from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

df = pd.read_csv('hogwarts_dataset.csv')

X = df.drop(['AluguelSugerido', 'VendaSugerida'], axis=1)
y_aluguel = df['AluguelSugerido']
y_venda = df['VendaSugerida']
X_train, X_test, y_aluguel_train, y_aluguel_test, y_venda_train, y_venda_test = train_test_split(X, y_aluguel, y_venda, test_size=0.2, random_state=42)

model_aluguel = RandomForestRegressor()
model_aluguel.fit(X_train, y_aluguel_train)

model_venda = RandomForestRegressor()
model_venda.fit(X_train, y_venda_train)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sugerir_valores", methods=["POST"])
def sugerir_valores():

    dados_usuario = request.get_json()

    dados_usuario_df = pd.DataFrame([dados_usuario])

    sugestao_aluguel = model_aluguel.predict(dados_usuario_df)[0]
    sugestao_venda = model_venda.predict(dados_usuario_df)[0]
    
    return jsonify({'SugestaoAluguel': sugestao_aluguel, 'SugestaoVenda': sugestao_venda})

if __name__ == '__main__':
    app.run(debug=True)
