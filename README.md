on windows:
```
    cd empty_folder_path
    git clone https://github.com/parsadany/alan.git .
    pip install -r requirements.txt
    python manage.py runserver
```

this will serve on localhost:8000, you can serve on NAT using:

```
    python manage.py runserver 0.0.0.0:7777
```

this will serve on all interfaces on your laptop, even in your wifi network, with the specified ip address and port 7777.

see localhost, this will raise a 404 and shows valid urls, you can use cache url.

this wil use the sqlite db beside the app included in the repo.