from flask import Flask, request
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/")
def welcome_note():
    return "<h1>Network Anomaly Classification App</h1>"

# reading the trained model's pickle file
gbdt_classifier_pickle = open("../artifacts/gbdt_classifier.pkl", "rb")

# loading the classifier model
classifier = pickle.load(gbdt_classifier_pickle)

@app.route("/classify", methods = ["POST"])
def classify():
    classify_request = request.get_json()

    # unpacking the json object
    duration = classify_request["duration"]
    srcbytes = classify_request["srcbytes"]
    dstbytes = classify_request["dstbytes"]
    land = classify_request["land"]
    wrongfragment = classify_request["wrongfragment"]
    urgent = classify_request["urgent"]
    hot = classify_request["urgent"]
    numfailedlogins = classify_request["numfailedlogins"]
    loggedin = classify_request["loggedin"]
    numcompromised = classify_request["numcompromised"]
    rootshell = classify_request["rootshell"]
    suattempted = classify_request["suattempted"]
    numfilecreations = classify_request["numfilecreations"]
    numshells = classify_request["numshells"]
    numaccessfiles = classify_request["numaccessfiles"]
    ishostlogin = classify_request["ishostlogin"]
    count = classify_request["count"]
    srvcount = classify_request["srvcount"]
    serrorrate = classify_request["serrorrate"]
    rerrorrate = classify_request["rerrorrate"]
    samesrvrate = classify_request["samesrvrate"]
    diffsrvrate = classify_request["diffsrvrate"]
    srvdiffhostrate = classify_request["srvdiffhostrate"]
    dsthostcount = classify_request["dsthostcount"]
    dsthostsrvcount = classify_request["dsthostsrvcount"]
    dsthostdiffsrvrate = classify_request["dsthostdiffsrvrate"]
    dsthostsamesrcportrate = classify_request["dsthostsamesrcportrate"]
    dsthostsrvdiffhostrate = classify_request["dsthostsrvdiffhostrate"]
    protocol = classify_request["protocol"]
    service = classify_request["service"]
    flag = classify_request["flag"]
    protocol_encoded = None
    service_encoded = None
    flag_encoded = None

    # encoding protocol_encoded
    if protocol == "tcp":
        protocol_encoded = 80114.28824898
    elif protocol == "udp":
        protocol_encoded = 141.21503368
    elif protocol == "icmp":
        protocol_encoded = 342.94156001
    
    # encoding service_encoded
    if service == "ftp_data":
        service_encoded = 143597.02653061223
    elif service == "other":
        service_encoded = 312548.73411332874
    elif service == "private":
        service_encoded = 90075.67057154624
    elif service == "http":
        service_encoded = 6006.81136893252
    elif service == "remote_job":
        service_encoded = 0.01282051282051282
    elif service == "name":
        service_encoded = 0.0022172949002217295
    elif service == "netbios_ns":
        service_encoded = 0.002881844380403458
    elif service == "eco_i":
        service_encoded = 11.793976429506765
    elif service == "mtp":
        service_encoded = 0.002277904328018223
    elif service == "telnet":
        service_encoded = 190410.34806629835
    elif service == "finger":
        service_encoded = 392462.37577815505
    elif service == "domain_u":
        service_encoded = 130.25666261196506
    elif service == "supdup":
        service_encoded = 0.001838235294117647
    elif service == "uucp_path":
        service_encoded = 0.001451378809869376
    elif service == "Z39_50":
        service_encoded = 0.001160092807424594
    elif service == "smtp":
        service_encoded = 32667.764255435526
    elif service == "csnet_ns":
        service_encoded = 0.001834862385321101
    elif service == "uucp":
        service_encoded = 0.05384615384615385
    elif service == "netbios_dgm":
        service_encoded = 0.0024691358024691358
    elif service == "urp_i":
        service_encoded = 134.14285714285714
    elif service == "auth":
        service_encoded = 11.256544502617801
    elif service == "domain":
        service_encoded = 55.479789103690685
    elif service == "ftp":
        service_encoded = 789039.1043329532
    elif service == "bgp":
        service_encoded = 0.0014084507042253522
    elif service == "ldap":
        service_encoded = 0.0
    elif service == "ecr_i":
        service_encoded = 878.9954427083334
    elif service == "gopher":
        service_encoded = 0.7915057915057915
    elif service == "vmnet":
        service_encoded = 0.0016207455429497568
    elif service == "systat":
        service_encoded = 0.0020964360587002098
    elif service == "http_443":
        service_encoded = 0.0
    elif service == "efs":
        service_encoded = 0.002061855670103093
    elif service == "whois":
        service_encoded = 0.001443001443001443
    elif service == "imap4":
        service_encoded = 1045.9876352395672
    elif service == "iso_tsap":
        service_encoded = 0.001455604075691412
    elif service == "echo":
        service_encoded = 0.029953917050691243
    elif service == "klogin":
        service_encoded = 0.0023094688221709007
    elif service == "link":
        service_encoded = 0.002105263157894737
    elif service == "sunrpc":
        service_encoded = 0.049868766404199474
    elif service == "login":
        service_encoded = 98.89044289044288
    elif service == "kshell":
        service_encoded = 0.0033444816053511705
    elif service == "sql_net":
        service_encoded = 0.004081632653061225
    elif service == "time":
        service_encoded = 0.5030581039755352
    elif service == "hostnames":
        service_encoded = 0.002173913043478261
    elif service == "exec":
        service_encoded = 0.014767932489451477
    elif service == "ntp_u":
        service_encoded = 96.0
    elif service == "discard":
        service_encoded = 1155332.1003717473
    elif service == "nntp":
        service_encoded = 0.10472972972972973
    elif service == "courier":
        service_encoded = 0.0013623978201634877
    elif service == "ctf":
        service_encoded = 0.0017761989342806395
    elif service == "ssh":
        service_encoded = 165.6816720257235
    elif service == "daytime":
        service_encoded = 0.06333973128598848
    elif service == "shell":
        service_encoded = 5525.307692307692
    elif service == "netstat":
        service_encoded = 0.002777777777777778
    elif service == "pop_3":
        service_encoded = 2761.4583333333335
    elif service == "nnsp":
        service_encoded = 0.0
    elif service == "IRC":
        service_encoded = 13334.684491978609
    elif service == "pop_2":
        service_encoded = 3.9358974358974357
    elif service == "printer":
        service_encoded = 2.0579710144927534
    elif service == "tim_i":
        service_encoded = 504.875
    elif service == "pm_dump":
        service_encoded = 473.6
    elif service == "red_i":
        service_encoded = 91.0
    elif service == "netbios_ssn":
        service_encoded = 0.052486187845303865
    elif service == "rje":
        service_encoded = 0.011627906976744186
    elif service == "X11":
        service_encoded = 3824927.5616438356
    elif service == "urh_i":
        service_encoded = 40.7
    elif service == "http_8001":
        service_encoded = 0.0
    elif service == "aol":
        service_encoded = 0.0
    elif service == "http_2784":
        service_encoded = 0.0
    elif service == "tftp_u":
        service_encoded = 1.0
    elif service == "harvest":
        service_encoded = 0.0

    # encoding flag_encoded
    if flag == "SF":
        flag_encoded = 20938.455295185224
    elif flag == "S0":
        flag_encoded = 0.02536512582135376
    elif flag == "REJ":
        flag_encoded = 0.0
    elif flag == "RSTR":
        flag_encoded = 889347.3907476249
    elif flag == "SH":
        flag_encoded = 0.0
    elif flag == "RSTO":
        flag_encoded = 444704.5544174136
    elif flag == "S1":
        flag_encoded = 77117.35342465753
    elif flag == "RSTOS0":
        flag_encoded = 36582897.84466019
    elif flag == "S3":
        flag_encoded = 252670.02040816325
    elif flag == "S2":
        flag_encoded = 50189.88976377953
    elif flag == "OTH":
        flag_encoded = 1931.5

    # scaling the training data
    scaler = StandardScaler()
    training_data = pd.read_csv("../datasets/x_train.csv", header = 0)
    training_data.drop(columns = ["Unnamed: 0"], inplace = True)
    training_data_scaled = scaler.fit_transform(training_data)

    model_inputs = pd.DataFrame([[duration, srcbytes, dstbytes, land, wrongfragment, urgent, hot, numfailedlogins, loggedin, numcompromised, rootshell, suattempted, numfilecreations, numshells, numaccessfiles, ishostlogin, count, srvcount, serrorrate, rerrorrate, samesrvrate, diffsrvrate, srvdiffhostrate, dsthostcount, dsthostsrvcount, dsthostdiffsrvrate, dsthostsamesrcportrate, dsthostsrvdiffhostrate, protocol_encoded, service_encoded, flag_encoded]], columns = training_data.columns)

    # transforming the input data
    model_inputs = scaler.transform(model_inputs)
    
    # predict the class of attack
    result = str(classifier.predict(model_inputs)[0])

    if result == "0":
        return {"Attack Type": "Normal"}
    elif result == "1":
        return {"Attack Type": "DoS"}
    elif result == "2":
        return {"Attack Type": "R2L"}
    elif result == "3":
        return {"Attack Type": "Probe"}
    elif result == "4":
        return {"Attack Type": "U2R"}
    else:
        return {"Attack Type": "Not recognized"}

if __name__ == "__main__":
    app.run(debug = True)
