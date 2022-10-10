import pandas
# import sys

name = ['Genesis', '2Chronicles', 'Daniel', 'Exodus', 'Ezra', 'Hosea', 'Leviticus', 'Nehemiah', 'Joel', 'Numbers', 'Esther', 'Amos', 'Deuteronomy', 'Job', 'Obadiah', 'Joshua', 'Psalms', 'Jonah', 'Judges', 'Proverbs', 'Micah', 'Ruth', 'Ecclesiastes', 'Nahum', '1Samuel', 'SongofSongs', 'Habakkuk', '2Samuel', 'Isaiah', 'Zephaniah', '1Kings', 'Jeremiah', 'Haggai', '2Kings', 'Lamentations', 'Zechariah', '1Chronicles', 'Ezekiel', 'Malachi', 'Matthew', 'Ephesians', 'Hebrews', 'Mark', 'Philippians', 'James', 'Luke', 'Colossians', '1Peter', 'John', '1Thessalonians', '2Peter', 'Acts', '2Thessalonians', '1John', 'Romans', '1Timothy', '2John', '1Corinthians', '2Timothy', '3John', '2Corinthians', 'Titus', 'Jude', 'Galatians', 'Philemon', 'Revelation']

# input_name = sys.argv[1]
for i in range(len(name)):
    input_name = name[i] + ".xlsx"
    output_name = input_name.split('.xlsx')[0] + '.csv'
    xlsx = pandas.read_excel(input_name)
    xlsx.to_csv(output_name)