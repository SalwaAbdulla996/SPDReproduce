import time
import pickle
import os

st = time.time()
a = ""

model_checkpoint = open("checkpoints/U2P-Transformer.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi10.py', 'w' ) as fout:
    fout.write(athletes)
import hi10
os.remove("./hi10.py")
hi10.fun6()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')