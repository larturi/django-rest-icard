# iCard - App para Restaurantes

### App para que los clientes puedan hacer la orden desde su móvil. Cuenta con panel de administrador.

# Get Started:

Instalar dependencias:
```
pipenv install
```

Crear el .env
```
cp .env.dist .env

# Modificar los valores si es necesario
```

Levantar Postgres con Docker
```
docker-compose up
```

Crear migraciones:
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Ejecutar servidor local
```
python manage.py runserver
```

##### Made with ❤️ by Leandro Arturi
