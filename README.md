TiDB  Workload Simulator
====================

The TiDB Workload Simulator is TOTALLY a fork from https://github.com/memsql/workload-simulator.  

Appreciate for MemSQL team to built such a handy tool for generating multi processes workload pressure in a visual way.

You can easily configure your workload concurrency , query commands via Web UI and save the config for backup or future use. Also A QPS graph monitors the real time query work load in clear way.  An embedded  SQL  command console makes the life much easier when try to add/modify the tables when doing the testing.

![alt text](https://github.com/deadjoe/tidb-workload-simulator/blob/master/screenshots.png)


The original support of MySQL makes the way easier for me to make the tool support TiDB distributed SQL database.

Requirements
------------

All command-line instructions assume that your working directory is the original location of this README file.

Tested on  RHEL7.x/CentOS 7.x and OSX (brew , easy_install, pip required)


Installing the workload simulator
---------------------------------

+ **Make sure you have python dev tools and pip installed**

```
sudo apt-get install python-dev python-setuptools libmysqlclient-dev
sudo easy_install pip
```

+ **Install dependencies**

```
sudo pip install flask sqlalchemy MySQL-python simplejson
```

Running the workload simulator
--------------------

+ **Start the server**

```
python runner
```

+ **You can stop it by sending SIGTERM to the parent python process. The easiest way to do this is to type `Ctrl-\` (control backslash) on your terminal.**


+ **Open http://localhost:9000 in a browser**

This is the "active mode" which allows you to run queries against the TiDB server. Let's start with a simple example.

+ **Install the key-value example database and table**

```
mysql -h 127.0.0.1 -u root -P 3306 -vv < workloads/key_value/key_value.sql
```

+ **Load the key-value workload**

On http://localhost:9000, click Load Workload and choose the file `workloads/key_value/key_value.json`

You will see three types of queries appear in a grid. Next to each there is a dial indicating how many times per second we will try to execute a query of that type.

+ **Hit PLAY**

The simulator starts executing queries against the database. The dials start showing the actual number of queries per second for each type of query. On the right you can see a real-time graph of the total number of queries per second being processed by TiDB.

+ **Console**

At any time, you can use the console on the right to run individual queries. Running your own queries may be useful for setting up schemas, inspecting the tables, and checking syntax.

+ **Running with TiDB**



Getting advanced
------------------------

+ **Try creating your own workload in active mode.**

Generate random numbers and strings with @ and ^, respectively. For example, to insert a random integer value in the key-value example, use the query `INSERT INTO t (k, v) VALUES (@, @);`

+ **Check out the sample workload from the video (https://vimeo.com/44087431)**

The sql schema is in `workloads/video/video.sql`. The workload is in `workloads/video/video.json`


Troubleshooting
-------------------

If a message pops up saying, "something went wrong...", you've run into an unhandled error. If the problem persists, restart the server from the command line by interrupting with Ctrl-\ and running "python runner".


