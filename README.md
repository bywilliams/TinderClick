# Tinder Auto-Click 
![Badge](https://img.shields.io/static/v1?label=python&message=3.8.3&color=blue&style=for-the-badge&logo=Python)
***
Projeto feito em Python, linguagem de auto nível e interpretativa. 
* Este projeto foi feito em Windows utilizando a IDE Pycharm(Disponível também para Linux)
* Este projeto depende de componentes externos para funcionar (relatados ao decorrer do documento)
### **Intuito**
***
O Intuito do projeto era criar um algoritmo que automatizasse os clicks no botão like(gostei) do tinder e gerasse matchs ao usuário do tinder na Web.
Além de criar um executável com icon para a aplicação.
___
___
### Explicação da Aplicação 
A aplicação tem por finalidade gerar mais matchs ao usuário do tinder na web, sem que este tenha que ficar na frente do seu PC ou notebook clicando no botão like 
&nbsp;

Site do tinder: [Tinder](https://tinder.com)
>**É necessário estar logado no site do tinder.** 
&nbsp;
### Explicando o Código &nbsp;
Explicando as principais funcionalidades no código.

##### Importando package Webbrowser
~~~
import webbrowser 
~~~
Digitar comando webbrowser.open('endereço do site')

~~~
import webbrowser

webbrowser.open('http://www.tinder.com')
~~~
##### Precisamos importar o módulo que dá acesso(controle) ao teclado e mouse
~~~ 
import pyautogui
~~~
##### Aqui fazemos o cursor mover até o botão like
~~~
pyautogui.moveTo(-443,587, duration=1)
~~~
>Obs; É necessário informar uma cordenada X e Y de acordo com aonde o botão like estará na sua tela (monitor).
>Também é preciso informar um duration(tempo(velocidade) até o cursor se mover e chegar no botão like).

##### Laço de repeticão para os clicks
    import time
    i = 0
    while i < 12:
        pyautogui.click()
        time.sleep(0.9)
        i += 1

* i = variável para estrutura de repetição. 
* while = estrutura de reptição usada.
* pyautogui.click() = comando para o click
* time.sleep() = tempo de espera para um novo clik (considerando a animação e tempo para aparecer uma nova pessoa).
* i += 1 = variável é somada e recebe 1.

# Imagem da Aplicação
Agora será mostrado como ficou a aplicação e layout feito por mim.
&nbsp;
![tinder click](/tinderclick.gif)
&nbsp;

### Instalação
Este projeto requer além do Python alguns packages e estes são: 
- Pyautogui:
- Webbrowser,

Obs; **A instalação dos componentes é feita diretamente na IDE Pycharm ou no terminal. O Executável foi gerado através do package pyinstaller com o seguinte comando:**
 ~~~
 pyinstaller -w -F -i "endereço do icone\icon.ico" nomearquivo.py
~~~
## Autor
***
> William Silva -> [Site e portfolio pessoal](https://bywilliams.github.io/portfolio/)

**Agradeço por terem acompanhdo a documentação e a explicação deste pequeno projeto, e trarei mais projetos.**




