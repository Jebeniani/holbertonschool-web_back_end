#!/usr/bin/env python3
"""hypermedia pagination
"""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """modified function that used in task 0
        """
        start_index = (page * page_size) - page_size
        end_index = page * page_size
        return ((start_index, end_index))

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """the get_page method
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        index_range = self.index_range(page, page_size)
        self.dataset()
        return (self.__dataset[index_range[0]:index_range[1]])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_hyper method
        """
        hyper = {}
        hyper["page_size"] = page_size
        hyper["page"] = page
        hyper["data"] = self.get_page(page, page_size)
        hyper["next_page"] = (page + 1) if page < page_size else None
        hyper["prev_page"] = (page - 1) if page != 1 else None
        hyper["total_pages"] = len(self.__dataset)
        return hyper
