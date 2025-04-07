#! /usr/bin/env python3

from src.getter_data import getData
from src.writter_data import write_data

def main():
    json_file = getData(departement="Essonne", region="Île-de-France").json()
    # write_data("data/recup/mydatas", json_file, timeInfo=True)

if __name__ =="__main__":
    main()