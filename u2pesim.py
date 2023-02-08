import time
import pickle
import os

st = time.time()
a = ""

model_checkpoint = open("checkpoints/U2P-ESIM.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi9.py', 'w' ) as fout:
    fout.write(athletes)
import hi9
os.remove("./hi9.py")
hi9.fun8()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')