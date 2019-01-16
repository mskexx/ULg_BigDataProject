import os
import pandas as pd
import settings
def totals():
    in_path = settings.month_path
    out_path = settings.year_path
    """
    Create the total grouped by building from a folder monthly structure
    :param in_path: Input folder of the data in .csv
    :param out_path: Output folder where files with totals will be saved
    :return: None
    """
    print("[PRE-PROCESS] Grouping consumption totals of a building")
    try:
        os.mkdir(out_path)
    except:
        pass

    total = {}
    folders = os.listdir(in_path)
    folders.sort(key=float)

    for folder in folders:
        folderpath = os.path.join(in_path, folder)
        print("[] Actual folder: ",folder)

        for file in (os.listdir(folderpath)):
            filename = file.split("_")
            filepath = os.path.join(folderpath, file)
            print("   Reading file: ", filename[1])

            data_xls = pd.read_csv(filepath, index_col=None, header=0)
            if filename[1] not in total:
                total[filename[1]] = []
            total[filename[1]].append(data_xls)

    for name, data in total.items():
        data_final = pd.concat(data)
        print("[SAVE] Saving file: ", name)
        destination = os.path.join(out_path, str(name)+".csv")
        data_final.to_csv(destination, encoding='utf-8', index=False)

    print("[DONE] Total consumption per building grouped")