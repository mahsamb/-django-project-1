@echo off
set PGDATA=%~dp0postgres_data
set PGLOG=%~dp0postgres.log
"C:\Program Files\PostgreSQL\14\bin\pg_ctl.exe" -D "%PGDATA%" -l "%PGLOG%" start
echo Local PostgreSQL started on localhost:5432
