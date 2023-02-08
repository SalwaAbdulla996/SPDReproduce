import time
import pickle
import os

st = time.time()
a = ""

model_checkpoint = open("checkpoints/C2P-BRET.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi.py', 'w' ) as fout:
    fout.write(athletes)
import hi
os.remove("./hi.py")
hi.fun9()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')