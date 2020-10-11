#!/usr/bin/python
import pymysql
import json

def main():
	print(example_inventory_query())

def get_Connection():
	connection = pymysql.connect(host='192.168.9.5',user='ansible',password='123456',\
			db='ansible',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	return connection
 
def example_inventory_query():
	data={}
	data["_meta"]={}
	data["_meta"]["hostvars"]={}
	data["all"]={}
	data["all"]["children"]=[]

	mysql_con=get_Connection()
	sql="select * from AS_HOSTS INNER JOIN AS_GROUPS ON host_group=group_id"
	try:
		sql="select * from AS_GROUPS" 
		with mysql_con.cursor() as cursor:
		  cursor.execute(sql)
		  for row in cursor:
		     data["all"]["children"].append(row['group_name'])

		sql="select group_name from AS_GROUPS"
		with mysql_con.cursor() as cursor:
		   cursor.execute(sql)
		   for row in cursor:
		      grpname=row['group_name']
		      data[grpname]={}
		      data[grpname]["hosts"]=[] 	
		      sql_host="select * from AS_HOSTS INNER JOIN AS_GROUPS ON host_group=group_id WHERE group_name='"+grpname+"'"
		      with mysql_con.cursor() as cursor_new:
		        cursor_new.execute(sql_host)
		        for row_new in cursor_new:
		           data[grpname]["hosts"].append(row_new['host_name'])
	finally:
		mysql_con.close()
	with open('inventory.json', 'w') as outfile:  
		json.dump(data, outfile) 
	with open('inventory.json', 'r') as infile:
		data_json = infile.read().replace('\n', '')
	return data_json


if __name__ == '__main__':
	main()
	
