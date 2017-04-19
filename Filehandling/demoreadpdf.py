import PyPDF2

readfileobj = open('C:\\python\\abc.pdf', 'rb')

readpdfobj=PyPDF2.PdfFileReader(readfileobj)
print(readpdfobj.numPages)

copyfile = open('copy.pdf', 'wb')
writepdfobj=PyPDF2.PdfFileWriter()

'''
Writing data to new pdf
'''

for page in range(readpdfobj.numPages):
    pdata = readpdfobj.getPage(page)
    writepdfobj.addPage(pdata)
    
writepdfobj.write(copyfile)   
copyfile.close()
readfileobj.close()
