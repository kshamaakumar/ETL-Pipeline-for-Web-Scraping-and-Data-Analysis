### ETL-Pipeline-for-Web-Scraping-and-Data-Analysis

Create an ETL pipeline to scrape data from a news website and perform data analysis on the collected articles. The target website will be "Google News" (https://news.google.com/). Collect the article titles, publication dates, and article links
Execution Steps: 

1.	Choose the Target Website: 
    - Website: BBC News (https://news.google.com/)
    -   Data to Collect: Article titles, publication dates, and article links.
2.	Web Scraping: 
    - Tools: Python,requests library.
    - Use the requests library to send an HTTP request to the website and get the HTML content of the page.
    - Parse the HTML content using Beautiful Soup to extract the relevant data (article titles, publication dates, and categories) using appropriate HTML tags and classes.
3.	Data Transformation:
    - Tools: Python (Pandas for data manipulation).
    - Create a DataFrame to store the scraped data.
    - Clean the data by handling any missing or incorrect values, removing duplicates, and converting data types if necessary.
    - Extract the publication date and format it to a standardized date format.
4.	Data Storage: 
    - Tools: SQLite database (Python's sqlite3 library).
    - Set up a SQLite database to store the cleaned data.
    -   Create a table in the database to hold the article data with appropriate columns for article titles, publication dates, and categories.
    -  Insert the cleaned data from the DataFrame into the database table.
5.	Data Analysis and Visualizations:
    - Tools: Python (Pandas, Matplotlib, Seaborn).
    - Load the data from the SQLite database into a DataFrame.
    - Perform exploratory data analysis (EDA) on the collected data using Pandas for statistical insights, data summaries, and visualizations.
    - Generate visualizations (e.g., bar charts, line plots) using Matplotlib and Seaborn to understand trends and patterns in the articles.
6.	**Automate the Pipeline: (In progress)** 
    - Tools: Python, Apache Airflow (for automation).
    - Develop a Python script that encapsulates all the above steps from web scraping to data analysis.
    - Set up an Apache Airflow workflow to schedule and automate the execution of the script at regular intervals (e.g., daily or weekly).
