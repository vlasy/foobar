# Simple example of migration problem

- I created the model - class `Failure` with only `id` and `description`
- I created initial fixture `initial.json`
- I added a field to `Failure` class
- I deleted SQLite DB and now I cannot run migration

After running `python manage.py migrate` I get 
`sqlite3.OperationalError - no such column 'confirmed`