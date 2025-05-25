import pickle
import pandas as pd
import gradio as gr

# Carregar modelo
with open("./modelotreinado.pkl", "rb") as f:
    modelo = pickle.load(f)

# Dicionário para decodificar o resultado
inverse_map_gravidade = {0: 'Leve', 1: 'Moderado', 2: 'Severo'}

# Função de predição
def gravidade_cancer(GENETICA, ARPOLUICAO, ALCOOL, FUMO, OBESIDADE):
    dados = pd.DataFrame({
        "GENETICA": [GENETICA],
        "ARPOLUICAO": [ARPOLUICAO],
        "ALCOOL": [ALCOOL],
        "FUMO": [FUMO],
        "OBESIDADE": [OBESIDADE]
    })
    predicao = modelo.predict(dados)[0]
    return f"A gravidade do câncer é: {inverse_map_gravidade.get(predicao, 'Desconhecida')}"

# Interface
interface = gr.Interface(
    fn=gravidade_cancer,
    inputs=[
        gr.Slider(0, 10, step=1, label="Predisposição genética para câncer"),
        gr.Slider(0, 10, step=1, label="Intensidade da poluição do ar na sua região"),
        gr.Slider(0, 10, step=1, label="Consumo de álcool"),
        gr.Slider(0, 10, step=1, label="Nível de fumo"),
        gr.Slider(0, 10, step=1, label="Grau de obesidade")
    ],
    outputs=gr.Textbox(label="Resultado da Predição", lines=3),
    title="Predição da Gravidade do Câncer",
    description="""
    Informe seus fatores de risco utilizando os controles deslizantes abaixo para prever a possível gravidade do câncer.
    Os valores devem ir de 0 (baixo risco) até 10 (alto risco).
    """
)

# Lançar a interface
interface.launch(share=False)

