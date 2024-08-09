from hacker_news_scraper import get_top_links

print('In top links')

page_links = get_top_links(10, 3)

print('Here are the links: ')

for index, page_link in enumerate(page_links):
    print(f'Link {index + 1}: {page_link.title}')
