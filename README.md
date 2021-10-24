# How to start the application
* Run `start.sh` script
```
./start.sh
```
# Docs
You can see all allowed api-methods and mannualy test them on ```http://0.0.0.0:8000/docs```
# Stop application
```
docker-compose stop
```
# Run tests
* First of all, please, stop running the application by the last command and than run ```test.sh``` script
```
./test.sh
```
You will see the result of the tests on your screen
# Finish
When you finish checking the app and tests run the command (it will stop running all processes in docker container and delete the container):
```
docker-compose down
```
