# https://www.youtube.com/watch?v=vEQ8CXFWLZU
# https://www.youtube.com/watch?v=SnoST-5Sz8U
# https://www.youtube.com/watch?v=4gZgWXJpX-w
# https://www.youtube.com/watch?v=oOBkFW9phQk

# Import the PypDF2 library to work with PDF files
import PyPDF2

# Create a PdfMerger object to merge PDFs
pdf_merger = PyPDF2.PdfMerger()

# Add the first PDF file('file1.pdf') to the merger object 
pdf_merger.append('D:\GCBS\HCM206\Chapter 1.pdf')

# Add the second PDF file('file2.pdf') to the merger object 
pdf_merger.append('D:\GCBS\HCM206\Chapter 2.pdf')

# Merge the PDFs into a single file and name it 'merged.pdf'
pdf_merger.write('Combined 1&2.pdf')

# Close the PdfMerger object to release resources
pdf_merger.close()

# Inform the user that the PDF files have been successfully merged
print('PDF files merged successfully into Combined 1&2.pdf')