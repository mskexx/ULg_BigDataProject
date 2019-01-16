import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

import settings


MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aut','Sep','Oct','Nov','Dec']
pf = "Plots"

def yearly():
    in_path = settings.year_path
    plot_folder = settings.plot_path #Path for Plots folder
    year_plots_folder = os.path.join(plot_folder, "Year")

    if not os.path.isdir(plot_folder):
        os.mkdir(plot_folder)
        print("[FOLDER] <Plots> folder created in root project path")

    if not os.path.isdir(year_plots_folder):
        os.mkdir(year_plots_folder)
        print("[FOLDER] <Year> folder created in <Plots> folder")



    buildings = filter(lambda b: ".csv" in b, os.listdir(in_path))

    for building in buildings:
        name = building.split(".")[0]
        path = os.path.join(year_plots_folder, name)  # Folder in Plots/Year/"

        if not os.path.isdir(path):  # Folder for plots of the building
            os.mkdir(path)
        building_data = pd.read_csv(os.path.join(in_path, building),
                                    index_col=None, header=0)

        plot_year(name, building_data, path)
        #Create plots for each variable in the building


def plot_year(name, b_data, save_path):
    headers = list(b_data)
    for col in headers[1:]:
        try:
            data_plot = b_data[col]
            plt.figure()
            plt.title(' '.join((name, col)))
            plt.xlabel("Date")
            plt.ylabel(col)
            plt.plot(range(len(data_plot)), data_plot)

            print("[PLOT] Saving", name, col)

            filename = '_'.join((name, col))
            plt.savefig(os.path.join(save_path, filename))
            plt.close()
        except:
            print("[ERROR] FILE: ", name)


def plot_lab():
    # B28 = 16
    in_path = settings.get_input()
    buildings = list(
        filter(lambda b: ".csv" in b, os.listdir(in_path)))
    for building in buildings[16:17]:
        name = building.split(".")[0]
        df = pd.read_csv(in_path + building, index_col=None,
                         header=0)
        try:
            totalkw = df['TotalkW']
            np_totalkw = np.array(totalkw.tolist())
            dates = df['Date']

            st = 130795 #Manual index now
            st = None
            num_week = 10
            data_per_week = 10087 #Aprox
            start_week = num_week * data_per_week
            if st:
                start_week = st #Manual
            end_week = start_week + data_per_week
            print(dates[st:end_week], totalkw[st:end_week])
            week_data = totalkw[start_week:end_week]
            plt.plot(range(len(totalkw)), totalkw)
            plt.title(name +" "+str(num_week)+ " week")
            plt.xlabel("# Observation (Cronological)")
            plt.ylabel("TotalkW")
            plt.plot(range(start_week,end_week), week_data ,c='red')
            plt.show()
            plt.savefig(in_path + "/plots/" + name + "_first_clean.png")
            plt.close()
        except Exception as e:
            print(e, name, " ERROR")


def cleaning(ret=False):
    in_path = settings.year_path
    out_path = settings.root_path
    plot_path = os.path.join(out_path, pf)
    if pf not in os.listdir(out_path):
        os.mkdir(plot_path)
    #B28 = 16
    #B42 = 24
    buildings = list(filter(lambda b: ".csv" in b, os.listdir(in_path)))
    for building in buildings[16:17]:
        name = building.split(".")[0]
        buildpath = os.path.join(in_path, building)
        df = pd.read_csv(buildpath, index_col=None, header=0)

        try:
            totalkw = df['TotalkW']
            np_totalkw = np.array(totalkw.tolist())
            if ret:
                return np_totalkw
            a = is_outlier(totalkw, 600)
            out = np.where(a)
            #Detection of big outliers -------------
            #totalkw = totalkw.drop(labels=out[0])
            # --------------------------------------
            print(name)

            num_week = 10
            data_per_week = 10087
            start_week = num_week * data_per_week
            end_week = start_week + data_per_week
            print(totalkw[100000:120000])
            #plt.plot(range(len(totalkw)), totalkw)
            plt.scatter(out[0], np_totalkw[out[0]], c='red')
            plt.plot(range(100000,110000), totalkw[100000:110000],
                        c='red')
            plt.show()
            save_path = os.path.join(plot_path, '_'.join((name, "_clean.png")))
            plt.savefig(save_path)
            plt.close()
        except Exception as e:
            print(e, name, " FALLA")


def is_outlier(points, thresh=3.5):

    if len(points.shape) == 1:
        points = points[:,None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh


if __name__ == "__main__":
    yearly()
    #cleaning()
    #plot_lab()