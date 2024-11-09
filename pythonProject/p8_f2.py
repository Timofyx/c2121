import logging

logging.basicConfig(level=logging.DEBUG, filename="log82.log", filemode="a",
                    format="We have new logging message:%(asctime)s:%(levelname)s:%(message)s")


try:
    print(10/0)
except Exception:
    logging.exception("Exception")
print("End program")
