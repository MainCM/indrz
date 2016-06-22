#!/bin/python
# coding: utf-8
import psycopg2
import time

# do a timestamp for being able to track execution time (if you want)
startscript = time.time()  # we will use this later

def create_db_conn():
    # Database Connection Info
    db_host = "137.208.3.187"
    #db_host = "localhost"
    db_user = "wuwien"
    #db_user = "postgres"
    #db_passwd = "12345"
    db_passwd = "oi4jtoiwjfds"
    db_database = "wuwien"
    db_port = "5432"



    # get a connection handle to Postgresql queries
    conn = psycopg2.connect(host=db_host, user=db_user, port=db_port, password=db_passwd, database=db_database)

    # get the cursor

    return conn

# list of the floors to update
# floor_list = ('ug01_poi', 'eg00_poi', 'og01_poi', 'og02_poi', 'og03_poi', 'og04_poi', 'og05_poi', 'og06_poi' )
pg_schema = ('geodata')
floor_n = ('ug01_', 'eg00_', 'og01_', 'og02_', 'og03_', 'og04_', 'og05_', 'og06_' )
floor_values = ('poi', 'rooms', 'umriss', 'networklines', 'carto_lines', 'doors', 'furniture' )
other_tables = ('parking_garage', 'raumlist_buchungsys', 'temp_wu_personal_data' )
outdoor_tables = ('od_all_fill', 'od_all_polygons', 'od_baeume_linien', 'od_blindeleitlinie', 'od_fahrradstellplatz', 'od_familie_linie',
                  'od_orientierungselemente_linie', 'od_raucherzone', 'od_relax_area')
bibliothek_tables = ('bibliothek')

building_ids = {'EA': 1, 'D5': 2, 'AD':3, 'LC': 999, 'D1': 999, 'D2': 999, 'D3': 999, 'D4': 999, 'SC': 999, 'TC': 999}

rooms_cols = ('refname', 'room_name', 'room_number', 'building', 'floor', 'description', 'geom', 'building_number',
              'aks_nummer', 'entrance_poi_id', 'room_code', 'category_en' )

indrz_spaces_cols = {'short_name': rooms_cols[1], 'geom': rooms_cols[6], 'room_number': rooms_cols[2],
                      'room_external_id': rooms_cols[8], 'room_number_sign': rooms_cols[10],
                     'fk_space_type_id': rooms_cols[11]}

# list of database field names that we want to update
# you can only update one field at one time
# possible field name you can use 'name'
# possible field name you can use 'cat_main'
# possible field name you can use 'cat_sub'
# possible field name you can use 'description'
# possible field name you can use 'name_en'
# possible field name you can use 'cat_main_en'
# possible field name you can use 'cat_sub_en'
# possible field name you can use 'description_en'
# possible field name you can use 'sort_order'

# here are your variables to change for updating the pois
update_field_name = 'building' #enter the name of the field you wish to update
#old_value = u"Essen und Trinken" # enter the old database values you want to change
new_value = u"TC" # enter the NEW database values you want
where_claus = 'building'
where_value = 'D1 TC'

# here you must change the
def gen_datalist(data_type=0):
    """
    pass in the position
    :param data_type:
    :return:
    """
    poi_list = []
    for floor in floor_n:
        poi_list.append('geodata.' + floor + floor_values[data_type])
    return poi_list

def union_floor_data(data_list):
    merged_data = [] # data for all floors
    for table_name in data_list:
        term = "WC"
        sql_q = "select * from {0}"
        conn = create_db_conn()
        cur = conn.cursor()
        cur.execute(sql_q.format(table_name,), dict(like='%' + term + '%'))
        all_values = cur.fetchall()
        merged_data.append(all_values)

    return merged_data

poi_list = gen_datalist(0)
room_list = gen_datalist(1)
umriss_list = gen_datalist(2)
networklines_list = gen_datalist(3)
carto_list = gen_datalist(4)
doors_list = gen_datalist(5)
furniture_list = gen_datalist(6)

print(poi_list)
print(room_list)
# term="WC"
# sql= "select room_name from geodata.og01_rooms where room_name LIKE %(like)s ESCAPE '='"
# cur.execute(sql, dict(like= '%'+term+'%'))

#cur.execute('select room_name from geodata.og01_rooms where room_name LIKE %(like)s'WC%';')
conn2 = create_db_conn()
cur2 = conn2.cursor()
cur2.execute('select room_name from geodata.eg00_rooms')
x = cur2.fetchall()
print(x)

for value in x:
    first_val = value[0]
    print(first_val)
    if first_val is not None:
        print(first_val)
print (x)
cols_names = [col_name[0] for col_name in cur2.description]
# print(cols_names)
# print(fx)


# if room_name value = x:
    # then set room type = foo:
# elif room_name value = y:
    # then set room _type = kaa

# def map_cols():
    # r = map(func, seq)





# for poi in poi_list:
#     cur.execute("UPDATE geodata."+poi+" SET "+update_field_name+" = %s WHERE "+where_claus+" = %s", (new_value, where_value,))

# conn.commit()
# cur.close()
# conn.close()

endscript = time.time()
endtime = endscript - startscript
print ('script run in ' + str(endscript - startscript) + ' seconds or ' + '\n'
       + str((endscript - startscript)*1000) + ' miliseconds')