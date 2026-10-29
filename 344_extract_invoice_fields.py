import re

text = input("Enter invoice text: ")
invoice_numbers = re.findall(r"(?i)invoice\\s*(?:no\\.?|number|#)?\\s*[:#-]?\\s*([A-Z0-9/-]+)", text)
dates = re.findall(r"\\b\\d{2}[-/]\\d{2}[-/]\\d{4}\\b", text)
amounts = re.findall(r"(?:₹|INR|Rs\\.?\\s*)\\s?\\d[\\d,]*(?:\\.\\d{2})?", text, re.IGNORECASE)
print("Invoice numbers:", invoice_numbers)
print("Dates:", dates)
print("Monetary amounts:", amounts)
