# Introduction
Detecting anomalies (threats or attacks) in a network is a crucial task in cybersecurity. It involves identifying unusual patterns in the network traffic. The traditional methods that are commonly deployed to detect anomalies in the network, rely on predefined set of rules based on known attack patterns. The problem with these is that they fail at recognizing threats that previously have not been encountered.

The challenge lies in accurately detecting these anomalies in real-time, where the network traffic is immense, and often noisy and heterogenous

With attackers finding new ways to bypass traditional security measures, cyber threats are evolving continuously. Also, new devices get added to the network time and again, this implies that a network is forever growing in size. Monitoring the various parameters associated with a network to find potential threats becomes increasingly difficult as a result. Hence, it is imperative to have a system in place that is both robust and adaptive in recognizing threats and threat patterns.
- Robust, because it has to cater to the need of threat detection in a network that is growing continuously.
- Adaptive, because it has to continuously evolve by learning from new incoming data and recognize threats.

To address these issue, multiple ML models have been built as a part of an experiment to find the best model that identifies threat patterns and classifies a network connection into either a normal or one of the attack types. This type of classification problem in machine learning (ML) is called as a multi-class classification problem.

# Jupyter Notebooks
[All Notebooks](notebooks)

# Blog
Medium: [Multi-Class Classification ML Model for Network Anomaly Detection](https://medium.com/@sirdesaividish/multi-class-classification-ml-model-for-network-anomaly-detection-f0368ac00dc5)

# Visualization
Tableau Public: [Analysis Of Factors Associated With Anomalies In A Network](https://public.tableau.com/app/profile/vidish.sirdesai/viz/network_anomaly_detection/final_story)

# Deployment Steps
### Virtual environment setup
1. `cd <project_directory_path>`.
2. `pip install virtualenv`.
3. `python<version> -m venv <virtual_environment_name>` or `python3 -m venv .venv`.
4. A folder named "`.venv`" will appear in the project directory.
5. Activate the virtual environment using one of the commands listed below depending on the Operating System,
    - MacOS and Linux, `source .venv/bin/activate`.
    - Windows command prompt, `.venv/Scripts/activate.bat`.
6. Once the virtual environment is active, the environment name (in this case "`.venv`") will be visible in the parantheses before the prompt, like so "`(.venv)`".
7. To confirm if the virtual environment has successfully been create, run `pip list`. The following should be the output,
```
(.venv) vidish@Vidishs-MacBook-Air network_anomaly_detection % pip list
Package    Version
---------- -------
pip        xx.x.x
setuptools xx.x.x
``` 
8. To deactivate the virtual environment, strictly run the following 2 commands in the same order,
    - `deactivate`.
    - `rm -r .venv`.

### Installing dependencies
1. Once the virtual environment is created, create a `.txt` file named, `requirements.txt`.
2. Add the names of the dependent (required) packages (libraries) that are required by the app to be functioning. The below is the list of packages that are required,
```
flask
pickle
pandas
scikit-learn
```
3. Once the `requirements.txt` file is created with all the dependencies included as a part of the file, save the file and run `pip install -r requirements.txt` from the terminal.
4. `pip list` can be run to check if the installation of all the packages has been successful.

### Network anomaly classification model
Gradient boosting decision tree was found to be the best model. Therefore, the same is chosen to build the classification app. The model is trained and the trained model is serialized using "`pickle`".

`pickle` is a Python package that is a powerful tool for serializing and deserializing Python objects.

Refer the following notebook where all of the above has been executed, 
- Notebook: [gbdt_classifier.ipynb](notebooks/gbdt_classifier.ipynb).

### Network anomaly classifier app
1. This app has been built and has been tested on Python version: `3.11.9`.
2. To run the application,
    - `cd src`.
    - `FLASK_APP=network_anomaly_classifier_app.py flask run`.
3. To view the welcome page, goto, http://127.0.0.1:5000.
4. To classify the anomaly type or the attack type, send a POST request to, http://127.0.0.1:5000/classify.
5. The POST request can be sent by running the following command in a terminal window: 
```
curl -X POST -H 'Content-Type: application/json' -d '{"duration": 38044, "srcbytes": 1, "dstbytes": 0, "land": 0, "wrongfragment": 0, "urgent": 0, "hot": 0, "numfailedlogins": 0, "loggedin": 0, "numcompromised": 0, "rootshell": 0, "suattempted": 0, "numfilecreations": 0, "numshells": 0, "numaccessfiles": 0, "ishostlogin": 0, "count": 2, "srvcount": 2, "serrorrate": 0.0, "rerrorrate": 1.0, "samesrvrate": 1.0, "diffsrvrate": 0.0, "srvdiffhostrate": 0.0, "dsthostcount": 255, "dsthostsrvcount": 2, "dsthostdiffsrvrate": 0.5, "dsthostsamesrcportrate": 1.0, "dsthostsrvdiffhostrate": 0.0, "protocol": "tcp", "service": "Z39_50", "flag": "RSTR"}' http://127.0.0.1:5000/classify
```
6. Expected response: `{"Attack Type":"Probe"}`.

# API Specification
### Base URL
http://127.0.0.1:5000/

### Endpoints
- GET `/`: Returns a welcome message indicating the applications's purpose.
- POST `/classify`: Classifies a network connection based on its features and predicts the type of attack (if any).

### Request format for POST /classify
Content-Type: application/json

The request body should be a JSON object containing the following features of a network connection,
- `duration` (int): Length of time a specific network connection was active for.
- `srcbytes` (int): Number of data bytes transferred from the source to the destination in a single connection.
- `dstbytes` (int): Number of data bytes transferred from the destination to source in a single connection.
- `land` (int): Indicates whether the source and destination IP addresses and port numbers are equal (1 if equal, 0 otherwise).
- `worngfragment` (int): Total number of worng fragments received in a connection.
- `urgent` (int): Number of urgent packets in this connection. Urgent packets are packets with the urgent bit activated.
- `hot` (int): Number of "hot" indicators, meaning the number of factors that are indicative of an anomaly or an attack.
- `numfailedlogins` (int): Count of failed login attempts.
- `loggedin` (int): Indicates whether a successful login occurred in a connection (1 if successfully logged in, 0 otherwise).
- `numcompromised` (int): Number of compromised conditions in a connection.
- `rootshell` (int): Indicates whether root shell access was obtained in a connection (1 if yes, 0 otherwise).
- `suattempted` (int): Indicates whether the `su root` command was attempted or used in a connection (1 if yes, 0 otherwise).
- `numfilecreations` (int): Count of file creation operations in a connection.
- `numshells` (int): Count of shell prompts in a connection.
- `numaccessfiles` (int): Count of operations on access control files in a connection.
- `ishostlogin` (int): Indicates whether a login belongs to the host list i.e., root or admin (1 if yes, 0 otherwise).
- `count` (int): Number of connections to the same destination host as the current connection in the past 2 seconds.
- `srvcount` (int): Number of connections to the same service as the current connection in the past 2 seconds.
- `serrorrate` (float): Percentage of connections that have activated the flag s0, s1, s2, or s3, among the connections aggregated in `count`.
- `rerrorrate` (float): Percentage of connections that have activated the flag REJ, among the connections aggregated in `count`.
- `samesrvrate` (float): Percentage of connections that were to the same service, among the connections aggregated in `count`.
- `diffsrvrate` (float): Percentage of connections that were to different services, among the connections aggregated in `count`.
- `srvdiffhostrate` (float): Percentage of connections that were to different destination machines, among the connections aggregated in `srvcount`.
- `dsthostcount` (int): Number of connections having the same destination host IP address.
- `dsthostsrvcount` (int): Number of connections having the same destination port number.
- `dsthostdiffsrvrate` (float): Percentage of connections that were to different services, among the connections aggregated in `dsthostcount`.
- `dsthostsamesrcportrate` (float): Percentage connections that were to the same source port, among the connections aggregated in `dsthostsrvcount`.
- `dsthostsrvdiffhostrate` (float): Percentage connections that were to different destination machines, among the connections aggregated in `dsthostsrvcount`.
- `protocol` (string): Type of communication protocol used in each connection.
- `service` (string): Type of DNS used in a connection.
- `flag` (string): Status of a connection.

### Response format for POST /classify
The response will be a JSON object with the following key,
- `Attack Type`: A string indicating one of the predicted type of attack,
    - "Normal".
    - "DoS".
    - "R2L".
    - "Probe".
    - "U2R".
    - "Not recognized" (if the model cannot classify the attack type).
