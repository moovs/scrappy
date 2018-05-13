from bs4 import BeautifulSoup
import requests

url="https://bugs.kde.org/buglist.cgi?bug_status=UNCONFIRMED&bug_status=CONFIRMED&bug_status=ASSIGNED&bug_status=REOPENED&columnlist=product%2Ccomponent%2Cassigned_to%2Cbug_status%2Cresolution%2Cshort_desc%2Cchangeddate%2Copendate%2Cbug_severity&field0-0-0=product&field0-0-1=component&field0-0-2=keywords&field0-0-3=alias&field0-0-4=short_desc&field0-0-5=status_whiteboard&field0-0-6=content&list_id=1513603&order=opendate%20DESC%2Cbug_status%2Cpriority%2Cassigned_to%2Cbug_id&query_format=advanced&type0-0-0=substring&type0-0-1=substring&type0-0-2=substring&type0-0-3=substring&type0-0-4=substring&type0-0-5=substring&type0-0-6=matches&value0-0-0=wayland&value0-0-1=wayland&value0-0-2=wayland&value0-0-3=wayland&value0-0-4=wayland&value0-0-5=wayland&value0-0-6=%22wayland%22"

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
html = BeautifulSoup(data, 'html.parser')

'''
use only with raw files
raw_html = open('raw.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
'''
tds_products = html.findAll('td', {'class': 'bz_product_column nowrap'})
tds_components = html.findAll('td', {'class': 'bz_component_column nowrap'})
all = []
for x in range(0, len(tds_products)):
    all.append(tds_products[x].text.strip() + " | " + tds_components[x].text.strip())

unique_values = {}

for value in all:
    if value not in unique_values:
        unique_values[value] = 1;
    else:
        unique_values[value] += 1;

sorted_values = sorted(unique_values, key=unique_values.get, reverse=True)

for key in sorted_values:
    print(key + " | " + str(unique_values[key]) + " occurences;")
