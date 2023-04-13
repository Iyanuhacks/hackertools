import camelot

# PDF file to extract tables from (from command-line)
file = input("enter file to extract pdf table:>>>")

# extract all the tables in the PDF file
tables = camelot.read_pdf(file)

# number of tables extracted
print("Total tables extracted:", tables.n)

# print the first table as Pandas DataFrame
print(tables[0].df)

# export individually as CSV
tables[0].to_csv("foo.csv")
# export individually as Excel (.xlsx extension)
tables[0].to_excel("foo.xlsx")

# or export all in a zip
tables.export("foo.csv", f="csv", compress=True)

# export to HTML
tables.export("foo.html", f="html")
#hackertools by iyanuhacks
#thanks for using this tool
