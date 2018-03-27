from hobby.models import Board
from hobby.models import Like
from hobby.models import Event
from hobby.models import Message
from hobby.models import Profile
from hobby.models import User
import random
import datetime

def insert_db():
    time_start = datetime.datetime.now()
    count = 10
    users = (User(username='User name %s' % i, password='password %s' % i, email='User email %s' % i)
        for i in range(count))
    users = User.objects.bulk_create(users)

    boards = (Board(title='board_title %s' % i, subject='board_subject %s' % i, created_by_id=random.randint(users[0].pk, users[-1].pk))
        for i in range(count))
    boards = Board.objects.bulk_create(boards)

    events = (Event(title='event_title %s' % i, subject='board_subject %s' % i, date='2020-10-10 10:10',
        created_by_id=random.randint(users[0].pk, users[-1].pk)) for i in range(count))
    events = Event.objects.bulk_create(events)

    Associate = Event.boards.through
    through = (Associate(event=events[i], board=boards[i]) for i in range(count))
    Associate.objects.bulk_create(through)

    message = (Message(message='message % i' % i, event_id=random.randint(events[0].pk, events[-1].pk),
        created_by_id=random.randint(users[0].pk, users[-1].pk)) for i in range(count))
    message = Message.objects.bulk_create(message)

    profiles = (Profile(user=users[i], is_organizer=random.choice([True, False]),
        birth_date='1996-05-06', bio='Hello, im %s' % i) for i in range(count))
    profiles = Profile.objects.bulk_create(profiles)

    likes = (Like(content_object=events[i], user=users[i]) for i in range(count))
    likes = Like.objects.bulk_create(likes)

    time_stop = datetime.datetime.now()
    print('time=', time_stop - time_start)


insert_db()


