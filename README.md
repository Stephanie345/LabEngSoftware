# Criar ambiente virtual

<p>Criar um diretório</p>
<p>Entrar no diretório</p>
<p>criar o nome do ambiente virtual: python3 -m venv venv</p>
<p>Verificar se foi listado: ls</p>
* Para activar o ambiente virtual:
<p>cd venv</p>
<p>cd Scripts</p>
<p>Para ativar o ambiente virtual: activate</p>
* Para instalar o flask:
<p>pip install flask</p>
* Rodar o arquivo app.py:
<p>python app.py</p>
* Criar o requeriments.txt:
<p>pip freeze > requirements.txt</p>


## arquivo app.py

* Linha 1: faz a importação da classe "Flask" do módulo "flask" e o render_templete
* Linha 3: cria uma instância da classe importada e passamos como argumento "primeira_entrega", indicando para o flask
qual diretório ele deve executar
* Linha 6: utiliza um decorador para criar uma rota."/" indica a rota raiz da aplicação
* Linha 7: defini um método que será executado quando a rota raiz for acessada
* Linha 8: retorna o conteúdo do arquivo index.html contendo as três linhas especificadas no requisito da tarefa
* Linha 9: app.run() função para rodar o arquivo app.py

## arquivo index.html
* Foi criada uma estrutura simples do html
na linha 3,4 e 5 contém as três frases necessárias para a entraga da tarefa que são:
* -Titulo do tarefa
* -Nome e RA
* -Nome do professor
________________________________________
Link do Vídeo:
https://youtu.be/p9qa4Td6-GI

Último commit realizado :
0498e2f12cebe5ff8fa2105ea828ee4b1e8d32cf
