# Car Price Prediction App
This is a simple app to show how to create a complete solution that uses a machine learning model for prediction. 

<img alt="Screenshot image" src="img/Screenshot.png">

## Project Structure
```
root
 +-data: contains the training data.
 |
 +-fronend: frontend application by Angular
 |
 +-model: backend predictor model in python and Flask API.
 
```

## How to Run

### Use docker-compose
Note: Make sure you have [Docker](https://docs.docker.com/engine/install/) installed.
* Go in to `frontend/src/assets/config.json` and change the `backendHost` to the hosting machine. 
* In the root of the project, run `docker-compose up`
* The two containers will run and your app will be available on the Host IP (port 80). 

### Use Docker
Both frontend and backend applications come with their own Docker file. 
1. Run the model (python):

    * change directory to `model/`
    * Run `docker built -t backend`
    * Run `docker run -p 8081:8081 backend`
    * The backend app will be running on `http://localhost:8081`.

2. Run the frontend (angular):
    * change directory to `frontend`
    * Run `docker build -t frontend .`
    * Run `docker run --rm --name car_price_front_app -p 80:80 frontend`
    * The frontend will be running on `http://localhost:80`.
      - `--rm` will remove the container after it terminates.
      - `--name` assigns a name to the container.
### Manual
1. Backend
  - Navigate to the `model/` folder: `cd model`
  - Create virtual env.
    - `python -m venv venv`
    - `source venv/bin/activate`
  - `pip install -r requirements.txt`
  - `cd app`
  - `python app.py`

2. Frontend

  - Note: Make sure you have [Node](https://nodejs.org/en/download) version 20 (or higher).
  - Navigate to `frontend/` folder: `cd frontend`
  - Install dependencies: `npm install`
  - `ng serve` to run your Angular application during development.
    - It's not recommended to use it in production.

