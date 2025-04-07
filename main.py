#! /usr/bin/env python3

from src.getter_data import getData
from src.writter_data import write_data

def main():
    json_file = getData().json()
    write_data("data/mydatas.json", json_file)

if __name__ =="__main__":
    main()