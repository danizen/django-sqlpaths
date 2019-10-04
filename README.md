# django-sqlpaths

Runs sql scripts upon the Django post_migrate signal in a way similar to flywaydb

## Management Commands

sqlpaths validate - validate the checksums of each of the files.

sqlpaths migrate - do the same thing as the post migration signal

sqlpaths info - give the status on each of the files and whether they've been run.

## Settings

```
SQLPATHS = {
   'root': ... path to a root directory, default os.path.join(BASE_DIR, 'sql')
   'include': ... glob pattern of files to include, default [ '**/*.sql' ]
   'exclude': ... list of regular expressions to exclude'
   'auto': ... pattern of files to run each time [ 'auto.sql' ]
   'enabled': ... true or fales, default True
   'dbshell': ... whether to run commands in a dbshell, default False
}
```

## Issues

Database Routing - sqlpaths must support some sort of specialized logic for database routing


