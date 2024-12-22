#!/bin/sh
sleep 5  # Wait for database to be ready

# check if migrations has been initialized
if [ ! -d "migrations/versions" ]; then
    flask db init
    flask db migrate -m "migration"
fi

# Apply migrations and start app
flask db upgrade
python app.py
