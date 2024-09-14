import fitz  

def pdf_page_to_png(pdf_path, page_number, output_png):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    # Check if the page number is within the range of the PDF
    if page_number < 1 or page_number > doc.page_count:
        raise ValueError(f"Invalid page number: {page_number}. PDF has {doc.page_count} pages.")
    
    # Select the page (page numbers start at 0 in PyMuPDF)
    page = doc.load_page(page_number - 1)
    
    # Render the page to an image (resolution 150 dpi for example)
    pix = page.get_pixmap(dpi=150)
    
    # Save the image as a PNG file
    pix.save(output_png)
    
    print(f"Page {page_number} saved as {output_png}")

# Example usage
pdf_path = "C:/Users/estra/Downloads/[Anna] - Korea Visa App May 2024.pdf"
page_number = 2  # Change to the page you want to convert
output_png = "C:/Users/estra/Downloads/testract1.png"

pdf_page_to_png(pdf_path, page_number, output_png)
