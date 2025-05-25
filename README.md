# 📊Atividade de Inteligência Artificial - Compet 2025

#### Índice

<p align="center"> 
    <a href="#sobre-a-atividade">Sobre a Atividade</a> &nbsp;&nbsp; | &nbsp;&nbsp;
    <a href="#conjunto-de-dados">Conjunto de Dados</a> &nbsp;&nbsp; | &nbsp;&nbsp;
    <a href="#tecnologias-utilizadas">Tecnologias Utilizadas</a> &nbsp;&nbsp; | &nbsp;&nbsp;
    <a href="#como-executar">Como Executar</a> &nbsp;&nbsp; | &nbsp;&nbsp;
    <a href="#autora">Autora</a> &nbsp;&nbsp; 
</p>
<br> 

## Sobre a Atividade 

1. Escolher uma base de dados pública. A base deve possibilitar resolver um problema de CLASSIFICAÇÃO e ter no máximo 10 variáveis.
2. Adicionar a fonte (link dos dados coletados, seja API ou repositório)
3. Fazer uma breve análise exploratória dos dados. Usando pandas e bibliotecas de visualização como matplotlib. Gere gráfico de barras, setores ou scatterplot para algumas variáveis da sua base.
4. Pré-processar os dados (remover variáveis não úteis, tratar valores faltantes, codificar variáveis categóricas etc, se for necessário).
5. Dividir os dados em treino e teste.
6. Treinar e avaliar pelo menos dois modelos de aprendizagem de máquina diferentes. Consulte a biblioteca scikit-learn para técnicas de classificação
7. Escolher o melhor modelo com base na métrica da acurácia (taxa de acerto).

## Conjunto de Dados 

📈 **Base de dados escolhida**: Global Cancer Patients, 2015 - 2024: Cancer Cases Report in all the world in last 10 years.

🔗**Link**: https://www.kaggle.com/datasets/zahidmughal2343/global-cancer-patients-2015-2024/data 

**Descrição**: Este conjunto de dados contém dados globais de pacientes com câncer relatados de 2015 a 2024, projetados para simular os principais fatores que influenciam o diagnóstico, o tratamento e a sobrevivência do câncer. Inclui uma variedade de características comumente estudadas na área médica, como idade, sexo, tipo de câncer, fatores ambientais e comportamentos de estilo de vida.

**Link da interface**: https://76c1eb8d17b44030bc.gradio.live | https://huggingface.co/spaces/xavierruth/predicao-gravidade-cancer 


#### Dicionário de Dados

Através de uma matriz de correlação, foi possível identificar que determinadas caracteristicas indicam os pacientes mais propensos a desenvolver algum tipo de câncer. Logo, podemos perceber que a genética, a exposição a poluição do ar, consumo de alcool, fumante e pessoas com alto nível de obesidade possuem tendencia de desenvolver uma maior gravidade da doença. 

| **Variáveis** | **Descrição** | 
|---------------|---------------| 
| Genética | O quanto a genética influencia no surgimento de um câncer |
| ARPOLUICAO | O quanto a poluição do ar influencia no surgimento de um câncer |
| ALCOOL | O quanto o consumo de bebidas alcólicas influencia no surgimento de um câncer |
| FUMO | O quanto fumar pode influenciar no surgimento de um câncer |
| OBESIDADE | O quanto a obesidade pode influenciar no surgimento de um câncer|
| GRAVE | Nível de gravidade da doença|

## Tecnologias Utilizadas

- Pandas
- Numpy
- Matplotlib
- Scikit-learn
- Seaborn
- Gradio

## Como Executar 

1. Criação do ambiente virtual

``` bash

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
    
```

2. Instalando as dependências 

``` bash

pip install -r requirements.txt
    
```

## Autora 

#### Ruth Xavier 

- [Linkedin](https://www.linkedin.com/in/ruthxavier/)
- [Github](https://github.com/xavierruth)
- [Behance](https://www.behance.net/xavierruth)