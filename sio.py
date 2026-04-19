from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.lib.units import inch
from datetime import datetime, timedelta
import os  # Added to use os.system() to send to the printer

# List of names
names = [
    "Adalynn Chinn", "Amelia Pierner", "Andrew Frink",
    "Beau Bussey", "Bellamy Li", "Benjamin Conly", "Bryson Alvarez-Barrad",
    "Camila Kiss", "Carlotta Garcia", "Cassian Goodarzi", "Charles Bulock", "Colin Sweeney",
    "Easton Stuckey", "Edison Amirkiai", "Elliot Barkel", "Emilia Miura", "Esa Ali Ahmad", "Esmé Slye", "Ethan Bell", "Sophie Bell", "Evelyn Plaza",
    "Ezra Kanemasu",
    "Francine Gallegos", 
    "Genevieve Reische", 
    "Harvey Stoops", "Hazel Dawson", "Holland Gibson",
    "Isaiah Ortiz", "Isla Lopez", 
    "Jack Sterling-Charlton", "Jacob Arneson", "Jillian Zimmerman", "Josephine Cruz", "Julian Fleming", 
    "Kai Malgieri", "Khalil Carlisle-Singh", "Kilian Petrik", "Kruz Wakabayashi", 
    "Lang Richman-Nguyen", "Leo Dougherty", "Leo Necoechea", "Liam Lucas IV", "Lily Bryant", "Lily Lincoln", "Lucia Comer", "Lukas Le", 
    "Maddie Smith", "Madison Hiers-Chin", 
    "Nadja Greene", "Noah Moriel",
    "Olive Warner", "Olivia Wiley", "Benjamin Wiley", "Ophelia Gonzalez-Brown", "Owen Goldmark",
    "Palmer Pudewell", "Parker Unruh", 
    "Rafael Martinez", "Rory Olson", "Rosalia Demarino", "Lorenzo Demarino", "Rudy Castillo", "Rylie Cunningham",
    "Sahana Yogeswaran", "Santiago Cabrera-Yu", "Shea Grua", "Shepherd Ploesch", "Spencer Hilton", 
    "Tam Jatkar",
    "Valentino Carrillo Bianchi", "Vincenzo Tufo", "Violet Dimitropoulos", 
    "Zachary Avelar", "Zeke McCarthy", "Alivia McCarthy", 
    
]

# Function to generate the sign-in/out sheet
def generate_sign_in_out_sheet(names, month, year):
    # Create a PDF document for all names
    filename = f"sio_{month}_{year}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=0.75*inch, rightMargin=0.75*inch, topMargin=0.2*inch, bottomMargin=0.5*inch)
    
    # Create a list to hold the elements of the document
    elements = []
    
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'Times-Roman'  # Use a professional font
    styles['Normal'].fontSize = 20
    
    # Loop through each name and generate a page for each
    for name in names:
        # Add the name in the top left after the margin
        name_paragraph = Paragraph(f"<b>Name:</b> <b>{name}</b>", styles['Normal'])
        elements.append(name_paragraph)
        
        # Add some space
        elements.append(Spacer(1, 0.35 * inch))
        
        # Create the table data
        table_data = [['Date', 'Time in', 'Parent Signature', 'Time out', 'Parent Signature']]
        
        # Calculate the number of days in the month
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        
        first_day = datetime(year, month, 1)
        last_day = datetime(next_year, next_month, 1) - timedelta(days=1)
        num_days = last_day.day
        
        # Fill the table with the appropriate dates
        for day in range(1, num_days + 1):
            date = f"{month}/{day}/{year}"
            current_date = datetime(year, month, day)
            day_of_week = current_date.strftime("%A")
            
            if current_date == datetime(2026, 1, 1):
                table_data.append([date, "Happy", "New", "Year", "!!"])
            elif current_date == datetime(2026, 4, 16):
                table_data.append([date, " Spring Break ", " School Closed ", " Spring Break ", " School Closed "])
            elif current_date == datetime(2026, 4, 17):
                table_data.append([date, " Spring Break ", " School Closed ", " Spring Break ", " School Closed "])
            elif current_date == datetime(2025, 12, 26):
                table_data.append([date, "School reopens", "Friday 01/02/2026", "Merry", "Christmas!"])
            elif current_date == datetime(2025, 12, 29):
                table_data.append([date, " - ", " - ", " - ", " - "])
            elif current_date == datetime(2025, 12, 30):
                table_data.append([date, " - ", " - ", " - ", " - "])
            elif current_date == datetime(2025, 12, 31):
                table_data.append([date, " - ", " - ", " - ", " - "])
            elif current_date == datetime(2025, 7, 4):
                table_data.append([date, " - ", " - ", " - ", " - "])
            elif day_of_week == "Saturday" or day_of_week == "Sunday":
                table_data.append([date, day_of_week, day_of_week, day_of_week, day_of_week])
            else:
                table_data.append([date, "", "", "", ""])
        
        # Create the table
        #####Edit row size!!!!!
        row_height = 20.7 # Set your desired row height here
        table = Table(table_data, colWidths=[1.2*inch, 1.2*inch, 1.7*inch, 1.2*inch, 1.7*inch], rowHeights=[row_height]*len(table_data))
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold header font
            ('FONTSIZE', (0, 0), (-1, 0), 12),  # Larger header font size
            ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),  # Body font
            ('FONTSIZE', (0, 1), (-1, -1), 10),  # Body font size
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),  # Center align header
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),  # Center align body (except the date column)
            ('ALIGN', (0, 1), (0, -1), 'CENTER'),  # Center align 'Date' column
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Middle align all cells
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # Add grid lines
        ]))
        
        elements.append(table)
        
        # Add Month and Year at the Bottom-Right Corner
        month_year_paragraph = Paragraph(f"<b>{first_day.strftime('%B')} {year}</b>", styles['Normal'])
        month_year_paragraph.alignment = 2  # 2 means right alignment

        elements.append(Spacer(1, 0.25 * inch))  # Add more space before the footer
        elements.append(month_year_paragraph)
        
        # Add space between pages
        elements.append(PageBreak())  # Ensure each person is on a new page
    
    # Build the PDF document
    doc.build(elements)

    print(f"Sign-in/out sheet for {month}/{year} generated successfully.")

# Generate the sign-in/out sheet for all names in the list
month = 4 # Month
year = 2026  # Year

generate_sign_in_out_sheet(names, month, year)

# If you need to send the document to the printer, you can uncomment this line:
# os.system(f"lp sign_in_out_sheets_{month}_{year}.pdf")  # Sends the PDF to the default printer
