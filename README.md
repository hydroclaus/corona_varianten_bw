# Corona Varianten in Baden-Württemberg

goal: Analyse / Visualisierung der Daten der Corona-Varianten in Baden-Württemberg

Datenquelle / data source: [Landesgesundheitsamt Baden-Württemberg](https://www.gesundheitsamt-bw.de/lga/DE/Fachinformationen/Infodienste_Newsletter/InfektNews/Seiten/Lagebericht_covid-19.aspx)

- presentation of data: [main jupyter notebook file](./new_variants_bw.ipynb) with plots of schools and kitas at the bottom
- associated [python helpfer file](./corona_variants_bw_helper.py)
- data are downloaded and updated into `./pdfs` via [`download_latest_pdf.ipynbs`](https://github.com/hydroclaus/corona_varianten_bw/blob/main/download_latest_pdf.ipynb)
- main data file: for overview and data entry: apple numbers workbook [data_corona_varianten.numbers](./data/data_corona_varianten.numbers), that is exported as a tab separated file [data_corona_varianten.tsv](./data/data_corona_varianten.tsv)