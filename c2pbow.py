import time
import pickle
import os

st = time.time()
a = ""

model_checkpoint = open("checkpoints/C2P-BOW.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi3.py', 'w' ) as fout:
    fout.write(athletes)
import hi3
os.remove("./hi3.py")
hi3.fun1()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')