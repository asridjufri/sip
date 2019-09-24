from django.db import connection

def get_tourisme_vs_pendapatan():
    query = ("SELECT b.categoryid, sum(a.pendapatan) as pendapatan "
             "FROM data_tourist a "
             "LEFT JOIN master_tourism b "
             "ON a.tourismid = b.tourismid "
             "WHERE lower(b.categoryid) in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') "
             "GROUP  by b.categoryid;")
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'categoryid':row[0], 'pendapatan':row[1]}
        results.append(item)
    return results

def get_tourisme_vs_pendapatan_annualy():
    query = ("SELECT year(a.date) year, b.categoryid, sum(a.pendapatan) as pendapatan "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "WHERE lower(b.categoryid) in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman')  "
            "GROUP  by year(a.date), b.categoryid "
            "order by categoryid, year, pendapatan ;")
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'year': row[0],'categoryid':row[1], 'pendapatan':row[2]}
        results.append(item)
    return results

def get_tourisme_vs_pendapatan_monthly():
    query =("SELECT a.date as date, b.categoryid,  sum(a.pendapatan) as pendapatan "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "WHERE lower(b.categoryid) in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') "
            "GROUP  by a.date, b.categoryid "
            "order by categoryid, a.date") 
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'date': row[0],'categoryid':row[1], 'pendapatan':row[2]}
        results.append(item)
    return results



def get_number_tourism_per_category_per_year(categoryid):
    query =("SELECT year(a.date) year, b.categoryid,sum(a.indonesia) as indonesia, sum(australia) as australia, "
            "sum(prancis) as prancis,sum(india) as india,sum(jepang) as jepang, sum(malaysia) as malaysia, "
            "sum(singapore) as singapore, sum(kanada) as kanada,sum(brazil) as brazil, sum(belanda) as belanda, "
            "sum(china) as china, sum(jerman) as jerman,sum(inggris) as inggris, sum(pakistan) as pakistan, "
            "sum(philipina) as philipina,sum(thailand) as thailand,sum(cili) as cili,sum(arab) as arab, "
            "sum(lainlain) as lainlain  "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "WHERE b.categoryid='%s'  "
            "GROUP  by b.categoryid, year(a.date); " %(categoryid)) 
    # in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman')


    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'year':row[0], 'categoryid': row[1],'indonesia':row[2], 'australia':row[3], 'prancis':row[4],'india':row[5],'jepang':row[6],
               'malaysia':row[7], 'singapore':row[8], 'kanada':row[9], 'brazil':row[10], 'belanda':row[11],
               'china':row[12], 'jerman':row[13], 'inggris':row[14], 'pakistan':row[15], 'philipina':row[16],
               'thailand':row[17], 'cili':row[18], 'arab':row[19], 'lainlain':row[20]
                }
        results.append(item)
    return results

def get_number_tourism_percategory_per_month(categoryid, ayear):
    query =( "SELECT month(a.date) month, b.categoryid,sum(a.indonesia) as indonesia, sum(australia) as australia, "
    "sum(prancis) as prancis,sum(india) as india,sum(jepang) as jepang, sum(malaysia) as malaysia, "
    "sum(singapore) as singapore, sum(kanada) as kanada,sum(brazil) as brazil, sum(belanda) as belanda, "
    "sum(china) as china, sum(jerman) as jerman,sum(inggris) as inggris, sum(pakistan) as pakistan, "
    "sum(philipina) as philipina,sum(thailand) as thailand,sum(cili) as cili,sum(arab) as arab, "
    "sum(lainlain) as lainlain, sum(a.mancanegara) as mancanegara "
    "FROM data_tourist a "
    "LEFT JOIN master_tourism b "
    "ON a.tourismid = b.tourismid "
    "WHERE b.categoryid='%s'  "
    "AND year(a.date)=%s "
    "GROUP  by b.categoryid, month(a.date); " %(categoryid, ayear) )
    #in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') 
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'month':row[0], 'categoryid': row[1],'indonesia':row[2], 'australia':row[3], 'prancis':row[4],'india':row[5],'jepang':row[6],
               'malaysia':row[7], 'singapore':row[8], 'kanada':row[9], 'brazil':row[10], 'belanda':row[11],
               'china':row[12], 'jerman':row[13], 'inggris':row[14], 'pakistan':row[15], 'philipina':row[16],
               'thailand':row[17], 'cili':row[18], 'arab':row[19], 'lainlain':row[20],'mancanegara':row[21]
                }
        results.append(item)
    return results

def get_number_tourism_per_category_per_year_domestic_mancanegara(categoryid):
    query=("SELECT year(a.date) year, b.categoryid,sum(a.indonesia) as indonesia, sum(a.mancanegara) as mancanegara "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "where b.categoryid='%s' "
            "GROUP  by year(a.date), b.categoryid; "%(categoryid)
    )
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'year':row[0], 'categoryid': row[1],'domestic':row[2], 'mancanegara':row[3] }
        results.append(item)
    return results
def get_number_tourism_percategories_at_year_domestic_mancanegara(categories, ayear):
    query=("SELECT b.categoryid,sum(a.indonesia) as domestic, sum(a.mancanegara) as mancanegara "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "where b.categoryid in (%s) "
            "and year(a.date)=%s " 
            "GROUP   b.categoryid; "%(categories, ayear)
    )
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'categoryid': row[0],'domestic':row[1], 'mancanegara':row[2] }
        results.append(item)
    return results
def get_number_tourism_per_category_per_month_domestic_mancanegara(ayear,idkecamatan=None):
    query=''
    if idkecamatan:
        query = ("SELECT month(a.date) month, b.categoryid,sum(a.indonesia) as domestic, sum(a.mancanegara) as mancanegara "
            " FROM data_tourist a "
            " LEFT JOIN master_tourism b "
            " ON a.tourismid = b.tourismid "
            " where b.categoryid in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') "
            " and year(a.date)=%s and b.kecamatanid = '%s' "
            " GROUP by  b.categoryid , month(a.date); " %(ayear,idkecamatan)
        )
    else:
        query = ("SELECT month(a.date) month, b.categoryid,sum(a.indonesia) as domestic, sum(a.mancanegara) as mancanegara "
            " FROM data_tourist a "
            " LEFT JOIN master_tourism b "
            " ON a.tourismid = b.tourismid "
            " where b.categoryid in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') "
            " and year(a.date)=%s "
            " GROUP by  b.categoryid , month(a.date); " %(ayear)
        )
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'month': row[0],'categoryid':row[1], 'domestic':row[2], 'mancanegara':row[3] }
        results.append(item)
    return results

def get_number_domestic_mancanegara_at_year(ayear,idkecamatan=None):
    query=''
    if idkecamatan:
        query =("SELECT year(a.date) ,sum(a.indonesia) as indonesia, sum(a.mancanegara) as mancanegara "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "where year(a.date) = %s and kecamatanid='%s' "
            "GROUP  by year(a.date); " %(ayear,idkecamatan))
    else:
        query =("SELECT year(a.date) ,sum(a.indonesia) as indonesia, sum(a.mancanegara) as mancanegara "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "where year(a.date) = %s "
            "GROUP  by year(a.date); " %(ayear))

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'year': row[0],'domestic':row[1], 'mancanegara':row[2] }
        results.append(item)
    return results

def get_number_tourist_per_categories_at_year(ayear, idkecamatan=None):
    
    query=''
    if idkecamatan:
        query =("SELECT year(a.date) , b.categoryid,sum(a.indonesia + a.mancanegara) as tourist "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "where year(a.date) = %s and b.categoryid in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') and b.kecamatanid = '%s' "
            "GROUP  by year(a.date), b.categoryid; " %(ayear,idkecamatan))
    else:
        query =("SELECT year(a.date) , b.categoryid,sum(a.indonesia + a.mancanegara) as tourist "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "where year(a.date) = %s and b.categoryid in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') "
            "GROUP  by year(a.date), b.categoryid; " %(ayear))

    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'year': row[0],'categoryid':row[1], 'tourist':row[2] }
        results.append(item)
    return results
    
def get_tourism_vs_wisatawan_annualy():
    query =("SELECT year(a.date) year, b.categoryid,sum(a.indonesia) as indonesia, sum(australia) as australia, "
            "sum(prancis) as prancis,sum(india) as india,sum(jepang) as jepang, sum(malaysia) as malaysia, "
            "sum(singapore) as singapore, sum(kanada) as kanada,sum(brazil) as brazil, sum(belanda) as belanda, "
            "sum(china) as china, sum(jerman) as jerman,sum(inggris) as inggris, sum(pakistan) as pakistan, "
            "sum(philipina) as philipina,sum(thailand) as thailand,sum(cili) as cili,sum(arab) as arab, "
            "sum(lainlain) as lainlain  "

            "FROM data_tourist a "

            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "WHERE lower(b.categoryid) in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman')  "
            "GROUP  by b.categoryid, year(a.date); ")
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={ 'year':row[0], 'categoryid': row[1],'indonesia':row[2], 'australia':row[3], 'prancis':row[4],'india':row[5],'jepang':row[6],
               'malaysia':row[7], 'singapore':row[8], 'kanada':row[9], 'brazil':row[10], 'belanda':row[11],
               'china':row[12], 'jerman':row[13], 'inggris':row[14], 'pakistan':row[15], 'philipina':row[16],
               'thailand':row[17], 'cili':row[18], 'arab':row[19], 'lainlain':row[20]
                }
        results.append(item)
    return results 

def get_number_tourism_vs_category_usaha_monhly():
    query =("SELECT a.date as date, b.categoryid,  sum(a.pendapatan) as pendapatan "
            "FROM data_tourist a "
            "LEFT JOIN master_tourism b "
            "ON a.tourismid = b.tourismid "
            "WHERE lower(b.categoryid) in ('MICE','spa','hiburan dan rekreasi','jasa perjalanan','akomodasi', 'jasa makanan dan minuman') "
            "GROUP  by a.date, b.categoryid "
            "order by categoryid, a.date") 
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows = cursor.fetchall()
    results = []
    for row in rows:
        item ={'date': row[0],'categoryid':row[1], 'pendapatan':row[2]}
        results.append(item)
    return results




