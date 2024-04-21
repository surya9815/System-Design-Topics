""" Problem Statement:
Document Generation: In a document processing application, a factory method pattern 
can be used to create different types of documents (e.g., PDF, Word, HTML) based on 
user preferences or document specifications.
"""
from abc import ABC, abstractmethod

#Abstract Product: Document
class Document(ABC):
    @abstractmethod
    def generate(self):
        pass

#Concrete Products: PDFDocument, WordDocument, HTMLDocument
class PDFDocument(Document):
    def generate(self):
        print ("Generating PDF document...")

class WordDocument(Document):
    def generate(self):
        print ("Generating Word document...")

class HTMLDocument(Document):
    def generate(self):
        print ("Generating HTML document...")
    
#Abstract Creator: Document Factory
class DocumentFactory(ABC):
    @abstractmethod
    def create_document(self):
        pass

# Concrete Creators: PDFDocumentFactory, WordDocumentFactory, HTMLDocumentFactory
class PDFDocumentFactory(DocumentFactory):
    def create_document(self):
        return PDFDocument()

class WordDocumentFactory(DocumentFactory):
    def create_document(self):
        return WordDocument()

class HTMLDocumentFactory(DocumentFactory):
    def create_document(self):
        return HTMLDocument()

#Client 
class Application:
    def __init__(self, document_factory):
        self.document_factory = document_factory
    
    def generate_document(self):
        document = self.document_factory.create_document()
        document.generate()

# Usage
pdf_factory = PDFDocumentFactory()
word_factory = WordDocumentFactory()
html_factory = HTMLDocumentFactory()

app1 = Application(pdf_factory)
app1.generate_document()  # Output: Generating PDF document...

app2 = Application(word_factory)
app2.generate_document()  # Output: Generating Word document...

app3 = Application(html_factory)
app3.generate_document()  # Output: Generating HTML document...