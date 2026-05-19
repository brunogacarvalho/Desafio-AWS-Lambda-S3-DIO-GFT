\# Desafio AWS Lambda Function e S3 - DIO \& GFT



\## Sobre o Projeto



Este projeto foi desenvolvido durante o bootcamp \*\*GFT - Fundamentos de Cloud com AWS\*\*, realizado pela DIO.



Preciso ser honesto: esse laboratório foi o mais desafiador que já fiz até hoje. Sou iniciante em Cloud e nunca tinha mexido com Lambda, S3 ou DynamoDB antes dessas aulas. Mas com calma, seguindo o passo a passo do professor, consegui fazer tudo funcionar! 🎉



O objetivo foi automatizar uma tarefa simples: fazer o upload de um arquivo JSON em um "bucket" (uma espécie de pasta na nuvem) e deixar que um código Python rodasse automaticamente toda vez que esse arquivo fosse enviado — sem precisar apertar nenhum botão.



Para não gastar dinheiro usando a AWS de verdade, usamos o \*\*LocalStack\*\*, que simula os serviços da AWS direto no computador.



\---



\## O que eu aprendi (com minhas palavras)



\- \*\*Amazon S3\*\* é como um Google Drive da AWS — você guarda arquivos lá na nuvem

\- \*\*AWS Lambda\*\* é uma função (código) que roda automaticamente quando algo acontece — no nosso caso, quando um arquivo chega no S3

\- \*\*DynamoDB\*\* é um banco de dados da AWS — guardamos os dados do JSON processado lá

\- \*\*LocalStack\*\* simula a AWS no seu próprio computador, sem gastar nada

\- \*\*AWS CLI\*\* são comandos que você digita no terminal para controlar os serviços da AWS

\- \*\*Docker\*\* foi necessário para rodar o LocalStack



\---



\## Tecnologias Utilizadas



\- AWS Lambda

\- Amazon S3

\- Amazon DynamoDB

\- LocalStack

\- AWS CLI

\- Docker Desktop

\- Python

\- GitHub



\---



\## Como o projeto funciona



Explico de forma simples:



```text

Você faz upload de um arquivo JSON no S3 (bucket)

&#x20;       ↓

O S3 percebe que chegou um arquivo novo

&#x20;       ↓

O S3 chama automaticamente a função Lambda

&#x20;       ↓

A Lambda lê o arquivo e processa os dados

&#x20;       ↓

Os dados ficam salvos no DynamoDB

```



Parece complicado, mas na prática é como uma "corrente": uma coisa aciona a outra automaticamente.



\---



\## Estrutura do Projeto



```text

Desafio-AWS-Lambda-S3-DIO-GFT/

│

├── images/                      ← prints das etapas

├── grava\_db.py                  ← código Python da função Lambda

├── notification\_roles.json      ← configuração de permissões

├── notas\_fiscais\_2025.json      ← arquivo de teste que fizemos upload

└── README.md

```



\---



\## Capturas de Tela



\### Visão Geral da Infraestrutura no LocalStack



> Essa tela mostra todos os serviços que criamos rodando juntos (S3, Lambda e DynamoDB)



!\[LocalStack Overview](images/localstack-stack-overview.png)



\---



\### Health Check do LocalStack



> Confirmação de que o LocalStack estava funcionando corretamente



!\[Health Check LocalStack](images/localstack-health-check.png)



\---



\### Bucket S3 Criado



> O "bucket" é onde os arquivos JSON são enviados



!\[Bucket S3](images/s3-bucket-criado.png)



\---



\### Tabela DynamoDB Criada



> Tabela onde os dados processados são salvos



!\[Tabela DynamoDB](images/dynamodb-tabela-criada.png)



\---



\### Função Lambda Criada



> A função Python que roda automaticamente quando um arquivo chega no S3



!\[Lambda Function](images/lambda-function-criada.png)



\---



\### Trigger S3 Configurado



> Essa configuração é o que "liga" o S3 à Lambda — sem ela, nada acontece automaticamente



!\[Trigger S3](images/s3-trigger-configurado.png)



\---



\### Upload do Arquivo JSON



> O momento em que enviamos o arquivo de teste e a automação entrou em ação



!\[Upload JSON](images/upload-arquivo-json.png)



\---



\## Dificuldades que tive



\- Nunca tinha usado o terminal (AWS CLI) para criar recursos — foi bem diferente de usar interfaces gráficas

\- Configurar o LocalStack com Docker deu um trabalho, mas depois que funcionou foi incrível

\- Entender a diferença entre S3, Lambda e DynamoDB levou um tempo, mas as aulas do professor ajudaram muito

\- Criar o "trigger" (gatilho) que conecta o S3 à Lambda foi a parte mais confusa para mim



\---



\## O que ficou de aprendizado



Esse projeto me mostrou que é possível criar sistemas que funcionam sozinhos, sem precisar ficar apertando botões. Isso é o que chamam de \*\*automação na nuvem\*\*.



Também aprendi que dá para testar tudo isso sem pagar nada, usando o LocalStack. Isso foi muito importante para mim como iniciante, porque tirou o medo de errar.



\---



\## Créditos



Projeto desenvolvido durante o bootcamp \*\*GFT - Fundamentos de Cloud com AWS\*\*.



\- \[DIO](https://www.dio.me)

\- \[GFT](https://www.gft.com/br/pt)



\*\*Especialista responsável pelo conteúdo:\*\*

\- \[Alexsandro Lechner - LinkedIn](https://linkedin.com/in/alexsandrolechner)

\- GitHub: \[@alexsandrolechner](https://github.com/alexsandrolechner)



\---



\## Autor



\*\*Bruno Carvalho\*\*



\[!\[LinkedIn](https://img.shields.io/badge/LinkedIn-brunogacarvalho-blue?style=flat\&logo=linkedin)](https://www.linkedin.com/in/brunogacarvalho/)



