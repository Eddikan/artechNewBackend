import os
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool
from alembic import context

# Import the Base and models
from app.db import Base  # Import your SQLAlchemy Base
from app.models.project import Project  # Import the Project model
from app.models.user import User  # Import the User model
from app.core.config import settings  # Import settings for the database URL

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set your target metadata here. This is the metadata that Alembic will use to detect changes.
target_metadata = Base.metadata

# Set the database URL dynamically from your settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

# Function to run migrations in online mode (when connected to the database)
def run_migrations_online():
    connectable = create_engine(settings.DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True  # Necessary for SQLite migrations
        )

        with context.begin_transaction():
            context.run_migrations()

# Function to run migrations in offline mode (without a DB connection)
def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# Choose the mode to run migrations based on the environment
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
