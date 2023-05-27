import datetime
import time
import gspread as gs
import _thread

jsonfile = "datatele-366319-0d5fecc26b48.json"
gc = gs.service_account(jsonfile)
tp = gc.open("Tele2")
wk = tp.get_worksheet(3)

def col1(i):
    for j in range(1, 4, 1):
        wk.update_cell(i, j, str(datetime.datetime.now().time()))
        time.sleep(0.5)
    # for j in range(4):
    #     print(i)
    #     time.sleep(2)


def col2(i):
    for j in range(1, 4, 1):
        wk.update_cell(i, j, str(datetime.datetime.now().time()))
        time.sleep(0.5)
    # for j in range(4):
    #     print(i)
    #     time.sleep(2)


def col3(i):
    for j in range(1,4,1):
        wk.update_cell(i, j, str(datetime.datetime.now().time()))
        time.sleep(0.5)
    # for j in range(4):
    #     print(i)
    #     time.sleep(2)

# col1(1)
_thread.start_new_thread(col1,(1,))
_thread.start_new_thread(col3,(2,))
_thread.start_new_thread(col3,(3,))
time.sleep((5))
# col2(2)
# col3(3)
print("hhe")
# wk.close()