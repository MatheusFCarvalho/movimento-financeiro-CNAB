## movimento-financeiro-CNAB

Aplicação back-end, com o intuito de parsear arquivo CNAB txt salvando as informações em um banco de dados(POSTGRES) e sendo possível também resgatar a partir do nome da loja.

# Técnologias utilizadas:
  - Django
  - Django Rest Framework

#Instruções para ver o projeto em sua máquina:
1. Clonar o repositório

2. Crie seu ambiente virtual
  - Comece pelo comando 'python -m venv venv'
  - Linux: rode em seguida o comando 'source venv/bin/activate'
  - Windows: rode em seguida o comando '.\venv\Scripts\activate'

3. Criar suas variáveis de ambiente
  - Criar um arquivo '.env' na raiz do projeto com base no '.env.example'
  - Este projeto foi feito com PostgreSQL

4. No terminal utilizar o comando 'pip install -r requirements.txt' (Aguardar a instalação dos pacotes)

5. Rode as migrações da aplicação com o comando 'python manage.py migrate'

6. Inicialize a aplicação com o comando 'python manage.py runserver'
  - Para interromper, pressione 'Ctrl+c'

7. A documentação está em 'http://localhost:8000/schema/swagger-ui/'

8. Testando/Utilizando a aplicação localmente
  *Método POST:
    -Utilize a rota `http://localhost:8000/api/parser/cnab/`
    - Envie um `Binary File` no formato txt (existe um cnab file na raiz do arquivo)

  *Método GET:
    - Utilize a rota `http://localhost:8000/api/report/<NOME DA LOJA>/`
    
    
Esta aplicação não possui testes.
