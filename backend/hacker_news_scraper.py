"""A scraper returning the links from the Hacker News website with the most points

To use:
from hacker_news_scraper import get_top_links

Then call:
top_links = get_top_links()

get_top_links is the only public function in this module
It returns the top num_links from the first num_pages of Hacker News
num_pages and num_links are two optional parameters for the get_top_links function
By default, num_pages is 5 and num_links is 15

The function returns the links as a list of dictionaries. Each dictionary has three elements:
    title: A string containing the title of the story
    link: A string containing a link to the story
    points: An integer with the number of points that story received on Hacker News

"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint

MAIN_PAGE_LINK = 'https://news.ycombinator.com/'
ADDITIONAL_PAGE_START_STRING = '?p='

POINTS_MINIMUM = 400

TOP_ROWS_SELECTOR = '.athing'
VOTE_SPANS_SELECTOR = '.score'
LINK_SELECTOR = '.titleline > a'


class NewsLink:
    def __init__(self, title, link, points):
        self.title = title
        self.link = link
        self.points = points


def _build_page_links_list(main_page_link, num_pages, additional_page_start_string):
    """Builds a list of URL links to the first num_pages of the Hacker News website

    The return value is a list of strings num_pages long containing links

    The input arguments are:
        main_page_link: A string containing the link to the main page of Hacker News Website
        num_pages: An integer containing the number of pages to build links for
        additional_page_string_string: A string to put between the main page link and the page

    """

    page_links = [main_page_link]
    for this_page in range(2, num_pages):
        page_links.append(main_page_link + additional_page_start_string + str(this_page))

    return page_links


def _get_rows_and_spans_from_page(page_link):
    res_page = requests.get(page_link)
    soup_page = BeautifulSoup(res_page.text, 'html.parser')
    top_rows = soup_page.select(TOP_ROWS_SELECTOR)
    vote_spans = soup_page.select(VOTE_SPANS_SELECTOR)

    return top_rows, vote_spans


def _convert_rows_to_dict_by_id(top_rows):
    top_rows_dict = {}
    for top_row in top_rows:
        row_id = top_row.get('id')
        top_rows_dict[row_id] = top_row

    return top_rows_dict


def _extract_info_from_vote_span(vote_span):
    news_id, points, is_error = None, None, True

    raw_news_id = vote_span.get('id')
    raw_points = vote_span.getText()

    if raw_news_id and 'score_' in raw_news_id and raw_points and ' points' in raw_points:
        news_id = raw_news_id.split('_')[1]
        points = int(raw_points.split(' ')[0])
        is_error = False

    return news_id, points, is_error


def _find_row_with_id(top_rows_dict, news_id):
    this_row, is_error = None, True

    this_row = top_rows_dict.get(news_id)
    if this_row is not None:
        is_error = False

    return this_row, is_error


def _extract_info_from_row(this_row):
    title, href, is_error = None, None, True

    link_single_list = this_row.select(LINK_SELECTOR)

    if len(link_single_list) == 1:
        link = link_single_list[0]

        title = link.getText()
        href = link.get('href', None)
        if href is not None:
            is_error = False

    return title, href, is_error


def _filter_hacker_news_links_from_page(top_rows, vote_spans, search_term, min_points):
    top_rows_dict = _convert_rows_to_dict_by_id(top_rows)

    this_pages_links = []
    for vote_span in vote_spans:
        news_id, points, is_error = _extract_info_from_vote_span(vote_span)
        if not is_error:
            if points >= min_points:
                this_row, is_error = _find_row_with_id(top_rows_dict, news_id)
                if not is_error:
                    title, href, is_error = _extract_info_from_row(this_row)
                    if not is_error and (len(search_term) == 0 or str(search_term).lower() in str(title).lower()):
                        this_pages_links.append(NewsLink(title, href, points))

    return this_pages_links


def _sort_news_links_by_points(hacker_news_links):
    return sorted(hacker_news_links, key=lambda d: d.points, reverse=True)


def get_top_links(num_links=5, num_pages=15, search_term='', min_points=400):
    page_links = _build_page_links_list(MAIN_PAGE_LINK, num_pages, ADDITIONAL_PAGE_START_STRING)

    hacker_news_links = []

    for page_link in page_links:
        top_rows, vote_spans = _get_rows_and_spans_from_page(page_link)
        hacker_news_links += _filter_hacker_news_links_from_page(top_rows, vote_spans, search_term, min_points)

    hacker_news_links = _sort_news_links_by_points(hacker_news_links)

    return hacker_news_links[0:num_links]


if __name__ == '__main__':
    top_links = get_top_links()

    top_links_as_dict = []
    for top_link in top_links:
        top_links_as_dict.append(vars(top_link))

    pprint(top_links_as_dict)
