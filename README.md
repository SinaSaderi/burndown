Salam
# BurnDown

A simple BurnDown chart generator.

# Screenshot

![Screenshot](http://sina.sinasaderi.ir/scrt.png)

## How to run

To run Burndown in development mode; Just use steps below:

1. Install `python2`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/SinaSaderi/burndown`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/SinaSaderi/burndown && cd burndown
  virtualenv -p python2 build  # Create virtualenv named build
  source build/bin/activate
  pip install -r requirements.txt
  python manage.py migrate  # Create database tables
  ```

4. Run `Burndown` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your chart version.

## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python2`, `pip`, `virtualenv`
2. Clone the project using:  `git clone https://github.com/SinaSaderi/burndown`.
3. Make Environment Ready Like This:
``` Command Prompt
cd burndown
virutalenv -p "PATH\TO\Python.exe" build # Give Full Path To python.exe
build\Scripts\activate # Activate The Virutal Environment
pip install -r requirements.txt
python manage.py migrate # Create Database Tables
```
4. Run `Burndown` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your Burndown version.

## Run tests

To run tests in Burndown simply use `python manage.py test`.
