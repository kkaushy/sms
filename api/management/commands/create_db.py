import sys
import logging
import MySQLdb

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

rds_host = 'sms-db.cluster-cfjpitkmjpbd.ap-south-1.rds.amazonaws.com'
db_name = 'smsdb'
user_name = 'smsuser'
password = 'welcome2020'
port = 3306

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = 'Creates the initial database'

    def handle(self, *args, **options):
        print('Starting db creation')
        try:
            db = MySQLdb.connect(host=rds_host, user=user_name,
                                 password=password, db="mysql", connect_timeout=5)
            c = db.cursor()
            print("connected to db server")
            c.execute("""CREATE DATABASE smsdb;""")
            c.execute(
                """GRANT ALL PRIVILEGES ON smsdb.* TO 'smsuser' IDENTIFIED BY 'smsuser';""")
            c.close()
            print("closed db connection")
        except:
            logger.error(
                "ERROR: Unexpected error: Could not connect to MySql instance.")
            sys.exit()























# import psycopg2
# from psycopg2 import sql
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
# host = "z71xobn9ff.execute-api.ap-south-1.amazonaws.com"
# user_name = "postgres"
# dbname = "sms_db_prod"
# password = "FdqOgi9kVYuLi9S1di9S"

# try:
#     con = psycopg2.connect(dbname=dbname, user=user_name, host=host, password=password)
#     con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE
#     cur = con.cursor()
#     # Use the psycopg2.sql module instead of string concatenation 
#     # in order to avoid sql injection attacs.
#     cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))

# except Exception as e:
#     print(e)
