import os
try:
    from distutils import dir_util
except ImportError:
    session.flash = T('requires distutils, but not installed')
<<<<<<< HEAD
    redirect(URL('default','site'))
=======
    redirect(URL('default', 'site'))
>>>>>>> upstream/master
try:
    from git import *
except ImportError:
    session.flash = T('requires python-git, but not installed')
<<<<<<< HEAD
    redirect(URL('default','site'))
=======
    redirect(URL('default', 'site'))

>>>>>>> upstream/master

def deploy():
    apps = sorted(file for file in os.listdir(apath(r=request)))
    form = SQLFORM.factory(
<<<<<<< HEAD
        Field('osrepo',default='/tmp',label=T('Path to local openshift repo root.'),
              requires=EXISTS(error_message=T('directory not found'))),
        Field('osname',default='web2py',label=T('WSGI reference name')),
        Field('applications','list:string',
              requires=IS_IN_SET(apps,multiple=True),
              label=T('web2py apps to deploy')))

    cmd = output = errors= ""
    if form.accepts(request,session):
=======
        Field(
            'osrepo', default='/tmp', label=T('Path to local openshift repo root.'),
            requires=EXISTS(error_message=T('directory not found'))),
        Field('osname', default='web2py', label=T('WSGI reference name')),
        Field('applications', 'list:string',
              requires=IS_IN_SET(apps, multiple=True),
              label=T('web2py apps to deploy')))

    cmd = output = errors = ""
    if form.accepts(request, session):
>>>>>>> upstream/master
        try:
            kill()
        except:
            pass
<<<<<<< HEAD
        
        ignore_apps = [item for item in apps if not item in form.vars.applications]
=======

        ignore_apps = [
            item for item in apps if not item in form.vars.applications]
>>>>>>> upstream/master
        regex = re.compile('\(applications/\(.*')
        w2p_origin = os.getcwd()
        osrepo = form.vars.osrepo
        osname = form.vars.osname
        #Git code starts here
        repo = Repo(form.vars.osrepo)
        index = repo.index
        assert repo.bare == False

        for i in form.vars.applications:
<<<<<<< HEAD
            appsrc = os.path.join(apath(r=request),i)
            appdest = os.path.join(osrepo,'wsgi',osname,'applications',i)
            dir_util.copy_tree(appsrc,appdest)
            #shutil.copytree(appsrc,appdest)
            index.add(['wsgi/'+osname+'/applications/'+i])
            new_commit = index.commit("Deploy from Web2py IDE")
        
=======
            appsrc = os.path.join(apath(r=request), i)
            appdest = os.path.join(osrepo, 'wsgi', osname, 'applications', i)
            dir_util.copy_tree(appsrc, appdest)
            #shutil.copytree(appsrc,appdest)
            index.add(['wsgi/' + osname + '/applications/' + i])
            new_commit = index.commit("Deploy from Web2py IDE")

>>>>>>> upstream/master
        origin = repo.remotes.origin
        origin.push
        origin.push()
        #Git code ends here
<<<<<<< HEAD
    return dict(form=form,command=cmd)
        
class EXISTS(object):
    def __init__(self, error_message='file not found'):
        self.error_message = error_message
    def __call__(self, value):
        if os.path.exists(value):
            return (value,None)
        return (value,self.error_message)
=======
    return dict(form=form, command=cmd)


class EXISTS(object):
    def __init__(self, error_message='file not found'):
        self.error_message = error_message

    def __call__(self, value):
        if os.path.exists(value):
            return (value, None)
        return (value, self.error_message)
>>>>>>> upstream/master
