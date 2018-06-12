TiDB  Workload Simulator
====================

The TiDB Workload Simulator is TOTALLY a fork from https://github.com/memsql/workload-simulator.  

Appreciate for MemSQL team to built such a handy tool for generating multi processes workload pressure in a visual way.

What did in this fork:

1. adjusted the code to support TiDB.
2. fixed one dependency problem on client lib.
3. built a docker image so that can be used more easier than worry about thos "pythonblem"  

You can easily configure your workload concurrency , query commands via Web UI and save the config for backup or future use. Also A QPS graph monitors the real time query work load in clear way.  An embedded  SQL  command console makes the life much easier when try to add/modify the tables when doing the testing.

![alt text](https://github.com/deadjoe/tidb-workload-simulator/blob/master/screenshots.png)


The original support of MySQL makes the way easier for me to make the tool support TiDB distributed SQL database.

Requirements
------------

All command-line instructions assume that your working directory is the original location of this README file.

Tested on  RHEL7.x/CentOS 7.x and OSX (brew , easy_install, pip required)
The latest Docker packages required if you run it in docker.


Installing the workload simulator (Do not required if you run it in docker way)
---------------------------------

+ **Make sure you have python dev tools and pip installed**

```
sudo apt-get install python-dev python-setuptools libmariadbclient-dev
sudo easy_install pip
```

+ **Install dependencies**

```
sudo pip install flask sqlalchemy MySQL-python simplejson
```

Running the workload simulator
--------------------
+ **Start the server via docker(Strong Suggested)**

```
docker run -d -p 9000:9000 deadjoe/tidb-workload-simulator
```

+ **Start the server in command**

```
python runner
```

+ **You can stop it by sending SIGTERM to the parent python process. The easiest way to do this is to type `Ctrl-\` (control backslash) on your terminal.**


+ **Open http://localhost:9000 in a browser**

+ **Hit PLAY**

The simulator starts executing queries against the database. The dials start showing the actual number of queries per second for each type of query. On the right you can see a real-time graph of the total number of queries per second being processed by TiDB.

+ **Console**

At any time, you can use the console on the right to run individual queries. Running your own queries may be useful for setting up schemas, inspecting the tables, and checking syntax.

+ **Running with TiDB**


Getting advanced
------------------------

+ **Try creating your own workload in active mode.**

Generate random numbers and strings with @ and ^, respectively. For example, to insert a random integer value in the key-value example, use the query `INSERT INTO t (k, v) VALUES (@, @);`

Troubleshooting
-------------------

If a message pops up saying, "something went wrong...", you've run into an unhandled error. If the problem persists, restart the server from the command line by interrupting with Ctrl-\ and running "python runner".
