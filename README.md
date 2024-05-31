## Dependencies Installation

To ensure you have all the necessary dependencies for your project, follow these steps:

1. **Open your terminal.**
2. **Navigate to your project directory.**
3. **Run the following command:**

```bash
pip install -r requirements.txt
```

This command will automatically download and install all the dependencies listed in the requirements.txt file, ensuring your project has everything it needs to run smoothly.

## Data Scraping Instructions

If you intend to scrape data, follow these steps:

### Prepare the URL:

Visit spitogatos.gr and configure your desired filters.
Copy the URL with the applied filters. For example:

```bash
https://www.spitogatos.gr/enoikiaseis-katoikies/athina-kentro/timi_eos-1000/emvado_apo-25/emvado_eos-80
```

### Run the Scraper Script:

Execute the spitogatoscraper.py script with the URL and the range of pages you want to scrape. For instance:

```bash
py spitogatoscraper.py https://www.spitogatos.gr/enoikiaseis-katoikies/athina-kentro/imi_eos-1000/emvado_apo-25/emvado_eos-80 1 3
```

This command will scrape pages 1 through 3. 

`IMPORTANT NOTE`: To avoid getting banned from the site, scrape slowly and responsibly. Aim to scrape **[1:4]** pages every **30 minutes**. While it is possible to speed up this process, it is crucial to respect the site's rules and limitations.

### Merge JSON Files:

After scraping, execute the merge_all_json.py script to merge all the JSON files into one.

```bash
py merge_all_json.py
```

### Run the Application:

Finally, execute app.py to analyze the scraped data and view average and median prices.

```bash
py app.py
```

That's all for now! Happy scraping!

### Clear All The Data

Although I could create a script to clear all the data, it is safer to perform this action manually to avoid accidental data loss. To clear the data, navigate to the `samples/` directory and manually delete the files you want to remove.
