
<h1 align="center"> VALIDADOR DE URL CONTRA ATAQUE PISHING </h1>

Definição sobre Ataque Pishing: O phishing é uma técnica de crime cibernético que usa fraude e engano para manipular as vítimas para que cliquem em links maliciosos ou divulguem informações pessoais confidenciai


<h1 align="center"> FASE DA SITUAÇÃO PROBLEMA </h1>
Este projeto é fruto de um contato com meu amigo que vive em Angola, na qual ele estava buscando uma solução que ajudasse a resolver problemas em relação a ataques Cybernético.
Confesso que este assunto não tenho muita profundidade, mais não me limitei apesar de estar nestas condições, no entanto em conversa acabei propondo em criamos uma solução direcionada para um tipo de público, já que em Angola maior parte da população usa bastante o Facebook, então muito deles não tenhem conhecimento sobre a questão de segurança, abrindo aspas essa questão vem sobre tudo pelo facto, de que maior parte da população tem pouca noção básica no uso da internet, então ai é que mora o perigo de não ter o minímo do senso crítico em clicar por exemplo em qualquer link com esta atitude torna-se o alvo para cair em qualquer ataque e sobre tudo o ataque pishing aonde muitos deles tenhem sido alvo. Já tive contato com familiares que passaram por essa expriencia em que alguém estava se passando pelo meu familiar no sentido de pedir dinheiro. Bem, voltando ao início da conversa,  este assunto é um escopo aberto então por isso acabei propondo ao meu amigo está sugestão de focar ao público do Facebook de modo a criar uma camada de segurança para este público.
Bem ai está um experimento que acabei propondo e daí parte para pesquisar a respeito do assunto e recorre ao Kaggle para ter uma base de dados e entender como deveria construir o modelo de aprendizado de máquina. 

<h1 align="center"> PRIMEIRA ETAPA </h1>

Fui ao Kaggle para extrair a base de dados para que assim pudesse ter dados para criar os primeiros experimentos. 

🗯 Aqui está a fonte de dados usadas para classificar a url em ser uma URL "boa" ou "ruim".

Link: https://www.kaggle.com/code/fadilparves/pishing-detection-using-machine-learning


<h1 align="center"> DESENHEI A ARQUITETURA USANDO O DRAW.IO </h1>

![image](https://github.com/laurindodumba/Validador_De_URL_Contra_Ataque_Pishing/assets/38964642/77b19e3b-4c11-4ef5-9ce3-810c2927ea17)


## SEGUNDA ETAPA PREPARAÇÃO DO  AMBIENTE DE DESENVOLVIMENTO:

1. Iniciei com a instação do ambiente virtual - virtualenv pishing
2. Na sequência fiz ativação do ambiente virtual
3. Organização das pastas e ficou conforme a imagem abaixo

![image](https://github.com/laurindodumba/Validador_De_URL_Contra_Ataque_Pishing/assets/38964642/abe94f55-267b-4ee2-b252-c19af178f3ed)


4. Instalei todas as dependências e salvei no arquivo requirements.txt, isto para garantir (Limpeza, segurança, conformidade e adequação as boas práticas de desenvolvimento)

   
6. Para reproduzir em vosso ambiente de desenvolvimento precisa usar este comando.

   
  a. pip install -r requirements.txt
 

<h1 align="center"> CONSTRUÇÃO DA APLICAÇÃO WEB (FRONT-END): </h1>

Para construir aplicação web usei o html aonde me possibilitou estrutrar a marcação da aplicação. No nosso caso o arquivo esta localizado na pasta static(index.html)

Também usei o framework Bootstrap para ajudar na estilização da aplicação, pelo facto de ser familiar pra mim e tmabém possuí recursos que ao meu ponto de vista atende o objetivo do projeto na justificativa de ter um resultado que por parte ao usuário me parace mais agradavél de se ter. 

<h1 align="center"> RESULTADO :</h1>

🎯 Este foi o resultado alcançado para ter uma expriência de validar os experimentos de classficação de URL contra ataque Pishing.

![image](https://github.com/laurindodumba/Validador_De_URL_Contra_Ataque_Pishing/assets/38964642/02ca86ce-7ec8-4ff0-9322-803b61beba6e)

<h1 align="center"> CONSTRUIR O BACK-END: </h1>

✔🚀 Para a parte do back end foi construida uma api com o FastApi usando o queridinho Python, para criar a rota e renderizar a pagina html toda vez que for solicitada a validação no modelo que salvo no formato de pickle.




![Badge Concluído](http://img.shields.io/static/v1?label=STATUS&message=%20CONCLUÍDO&color=GREEN&style=for-the-badge)


# Autor:

| [<br><sub>Laurindo Dumba</sub>](https://github.com/laurindodumba) 
| :---: | 


