import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent(interval=1)
    mem_metric = psutil.virtual_memory().percent
    Message = ""
    if cpu_metric > 80 or mem_metric > 80:
        Message = "High CPU or Memory Detected, scale up!!!"
    return f"cpu utilization: {cpu_metric} and memory utilization: {mem_metric} {Message}"

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')