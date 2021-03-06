Operadores Aritméticos
Assim como qualquer outra linguagem de programação, subtração, multiplicação, e operadores de divisão podem ser usados com números.

número = 1 + 2 * 3 / 4.0
Tente adivinhar qual será a resposta. Será que Python segue a ordem de operações?

Outro operador disponível é o operador de módulo (%), que retorna o número que é o resto da divisão. Dividendo % divisor = resto.

resto = 11 % 3
Usar dois símbolos de multiplicação forma um relacionamento de potenciação.

quadrado = 7 ** 2
cubo = 2 ** 3
Usando Operadores Com Strings
Python suporta concatenar strings usando o operador de adição:

olamundo = "ola" + " " + "mundo"
Python também suporta multiplicar strings para formar uma string com uma sequência repetida:

varios-ois = "oi" * 10
Usando Operadores Com Listas
Listas podem ser combinadas com operadores de adição:

numeros_pares = [2,4,6,8]
numeros_impares = [1,3,5,7]
todos_numeros = numeros_impares + numeros_pares

Assim como em strings, Python suporta a formação de novas listas com uma sequência repetida usando o operador de multiplicação:

print [1,2,3] * 3
////////////////////////////////////////////////////////

Variáveis, constantes e literais do Python
Neste artigo, você aprenderá sobre variáveis ​​Python, constantes, literais e seus casos de uso.

Índice
Variável
Declarando Variáveis ​​em Python
Atribuindo valor a uma variável em Python
Constantes
Atribuindo valor a uma constante em Python
Regras e Convenção de Nomenclatura de Variáveis ​​e Constantes
Literais
Literais Numéricos
Literais de cordas
Literatura Booleana
Literais Especiais
Coleção Literal
Variável
Na maioria das linguagens de programação, uma variável é um local nomeado usado para armazenar dados na memória. Cada variável deve ter um nome exclusivo chamado identificador. É útil pensar em variáveis ​​como contêiner que armazenam dados que podem ser alterados posteriormente durante a programação.

Não tecnicamente, você pode supor variável como um saco para armazenar livros nele e esses livros podem ser substituídos a qualquer momento.

Nota: No Python, não atribuímos valores às variáveis, enquanto o Python fornece a referência do objeto (valor) à variável.

Declarando Variáveis ​​em Python
No Python, as variáveis ​​não precisam de declaração para reservar espaço de memória. A "declaração de variável" ou "inicialização variável" acontece automaticamente quando atribuímos um valor a uma variável.

Atribuindo valor a uma variável em Python
Você pode usar o operador de atribuição =para atribuir o valor a uma variável.

Exemplo 1: Declarando e atribuindo um valor a uma variável
script.py
Shell IPython

Corre
Alimentado por DataCamp
Quando você executa o programa, a saída será:

Apple.com
No programa acima, atribuímos um valor Apple.comao site da variável . Em seguida, imprimir o valor atribuído ao website ie Apple.com.

Nota: Python é um tipo de linguagem inferida , ele pode inferir automaticamente (saber) Apple.comé um String e declarar o site como uma String.

Exemplo 2: Alterando o valor de uma variável
script.py
Shell IPython

Corre
Alimentado por DataCamp
Quando você executa o programa, a saída será:

Programiz.com
No programa acima, atribuímos novo valor Programiz.comao site . Agora, o novo valor Programiz.comsubstituirá o valor antigo Apple.com. Para a confirmação, imprimimos o site e exibiremos novo valor Programiz.com.

Exemplo 3: Atribuindo vários valores a várias variáveis
script.py
Shell IPython

Corre
Alimentado por DataCamp
Se queremos atribuir o mesmo valor a múltiplas variáveis ​​de uma só vez, podemos fazer isso como

script.py
Shell IPython

Corre
Alimentado por DataCamp
O segundo programa atribui a samestring a todas as três variáveis x , y e z .

Constantes
Uma constante é um tipo de variável cujo valor não pode ser alterado. É útil pensar em constantes como contêineres que contêm informações que não podem ser alteradas posteriormente.

Não tecnicamente, você pode pensar em constante como uma bolsa para armazenar alguns livros e esses livros não podem ser substituídos uma vez colocados dentro da bolsa.

Atribuindo valor a uma constante em Python
No Python, as constantes são geralmente declaradas e atribuídas em um módulo. Aqui, o módulo significa um novo arquivo contendo variáveis, funções, etc., que são importadas para o arquivo principal. Dentro do módulo, as constantes são escritas em letras maiúsculas e sublinhadas, separando as palavras.

Exemplo 3: Declarando e atribuindo valor a uma constante
Crie um constant.py

PI = 3.14
GRAVITY = 9.8
Crie um main.py

import constant

print(constant.PI)
print(constant.GRAVITY)
Quando você executa o programa, a saída será:

3,14
9,8
No programa acima, criamos um arquivo de módulo constant.py. Em seguida, atribuímos o valor constante a PI e GRAVITY. Depois disso, criamos um arquivo main.py e importamos o módulo constante. Finalmente, imprimimos o valor constante.

Nota: Na realidade, não usamos constantes em Python. O módulo globals ou constantes é usado em todos os programas Python.

Regras e convenção de nomenclatura para variáveis ​​e constantes
Crie um nome que faça sentido. Suponha que a  vogal faça mais sentido que v .
Use a notação camelCase para declarar uma variável. Começa com letra minúscula. Por exemplo:
o meu nome
minha idade
meu endereço
Use letras maiúsculas, quando possível, para declarar uma constante. Por exemplo:
PI
G
MASSA
TEMP
Nunca use símbolos especiais como!, @, #, $,%, Etc.
Não comece o nome com um dígito.
As constantes são colocadas nos módulos do Python e não significam alterações.
Os nomes de constantes e variáveis ​​devem ter combinação de letras em minúsculas (a a z) ou maiúsculas (A a Z) ou dígitos (0 a 9) ou um sublinhado (_). Por exemplo:
snake_case
MACRO_CASE
camelCase
CapWords
Literais

Literal é um dado bruto dado em uma variável ou constante. Em Python, existem vários tipos de literais que são os seguintes:

Literais Numéricos
Literais Numéricos são imutáveis ​​(imutáveis). Os literais numéricos podem pertencer a 3 tipos numéricos diferentes: Integer, Float e Complex.

Exemplo 4: Como usar literais numéricos em Python?
script.py
Shell IPython

Corre
Alimentado por DataCamp
Quando você executa o programa, a saída será:

10 100 200 300
10,5 150,0
3,14j 3,16 0,0
No programa acima,

Nós atribuímos literais inteiros em diferentes variáveis. Aqui, a é literal binário, b é um literal decimal, c é um literal octal e d é um literal hexadecimal.
Quando imprimimos as variáveis, todos os literais são convertidos em valores decimais.
10.5 e 1.5e2 são literais de ponto flutuante. 1.5e2 é expresso com exponencial e é equivalente a 1,5 * 10 2 .
Nós atribuímos um literal complexo, isto é, 3,14j na variável x. Então, usamos o literal imaginário (x.imag) e o literal real (x.real) para criar uma parte imaginária e real do número complexo.
Para aprender mais sobre Literais Numéricos, consulte  Números do Python .

Literais string
Uma string literal é uma sequência de caracteres entre aspas. Podemos usar aspas simples, duplas ou triplas para uma string. E, um literal de caractere é um caractere único cercado por aspas simples ou duplas.

Exemplo 7: Como usar literais de string em Python?
script.py
Shell IPython

Corre
Alimentado por DataCamp
Quando você executa o programa, a saída será:

Este é o Python
C
Esta é uma string multilinha com mais de um código de linha.
Ünicöde
raw \ n string
No programa acima, This is Pythoné uma string literal e Cé um literal de caractere. O valor com aspas triplas """atribuídas no multiline_str é um literal de cadeia de várias linhas. O u"\u00dcnic\u00f6de"é um literal unicode que suporta caracteres diferentes do inglês e r"raw \n string"é um literal de string não processada.

Literais booleanos
Um literal booleano pode ter qualquer um dos dois valores: Trueou False.

Exemplo 8: Como usar literais booleanos em Python?
script.py
Shell IPython

Corre
Alimentado por DataCamp
Quando você executa o programa, a saída será:

x é verdadeiro
y é falso
um: 5
b: 10
No programa acima, usamos literal booleano Truee False. Em Python, Truerepresenta o valor como 1e Falsecomo 0. O valor de x é Trueporque 1é igual a True. E o valor de y é Falseporque 1não é igual a False.

Da mesma forma, podemos usar o Truee Falseem expressões numéricas como o valor. O valor de a é 5porque adicionamos Truequal valor é 1com 4. Da mesma forma, b é 10porque adicionamos o Falsevalor de ter 0com 10.

Literais Especiais
Python contém um literal especial ie None. Usamos para especificar para esse campo que não é criado.

Exemplo 9: Como usar literais especiais em Python?
script.py
Shell IPython

Corre
Alimentado por DataCamp
Quando você executa o programa, a saída será:

acessível
Nenhum
No programa acima, nós definimos uma menufunção. No interior menu, quando definimos o parâmetro como drink, ele é exibido Available. E, quando o parâmetro é food, ele é exibido None.

Coleções literais
Há quatro literais de lista de coleções literais diferentes, literais de tupla, literais de ditado e literais de conjunto.

Exemplo 10: Como usar coleções literais em Python?
script.py
Shell IPython

Corre
Alimentado por DataCamp
Quando você executa o programa, a saída será:

['maçã', 'manga', 'laranja']
(1, 2, 3)
{'a': 'apple', 'b': 'bola', 'c': 'gato'}
{'e', 'a', 'o', 'i', 'u'}
No programa acima, criamos uma lista de frutas , tuplas de números , ditador de dicionário com valores com chaves desginadas para cada valor e conjunto de vogais .
////////////////////////////////////////////////////////////////////////
Nomes de Varíaveis e Palavras Reservadas
Nomes de variáveis podem ser longos. Eles podem conter letras e dígitos, porém devem começar com uma letra ou sublinhado (_). Apesar de ser possível usar letras maiúsculas, em geral não fazemos isso. Se você fizer, lembre-se que Dia e dia são variáveis diferentes.

Caution

Nomes de variáveis nunca podem conter espaços em branco.

O caractere sublinhado (_) também pode aparecer em um nome. Ele é usado às vezes em nomes com várias palavras, como meu_nome ou preco_do_cafe. Há algumas situações onde nomes começando com sublinhado têm um significado especial, portanto uma dica boa para iniciantes é sempre começar os nomes com uma letra.

Se você der um nome ilegal a uma variável, você terá um erro de sintaxe. No exemplo abaixo, todos os nomes são ilegais.

76trombones = "grande parada"
mais$ = 1000000
class = "Computação I"
76trombones é ilegal porque não começa com uma letra mais$ é ilegal porque contém um caractere inválido, o sinal de dólar. Mas qual é o problema com class?

Acontece que class é uma das palavras reservadas de Python. As palavras reservadas definem as regras de sintaxe e estrutura da linguagem, e elas não podem ser usadas como nomes de variáveis. Python tem aproximadamente 30 palavras reservadas (e esse número pode variar, à medida em que a linguagem evolui):

and	as	assert	break	class	continue
def	del	elif	else	except	exec
finally	for	from	global	if	import
in	is	lambda	nonlocal	not	or
pass	raise	return	try	while	with
yield	True	False	None	 	 
Uma sugestão é deixar essa lista à mão. Se o interpretador reclamar de um nome de uma das suas variáveis e você não souber o motivo, verifique se ele está nessa lista.

Programadores geralmente escolhem nomes que façam sentido para os humanos que irão ler o programa — esses nomes ajudam o programador a documentar, ou se lembrar, qual é o papel de cada variável.

Teste seu entendimento



