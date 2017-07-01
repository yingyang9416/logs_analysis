#!/usr/bin/env python3
import psycopg2
DBNAME = "news"


def connect(database_name):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"
        sys.exit(1)


def print_top_articles():
    db, c = connect(DBNAME)
    c.execute("""select articles.title,count(*) as num
                 from log
                 join articles on articles.slug=substring(log.path from 10)
                 group by articles.title
                 order by num desc limit 3""")
    results = c.fetchall()
    db.close()
    print ("1. The most popular three articles are:")
    for row in results:
        print ("\"%s\" -- %s views") % (row[0], row[1])


def print_top_authors():
    db, c = connect(DBNAME)
    c.execute("""select authors.name, count(*) as num
                 from log
                 join articles on articles.slug=substring(log.path from 10)
                 join authors on authors.id=articles.author
                 group by authors.name
                 order by num desc limit 3""")
    results = c.fetchall()
    db.close()
    print ("\n"+"2. The most popular three authors are:")
    for row in results:
        print ("%s -- %s views") % (row[0], row[1])


def print_top_error_days():
    db, c = connect(DBNAME)
    c.execute("""create view total_visit_per_day
                 as select date_trunc('day', time) as day1,
                 count(status) as total_per_day
                 from log
                 group by day1""")

    c.execute("""create view errors
                 as select status, date_trunc('day', time) as day2
                 from log
                 where status !='200 OK'""")

    c.execute("""create view error_per_day
                 as select day2, count(status) as error_per_day
                 from errors
                 group by day2""")

    c.execute("""create view refined_log
                 as select *
                 from total_visit_per_day
                 join error_per_day on day1 = day2""")

    c.execute("""create view final_result
                 as select day1,
                 cast(error_per_day as float)/cast(total_per_day as float)
                 as rate
                 from refined_log
                 where cast(error_per_day as float)
                 /cast(total_per_day as float)>=0.01
                 order by rate desc""")

    c.execute("""select to_char(day1,'mm/dd/yy') as date, rate
                 from final_result""")
    results = c.fetchall()
    db.close()

    print ("\n" + "3. On these days more than 1% of requests lead to errors:")
    for row in results:
        rate = "%.2f" % (row[1] * 100)
        print ("%s -- %s%%") % (row[0], rate)


def main():
    print_top_articles()
    print_top_authors()
    print_top_error_days()

if __name__ == '__main__':
    main()
