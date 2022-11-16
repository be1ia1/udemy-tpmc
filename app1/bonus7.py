filenames = ['1.doc', '1.report', '1.presentation']

print([filename.replace('.','-')+'.txt' for filename in filenames])