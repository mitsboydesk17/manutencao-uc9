# 👾 Atividade 7 – Versionamento com Git

---

### Introdução:

Na atividade 7 iremos colocar em dia a prática de controle de versão utilizando o GitHub em 10 códigos com erros.

---

Objetivos: 

1. Crie um repositório no GitHub chamado manutencao-uc09.
2. Faça o primeiro commit com um arquivo README.md.
3. Crie uma branch chamada correcao-bug.
4. Corrija uns erros simples em código fornecido pelo professor.
5. Realize o merge da branch correcao-bug para a branch principal (main ou master).

---

# Desafio 1

### Código problematico:

def dividir(a, b):
return a / b
a = 10
b = 0
resultado = dividir(a, b)
print(f"O resultado da divisão é: {resultado}")

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio.py](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio.py)

### Erros Encontrados:

- Não possui a condição if e um return de debug

### Melhorias:

- Adição da função if b==0, se ele for igual a zero apresentara um erro de divisão por zero

---

# Desafio 2

### Código problemático:

nome_usuario = "Professor(a)"
print("Olá, " + nome_usuar)

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio2.py](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio2.py)

### Erros Encontrados:

- Possui um erro ao chamar “nome_usuario” esta definido como nome_usuar

### Melhorias:

- Corrigindo o nome de “nome_usuar” para “nome_usuario”

---

# Desafio 3

### Código problemático:

frutas = [maçã, "banana", "laranja"]
print(f"Minhas frutas favoritas: {frutas}")

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio3.py](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio3.py)

---

# Desafio 4

### Código problemático:

![Captura de tela 2025-10-07 151358.png](Captura_de_tela_2025-10-07_151358.png)

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio4.html](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio4.html)

### Erros Encontrados:

- nome da tag <p> de paragrafo com fechamento de </pa>

### Melhorias:

- Corrigindo a tag de fechamento </pa> para

</p>

---

# Desafio 5

### Código problemático:

.titulo {
font-size: 24px;
color: blue
background-color: yellow;
padding: 10px

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio5.css](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio5.css)

### Erros Encontrados:

- a estilização de color: blue não possui fechamento com ;

### Melhorias:

- Adicionamos ; ao final da estilização de color = color: blue;

---

# Desafio 6

### Código problemático:

let valor = 5;
let elemento = document.getElementById("status");
if (valor = 10) {
elemento.innerText = "A condição é sempre verdadeira! (Bug de Lógica)";
} else {
elemento.innerText = "A condição é falsa.";
}

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio6.js](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio6.js)

### Erros Encontrados:

- função document.GetElementById(”status”)
- valor esta definido como 10

### Melhorias:

- Trocamos a função próblematica document.GetElementById(”status”) e alteramos para decodeURIComponent
- Corrigimos a definição de (” valor = 10 ”) para (” valor ===  10 ”) se o valor for igual a 10 apresentação a condição e falsa

---

# Desafio 7

### Código problemático:

# from django.http import HttpResponse
def saudacao(request):
return HttpResponse("Olá do Django!")

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio7.py](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio7.py)

### Erros Encontrados:

- a parte de importação do django esta comentada por hashtag #

### Melhorias:

- Concertamos a importação do django retirando o comentário

---

# Desafio 8

### Código problemático:

from django.urls import path
from . import views
def outra_view(request):
pass
urlpatterns = [
path('ola/', views.saudacao)
path('outra/', views.outra_view),
]

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio8.py](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio8.py)

### Erros Encontrados:

- na primeira importação do path ( path('ola/', views.saudacao) ) não possui uma virgula no final

### Melhorias:

- importamos o path corretamente e adicionando a virgula ao final: “  path('ola/', views.saudacao), ”

---

# Desafio 9

### Código problemático:

from kivy.app import Ap
from kivy.uix.label import Label
class MinhaApp(Ap):
def build(self):
return Label(text='Kivy App com Bug de Importação')
MinhaApp().run()

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio9.py](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio9.py)

### Erros Encontrados:

- importação incorreta de App com Ap
- Erro na class MinhaApp(Ap)

### Melhorias:

- Corrigindo o nome de Ap Para App tanto na clase quanto na importação

---

# Desafio 10

### Código problemático:

from kivy.app import App
from kivy.uix.button import Button
class OutraApp(App):
def build(self)
Button(text='Corrija o Retorno!').run()
OutraApp().run()

### Código corrigido

[https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio10.py](https://github.com/mitsboydesk17/manutencao-uc9/blob/main/desafio10.py)

### 

### Erros Encontrados:

- Um Button sem um return Button(text='Corrija o Retorno!').run()

### Melhorias:

- Adicionamos um return  Button(text='Corrija o Retorno!').run()
