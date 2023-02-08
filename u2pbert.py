import time
import pickle
import os


st = time.time()
a = ""

model_checkpoint = open("checkpoints/U2P-BRET.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi6.py', 'w' ) as fout:
    fout.write(athletes)
import hi6
os.remove("./hi6.py")
hi6.fun10()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')