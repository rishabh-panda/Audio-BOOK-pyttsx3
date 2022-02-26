#text-to-speech module
import pyttsx3

#PDF reader module
import  PyPDF2

#variable opening the book (rb - binary file format)
book = open('Machine Learning For Dummies.pdf', 'rb')

#variable reading the book file
PDFReader = PyPDF2.PdfFileReader(book)

#printing book data
total_page_count = PDFReader.numPages
book_info = PDFReader.getDocumentInfo()
book_fields = PDFReader.getFields()

print("Document info: ",book_info)
print("Number of pages: ",total_page_count)
print("Book fields: ",book_fields)

#initializiation of text-to-speech module
speaker = pyttsx3.init()

#accessing a particular book page
access_specific_page = PDFReader.getPage(270)

extracted_text = access_specific_page.extractText()
speaker.say(extracted_text)
speaker.runAndWait()

#closing the book
book.close()

'''
For reading the entire book apply for loop:-

for i in range (0, total_page_count):
    access_specific_page = PDFReader.getPage(i)
    extracted_text = access_specific_page.extractText()
    speaker.say(extracted_text)
    speaker.runAndWait()
'''
