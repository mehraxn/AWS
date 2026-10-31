# Amazon Textract

## Simple definition

Amazon Textract is an AWS service that automatically reads text and structured data from scanned documents.

It can extract printed text, handwriting, tables, and form fields without requiring you to build your own OCR solution.

---

## Core idea in plain English

Think of Amazon Textract as a smart document reader.

If you upload a paper document such as an invoice, receipt, tax form, or application form, Textract can analyze the image or PDF and tell you what text appears on the page and how that data is organized.

This is more advanced than simple OCR because Textract can also understand document structure, such as which value belongs to which label and which values are part of a table.

---

## Main use cases

### 1. Invoice and receipt processing

Textract can extract important fields such as invoice number, total amount, vendor name, and date from scanned financial documents.

### 2. Form and application processing

It can pull out key-value pairs from forms such as names, addresses, ID numbers, and submission dates.

### 3. Insurance and claims document automation

Companies can use Textract to read claim forms and supporting documents instead of entering the data manually.

### 4. Scanned PDF text extraction

Textract can read scanned PDFs and convert the document contents into machine-readable text.

### 5. Table extraction from business documents

It can detect rows, columns, and cell values in documents such as reports, statements, and spreadsheets saved as images or PDFs.

### 6. Digitization of paper records

Organizations can use Textract to turn large collections of paper documents into searchable digital information.

### 7. Workflow automation

Textract can feed extracted document data into applications, databases, approval systems, or analytics pipelines.

---

## Key features

### 1. Printed text extraction

Textract can detect and extract printed text from scanned images and PDF documents.

### 2. Handwriting recognition

It can also identify handwritten content in many document-processing scenarios.

### 3. Form field detection

Textract can identify relationships between labels and values, such as `Name: Maria Rossi` or `Invoice Number: INV-1001`.

### 4. Table detection

It can recognize table structures and return data in rows and columns instead of as plain text only.

### 5. Structured output

Textract does not just return text lines. It can return words, lines, key-value pairs, and table elements in a structured format.

### 6. Support for scanned documents

It is designed for images and scanned PDFs, which makes it useful for real-world paper document workflows.

### 7. Fully managed service

AWS manages the infrastructure, scaling, and availability, so you do not need to run your own OCR servers.

### 8. Integration with other AWS services

Textract can work with services such as Amazon S3, AWS Lambda, Step Functions, and Amazon Comprehend to build automated document workflows.

---

## How it works

### Step 1. Upload a document

You provide a scanned image or PDF, commonly stored in Amazon S3.

### Step 2. Textract analyzes the content

Textract scans the document and identifies text, forms, and tables.

### Step 3. Structured results are returned

The service returns extracted data such as words, lines, key-value pairs, and table structure.

### Step 4. Use the data in your application

Your application can store, search, validate, review, or process the extracted information further.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, the main point is this:

**Amazon Textract is the AWS service used to extract text and structured data from scanned documents.**

You should think of Textract when the exam mentions:

* OCR-like document processing
* invoices
* receipts
* scanned forms
* tables in documents
* scanned PDFs
* document digitization
* extracting data from paper-based files

The exam often tests whether you can choose the correct service based on the type of content being processed.

---

## Related AWS services and differences

### Amazon Textract vs Amazon Rekognition

* **Textract** is for reading documents and extracting text, forms, and tables.
* **Rekognition** is for analyzing images and videos, such as faces, objects, scenes, and unsafe content.

Use Textract for invoices, forms, and scanned pages.
Use Rekognition for people, objects, labels, and image moderation.

### Amazon Textract vs Amazon Comprehend

* **Textract** extracts text and document structure.
* **Comprehend** analyzes the meaning of text, such as sentiment, entities, and key phrases.

A common pattern is:

* Textract reads the document.
* Comprehend analyzes the extracted text.

### Amazon Textract vs Amazon Kendra

* **Textract** pulls text out of documents.
* **Kendra** helps users search across documents intelligently.

### Amazon Textract vs Amazon Transcribe

* **Textract** works with documents and images.
* **Transcribe** converts speech into text.

### Amazon Textract vs Amazon Polly

* **Textract** reads text from documents.
* **Polly** converts text into speech.

---

## Common exam traps

### 1. Confusing Textract with Rekognition

This is a common mistake. If the question is about a scanned form, invoice, or document image, the correct choice is usually Textract, not Rekognition.

### 2. Confusing text extraction with text understanding

Textract extracts the text and document structure. If the question asks about sentiment analysis, entity recognition, or language understanding, the correct service is more likely Amazon Comprehend.

### 3. Confusing documents with audio processing

If the source is recorded speech, calls, or audio files, the answer is Amazon Transcribe, not Textract.

### 4. Thinking Textract is only basic OCR

Textract does more than simply detect characters. It can also identify form fields and tables, which makes it more powerful than plain OCR in exam scenarios.

### 5. Choosing a storage service instead of a processing service

Amazon S3 stores files. Amazon Textract processes files to extract information from them.

### 6. Mixing up extraction and search

Textract extracts content from documents. Amazon Kendra is used when the goal is intelligent search across many documents.

---

## AWS exam keywords for Amazon Textract

Watch for these keywords and phrases in exam questions:

* scanned documents
* OCR
* document text extraction
* extract text from PDF
* forms
* form fields
* key-value pairs
* invoices
* receipts
* tables
* handwritten text
* digitize paper records
* document processing
* structured data from documents
* scanned image analysis
* read text from image

If the question focuses on **extracting text or structure from a document**, Amazon Textract is a strong answer.

---

## Easy real-world example

A company receives thousands of invoice PDFs every month.

Instead of employees opening each file and manually typing the invoice number, date, and total amount into a system, the company uploads the invoices to Amazon S3.

Amazon Textract reads each invoice and extracts the important fields automatically.

This saves time, reduces manual work, and lowers the number of human errors.

---

## Final summary

Amazon Textract is AWS’s document text extraction service.

It helps businesses read scanned documents automatically and extract useful information such as text, form fields, and tables.

For the exam, remember it as the AWS service for **document OCR and structured data extraction**.

---

## Short exam answer

Amazon Textract is a fully managed AWS service that extracts printed text, handwriting, tables, and form data from scanned documents.

---

## Memory trick

**Textract = Text + Extract**

If AWS needs to extract text from documents, think **Textract**.
