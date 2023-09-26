import os
import time
import eel


@eel.expose
def hello():
    print('Hello from %s' % time.time())


eel.init(str(os.path.split(os.path.realpath(__file__))[0]) + '/../static_web')
eel.start('index.html', mode='chrome')
