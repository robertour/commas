commas
======

Django-CMS Website

Installation instructions
---------------------------------

1.  Install pip and virtualenv in your machine:

        sudo apt-get install python-pip python-dev build-essential
        sudo pip install --upgrade pip
        sudo pip install --upgrade virtualenv

2. Install virtualenvwrapper:

        sudo pip install virtualenvwrapper
        mkdir -p ~/.venvs
        export WORKON_HOME=~/.venvs
        source /usr/local/bin/virtualenvwrapper.sh

3. Add the this at the end of your .basrhc:

        export WORKON_HOME=~/.venvs
        source /usr/local/bin/virtualenvwrapper.sh

4. Create a virtualenv for the project:

        mkvirtualenv commas --no-site-packages

5. You should be able to enable and disable it. The system prompt must change where you have it enable:

        workon commas
        deactivate

6. Clone the project it in your desired location:

        cd $HOME
        git clone https://github.com/robertour/commas

7. Enter in the new location and update the virtual environment previously created:

        cd git/commas
        workon commas
        pip install -U -r requirements.txt

8. Create the database (tico-tico):

        python manage.py syncdb --all
        python manage.py migrate --fake

9. Migrate the tables:

        python manage.py migrate


Update tables:
--------------

        python manage.py syncdb
        python manage.py migrate



