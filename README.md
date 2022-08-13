# **snowball**  ❅  a financial independence tool

> Developed by [Mara](https://github.com/mhubelbank) && [Timmy](https://github.com/M-Allahham)

<br />

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pretium lectus quam id leo in. Ac tincidunt vitae semper quis lectus nulla at volutpat diam. Dapibus ultrices in iaculis nunc sed augue lacus viverra. Ac feugiat sed lectus vestibulum. Tempus egestas sed sed risus. Porttitor leo a diam sollicitudin tempor id eu nisl nunc. Fermentum et sollicitudin ac orci. Elementum facilisis leo vel fringilla est. Mauris vitae ultricies leo integer malesuada nunc vel. Fringilla phasellus faucibus scelerisque eleifend donec pretium. Tellus rutrum tellus pellentesque eu. Lectus proin nibh nisl condimentum. Sagittis nisl rhoncus mattis rhoncus urna.

<br />

> Built with:

- [Django Web Framework](https://www.djangoproject.com/)
- [Atlantis Dark UI Template](https://appseed.us/product/atlantis-dark/django/)
  
<br />

## Developer Guide

### Clone the Repository

```bash
git clone https://github.com/mhubelbank/snowball.git
cd snowball
```

<br />

### Set up Virtual Environment
> For `Unix` & `MacOS` 

```bash
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

> For `Windows` 
```
# Python 3.7 or higher is needed
virtualenv --python=3.10.6 env
. env/Scripts/activate
pip3 install -r requirements.txt 
```

<br />

### Create Local Database
```bash
python manage.py makemigrations
python manage.py migrate
```

<br />

### Run the Snowball App

```bash
python manage.py runserver
```

Then, navigate to `http://127.0.0.1:8000/`. 

<br />
