
import requests
import bs4
import random


def pracuj(user_input):

    url = requests.get(f'https://www.pracuj.pl/praca/{user_input};kw?rd=30\n')

    soup_parsed = bs4.BeautifulSoup(url.content, 'html.parser')

    results = soup_parsed.find(id='results')

    splitter = results.find_all(class_='results__list-container')

    # Found data to be appended to main data
    data = []
    data_2 = []
    data_3 = []
    data_links = []

    data_loc = []

    # Main data dictionary
    main_data = {}

    # Index Positions
    pos_beg, pos_end = 0, 1
    links_beg_pos = 0

    # Search loop
    for line in splitter:
        line_finder_comp = line.find_all(class_='offer-company')
        line_finder_loc = line.find_all(class_="offer-labels__item--location")
        for i in line_finder_loc:
            data_loc.append(i.text.split())
        for h in line.find_all('a', class_='offer-details__title-link'):
            data_links.append(h['href'])
            data.append(h.text)

    # Additional information
    for elem in line_finder_comp:
        data_2.append(elem.text.split())

    # Generate a random serial for duplicate postings
    for n in range(len(data)):
        if data[n] in main_data:
            rand = random.randrange(10000, 100000)
            data[n] += (f' {rand}')

        # Append Posting and Additional info
        main_data[data[n]] = data_2[pos_beg:pos_end]
        for i in main_data[data[n]]:
            data_3.append(' '.join(i))
            main_data[data[n]] = data_3[pos_beg:pos_end]
        pos_beg += 1
        pos_end += 1

    # Return all jobs postings
    res_list = []
    for k, v in main_data.items():
        res_list.append(("\n\nJob description: ", k, '| Link: ',
                         data_links[links_beg_pos], "\n\nCompany name: ", ' - '.join(v), '\nLocation :', ' '.join(data_loc[links_beg_pos], )))
        links_beg_pos += 1
    return res_list


def olx(user_input):

    url = requests.get(f'https://www.olx.pl/praca/q-{user_input}\n')

    soup_parsed = bs4.BeautifulSoup(url.content, 'html.parser')

    results = soup_parsed.find(id='body-container')

    splitter = results.find_all(class_='rel listHandler')

    # Found data to be appended to main data
    data = []
    data_2 = []
    data_3 = []
    data_links = []

    # Main data dictionary
    main_data = {}

    # Index Positions
    pos_beg, pos_end = 0, 4
    links_beg_pos = 0

    # Search loop
    for line in splitter:
        line_finder_loc = line.find_all('small')
        for elem in line_finder_loc:
            data_2.append(elem.text.split())
        for h in line.find_all('a', class_='link'):
            if 'oferta' not in h['href']:
                continue
            data_links.append(h['href'])
            data.append(h.find('strong').text)

    # Generate a random serial for duplicate postings
    for n in range(len(data)):
        if data[n] in main_data:
            rand = random.randrange(10000, 100000)
            data[n] += (f' {rand}')

        # Append Posting and Additional info
        main_data[data[n]] = data_2[pos_beg:pos_end]
        for i in main_data[data[n]]:
            data_3.append(' '.join(i))
            main_data[data[n]] = data_3[pos_beg:pos_end]
        pos_beg += 4
        pos_end += 4
        if pos_end > len(data_2):
            break

    # Return all jobs postings
    res_list = []
    for k, v in main_data.items():
        res_list.append(("\n\nJob description: ", k, r'| Link: ',
                         data_links[links_beg_pos], "\n\nMore info: ", ' - '.join(v)))
        links_beg_pos += 1
        if links_beg_pos > len(data_links):
            break
    return res_list


def gumtree(user_input):

    url = requests.get(
        f'https://www.gumtree.pl/s-oferty-pracy/v1c8p1?q={user_input}')

    soup_parsed = bs4.BeautifulSoup(url.content, 'html.parser')

    results = soup_parsed.find(id='wrapper')

    splitter = results.find_all(class_='results list-view')

    # Found data to be appended to main data
    data = []
    data_2 = []
    data_3 = []
    data_links = []

    data_loc = []

    # Main data dictionary
    main_data = {}

    # Index Positions
    pos_beg, pos_end = 0, 1
    links_beg_pos = 0

    # Search loop
    for line in splitter:
        line_finder_comp = line.find_all(class_='offer-company')
        line_finder_loc = line.find_all(class_="category-location")
        for i in line_finder_loc:
            data_loc.append(i.text.split())
        for h in line.find_all('a', class_='href-link tile-title-text'):
            data_links.append(h['href'])
            data.append(h.text)

    # Additional information
    # for elem in line_finder_comp:
    #     data_2.append(elem.text.split())

    # Generate a random serial for duplicate postings
    for n in range(len(data)):
        if data[n] in main_data:
            rand = random.randrange(10000, 100000)
            data[n] += (f' {rand}')

        # Append Posting and Additional info
        main_data[data[n]] = data_2[pos_beg:pos_end]
        for i in main_data[data[n]]:
            data_3.append(' '.join(i))
            main_data[data[n]] = data_3[pos_beg:pos_end]
        pos_beg += 1
        pos_end += 1

    # Return all jobs postings
    res_list = []
    for k, v in main_data.items():
        res_list.append(("\n\nJob description: ", k,
                         '| Link: ', f"https://www.gumtree.pl{data_links[links_beg_pos]}", '\n\nLocation :', ''.join(data_loc[links_beg_pos][-1])))
        links_beg_pos += 1
    return res_list
