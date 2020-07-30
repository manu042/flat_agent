# Flatagent
Web scraper which searches automatically new real estate on Immobilienscout24


## Usage

1. Go to [Immobilienscout24](https://www.immobilienscout24.de/) and start a new search
2. Change the sort order so that the most recent results are listed first
3. Then copy the link from the address bar
4. Open docker-compose.yml and replace the environment variable **SEARCH_URL** with your copied link
5. Replace the other environment variables with your mail settings.
6. Run docker-compose
```
docker-compose up -d
```
