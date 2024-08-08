import requests
from bs4 import BeautifulSoup
from pprint import pprint

MAIN_PAGE_LINK = 'https://news.ycombinator.com/'
NUM_PAGES = 15
ADDITIONAL_PAGE_START_STRING = '?p='

POINTS_MINIMUM = 400

TOP_ROWS_SELECTOR = '.athing'
VOTE_SPANS_SELECTOR = '.score'
LINK_SELECTOR = '.titleline > a'


def build_page_links_list(main_page_link, num_pages, additional_page_start_string):
    page_links = [main_page_link]
    for this_page in range(2, num_pages):
        page_links.append(main_page_link + additional_page_start_string + str(this_page))

    return page_links


def get_rows_and_spans_from_page(page_link):
    res_page = requests.get(page_link)
    soup_page = BeautifulSoup(res_page.text, 'html.parser')
    top_rows = soup_page.select(TOP_ROWS_SELECTOR)
    vote_spans = soup_page.select(VOTE_SPANS_SELECTOR)

    return top_rows, vote_spans


def convert_rows_to_dict_by_id(top_rows):
    top_rows_dict = {}
    for top_row in top_rows:
        row_id = top_row.get('id')
        top_rows_dict[row_id] = top_row

    return top_rows_dict


def extract_info_from_vote_span(vote_span):
    news_id, points, is_error = None, None, True

    raw_news_id = vote_span.get('id')
    raw_points = vote_span.getText()

    if raw_news_id and 'score_' in raw_news_id and raw_points and ' points' in raw_points:
        news_id = raw_news_id.split('_')[1]
        points = int(raw_points.split(' ')[0])
        is_error = False

    return news_id, points, is_error


def find_row_with_id(top_rows_dict, news_id):
    this_row, is_error = None, True

    this_row = top_rows_dict.get(news_id)
    if this_row is not None:
        is_error = False

    return this_row, is_error


def extract_info_from_row(this_row):
    title, href, is_error = None, None, True

    link_single_list = this_row.select(LINK_SELECTOR)

    if len(link_single_list) == 1:
        link = link_single_list[0]

        title = link.getText()
        href = link.get('href', None)
        if href is not None:
            is_error = False

    return title, href, is_error


def filter_hacker_news_links_from_page(top_rows, vote_spans):
    top_rows_dict = convert_rows_to_dict_by_id(top_rows)

    this_pages_links = []
    for vote_span in vote_spans:
        news_id, points, is_error = extract_info_from_vote_span(vote_span)
        if not is_error:
            if points >= POINTS_MINIMUM:
                this_row, is_error = find_row_with_id(top_rows_dict, news_id)
                if not is_error:
                    title, href, is_error = extract_info_from_row(this_row)
                    if not is_error:
                        this_pages_links.append({'title': title, 'link': href, 'points': points})

    return this_pages_links


def sort_news_links_by_points(hacker_news_links):
    return sorted(hacker_news_links, key=lambda d: d['points'], reverse=True)


page_links = build_page_links_list(MAIN_PAGE_LINK, NUM_PAGES, ADDITIONAL_PAGE_START_STRING)

hacker_news_links = []

for page_link in page_links:
    top_rows, vote_spans = get_rows_and_spans_from_page(page_link)
    hacker_news_links += filter_hacker_news_links_from_page(top_rows, vote_spans)

hacker_news_links = sort_news_links_by_points(hacker_news_links)

pprint(hacker_news_links[0:5])
