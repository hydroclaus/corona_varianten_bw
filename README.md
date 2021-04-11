# Corona Varianten in Baden-Württemberg

goal: Analyse / Visualisierung der Daten der Corona-Varianten in Baden-Württemberg

Datenquelle / data source: [Landesgesundheitsamt Baden-Württemberg](https://www.gesundheitsamt-bw.de/lga/DE/Fachinformationen/Infodienste_Newsletter/InfektNews/Seiten/Lagebericht_covid-19.aspx)

- presentation of data: [main jupyter notebook file](./new_variants_bw.ipynb) with plots of schools and kitas at the bottom
- associated [python helpfer file](./corona_variants_bw_helper.py)
- data are downloaded and updated into `./pdfs` via [`download_latest_pdf.ipynbs`](https://github.com/hydroclaus/corona_varianten_bw/blob/main/download_latest_pdf.ipynb) (with inspiration from [this gist](https://gist.github.com/elssar/5160757))
- main data file: for overview and data entry: apple numbers workbook [data_corona_varianten.numbers](./data/data_corona_varianten.numbers), that is exported as a tab separated file [data_corona_varianten.tsv](./data/data_corona_varianten.tsv)
- secondary data: population distribution over ages: [Altersstruktur_BW.csv](https://github.com/hydroclaus/corona_varianten_bw/blob/main/data/Altersstruktur_BW.csv)


## Typical Workflow

1. Update data using [`download_latest_pdf.ipynbs`](https://github.com/hydroclaus/corona_varianten_bw/blob/main/download_latest_pdf.ipynb)
2. Update numbers file [`data_corona_varianten.numbers`](./data/data_corona_varianten.numbers) and export to [tab separated file](https://github.com/hydroclaus/corona_varianten_bw/blob/main/data/data_corona_varianten.tsv) that is read in the following
3. run the main jupyter notebook [`new_variants_bw.ipynb`](./new_variants_bw.ipynb) 
4. Output (figures) are stored in [`./out/`](https://github.com/hydroclaus/corona_varianten_bw/tree/main/out)



Notes

- 20210322: I started this on 8-Feb-2021. Then, the largest spike in any age-group was 150. Now, the increase per day is more than 250.