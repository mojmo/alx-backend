#!/usr/bin/env python3

"""
Retrieves a page of data from the dataset along with hypermetadata
describing the pagination details.
"""

import csv
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the starting and ending indices for a given page
    within a dataset.

    This function assumes 1-based indexing for pages.

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the starting and ending indices for
        the specified page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a page of data from the dataset."""

        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index > len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves a page of data from the dataset along with hypermetadata
        describing the pagination details.
        """
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = (len(dataset) + page_size - 1) // page_size
        return {
            "page_size": len(data),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
