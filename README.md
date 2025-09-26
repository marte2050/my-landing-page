![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Wagtail](https://img.shields.io/badge/wagtail-%2300ADEF.svg?style=for-the-badge&logo=wagtail&logoColor=white) ![Tailwind CSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

# Landing Page

Esse é um projeto de uma landing page para meu website provida através do cms wagtail, ao qual é um CMS construído em cima do framework Django. Esse projeto utiliza as seguintes tecnologias:

- Wagtail;
- Django;
- Python;
- Webcomponente construído em stenciljs, ao qual pode ser acessado [mywebcomponents](https://github.com/marte2050/my-webcomponents).
- Tailwind;
- Docker;

## Rodando o projeto em desenvolvimento

Para rodar o projeto em desenvolvimento, você precisa ter o Docker instalados na sua máquina. Siga os passos abaixo:

1. Clone o repositório

```bash
git clone https://github.com/marte2050/my-landing-page
cd mylandingpage
```

2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```bash
mv env.sample .env
```

3. Construa e rode os containers do Docker

```bash
docker compose up --build
```

4. Rode as migrações:

```bash
docker exec -it mylandingpage bash
poetry shell
python manage.py migrate
```

5. Rodando o projeto em desenvolvimento

```bash
docker exec -it mylandingpage bash
poetry shell
python manage.py runserver 0:8000
```

6. Criando um superusuário para acessar o admin do Wagtail

```bash
docker exec -it mylandingpage bash
poetry shell
python manage.py createsuperuser
```

