commas
======

Django-CMS Website

Installation instructions
---------------------------------

1.  Install pip and virtualenv in your machine:

        sudo apt-get install python-pip python-dev build-essential
        sudo pip install --upgrade pip
        sudo pip install --upgrade virtualenv
        
2.  Install the dependencies for PIL

        sudo apt-get install python-imaging  python-dev libjpeg8 libjpeg8-dev libfreetype6 libfreetype6-dev

3. Install virtualenvwrapper:

        sudo pip install virtualenvwrapper
        mkdir -p ~/.venvs
        export WORKON_HOME=~/.venvs
        source /usr/local/bin/virtualenvwrapper.sh

4. Add the this at the end of your .basrhc:

        export WORKON_HOME=~/.venvs
        source /usr/local/bin/virtualenvwrapper.sh

5. Create a virtualenv for the project:

        mkvirtualenv commas --no-site-packages

6. You should be able to enable and disable it. The system prompt must change where you have it enable:

        workon commas
        deactivate

7. Clone the project it in your desired location:

        cd $HOME
        git clone https://github.com/robertour/commas

8. Enter in the new location and update the virtual environment previously created:

        cd git/commas
        workon commas
        pip install -U -r requirements.txt

9. Create the database (tico-tico):

        python manage.py syncdb --all
        python manage.py migrate --fake

10. Migrate the tables:

        python manage.py migrate


Update tables:
--------------

        python manage.py syncdb
        python manage.py migrate



