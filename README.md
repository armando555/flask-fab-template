# Tiwala

## Made by: 
Twelve Network

## Authors:
- Armando Rios (armando.rios@twelve.net.co)


## Coding rules
- Do not create more than one class per file, unless it is really needed.
- Follow PEP 8 https://www.python.org/dev/peps/pep-0008/ (install a code linter and an autoformater like pylance)
- All models will be defined under the app.models module, and must be imported in app.models file.
- All views will be defined under the app.views module, and must be imported and registered in the app.views.file.

## Installation
### Install virtualenv
Run
```bash
python3 -m pip install virtualenv
```
### Create virtual environment
Change directory into `tiwala`.
```bash
cd tiwala
```
Run
```bash
python3 -m virtualenv --system-site-packages venv
```
### Activate virtual environment
Run
```bash
source ./venv/bin/activate
```
Optionally check if the virtual environment is working correctly with:
```bash
which python3
```
This should output the path to the currently used python3 interpreter and should look something like this.

```bash
/path/to/your/venv/bin/python3
```
## Running application

__Note:__ Running applications on the ports 80 and 443 is restricted. For that you should setup a proper web server or run them as root/sudo.

### With flask run
__Warning:__ Use this only for testing, it runs as a development server and may be vulnerable.

# Command to seed database
```bash
flask seed_db
```

## in repo.tiwala/tiwala
```bash
export FLASK_APP=app
python3 -m flask run --port 7000
```

# Migrations
Primero debes hacer pull del repo, luego ejecutar el upgrade para actualizar la BD basada en la ultima migración descargada.

```bash
flask db upgrade
```
```bash
flask db migrate -m "message"
```

ya una vez actualziada la BD el proceso es simple, se cambia un modelo y se hace migrate. y finalmente upgrade para poder actualizar la BD.
## this command can solve some problems. Sets the revision in the database to the one given as an argument, without performing any migrations.
```bash
flask db stamp head
```

# download mysql docker image and stop services of mysql
```bash
docker pull mysql
```
```bash
docker stop mysql && docker rm mysql
```
# run a database container  and connect to the container an create database
```bash
sudo docker run -d -p 33061:3306 --name mysql -e MYSQL_ROOT_PASSWORD=root mysql
```
```bash
docker exec -i -t mysql /bin/bash
```
and create manually the database called "tiwala_test" or use this command
```bash
docker exec -i mysql mysql -uroot -proot <<< "create database tiwala_test;"
```



# In docker
# Stop container
```bash
sudo docker stop tiwala-test && sudo docker rm tiwala-test
```
# build the latest image from source
```bash
sudo docker build -t twelve/tiwala-backend .
```

# run backend the first command is for use SLQITE
```bash
sudo docker run --name tiwala-test -p 4443:4443 -d twelve/tiwala-backend:latest
```
# this command is for use MYSQL with the docker
```bash
sudo docker run --name tiwala-test -e MYSQL_PASSWORD=root -e MYSQL_HOST=localhost -e MYSQL_PORT=33061 -e MYSQL_USER=root -d -p 4443:4443  twelve/tiwala-backend:latest
```
# connect to the container and create administrator
```bash
sudo docker exec -it tiwala-test /bin/sh
```
# create admin
```bash
flask fab create-admin --username="admin" --firstname="Armando" --lastname="Rios Gallego" --email="armando.rios@twelve.net.co" --password="1234"
```
# Command to seed database
```bash
flask seed_db
```
# That's all for the back
# see errors in the docker
```bash
docker logs tiwala_test
```

# cancel dev server and that's all
ctrl+c 



