import reddit_scraper
import content_generator
import email_system


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scraped_data = reddit_scraper.scrape()
    content_generator.generate(scraped_data)
    email_system.sendMail("email_list.json", "me", "code structuring success")