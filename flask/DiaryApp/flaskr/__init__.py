import os

from flask import Flask, app


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)  #instance_relative_config creates a instance folder relative to the root of the app. that is basicflask and not flaskr
    app.config.from_mapping(
        #SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #creates flaskr.sqlite file
        UPLOAD_FOLDER=os.path.join(app.instance_path,'uploads')  #creates uploads folder
    )

    #tries to fetch the config file or test_config and override the mapping of the data initilaise before.
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True) 
    else:
        app.config.from_mapping(test_config)


    #ensures that app.instance_path exists. Flask doesn’t create the instance folder automatically 
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass 

    try:
        os.makedirs(app.config['UPLOAD_FOLDER'])
    except OSError:
        pass
  
    #This imports the db module from the current package and calls init_app function by passing app object to it.  
    from . import db
    db.init_app(app)

    #This registers a Flask blueprint named bp from the auth module with the application
    from . import auth
    app.register_blueprint(auth.bp)

    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')


    return app



'''flask --app flaskr run //to run the app'''

'''

config.py file needs to created in the instance folder. 
double check to see if SECRET_KEY has been assigne by entering the shell: flask --app flaskr shell and do this -> print(app.config['SECRET_KEY']) 

'''