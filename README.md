# Heimdall The Gatekeeper

# Overview
This API gatekeeper built to maintain data manipulation without directly accessing the database to avoid potentially harming the database performance. The manipulation means to process the key-value json formatted into column-value to be able to operate it into database

![image](https://user-images.githubusercontent.com/71366136/117530151-c9afd180-b005-11eb-944b-70eb34872230.png)


# Installation
Clone this repository
```
git clone https://github.com/Jomen034/heimdall-the-gatekeeper.git
```

## Prerequisite
For being able work with `FastAPI`, make sure you have `python 3.6+` installed on your PC
```
> python --version
> Python 3.8.5
```

Install the prerequisite library used for this project
```
pip install -r requirements.txt
```

Also you need to install `Kafka`. See the [Kafka Documentation](https://kafka.apache.org/quickstart) to download and see how to install it

# Usage
## Set up your Kafka
1. Activate the `zookeeper`
```
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
```

2. Activate the `kafka`
```
.\bin\windows\kafka-server-start.bat .\config\server.properties
```

3. Create `topic`
```
.\bin\windows\kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic <your topic name>
```

4. Activate the `kafka producer`
```
.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic <your topic name>
```

5. Activate the `kafka consumer`
```
.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic <your topic name>
```

## Run The `main.py` & `consumer.py`
On your command promt, run the following command
```
python main.py
```
On another command promt, run the `consumer.py`
```
python consumer.py
```

## Go to Your API Gateway
By default, it will be on <http://127.0.0.1:8000>. Go to the **docs** <http://127.0.0.1:8000/docs>

![image](https://user-images.githubusercontent.com/71366136/117530602-362bd000-b008-11eb-8c70-2f40a44fc744.png)

Try to create the request and execute it. You will see on the response body

![image](https://user-images.githubusercontent.com/71366136/117530646-755a2100-b008-11eb-84e0-b4a4761c738c.png)

On the consumer you will have this result

![image](https://user-images.githubusercontent.com/71366136/117530669-9b7fc100-b008-11eb-9246-ed9af20c40ba.png)

This result will be manipulated by consumer to be able to load into database

_**For this step, I still working on it**_
