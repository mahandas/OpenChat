import psycopg2
import json
from sqlalchemy import create_engine  
from sqlalchemy import Table, Column, String, MetaData


value1=  json.loads('{"email":"saurabh.n@finiq.com","first_name":"saurabh","last_name":"negi","gender":"M","password":"12345"}')
conn =  psycopg2.connect(host="127.0.0.1",port="14214",database="postgres", user="postgres", password="mahandas")
	
cur = conn.cursor()
cur.execute('SET search_path TO finiqchatengine')
print("SET search path done")
val = cur.execute('SELECT * FROM finiqchatengine.add_user_if_not_present(\'{"email":"saurabh.n@finiq.com","first_name":"saur1abh","last_name":"negi","gender":"M","password":"12345"}\')')
print(val)

db_string = "postgres://postgres:mahandas@127.0.0.1:14214/postgres"

db = create_engine(db_string)
meta = MetaData(db)
userTable = Table('user_details',meta,Column('user_id'),Column('mobile_no'))

with db.connect() as conn:

    # Read
    select_statement = userTable.select()
    result_setet = conn.execute('SET search_path TO finiqchatengine')
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)
