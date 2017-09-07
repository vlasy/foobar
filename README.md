# Simple example of migration problem

1 - I created the model - class Failure with only id and description
2 - I created initial fixture initial.json
3 - I added a field to Failure class
4 - I deleted SQLite DB and now I cannot run migration

After running python manage.py migrate I get 
"sqlite3.OperationalError - no such column 'confirmed' "