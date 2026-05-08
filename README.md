# 🅿️ SAEPD — Sistema de API de Estacionamento com Python e Django

> API REST completa para gestão de estacionamento de veículos — controle de vagas, clientes, veículos e registros de entrada e saída com autenticação JWT e painel administrativo.

<br>

## 📋 Sobre o Projeto

O SAEPD é um sistema backend de gestão de estacionamento desenvolvido como projeto prático de aprendizado, seguindo os requisitos do **Parking Service** (py_live #039-#042). O sistema permite o controle completo de vagas, cadastro de clientes e veículos, e registro de entradas e saídas com atualização automática do status das vagas via Django Signals.

Desenvolvido com foco em boas práticas de desenvolvimento backend: arquitetura em apps separados por domínio, autenticação JWT, permissões por objeto, painel administrativo com Jazzmin e código padronizado com PEP8.

<br>

## 🚀 Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.12 | Linguagem principal |
| Django 6.0 | Framework web |
| Django REST Framework | API REST |
| Simple JWT | Autenticação stateless |
| SQLite / PostgreSQL | Banco de dados |
| Django Jazzmin | Interface administrativa customizada |
| flake8 + autopep8 | Linter e formatação PEP8 |

<br>

## 🗂️ Estrutura de Apps

```
SAEPD/
├── authentication/  # Autenticação JWT (login, refresh, registro)
├── core/            # Settings, urls raiz e configurações globais
├── customers/       # Cadastro e gestão de clientes
├── parkings/        # Vagas e registros de entrada/saída
├── vehicles/        # Tipos e cadastro de veículos
├── static/          # Arquivos estáticos (CSS, JS, imagens)
├── staticfiles/     # Arquivos estáticos coletados
├── manage.py
├── requirements.txt
├── .flake8
└── .gitignore
```

<br>

## ⚙️ Funcionalidades

- ✅ Cadastro e gestão de **clientes**
- ✅ Cadastro de **veículos** por tipo (carro, moto, etc.)
- ✅ Gestão de **vagas** com status automático (livre/ocupada)
- ✅ Registro de **entrada e saída** de veículos
- ✅ **Status da vaga atualizado automaticamente** via Django Signals
- ✅ **Permissões por perfil** — cliente vê apenas seus próprios veículos e registros
- ✅ Autenticação com **JWT** (access + refresh token)
- ✅ Painel administrativo com **Django Jazzmin**
- ✅ Código padronizado com **PEP8**

<br>

## 🔐 Níveis de Acesso

| Nível | Quem | Acesso |
|---|---|---|
| Admin | `is_staff=True` | Acesso total via API e painel admin |
| Autenticado | Token JWT válido | Acesso apenas aos próprios dados |
| Público | Sem token | Sem acesso à API |

<br>

## 📡 Principais Endpoints

### Autenticação
```
POST   /api/v1/auth/token/          → Login (retorna access + refresh token)
POST   /api/v1/auth/token/refresh/  → Renovar access token
```

### Clientes
```
GET    /api/v1/customers/           → Listar clientes
POST   /api/v1/customers/           → Cadastrar cliente
GET    /api/v1/customers/{id}/      → Detalhar cliente
PATCH  /api/v1/customers/{id}/      → Atualizar cliente
DELETE /api/v1/customers/{id}/      → Remover cliente
```

### Veículos
```
GET    /api/v1/vehicles/            → Listar veículos
POST   /api/v1/vehicles/            → Cadastrar veículo
GET    /api/v1/vehicles/{id}/       → Detalhar veículo
PATCH  /api/v1/vehicles/{id}/       → Atualizar veículo
DELETE /api/v1/vehicles/{id}/       → Remover veículo
```

### Vagas e Registros
```
GET    /api/v1/parkings/spots/          → Listar vagas (livre/ocupada)
POST   /api/v1/parkings/spots/          → Criar vaga
GET    /api/v1/parkings/spots/{id}/     → Detalhar vaga
PATCH  /api/v1/parkings/spots/{id}/     → Atualizar vaga

GET    /api/v1/parkings/records/        → Listar registros de entrada/saída
POST   /api/v1/parkings/records/        → Registrar entrada de veículo
GET    /api/v1/parkings/records/{id}/   → Detalhar registro
PATCH  /api/v1/parkings/records/{id}/   → Registrar saída (exit_time)
```

<br>

## 🧠 Django Signals

O status das vagas é gerenciado automaticamente via Signals — ao registrar uma entrada, a vaga é marcada como ocupada; ao registrar a saída, volta para livre.

```python
# Registro de entrada → Signal atualiza vaga para ocupada
ParkingRecord.objects.create(vehicle=veiculo, parking_spot=vaga, ...)
# vaga.is_occupied: False → True ✅

# Registro de saída (exit_time preenchido) → Signal libera a vaga
record.exit_time = datetime.now()
record.save()
# vaga.is_occupied: True → False ✅
```

<br>

## 🛠️ Como rodar localmente

### Pré-requisitos

- Python 3.12+
- pip
- Git

### Passo a passo

**1. Clone o repositório**
```bash
git clone https://github.com/mathRyan889/SAEPD.git
cd SAEPD
```

**2. Crie e ative o ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Rode as migrations**
```bash
python manage.py migrate
```

**5. Crie o superusuário**
```bash
python manage.py createsuperuser
```

**6. Inicie o servidor**
```bash
python manage.py runserver
```

Acesse em: `http://127.0.0.1:8000`

<br>

## 🖥️ Painel Administrativo

O projeto utiliza **Django Jazzmin** para uma interface administrativa moderna e responsiva.

| Interface | URL |
|---|---|
| Django Admin | `http://127.0.0.1:8000/admin/` |
| API Browsable | `http://127.0.0.1:8000/api/v1/` |

<br>

## 📁 Padrões de código

O projeto utiliza **flake8** para análise estática e **autopep8** para formatação automática seguindo PEP8.

```bash
# Verificar erros
flake8 .

# Formatar automaticamente
autopep8 --in-place --recursive .
```

<br>

## 📦 Dependências principais

```
Django==6.0.4
djangorestframework
djangorestframework-simplejwt
django-jazzmin
flake8
autopep8
```

> Veja o arquivo `requirements.txt` para a lista completa.

<br>

## 🗺️ Roadmap

Funcionalidades planejadas para as próximas etapas do projeto:

- [ ] Filtros avançados com **dj-rql**
- [ ] Documentação **Swagger** com drf-spectacular
- [ ] **Docker** + docker-compose
- [ ] **PostgreSQL** em container
- [ ] **Celery** + RabbitMQ para tasks assíncronas
- [ ] Notificações via **WhatsApp** (EvolutionApi)
- [ ] **Testes unitários** com pytest-django

<br>

## 👤 Autor

**Matheus Ryan**
- GitHub: [@mathRyan889](https://github.com/mathRyan889)
- LinkedIn: [matheus-ryan-74110521b](https://linkedin.com/in/matheus-ryan-74110521b)
- Website: [stolus.pythonanywhere.com](https://stolus.pythonanywhere.com)