from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, PageBreak
from reportlab.lib.units import inch
from datetime import datetime, timedelta
import os  # Added to use os.system() to send to the printer

# Add list of names here
names = []


def generate_sign_in_out_sheet(names, month, year):
    filename = f"sio_{month}_{year}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=0.75*inch, rightMargin=0.75*inch, topMargin=0.2*inch, bottomMargin=0.5*inch)
    elements = []
    
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'Times-Roman'  
    styles['Normal'].fontSize = 20
    
    # Loop through each name and generate a page for each
    for name in names:
        name_paragraph = Paragraph(f"<b>Name:</b> <b>{name}</b>", styles['Normal'])
        elements.append(name_paragraph)
        
        elements.append(Spacer(1, 0.35 * inch))
        
        table_data = [['Date', 'Time in', 'Parent Signature', 'Time out', 'Parent Signature']]
        
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
        row_height = 20.7 # Set  desired row height here
        table = Table(table_data, colWidths=[1.2*inch, 1.2*inch, 1.7*inch, 1.2*inch, 1.7*inch], rowHeights=[row_height]*len(table_data))
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
            ('FONTSIZE', (0, 0), (-1, 0), 12), 
            ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'), 
            ('FONTSIZE', (0, 1), (-1, -1), 10), 
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'), 
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'), 
            ('ALIGN', (0, 1), (0, -1), 'CENTER'),  
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  
        ]))
        
        elements.append(table)
        
     
        month_year_paragraph = Paragraph(f"<b>{first_day.strftime('%B')} {year}</b>", styles['Normal'])
        month_year_paragraph.alignment = 2  

        elements.append(Spacer(1, 0.25 * inch))  
        elements.append(month_year_paragraph)
        
        # Add space between pages
        elements.append(PageBreak())  # each person is on a new page
    
    #build the PDF document
    doc.build(elements)

    print(f"Sign-in/out sheet for {month}/{year} generated successfully.")


month = 4
year = 2026  

generate_sign_in_out_sheet(names, month, year)

