# -*- coding: utf-8 -*-
# Code By Severin Orth (MartinMartimeo)
# martin@martimeo.de
# Do not use without permission or care

__author__  = "Severin <MartinMartimeo> Orth <martin@martimeo.de>"
__date__    = "$25.05.2011 11:19:34$"

import logging
import os

from sqlalchemy import *
import sqlalchemy.ext.declarative
import sqlalchemy.orm

class DatabaseError(Exception):
    pass

class DatabaseObject(object):
    pass

class Database(object):

    """
        Connects to Database
        adds riso.data for quering
    """
    def __init__(self, riso):

        self.riso = riso
        self.config = riso.config

        # Config Values
        self.sqla = DatabaseObject()
        self.sqla.type = self.config("database/type", "sqllite")
        self.sqla.user = self.config("database/user", "")
        self.sqla.pwd = self.config("database/password", "")
        self.sqla.host = self.config("database/host", "")
        self.sqla.name = self.config("database/dbname", "riso")
        self.dns = self.config("database/dns", "%s://%s:%s@%s/%s" % (self.sqla.type, self.sqla.user, self.sqla.pwd, self.sqla.host, self.sqla.name))

        # Engine
        self.db = create_engine(self.dns)

        # Bind Base and Metadata
        from classes.dbbase import DbBase
        self.base = DbBase
        self.metadata = self.base.metadata

        # Create Session
        DatabaseSession = sqlalchemy.orm.sessionmaker(bind=self.db, autoflush=True, autocommit=True)
        self.session = DatabaseSession()

        # Logging
        if self.config("database/debug", "error") == "debug":
            logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)
            logging.getLogger('sqlalchemy.orm').setLevel(logging.DEBUG)
        if self.config("database/debug", "error") == "info":
            logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
            logging.getLogger('sqlalchemy.orm').setLevel(logging.INFO)
        if self.config("database/debug", "error") == "error":
            logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)
            logging.getLogger('sqlalchemy.orm').setLevel(logging.ERROR)

        # Load all Models
        self.models = {}
        models = os.listdir('./models')
        for model in models:
            if model.endswith('.py') and model != '__init__.py':
                model_name = 'models.%s' % model[:-3]
                self.models[model_name] = __import__(model_name, fromlist=True)

        # Drop all Tables
        if self.config("database/developing", True):
            self.metadata.drop_all(bind=self.db)

        # Check existance of all Tables
        try:
            self.metadata.create_all(bind=self.db)
        except sqlalchemy.exc.OperationalError, msg:
            raise DatabaseError("Could not create Tables: %s" % msg)

        # Make available via Riso
        riso.data = self.session

        logging.info("Connecting to Database succesfull")