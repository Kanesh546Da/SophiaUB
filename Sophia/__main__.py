from Sophia import *
from pyrogram import Client, filters
import os
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

if __name__ == "__main__":
    ACCESS = decode_key(ACCESS_CODE, ACCESS_PIN)
    if ACCESS == "oTaZUki004nandhaiSgeY":
        Sophia.run()
        print("[INFO] Correct Access Key Bot Started")
    else:
        print("[INFO] Invalid Access Key, Access Key is required to Use Sophia Beta Try Again")
        exit()
