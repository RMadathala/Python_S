import cx_Oracle
conn: object = cx_Oracle.connect(user="srvap162960dev", password='Snap!0gic',dsn="eipcd1.cnmevkzwtu3w.us-east-1.rds.amazonaws.com/eipcd1", encoding="UTF-8")
cursor = conn.cursor()
cursor.execute("select OWNER,table_name from all_tables where owner in ('STG_FFGE','A628961')")
tables=[(row[0],row[1]) for row in cursor.fetchall()]
for schema,table in tables:
    print(f"Displaing data for scema:{schema} and table:{table}")
    cursor.execute(f"select * from {schema}.{table}")
    rows=cursor.fetchall()
   # column_names=[desc[0] for desc in cursor.description]
    #print("\t".join(column_names))
    for row in rows:
        print("\t".join(str(cell) for cell in row))
cursor.close()
conn.close()
