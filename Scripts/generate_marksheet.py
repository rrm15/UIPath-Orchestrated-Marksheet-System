from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from datetime import datetime

def generate_marksheet(name, roll_number, dob, semester, year, department,
                       subject1, mark1, grade1,
                       subject2, mark2, grade2,
                       subject3, mark3, grade3,
                       subject4, mark4, grade4,
                       subject5, mark5, grade5,
                       gpa, institution_name, output_path):
    """
    Generate a professional marksheet PDF with student details, marks, grades, and GPA.
    
    Parameters:
        19 parameters including student details, 5 subjects with marks/grades, GPA, institution name, and output path
    
    Returns:
        str: Path to the generated PDF file
    """
    try:
        # Create PDF document
        doc = SimpleDocTemplate(output_path, pagesize=A4,
                              topMargin=0.5*inch, bottomMargin=0.5*inch,
                              leftMargin=0.75*inch, rightMargin=0.75*inch)
        story = []
        styles = getSampleStyleSheet()
        
        # Header
        header_style = ParagraphStyle('CustomHeader', 
                                     parent=styles['Heading1'], 
                                     alignment=TA_CENTER, 
                                     fontSize=18, 
                                     textColor=colors.HexColor('#1a237e'),
                                     spaceAfter=6,
                                     fontName='Helvetica-Bold')
        
        title_style = ParagraphStyle('TitleStyle', 
                                    parent=styles['Heading2'], 
                                    alignment=TA_CENTER, 
                                    fontSize=14,
                                    textColor=colors.HexColor('#283593'),
                                    spaceAfter=12,
                                    fontName='Helvetica-Bold')
        
        story.append(Paragraph(institution_name, header_style))
        story.append(Paragraph("PROVISIONAL MARKSHEET", title_style))
        story.append(Spacer(1, 0.3*inch))
        
        # Student Details Section
        student_data = [
            ["Name:", str(name), "Roll Number:", str(roll_number)],
            ["Date of Birth:", str(dob), "Semester:", str(semester)],
            ["Year:", str(year), "Department:", str(department)]
        ]
        
        student_table = Table(student_data, colWidths=[1.5*inch, 2.5*inch, 1.5*inch, 2*inch])
        student_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTNAME', (3, 0), (3, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(student_table)
        story.append(Spacer(1, 0.3*inch))
        
        # Marks Table
        marks_data = [
            ["S.No", "Subject Name", "Marks Obtained", "Grade"],
            ["1", str(subject1), str(mark1), str(grade1)],
            ["2", str(subject2), str(mark2), str(grade2)],
            ["3", str(subject3), str(mark3), str(grade3)],
            ["4", str(subject4), str(mark4), str(grade4)],
            ["5", str(subject5), str(mark5), str(grade5)]
        ]
        
        marks_table = Table(marks_data, colWidths=[0.8*inch, 3.5*inch, 1.5*inch, 1*inch])
        marks_table.setStyle(TableStyle([
            # Header row styling
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3f51b5')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('TOPPADDING', (0, 0), (-1, 0), 12),
            
            # Data rows styling
            ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f5f5')),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#9e9e9e')),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(marks_table)
        story.append(Spacer(1, 0.3*inch))
        
        # GPA Section
        gpa_data = [["Grade Point Average (GPA):", f"{float(gpa):.2f}/10.00"]]
        gpa_table = Table(gpa_data, colWidths=[4*inch, 2.8*inch])
        gpa_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'CENTER'),
            ('BOX', (0, 0), (-1, -1), 1.5, colors.HexColor('#3f51b5')),
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#e8eaf6')),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        story.append(gpa_table)
        story.append(Spacer(1, 0.5*inch))
        
        # Grade Scale Reference (small text)
        grade_scale = Paragraph(
            "<font size=8>Grade Scale: A(90-100) | B(80-89) | C(70-79) | D(60-69) | E(50-59) | F(Below 50)</font>",
            styles['Normal']
        )
        story.append(grade_scale)
        story.append(Spacer(1, 0.3*inch))
        
        # Footer
        footer_data = [
            [f"Date: {datetime.now().strftime('%d-%m-%Y')}", "Controller of Examinations\n___________________"]
        ]
        footer_table = Table(footer_data, colWidths=[3.4*inch, 3.4*inch])
        footer_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('ALIGN', (0, 0), (0, 0), 'LEFT'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
        ]))
        story.append(footer_table)
        
        # Build PDF
        doc.build(story)
        print(f"PDF generated successfully: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"Error generating PDF: {str(e)}")
        raise

# Command-line execution
if __name__ == "__main__":
    import sys
    
    # Check if run with arguments (from UiPath) or standalone test
    if len(sys.argv) > 1:
        # Called with command-line arguments from UiPath
        if len(sys.argv) != 25:  # Script name + 24 parameters
            print(f"Error: Expected 24 arguments, got {len(sys.argv)-1}")
            print("Usage: python generate_marksheet.py <name> <roll_number> <dob> <semester> <year> <department> <subject1> <mark1> <grade1> ... <gpa> <institution_name> <output_path>")
            sys.exit(1)
        
        # Extract arguments (sys.argv[0] is script name, so start from 1)
        name = sys.argv[1]
        roll_number = sys.argv[2]
        dob = sys.argv[3]
        semester = sys.argv[4]
        year = sys.argv[5]
        department = sys.argv[6]
        subject1 = sys.argv[7]
        mark1 = int(sys.argv[8])
        grade1 = sys.argv[9]
        subject2 = sys.argv[10]
        mark2 = int(sys.argv[11])
        grade2 = sys.argv[12]
        subject3 = sys.argv[13]
        mark3 = int(sys.argv[14])
        grade3 = sys.argv[15]
        subject4 = sys.argv[16]
        mark4 = int(sys.argv[17])
        grade4 = sys.argv[18]
        subject5 = sys.argv[19]
        mark5 = int(sys.argv[20])
        grade5 = sys.argv[21]
        gpa = float(sys.argv[22])
        institution_name = sys.argv[23]
        output_path = sys.argv[24]
        
        # Generate the marksheet
        generate_marksheet(
            name, roll_number, dob, semester, year, department,
            subject1, mark1, grade1,
            subject2, mark2, grade2,
            subject3, mark3, grade3,
            subject4, mark4, grade4,
            subject5, mark5, grade5,
            gpa, institution_name, output_path
        )
    else:
        # Standalone test mode (no arguments)
        print("Running in test mode...")
        test_output = "test_marksheet.pdf"
        generate_marksheet(
            "John Doe", "2024001", "01-01-2000", "Fall 2024", "2024", "Computer Science",
            "Mathematics", 95, "A",
            "Physics", 88, "B",
            "Chemistry", 82, "B",
            "English", 75, "C",
            "Programming", 92, "A",
            9.0, "ABC University", test_output
        )
