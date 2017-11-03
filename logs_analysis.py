import psycopg2
DB_NAME = "news"

"""Return top 3 popular articles of all time"""


def three_popular_articles():
    query1 = "select articles.title, count(*) \
              from articles join log \
              on concat('/article/', articles.slug) = log.path \
              group by articles.title order by count desc limit 3"
    conn = psycopg2.connect(database=DB_NAME)
    c = conn.cursor()
    c.execute(query1)
    result = c.fetchall()
    with open('analysis.txt', 'w') as f:
        print("three popular articles")
        f.write("Popular Articles \n")
        for row in result:
            print(row)
            f.write("{} -- {} views\n".format(str(row[0]), str(row[1])))
        f.write("\n \n")
    conn.close()

    
"""return the popular authors"""
def popular_authors():
    query2 = "select authors.name , count(log.path) \
              from authors inner join articles \
              on authors.id = articles.author \
              inner join log \
              on concat('/article/', articles.slug) = log.path \
              group by authors.name order by count desc"
    conn = psycopg2.connect(database=DB_NAME)
    c = conn.cursor()
    c.execute(query2)
    result = c.fetchall()
    with open('analysis.txt', 'a') as f:
        print("Popular Authors")
        f.write("Popular Authors \n")
        for row in result:
            print(row)
            f.write("{} -- {} views\n".format(str(row[0]), str(row[1])))
        f.write("\n \n")
    conn.close()

    
"""Returns the day with more that 1% of the requests leading to errors"""
def error_log():
    query3 = "select db1.table1time as date, \
              cast((cast(db1.errorcount as decimal)/\
              cast(db2.totalcount as decimal)*100) \
              as decimal(50,3)) as percerror \
              from \
              (select date(a.time) as table1time, count(b.status) \
              as errorcount \
                  from log a , log b where a.id = b.id and b.status \
                  like '404 NOT FOUND' \
                  group by date(a.time)) as db1 \
              join \
              (select date(a.time) as table2time, count(b.status) \
              as totalcount \
                  from log a , log b where a.id = b.id \
                  group by date(a.time)) as db2 \
              on db1.table1time = db2.table2time \
              where \
              cast((cast(db1.errorcount as decimal)/\
              cast(db2.totalcount as decimal)*100) \
              as decimal) > 1"
    conn = psycopg2.connect(database=DB_NAME)
    c = conn.cursor()
    c.execute(query3)
    result = c.fetchall()
    with open('analysis.txt', 'a') as f:
        print("day with more that 1% of the requests leading to errors")
        for row in result:
            print(row)
            f.write("Request Errors more than 1% \n")
            f.write("{} -- {} percent\n".format(str(row[0]),
                    str(row[1])))
    conn.close()

    
"""Function to execute all the queries. """
three_popular_articles()
popular_authors()
error_log()
