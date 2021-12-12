# Сборка протестирована на Ubuntu 18.04 LTS
```
Для запуска может потребоваться:

1) sudo apt install gnupg2 pass
2) sudo nano /etc/docker/daemon.json
3) { "features": { "buildkit": true } }
4) ctrl+x y enter
5) sudo service docker restart

```

# Запустить airflow:
```
cd airflow
sudo bash ./start.sh

```


# Запустить проект:
```
sudo bash ./start.sh

Данные генеряться не моментально, примерно через 10-20 секунд появяться age.csv и age_sql.csv

```
# Остановить проект:
```
sudo bash ./stop.sh

```

