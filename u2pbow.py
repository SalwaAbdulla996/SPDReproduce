import time
import pickle
import os

st = time.time()
a = ""

model_checkpoint = open("checkpoints/U2P-BOW.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi8.py', 'w' ) as fout:
    fout.write(athletes)
import hi8
os.remove("./hi8.py")
hi8.fun2()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')