[![GitHub](https://img.shields.io/github/license/jdeveloperanalyst/Analise-de-Dados)](https://github.com/jdeveloperanalyst/Analise-de-Dados/blob/master/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-05122A?style=flat&logo=linkedin)](https://www.linkedin.com/in/jonatas-silva-dev-6a6f6e/)
# Envio de SMS Biblioteca Twilio

Este projeto tem como objetivo automatizar um fluxo utilizando a linguagem de programação <kbd>Python</kbd> no qual é analisado os funcionários que bateram a meta de vendas em mais de R$55.000 reais em uma determinada empresa, onde será feito o envio de um SMS para um destinatário predefinido (sendo ele um gestor ou uma pessoa com cargo de liderança) e o funcionário que bater a meta terá uma bonificação..
<br>

## Sobre o Projeto

Para este projeto foi utilizado 6 bases de dados que basicamente são <kbd>arquivos Excel</kbd> de cada mês referente ao primeiro semestre do ano, onde contém informações como <kbd>nome do vendedor</kbd> e também o <kbd>valor das vendas</kbd> de cada mês. Sendo assim, utilizando os recursos que o Python nos fornece, este script será responsável em ler/analisar essas 6 bases de dados, fazendo com que seja possível identificar os funcionários que bateram a meta e a partir da biblioteca <kbd>Twilio</kbd> realizar o envio de um SMS com essas informações para que os responsáveis pelo bom trabalho sejam bonificados. Tudo isso de forma totalmente automática.

## Twilio

O <kbd>Twilio</kbd> é uma biblioteca auxiliar do Python que facilita a interação com a <kbd>API Twilio</kbd> com diversas funcionalidades. Vale destacar dois pontos importantes, no qual se refere à <kbd>realização de um cadastro</kbd> na plataforma Twilio e ao <kbd>uso de credênciais</kbd> que são geradas na aplicação web após o cadastro. Será mostrado também como atriubui essas credênciais em váriaveis, impedindo que terceiros tenha acesso as mesmas no código.

1. Cadastro
   1. Primeiramente é feito o cadastro na plataforma Twilio (https://www.twilio.com/try-twilio) inserindo os dados no qual é solicitado conforme imagem abaixo:

      ⚠️ _Atenção: Fazer o cadastro **"sem a necessidade de hospedagem de código no Twilio"**, essa funcionalidade será perguntada ao usuário quando o mesmo estiver realizando o cadastro._ 
   
       ![image](https://user-images.githubusercontent.com/112918533/230236529-5376f5c1-fa3c-467f-8eba-472e0f440d1e.png)
      
   2. Após o simples cadastro, será possível verificar na tela inicial as credênciais responsáveis pela autenticação no cliente <kbd>(Twilio)</kbd>. Porém antes de utiliza-los no script em questão para enviar ou receber um SMS com Twilio, você precisará de um número de telefone virtual da Twilio. Um número de telefone virtual é um número de telefone padrão que não está bloqueado para um telefone específico. Ele pode rotear uma chamada de voz ou mensagem de texto para qualquer fluxo de trabalho de telefone ou aplicativo. Além disso, você precisará do SID da conta Twilio e do token Auth para conectar o Twilio ao seu aplicativo. Ainda na tela inicial é possível criar um número de telefone virtual seguindo o <kbd>Step 1</kbd> conforme mostra a imagem abaixo:

      ![image](https://user-images.githubusercontent.com/112918533/230239805-5004088e-9674-4ac3-b130-98562c2e8cd1.png)
   
      _Para este caso, meu número ja foi criado. Entretando, após realizar o cadastro terá um botão com a seguinte escrita: <kbd>Get a trial phone number</kbd> que estará neste <kbd>Step 1</kbd> para que seja criado um número de telefone teste_.
      
   3. Em seguida, com o cadastro realizado e com o número de telefone virutal criado, será possível ver na tela inicial as credênciais para autenticação criadas com sucesso, sendo eles: <kbd>Account SID</kbd>, <kbd>Auth Token</kbd> e o <kbd>My Twilio phone number</kbd> conforme imagem abaixo:

      ![image](https://user-images.githubusercontent.com/112918533/230244611-5fe59d3b-e403-4099-96f0-a4dbbc1305b2.png)

2. Credênciais
   1. É muito importante ressaltar o <kbd>uso devido</kbd> das credênciais no código. Sendo assim, com o objetivo de não deixar essas credênciais explicitas no arquivo principal, dentro do projeto criei um novo arquivo Python no PyCharm chamado <kbd>Credenciais.py</kbd> e neste arquivo criei uma váriável chamada <kbd>secret</kbd> que recebe um dicionário onde contém chaves que recebem essas credênciais, conforme mostrado abaixo: 
   
      Credenciais.py
      ```
      secret = {'sid': 'abcdefghijklmnopqrstuvwxyz',
                'token': 'aaaa111bbbb2222cccc',
                'my_cellphone': '+1111111111111',
                'twilio_phone': '+22222222222'}
       ```
       ⚠️ _Atenção: A partir do momento que essas credênciais ficam explicitas em repositórios na internet, por questões de segurança ao fazer o login na aplicação web Twilio com seu usuário e senha é solicitado a troca dessas credênciais. Sendo assim, para melhor segurança nos dados é necessário atribui-las em váriáveis e se necessário criptografa-las para o uso devido. Além disso, o arquivo <kbd>Credenciais.py</kbd> foi adicionado ao .gitignore para que não fosse expostos os dados utilizados para este projeto._
    
    2. Com isto, no arquivo principal no qual intitulei como <kbd>Envio-SMS-Twilio.py</kbd> importei a variável <kbd>secret</kbd> a partir do arquivo <kbd>Credenciais.py</kbd> para acessar os dados e conseguir autenticar a conexão do twilio para envio do SMS utilizando o script Python criado. Confira abaixo como é importado a variável que recebe um dicionário a partir do arquivo <kbd>Credenciais.py</kbd> que foi criado:
   
       Envio-SMS-Twilio.py
       ```
       from twilio.rest import Client
       from Credenciais import secret
       
       account_sid = secret['sid']
       auth_token = secret['token']
       client = Client(account_sid, auth_token)
       ```
       _Com isto, é feito a conexão com Twilio para o envio do SMS._
       
## Estrutura do Código

Mostrando a estrutura do código, irei falar sobre as bibliotecas utilizadas, e cada etapa do processo até a execução do script para envio do SMS. <kbd>Confira sobre o link abaixo:</kdb> 

_[Clique aqui](https://drive.google.com/file/d/1tAFkhntNOcD3i3kurQnfe6riJEWmrLSe/view?usp=share_link) para ver a <kbd>parte 1</kbd> do vídeo no Google Drive._

## Incremento Biblioteca Time

Nesta etapa do processo decidi incrementar a biblioteca <kbd>Time</kbd> utilizando o metodo <kbd>Sleep</kbd> com a finalidade de ter um intervalo de tempo entre o envio de um sms e outro, para que não tenha algum conflito de conexão com a aplicação web Twilio na execuçao do script ou algum eventual erro. Além disso, realizei um teste espelhando a tela do meu celular para visualizar em tempo real a chegada do SMS ao executar o script.

_[Clique aqui](https://drive.google.com/file/d/18NeJ-Cbv9SLb4PpDlVp05vf6mtf3qrtR/view?usp=share_link) para ver a <kbd>parte 2</kbd> do vídeo no Google Drive._

## Subindo Alterações

Como decidi incrementar a biblioteca <kbd>Time</kbd> no script de última hora, achei válido fazer um vídeo simples subindo essas alterações locais para o repositório remoto.

_Subindo as alterações locais para o repositório remoto via terminal. > [clique aqui](https://drive.google.com/file/d/1DKDi39HA3WbbTAnT-BvwNjikvNz_5Nwo/view?usp=share_link)._

***

<br>

> Transmitir conhecimento não é apenas falar o que sabe, mas inspirar novas atitudes.
