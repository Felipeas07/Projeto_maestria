Projeto de Web com Django
Introdução
Este projeto tem como objetivo desenvolver uma plataforma para a gestão de anúncios, onde usuários podem cadastrar, visualizar e filtrar anúncios baseados em categorias e valores.

Estrutura do Projeto
•	Django: Framework de desenvolvimento web robusto, utilizado para criar a aplicação.
•	SQLite3: Banco de dados utilizado, que é leve e já vem integrado no Django por padrão, ideal para projetos menores e em fase de desenvolvimento.
•	Estrutura de Diretórios:
•	galeria: Aplicativo responsável pela lógica de negócios, incluindo:
•	models.py: Define as classes para os anúncios e usuários.
•	views.py: Gerencia a lógica de apresentação de dados aos usuários.
•	urls.py: Define as rotas e endereços da aplicação.
•	setup: Diretório de configurações do projeto, incluindo o settings.py, onde o banco de dados e outras configurações importantes estão definidas.
os arquivos models.py, forms.py, views.py, etc, do seu projeto contêm classes e métodos que desempenham papéis importantes na estrutura e funcionalidade da aplicação:

•	models.py: Contém as definições dos modelos que representam os dados do sistema, como os anúncios e os usuários (abelas do banco de dados, incluindo atributos e métodos para manipulação de dados).
•	views.py: Contém as funções que manipulam as requisições e as respostas do servidor, exibindo as páginas HTML correspondentes e realizando operações de CRUD (criação, leitura, atualização e deleção) nos anúncios.
•	urls.py: Define as rotas do aplicativo, mapeando URLs para as funções de visualização correspondentes.
•	forms.py: Possivelmente contém as definições de formulários para entrada de dados, como o registro de anúncios e o formulário de contato.
•	templates/: Diretório que armazena os arquivos HTML usados para renderizar as páginas do aplicativo. Este diretório provavelmente contém as páginas relacionadas à listagem de anúncios, página inicial e formulário de contato.
•	static/: Armazena arquivos estáticos como CSS e JavaScript, que são utilizados para estilizar e adicionar interatividade às páginas.

Descrição dos Apps:
1.	django.contrib.admin:
•	O painel de administração do Django, que fornece uma interface de gerenciamento para os modelos do seu projeto.
2.	django.contrib.auth:
•	Sistema de autenticação, que lida com usuários, grupos, permissões e autenticação de sessão.
3.	django.contrib.contenttypes:
•	Permite que o Django rastreie os tipos de modelos e suas instâncias, essencial para o sistema de permissões.
4.	django.contrib.sessions:
•	Lida com sessões de usuário, permitindo que o Django mantenha o estado entre as requisições.
5.	django.contrib.messages:
•	Sistema de mensagens que permite exibir mensagens de feedback para os usuários (como confirmações de ações).
6.	django.contrib.staticfiles:
•	Gerencia arquivos estáticos, como CSS e JavaScript, facilitando o desenvolvimento e a coleta desses arquivos para produção.
7.	galeria:
•	Este é o seu aplicativo personalizado, onde você deve ter implementado as funcionalidades específicas do seu projeto de gestão de anúncios.

Funcionalidades
•	Gestão de Anúncios: Os anúncios incluem dados como anunciante, fotos e valor.
•	Filtros de Anúncios: Permite que os usuários filtrem os anúncios com base em categorias e faixas de valor.
•	Sistema de Usuários:
•	Usuários Públicos: Podem visualizar e filtrar anúncios.
•	Administrador: Um único administrador que gerencia os anúncios e usuários.
O sistema de autenticação do Django permite a criação de usuários diferenciados com permissões específicas.

Estrutura do Banco de Dados
O projeto está utilizando o SQLite3, que é o banco de dados padrão do Django para ambientes de desenvolvimento. Isso está definido no arquivo
settings.py com a seguinte configuração:
python
Copiar código DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3',
}
}

Esse banco de dados é simples, armazenado localmente no arquivo db.sqlite3, e adequado para projetos de pequeno porte ou em desenvolvimento inicial.

Comandos Utilizados para Criar o Projeto
1.	Criar Ambiente Virtual:

python -m venv env

2.	Ativar Ambiente Virtual:
•	Windows:
bash
Copiar código
.\env\Scripts\activate

•	macOS/Linux:
bash
Copiar código
source env/bin/activate

3.	Instalar Django:
bash
Copiar código
python -m pip install django~=5.0

4.	Criar o Projeto Django:
bash
Copiar código
django-admin startproject nome_do_projeto .

5.	Criar Aplicativo:
bash
Copiar código
python manage.py startapp galeria

6.	Migrar Banco de Dados: Como o banco de dados é SQLite3, o Django automaticamente cria o arquivo db.sqlite3 ao rodar o comando de migração:
bash
Copiar código
python manage.py migrate

7.	Criar Superusuário: Para acessar o painel de administração:
bash
Copiar código
python manage.py createsuperuser

8.	Iniciar o Servidor de Desenvolvimento:
bash
Copiar código
python manage.py runserver
Análise das Configurações:
1.	Importações e Variáveis Ambientais:
•	O arquivo usa dotenv para carregar variáveis de ambiente de um arquivo .env, o que ajuda a manter as informações sensíveis fora do código-fonte.
2.	Configurações Básicas:
•	BASE_DIR: Define o diretório base do projeto.
•	SECRET_KEY: Chave secreta utilizada pelo Django, carregada de variáveis de ambiente.
•	DEBUG: Habilita ou desabilita o modo de depuração com base na variável de ambiente.
3.	Hosts Permitidos:
•	ALLOWED_HOSTS: Lista de hosts permitidos para o projeto, também configurável via variável de ambiente.
4.	Aplicativos Instalados:
•	A lista INSTALLED_APPS inclui os aplicativos padrão do Django e o aplicativo personalizado galeria.
5.	Middleware:
•	O middleware configura a proteção e o gerenciamento de sessões e segurança.
6.	Banco de Dados:
•	A seção DATABASES configura o banco de dados PostgreSQL, permitindo que as credenciais sejam definidas em variáveis de ambiente.
7.	Validação de Senhas:
•	A lista de AUTH_PASSWORD_VALIDATORS define as regras para a validação de senhas.
8.	Internacionalização:
•	LANGUAGE_CODE e TIME_ZONE definem a localização e fuso horário padrão do projeto.
9.	Arquivos Estáticos:
•	STATIC_URL: Define a URL para os arquivos estáticos. 10.Campo de Chave Primária:
•	DEFAULT_AUTO_FIELD: Define o tipo padrão de chave primária para os modelos.
