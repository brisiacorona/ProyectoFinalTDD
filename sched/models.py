from sqlalchemy import datetime
from sqlalchemy import Column, Boolean, ForeignKey
from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import synonym, relationship
from sqlalchemy.ext.declarative import declarative_base
from werkzeug import check_password_hash
from werkzeug import generate_password_hash
#from datetime import timedelta
from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class User(Base):
    name = Column('name', String(200))
    email = Column(String(100), unique=True, nullable=False)
    active = Column(Boolean, default=True)
    _password = Column('password', String(100))


def _get_password(self):
    return self._password


def _set_password(self, password):
    if password:
        self._password = generate_password_hash(password)
        password_descriptor = property(_get_password,
                                       _set_password)
        password = synonym('_password',
                           descriptor=password_descriptor)


class Appointment(Base):

    """An appointment on the calendar."""
    __tablename__ = 'appointment'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, default=datetime.now)
    modified = Column(DateTime, default=datetime.now,
                      onupdate=datetime.now)

    title = Column(String(255))
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)
    allday = Column(Boolean, default=False)
    location = Column(String(255))
    description = Column(Text)

    user_id = Column(Integer,
                     ForeignKey('user.id'), nullable=False)
    user = relationship(User, lazy='joined', join_depth=1)


def get_id(self):
    return str(self.id)


def is_active(self):
    return True


def is_anonymous(self):
    return False


def is_authenticated(self):
    return True


@property
def duration(self):
    delta = self.end - self.start
    return delta.days * 24 * 60 * 60 + delta.seconds


def __repr__(self):
    return (u'<{self.__class__.__name__}: {self.id}>'
            .format(self=self))

if __name__ == '__main__':
    engine = create_engine('sqlite:///sched.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    now = datetime.now()
    session.add(Appointment(
        title='Important Meeting',
        start=now + timedelta(days=3),
        end=now + timedelta(days=3, seconds=3600),
        allday=False,
        location='The Office'))
    session.commit()

    usuario = User(
        name='mayra',
        email='sun.prinsses@hotmail.com',
        active=True,
        user_id='mayra',
        user='mayra')
    usuario._set_password("mayra")
    session.add(usuario)
    session.commit()
