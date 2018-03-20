import datetime

from hobby.models import User


def clear():
    time_start = datetime.datetime.now()
    users = User.objects.all().exclude(username='artur')
    users.delete()
    print('all clear!')
    time_stop = datetime.datetime.now()
    print('time=', time_stop - time_start)


clear()

