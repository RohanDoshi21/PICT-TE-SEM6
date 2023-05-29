```bash

    cd hadoop-3.3.5/sbin

    # Start hadoop and yarm
    start-dfs.sh
    start-yarn.sh

    # Check hadoop and yarm
    jps

    # Create a new directory in HDFS
    hdfs dfs -mkdir /input

    # Add input file to HDFS
    hdfs dfs -put $(pwd)/input1.txt /input

    # View if the file is added
    hdfs dfs -ls /input

    # Run the word count program
    yarn jar $(pwd)/../share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.0.jar wordcount /input /output

    # View the output
    hdfs dfs -ls /output

    # View the output
    hdfs dfs -cat /output/part-r-00000

    # Stop hadoop and yarm
    stop-dfs.sh
    stop-yarn.sh

```
