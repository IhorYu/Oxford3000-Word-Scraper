<html>
  <head>
  </head>
  <body>
    <h1>Oxford 3000 Word Scraper</h1>
    <p>This script uses the <code>requests</code> and <code>Beautiful Soup 4</code> libraries to scrape the <a href="https://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/Oxford3000_A-B">Oxford 3000</a> page and extract a list of words from it. The list is then saved to a CSV file.</p>
    <h2>Requirements</h2>
    <ul>
      <li>Python 3</li>
      <li><code>requests</code> library</li>
      <li><code>csv</code> library</li>
      <li><code>bs4</code> (Beautiful Soup 4) library</li>
    </ul>
    <h2>Usage</h2>
    <ol>
      <li>Clone or download this repository</li>
      <li>Navigate to the directory where the script is located</li>
      <li>Run the script using <code>python main.py</code></li>
    </ol>
    <p>The script will scrape the Oxford 3000 page and save the list of words to a CSV file called <code>oxford3000.csv</code> in the same directory.</p>
    <h2>Configuration</h2>
    <p>By default, the script scrapes the list of words in groups of A-B, C-D, E-G, H-K, L-N, O-P, Q-R, S, T, U-Z. You can modify the <code>words_groups</code> list to scrape a different set of groups.</p>
    <p>You can also modify the number of pages to scrape for each group by adjusting the range in the <code>for</code> loop on line 16. The default value is <code>range(1, 6)</code>, which will scrape the first 5 pages of each group.</p>
    <h2>Note</h2>
    <p>This script is for personal use only. Please respect the website's terms of use and do not use this script to scrape the website excessively.</p>
  </body>
</html>
