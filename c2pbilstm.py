import time
import pickle
import os

st = time.time()
a = ""

model_checkpoint = open("checkpoints/C2P-BiLSTM.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi2.py', 'w' ) as fout:
    fout.write(athletes)
import hi2
os.remove("./hi2.py")
hi2.fun3()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')