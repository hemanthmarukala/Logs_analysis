#! /usr/local/bin/python3

import psycopg2
DB_NAME = "news"

"""Return top 3 popular articles of all time"""


def three_popular_articles():
    query1 = "select articles.title, count(*) \
              from articles join log \
              on concat('/article/', articles.slug) = log.path \
              group by articles.title order by count desc limit 3"
    result = connection(query1)
    with open('analysis.txt', 'w') as f:
        print("Three popular articles")
        f.write("Popular Articles \n")
        printing_Query_Results(result,f)

"""return the popular authors"""


def popular_authors():
    query2 = "select authors.name , count(log.path) \
              from authors inner join articles \
              on authors.id = articles.author \
              inner join log \
              on concat('/article/', articles.slug) = log.path \
              group by authors.name order by count desc"
    result = connection(query2)
    with open('analysis.txt', 'a') as f:
        print("Popular Authors")
        f.write("\nPopular Authors \n")
        printing_Query_Results(result,f)

"""Returns the day with more that 1% of the requests leading to errors"""


def error_log():
    query3 = """select to_char(a.date, 'Mon DD, YYYY'), 
                      (a.errors * 100 / b.requests)
                      from (select time::date as date, count(*) as errors
                            from log where status != '200 OK'
                            group by date) as a,
                            (select time::date as date, count(*) as requests 
                      from log group by date) as b
                      where a.date = b.date
                      and (a.errors * 100 / b.requests) >= 1"""
    result = connection(query3)
    with open('analysis.txt', 'a') as f:
        print("Day with more that 1% of the requests leading to errors")
        printing_Query_Results(result,f)

"""Function to connect to the database"""


def connection(query):
    conn = psycopg2.connect(database=DB_NAME)
    c = conn.cursor()
    c.execute(query) 
    result = c.fetchall()
    return result

""" Printing the results"""


def printing_Query_Results(result,f):
    for row in result:
      print(row)
      f.write("{} -- {} views\n".format(str(row[0]), str(row[1])))
    f.write("\n \n")
    f.write("-"*70)
    print("-"*70)    

"""Function to execute all the queries. """
if __name__ == "__main__":
  three_popular_articles()
  popular_authors()
  error_log()
