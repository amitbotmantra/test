
from fpdf import FPDF
import datetime


# class PDF(FPDF):
pdf = FPDF()
# pdf.alias_nb_pages()
pdf.add_page()
# pdf.set_font('Times', '', 8)
# Logo
pdf.image(r'C:\Users\User\Desktop\l2\transparent_image.png', 170, 5, 30)
# Arial bold 15
pdf.set_font('Arial', 'B', 10)
# Move to the right
pdf.cell(80)
# Title
pdf.cell(30, 5, 'Statement Of Account', 0, 0, 'C')
# Line break
pdf.ln(10)
text="amit"
pdf.cell(60, 1, f'From Date:{text}','L')
pdf.cell(80, 1, f'To Date:{text}', 'L')
pdf.cell(0, 1, f'Doctor Name:{text}', 'L')
pdf.ln(5)
pdf.cell(140, 0, f'Doctor Code:{text}', 'L')
pdf.cell(0, 0, f'PAN:{text}','L')
pdf.ln(10)

# Page footer
# # Position at 1.5 cm from bottom
# pdf.set_y(-15)
# # Arial italic 8
# pdf.set_font('Arial', 'I', 8)
# # Page number
# pdf.cell(0, 10, 'Page ' + str(pdf.page_no()) + '/{nb}', 0, 0, 'C')


TABLE_COL_NAMES = ('Center', 'Client\nName', 'Sample\nprocess\ndate', 'Dly Hosp Code', 'Dly Hosp Name', 'Dr payout status', 'Gross', 'TDS', 'Net', 'Payment amount', 'Payment mode', 'Payment Ref', 'Payment Date', 'Clearance status')

TABLE_DATA= (
    ('160000900801', 'Priyanka N', '09-12-2016', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('160000900830', 'Bhumi Bhar', '12-01-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('170000900139', 'Pooja Shah', '25-03-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('170000900177', 'Rashmi Sha', '13-07-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('170000900200', 'Dimpy Shah', '01-04-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('170000900243', 'Megha Shuk', '12-08-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('170000900248', 'Shirneyswa', '28-04-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('170000900281', 'Jinal Kant', '01-05-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('170000900779', 'Hiral Gada', '27-12-2017', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('180000700220', 'Bidya Shah', '10-05-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('180000900010', 'Anjali Sha', '20-01-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('180000900042', 'Ushma Panc', '05-02-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('180000900094', 'Vedika Fat', '03-03-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('180000900112', 'Ankita Jan', '04-03-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('180000900348', 'Sonam Agra', '21-06-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('180000900594', 'Hiral Pate', '07-01-2019', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('180000900617', 'Neerja Sha', '27-12-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('180000900689', 'Komal Nare', '27-12-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('180000900721', 'Hiti Saluj', '29-12-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('180005300053', 'Priyal Pan', '14-04-2018', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('190000900035', 'Parita She', '26-01-2019', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''),
    ('190000900097', 'Puja Malvi', '23-02-2019', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('190000900154', 'Elina Bhar', '11-04-2019', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), 
    ('190000900162', 'Kunjal Pat', '24-03-2019', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), ('190000900232', 'Dipali Par', '04-05-2019', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), ('190000900249', 'Priyanka A', '30-06-2019', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), ('190000900696', 'Aarti Maji', '06-02-2020', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, ''), ('200000900036', 'Neha Brahm', '29-02-2020', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', 
None, ''), ('200000900037', 'Neha Brahm', '29-02-2020', 'Ven06-11708', 'Dr.Sujal Munshi', 'Payment Amount Zero', 0.0, 0.0, 0.0, 0.0, '', '', None, '')
)



spacing=3
line_height = spacing * 5
col_width = pdf.epw / 14  # distribute content evenly

def render_table_header():
    pdf.set_font('Times', 'B', 10)  # enabling bold text
    for col_name in TABLE_COL_NAMES:
        pdf.multi_cell(col_width, line_height,col_name, border=1,align='C',ln=3,max_line_height=pdf.font_size)
    pdf.ln(line_height)
    pdf.set_font(style="")  # disabling bold text

render_table_header()
# for _ in range(10):  # repeat data rows
spacing=3
line_height1 = spacing * 5
for row in TABLE_DATA:
    print(row)
    if pdf.will_page_break(line_height1):
        render_table_header()
    for datum in range(len(row)):
        data_to_insert=row[datum] if row[datum] else ""
        # datum=datum if datum else ""
        datum=datum.strftime("%d/%m/%Y") if type(datum)==datetime.datetime else datum
        data_to_insert=data_to_insert.strftime("%d/%m/%Y") if type(data_to_insert)==datetime.datetime else data_to_insert
        if datum in [2,7,12]:
            pdf.set_font("Times","",6)
            pdf.multi_cell(col_width, line_height1, txt=data_to_insert, border=1,ln=3,max_line_height=pdf.font_size,align='c')
        else:
            pdf.set_font("Times","",8)
            pdf.multi_cell(col_width, line_height1, txt=data_to_insert, border=1,ln=3,max_line_height=pdf.font_size,align='c')
            
    pdf.ln(line_height1)

pdf.output("table_with_headers_on_every_page123.pdf")