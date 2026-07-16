# smallest_django_repo
Example project, that demonstrates that django projects can be not so huge as its known.

# Here we go
As out project is small as possible, so batteries are not included: 
```commandline
pip install Django==6.0.7
```
Make django know about our project:
Powershell:
```powershell
$Env:DJANGO_SETTINGS_MODULE = "settings"
```
Linux:
```bash
export DJANGO_SETTINGS_MODULE=settings
```
Initialize the database:
```bash
python -m django migrate
```
Create superuser:
```commandline
python -m django createsuperuser
```
Run debug server:
```commandline
python -m django runserver
```
Open in browser: http://127.0.0.1:8000/admin/ and login with your superuser credentials. It works!

