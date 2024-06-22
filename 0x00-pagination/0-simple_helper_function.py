#!/usr/bin/env python3

"""
This script defines a function `index_range` that calculates the starting
and ending indices for a given page within a dataset with a specific page size.
"""

from typing import Tuple


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
