import RPi.GPIO as GPIO
import time
import sys
import os
import hashlib
import random
from flask import Flask, request, jsonify, make_response, Response, redirect
from flask_cors import CORS
from threading import Thread, Lock
from pathlib import Path
from datetime import datetime, date, timedelta



APP_DEBUG = os.getenv('APP_DEBUG', 'false').lower() == "true"





# Flask Init
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
if(APP_DEBUG):
    app.secret_key = hashlib.sha256(datetime.now().strftime("%Y-%m-%d").encode()).digest()
else:
    app.secret_key = random.randbytes(32)








@app.route('/open', methods=['GET'])
def open_HTTPGET():
    args = request.args
    
    numberplate = ""
    if("numberplate" in args):
        numberplate = args.get("numberplate")

    print("OPENED")
    GPIO.output(17, GPIO.HIGH)
    Path('OPENED').touch(exist_ok=True)

    with open("/data/openings.txt", "a") as f:
        timeNow = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(timeNow + ":" + numberplate + "\n")

    return Response("{}", mimetype='application/json')





if __name__ == '__main__':

    # Raspberry Pi GPIO Init
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)

    # Background Task for releasing relay
    def background_task(interval_sec):
        x = 0
        while True:
            time.sleep(1)

            if(x > 0):
                x -= 1
            else:
                if(Path("OPENED").is_file()):
                    x = 5
                    Path("OPENED").unlink()
                elif(x == 0):
                    GPIO.output(17, GPIO.LOW)
                    print("CLOSED")
                    x -= 1
                else:
                    GPIO.output(17, GPIO.LOW)

            
    daemon = Thread(target=background_task, args=(1,), daemon=True, name='Background')
    daemon.start()



    if(len(sys.argv) == 1):
        print("[*] Explanation is comming... ")

    elif(sys.argv[1] == "--http"):
        app.run(host='0.0.0.0', port=8000, debug=APP_DEBUG)
