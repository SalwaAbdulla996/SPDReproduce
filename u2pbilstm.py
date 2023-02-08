import time
import pickle
import os

st = time.time()
a = ""

model_checkpoint = open("checkpoints/U2P-BiLSTM.ckpt", "rb")
athletes = pickle.load(model_checkpoint)
model_checkpoint.close()


with open('hi7.py', 'w' ) as fout:
    fout.write(athletes)
import hi7
os.remove("./hi7.py")
hi7.fun4()
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Total Execution time:', elapsed_time, 'seconds')