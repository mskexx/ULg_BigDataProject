"""
Transformation module, process to make the initial changes:
 - from xls to csv
 -
"""
import pandas as pd
import os
from threading import Thread

N_THREADS = 8

def transformation(path, output):
    """
    First divide the folders into multiple chunks, then make multi-threading to
    speed up the transformation from .xls to .csv
    :param path: Input path of data
    :param output: Output path to save transformed data
    :return: None = Finish
    """
    try:
        os.mkdir(output)
    except:
        pass

    folders = [ f for f in os.listdir(path)
                if os.path.isdir(os.path.join(path, f)) ]

    #Divide folders to process in N chunks for multithreading
    threads = []
    n_threads = N_THREADS
    size = int(len(folders) / n_threads)
    tasks = [folders[i:i + size] for i in range(0, len(folders), size)] #Chunks

    #Multithreading
    for i in range(n_threads):
        threads.append(threading(path, output, tasks[i]))

    for t in threads:
        t.join()

    print("[DONE] Transformation xls to csv")

def threading(i, o, task):
    # Init a thread with the task and function
    thread = Thread(target=to_csv, args=[i, o, task])
    thread.start()
    return thread

def to_csv(in_path, out_path, folders):
    """
    :param in_path: Input path of the data
    :param out_path: Where the transformed files will be saved
    :param folders: Folder that the thread have to process
    :return: None. thread flow continue the execution
    """
    for folder in folders:
        fpath = os.path.join(in_path, folder)
        npath = os.path.join(out_path,folder)
        try:
            os.mkdir(npath)
        except:
            pass
        for file in (os.listdir(fpath)):
            print("Processing:", file)
            filepath = os.path.join(fpath, file)
            data_xls = pd.read_excel(filepath)
            new_name = file.replace(".xls", ".csv")
            data_xls.to_csv(os.path.join(npath, new_name), encoding='utf-8',
                            index=False)


def totals():
    '''
    Create the total grouped by building from a folder monthly structure
    '''
    path = "./DATA_CSV/"
    final_path = "./TOTAL_CSV/"
    total = {}
    folders = os.listdir(path)
    folders.sort(key=float)

    for folder in folders:
        fpath = path + folder + "/"
        print("Actual folder: ",folder)
        for file in (os.listdir(fpath)):
            fname = file.split("_")
            print("   Actual file: ", fname[1])

            data_xls = pd.read_csv(fpath + file,index_col=None, header=0)
            if fname[1] not in total:
                total[fname[1]] = []
            total[fname[1]].append(data_xls)

    for name, data in total.items():
        data_final = pd.concat(data)
        print(">Saving ", name)
        data_final.to_csv(final_path + name + ".csv", encoding='utf-8',
                       index=False)

if __name__ == '__main__':
    #tocsv()
    totals()