from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import boto3
import json
import io

def lambda_handler(event, context):
    group_name = "grupo10"

    body = json.loads(event.get('body', '{}'))
    user_info = body.get('user_info', {})
    stock_info = body.get('stock_info', {})

    transaction_id = stock_info.get('id', None)
    
    pdf_data = generate_pdf(group_name, user_info, stock_info)
    file_name = f'{transaction_id}.pdf'
    #file_name = "john@example.com_AAPL_GOOGL.pdf"
    upload_pdf_to_s3(pdf_data, file_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Successfully uploaded PDF to S3 at: https://grupo10-invoice-bucket.s3.amazonaws.com/{file_name}')
    }


def generate_pdf(group_name, user_info, stock_info):
    buffer = io.BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    data = [
        ["Grupo:", group_name],
        ["Usuario:", user_info["name"]],
        ["Email:", user_info["email"]],
        ["id:", stock_info["id"]],
        ["stock:", stock_info['symbol']],
        ["Comprado:", stock_info['quantity']],
        ["Precio:", stock_info['price']]
    ]

    #for stock in stock_info:
    #    data.append([f"Stock {stock['symbol']}", f"Comprado: {stock['quantity']}", f"Precio: {stock['price']}"])

    table = Table(data)

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

    buffer.seek(0)
    return buffer.read()

def upload_pdf_to_s3(pdf_data, pdf_name):
    s3 = boto3.client('s3')

    try:
        s3.put_object(
            Bucket="grupo10-invoice-bucket",
            Key=pdf_name,  # Reemplaza con el nombre deseado del archivo en S3
            Body=pdf_data,
            ContentType="application/pdf"
        )
        print("Successfully uploaded PDF to grupo10-invoice-bucket.")
    except Exception as e:
        print(f"Could not upload to S3: {e}")
