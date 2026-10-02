
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    return render_template('index.html')
    
@app.route('/equipe')
def equipe ():
    return render_template('equipe.html')


if __name__ == '__main__':
    
    app.run(debug=True)



from flask import Flask, render_template, request

app = Flask(__name__)

# Fatores e nomes de exibição para a Calculadora de Carbono
FATORES_IMC = {
    'nome': text,
    'peso': 0.00,
    'altura': 0.00,
    
}

@app.route('/')
def index():
    """Página inicial com os 3 cards dos projetos e equipe."""
    return render_template('index.html')


@app.route('/imc', methods=['GET', 'POST'])
def calculadora_imc():
    """Tema A: Calculadora IMC."""
    erros = []
    resultado = None
    dados_form = {
        'nome': '',
        'peso': '',
        'altura': '',
    }

    if request.method == 'POST':
        nome_str = request.form.get('nome', '').strip()
        peso_str = request.form.get('peso', '').strip()
        altura_str = request.form.get('altura', '').strip()
        
        dados_form['nome'] = nome_str
        dados_form['peso'] = peso_str
        dados_form['altura'] = altura_str
        

        nome = None
        peso = None
        altura = None

        # Validação do campo Peso
        if not peso_str_str:
            erros.append('Informe o peso atual.')
        else:
            try:
                peso = float(peso_str.replace(',', '.'))
                if peso <= 0:
                    erros.append('peso não pode ser 0.')
            except ValueError:
                erros.append('Peso inválido.')

        # Validação Altura
        if not altura_str:
            erros.append('Informe a sua altura.')
        else:
            try:
                altura = float(altura_str)
                if altura < 1 or altura > 7:
                    erros.append('obrigatório, de 0,5 a 2,5.')
            except ValueError:
                erros.append('altura inválida.')


        # Cálculo e classificação se não houver erros
        if not erros:
            imc = peso * altura ^2
           
          
            # Classificação por faixas usando if / elif / else
            if imc <= 18.5:
                faixa = 'Abaixo do peso'
                classe_alerta = 'aalert-info'
                icone = '🔵'
            elif imc <= 25 :
                faixa = 'Peso Normal'
                classe_alerta = 'alert-success'
                icone = '🟢'
            elif imc  <= 30:
                faixa = 'Sobrepeso'
                classe_alerta = 'alert-warning'
                icone = '🟡'
            else:
                faixa = 'Obesidade'
                classe_alerta = 'alert-danger'
                icone = '🔴'

            resultado = {
                'peso': peso,
                'altura': altura,
                'nome': NOME[nome],
                'imc': imc,
                'faixa': faixa,
                'classe_alerta': classe_alerta,
                'icone': icone
            }

    return render_template(
        'index.html',
        erros=erros,
        resultado=resultado,
        dados_form=dados_form
    )


@app.route('/equipe')
def pagina_equipe():
    """Página de apresentação da equipe do projeto."""
    return render_template('equipe.html')


if __name__ == '__main__':
    app.run(debug=True)