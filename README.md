1. To start the project, first add a `.env` file following the 
   variables in the `.env.example`

2. To apply the initial migrations run
   `docker-compose run --rm app python manage.py migrate`

3. To seed the database with chinook dataset run
   `docker-compose run --rm app python loaddata chinook.json`

4. To make ORM queries use `python manage.py shell_plus --ipython`