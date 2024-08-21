import requests
from bs4 import BeautifulSoup

# Function to scrape information from a specific URL
def scrape_venue_info(url, venue_selector, city_selector, country_selector, capacity_selector, genre_selector):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        venues = soup.select(venue_selector)
        cities = soup.select(city_selector)
        countries = soup.select(country_selector)
        capacities = soup.select(capacity_selector)
        genres = soup.select(genre_selector)

        # Extract text content
        venue_info = []
        for venue, city, country, capacity, genre in zip(venues, cities, countries, capacities, genres):
            venue_info.append({
                'venue': venue.get_text(strip=True),
                'city': city.get_text(strip=True),
                'country': country.get_text(strip=True),
                'capacity': capacity.get_text(strip=True),
                'genre': genre.get_text(strip=True)
            })

        return venue_info
    else:
        return []

# URLs and their corresponding selectors for the desired information
websites = [
    {
        "url": "https://www.gq-magazine.co.uk/culture/article/best-small-music-venues-uk",
        "venue_selector": "h2.venue-name",  # Adjust based on the structure of the site
        "city_selector": "span.city",       # Adjust based on the structure of the site
        "country_selector": "span.country", # Adjust based on the structure of the site
        "capacity_selector": "span.capacity",  # Adjust based on the structure of the site
        "genre_selector": "span.genre"      # Adjust based on the structure of the site
    },]

# Scrape and print venue information from each website
for site in websites:
    print(f"Scraping venue information from: {site['url']}")
    venue_info = scrape_venue_info(
        site['url'],
        site['venue_selector'],
        site['city_selector'],
        site['country_selector'],
        site['capacity_selector'],
        site['genre_selector']
    )
    if venue_info:
        for i, info in enumerate(venue_info, start=1):
            print(f"{i}. Venue: {info['venue']}, City: {info['city']}, Country: {info['country']}, Capacity: {info['capacity']}, Genre: {info['genre']}")
    else:
        print("No information found or failed to retrieve content.")
    print("\n" + "-"*40 + "\n")
