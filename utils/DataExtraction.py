#!/usr/bin/env python
# coding: utf-8

# In[11]:


#pip install pypdf2
#!pip install python-docx


# In[10]:


#Code To Extract Text From PDF File
import PyPDF2

#Opening The Pdf
a = PyPDF2.PdfFileReader("ip choices.pdf")

#Getting The Number of Pages in PDF
pg_no = a.getNumPages()

text = ""

#Reading and Extracting The Data of PDF Page Wise
for i in range(pg_no):
    text += a.getPage(i).extractText()
    

# print(text)


# In[15]:


#Code To Extract Text From Document File

#importing the Document Package
from docx import Document

#Function to Get Text From Word File
def get_Text_from_Word_File(file_path):
    doc_obj = open(file_path,"rb")
    doc_reader = Document(doc_obj)
    data = ""
    for i in doc_reader.paragraphs:
        data += i.text+"\n"
    print(data)

# get_Text_from_Word_File("AFFIDAVIT.docx")


# In[20]:


#Code To Extract Text From Text File

myfile = open("1.txt", "rt")     # open lorem.txt for reading text
contents = myfile.read()         # read the entire file to string
myfile.close()                   # close the file
print(contents)


# In[ ]:




