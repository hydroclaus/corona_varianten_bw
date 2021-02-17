#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Helper script for corona_varianten_bws
"""
# import sys
# import os
# import datetime
# import numpy as np
import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import date2num

__author__ = "Claus Haslauer (mail@planetwater.org)"
__version__ = "$Revision: 0.1 $"
__date__ = datetime.date(2021,2,16)
__copyright__ = "Copyright (c) 2021 Claus Haslauer"
__license__ = "Python"



def plot_pflege_schule_kitas(data, flag=""):
    fig, ax = plt.subplots(nrows=4, ncols=1, sharex=True, figsize=(8,12))
    color_faelle = 'darkgray'

    # ------------------------------------------------------------
    #                                                    Varianten
    # ------------------------------------------------------------
    n_varianten = ax[0].plot(data["Timestamp"],
                             data["Faelle_Varianten_Typ"],
                             "o-",
                             label=flag+"Faelle_Varianten_Typ",
                             )
    n_b117 = ax[0].plot(data["Timestamp"],
                        data["B117"],
                        "o-",
                        label=flag+"B117",
                        )
    n_b1351 = ax[0].plot(data["Timestamp"],
                         data["B1351"],
                         "o-",
                         label=flag+"B1351"
                         )
    lns = n_varianten + n_b117 + n_b1351
    if flag == "Δ":
        ax0 = ax[0].twinx()
        perc_varianten = data["Faelle_Varianten_Typ"] / data["n_ges"] * 100.0
        perc_var = ax0.plot(data["Timestamp"],
                            perc_varianten,
                            "o--",
                            c=color_faelle)
        ax0.set_ylim(-20., 40.)
        ax0.set_ylabel("Percent Varianten")
        lns = n_varianten + n_b117 + n_b1351 + perc_var
        
    
    labs = [l.get_label() for l in lns]
    ax[0].legend(lns, labs, bbox_to_anchor=(1.1,1), loc="upper left")
    ax[0].grid(True)
    ax[0].title.set_text(flag+"Varianten")

    # ------------------------------------------------------------
    #                                                  Pflegeheime
    # ------------------------------------------------------------
    n_pflegeheime = ax[1].plot(data["Timestamp"],
                               data["n_Ausbrueche_Pflegeheimen"],
                               "o-",
                               label=flag+"n_Ausbrueche_Pflegeheimen",
                               )
    ax1 = ax[1].twinx()
    n_pflegeheime_faelle = ax1.plot(data["Timestamp"],
                                      data["nAusbrueche_Pflefeheimen_Varianten"],
                                      "o--",
                                      c=color_faelle,
                                      label=flag+"nAusbrueche_Pflefeheimen_Varianten",
                                      )

    ax1.set_ylabel(flag+"n Varianten in Pflegeheimen")
    ax[1].set_ylabel("Faelle")

    lns = n_pflegeheime + n_pflegeheime_faelle #+ herbstferien
    labs = [l.get_label() for l in lns]
    ax[1].legend(lns, labs, bbox_to_anchor=(1.1,1), loc="upper left")
    ax[1].grid(True)
    ax[1].title.set_text(flag+"Pflegeheime")
    ax[1].set_ylabel(flag+"Faelle")

    # ------------------------------------------------------------
    #                                                      Schulen
    # ------------------------------------------------------------
    n_schule = ax[2].plot(data["Timestamp"],
                          data["n_Ausbrueche_Schulen"],
                          "o-",
                          label=flag+"n_Ausbrueche_Schulen",
                          )
    ax2 = ax[2].twinx()
    n_schule_varianten = ax2.plot(data["Timestamp"],
                                  data["n_Ausbrueche_Schulen_Varianten"],
                                  "o--",
                                  c=color_faelle,
                                  label=flag+"n_Ausbrueche_Schulen_Varianten",
                                  )
    ax2.set_ylabel(flag+"n Varianten in Schulen")
    ax[2].set_ylabel(flag+"Faelle")

    herbstferien = ax[2].axvspan(date2num(datetime.datetime(2021,2,13)),
                                 date2num(datetime.datetime(2021,2,21)),
                                 label="Herbstferien",
                                 color="crimson",
                                 alpha=0.3)
    ax[2].annotate('Faschingsferien', 
                  (date2num(datetime.datetime(2021,2,13)), data["n_Ausbrueche_Schulen"].min()),
                  xycoords='data',
                  color='red',
                  xytext=(5, 5),
                  textcoords='offset points'
                  )

    lns = n_schule + n_schule_varianten #+ herbstferien
    labs = [l.get_label() for l in lns]
    ax[2].legend(lns, labs, bbox_to_anchor=(1.1,1), loc="upper left")

    ax[2].grid(True)
    ax[2].title.set_text(flag+"Schulen")


    # ------------------------------------------------------------
    #                                                        Kitas
    # ------------------------------------------------------------
    n_kitas = ax[3].plot(data["Timestamp"],
                         data["n_Ausbrueche_Kitas"],
                         "o-",
                         label=flag+"n_Ausbrueche_Kitas",
                         )
    ax3 = ax[3].twinx()
    n_kitas_faelle = ax3.plot(data["Timestamp"],
                                data["n_Ausbrueche_Kitas_Varianten"],
                                "o--",
                                c=color_faelle,
                                label=flag+"n_Ausbrueche_Kitas_Varianten",
                                )
    lns = n_kitas + n_kitas_faelle #+ herbstferien
    labs = [l.get_label() for l in lns]
    ax[3].legend(lns, labs, bbox_to_anchor=(1.1,1), loc="upper left")

    ax3.set_ylabel(flag+"n Varianten in Kitas")
    ax[3].set_ylabel(flag+"Faelle")

    ax[3].grid(True)
    ax[3].title.set_text(flag+"Kitas")


    fig.autofmt_xdate(rotation=90)


def main():
    pass
 
if __name__ == '__main__':
    main()