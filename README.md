# Criar ambiente virtual

<p>Criar um diretório</p>
<p>Entrar no diretório</p>
<p>Para criar o nome do ambiente virtual: python3 -m venv venv</p>


## arquivo app.py

* Linha 1: faz a importação da classe "Flask" do módulo "flask" e o render_templete
* Linha 3: cria uma instÂncia da classe importada e passamos como argumento "teste_labEng", indicando para o flask
qual arquivo ele deve executar
* Linha 6: utiliza um decorador para criar uma rota."/" indica a rota raiz da aplicação
* Linha 7: defini um método que será executado quando a rota raiz for acessada
* Linha 8: retorna o conteúdo do arquivo index.html contendo as três linhas especificadas no requisito da tarefa

## arquivo index.html
* Foi criada uma estrutura simples do html
na linha 3,4 e 5 contém as três frases necessárias para a entraga da tarefa que são:
* -Titulo do tarefa
* -Nome e RA
* -Nome do professor
