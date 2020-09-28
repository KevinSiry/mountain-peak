# mountain-peak

## Launch the project
After pulling the project, it's better to create a virtual env to install all the dependencies.

```
virtualenv venv
```

Then install the dependencies.

```
pip install -r .\requirements.txt
```

Finally you can launch the docker-compose file to start the project.

```
docker-compose up
```

## What's inside this project
REST API to manage peaks with different features:

* Add a peak
* Remove a peak
* Update a peak
* Get a peak
* Get peaks in a given geographical bounding box

## Swagger
https://app.swaggerhub.com/apis/KevinSiry132/moutainpeak/1.0.0