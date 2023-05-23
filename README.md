# Task-1
How to run the code in terminal 
- Create a virtual environment for the backend

virtualenv .venv

- Activate the virtual environment

source .venv/bin/activate

- Install the packages
 
pip install req.txt

- Install nodemon gloablly to auto-reload the server when making changes in the files

npm install -g nodemon

- cd into the frontend directory

cd frontend

- Install packages for the React app

npm install

- run the frontend

npm start

- open another terminal

source .venv/bin/activate
cd .. && cd backend

- To run Django dev server and watch file changes in the app

nodemon --exec python manage.py runserver

#(If you have a problem with the database and the server not being able to 
#connect to it, run your own mysql server. Don’t forget to go backend/DJCrudAPI/settings.py and change the database settings.

cd backend

- migrate to database (mysql )

python manage.py makemigrations
python manage.py migrate 

- then run the server again

)



