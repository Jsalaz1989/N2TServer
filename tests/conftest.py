import pytest
from app import create_app



@pytest.fixture(scope='session')
def database(request):
    '''
    Create a Postgres database for the tests, and drop it when the tests are done.
    '''
    # pg_host = DB_OPTS.get("host")
    # pg_port = DB_OPTS.get("port")
    # pg_user = DB_OPTS.get("username")
    # pg_db = DB_OPTS["database"]

    pg_host = "localhost"
    pg_port = 8300
    pg_user = "admin"
    pg_db = "n2t"

    init_postgresql_database(pg_user, pg_host, pg_port, pg_db)

    @request.addfinalizer
    def drop_database():
        drop_postgresql_database(pg_user, pg_host, pg_port, pg_db, 11.5)


@pytest.fixture(scope='session')
def app(database):
    '''
    Create a Flask app context for the tests.
    '''
    app = create_app()

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONN

    return app


@pytest.fixture(scope='session')
def _db(app):
    '''
    Provide the transactional fixtures with access to the database via a Flask-SQLAlchemy
    database connection.
    '''
    db = SQLAlchemy(app=app)

    return db