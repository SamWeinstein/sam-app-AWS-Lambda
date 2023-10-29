from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import boto3

def generate_pdf(group_name, user_info, stock_info):
    pdf_path = f"{group_name}_boleta.pdf"

    pdf = SimpleDocTemplate(
        pdf_path,
        pagesize=letter
    )

    # Datos para la tabla
    data = [
        ["Grupo:", group_name],
        ["Usuario:", user_info["name"]],
        ["Email:", user_info["email"]],
    ]

    for stock in stock_info:
        data.append([f"Stock {stock['symbol']}", f"Comprado: {stock['quantity']}", f"Precio: {stock['price']}"])

    # Crear tabla
    table = Table(data)

    # Estilo de tabla
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements = []
    elements.append(table)
    pdf.build(elements)

    return pdf_path

# Ejemplo de uso
#user_info = {"name": "John Doe", "email": "john@example.com"}
#stock_info = [{"symbol": "AAPL", "quantity": 10, "price": 150}, {"symbol": "GOOGL", "quantity": 5, "price": 2000}]

#generated_pdf_path = generate_pdf("Grupo10", user_info, stock_info)


def upload_pdf_to_s3(pdf_path):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(pdf_path, "grupo10-invoice-bucket", pdf_path)
        print(f"Successfully uploaded {pdf_path} to grupo10-invoice-bucket.")
    except Exception as e:
        print(f"Could not upload to S3: {e}")

# Ejemplo de uso

#upload_pdf_to_s3(generated_pdf_path)