[![GitHub](https://img.shields.io/github/license/jdeveloperanalyst/Analise-de-Dados)](https://github.com/jdeveloperanalyst/Analise-de-Dados/blob/master/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-05122A?style=flat&logo=linkedin)](https://www.linkedin.com/in/jonatas-silva-dev-6a6f6e/)
# Envio de SMS Biblioteca Twilio

Este projeto tem como objetivo automatizar um fluxo no qual é analisado os funcionários que bateram a meta de vendas em mais de R$55.000 reais em uma determinada empresa, no qual será feito o envio de um SMS para um destinatário predefinido (sendo ele um gestor ou uma pessoa com cargo de liderança) e o funcionário que bater a meta terá uma bonificação..
<br>

## Sobre o Projeto

Para este projeto foi utilizado 6 bases de dados que basicamente são <kbd>arquivos Excel</kbd> de cada mês referente ao primeiro semestre do ano, onde contém informações como <kbd>nome do vendedor</kbd> e também o <kbd>valor das vendas</kbd> de cada mês. Sendo assim, utilizando os recursos que o Python nos fornece, este script será responsável em ler/analisar essas 6 bases de dados, fazendo com que seja possível identificar os funcionários que bateram a meta e a partir da biblioteca <kbd>Twilio</kbd> será possível realizar o envio de um SMS com essas informações para que os responsáveis pelo bom trabalho sejam bonificados. Tudo isso de forma totalmente automática.

## Twilio

O <kbd>Twilio</kbd> é uma biblioteca auxiliar do Python que facilita a interação com a <kbd>API Twilio</kbd> com diversas funcionalidades. Vale destacar dois pontos importantes, no qual se refere à <kbd>realização de um cadastro</kbd> na plataforma Twilio e ao <kbd>uso de credênciais</kbd> que são geradas na aplicação web após o cadastro. Será mostrado também como atriubui essas credênciais em váriaveis, tornando-a discreta no código e no GitHub.

1. Cadastro
   1. Primeiramente é feito o cadastro na plataforma Twilio (https://www.twilio.com/try-twilio) inserindo os dados no qual é solicitado conforme imagem abaixo:

      ⚠️ _Atenção: Fazer o cadastro **"sem a necessidade de hospedagem de código no Twilio"**, essa funcionalidade será perguntada ao usuário quando o mesmo estiver realizando o cadastro._ 
   
       ![image](https://user-images.githubusercontent.com/112918533/230236529-5376f5c1-fa3c-467f-8eba-472e0f440d1e.png)
      
   2. Após o simples cadastro, será possível verificar na tela inicial as credênciais responsáveis pela autenticação no cliente <kbd>(Twilio)</kbd>. Porém antes de utiliza-los no script em questão para enviar ou receber um SMS com Twilio, você precisará de um número de telefone virtual da Twilio. Um número de telefone virtual é um número de telefone padrão que não está bloqueado para um telefone específico. Ele pode rotear uma chamada de voz ou mensagem de texto para qualquer fluxo de trabalho de telefone ou aplicativo. Além disso, você precisará do SID da conta Twilio e do token Auth para conectar o Twilio ao seu aplicativo. Ainda na tela inicial é possível criar um número de telefone virtual seguindo o <kbd>Step 1</kbd> conforme mostra a imagem abaixo:

      ![image](https://user-images.githubusercontent.com/112918533/230239805-5004088e-9674-4ac3-b130-98562c2e8cd1.png)
   
      _Para este caso, meu número ja foi criado. Entretando, após realizar o cadastro terá um botão com a seguinte escrita: <kbd>Get a trial phone number</kbd> que estará neste <kbd>Step 1</kbd> para que seja criado um número de telefone teste_.

<br>
<h3 align="center">
Código 100% Funcional
</h3>

<br>
<h5 align="center">
  :construction: Projeto README :rocket: em construção :construction:
</h5>

