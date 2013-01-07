def webapp_add_wsgi_middleware(app):
    from google.appengine.ext.appstats import recording
    app = recording.appstats_wsgi_middleware(app)
    return app
<<<<<<< HEAD:appengine_config.py





=======
>>>>>>> upstream/master:appengine_config.example.py
