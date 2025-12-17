from fpdf import FPDF


pdf = FPDF()


def main():
    name = input("Name: ")
    pdf = FPDF(orientation = "P",format ="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 45)
    pdf.cell(0, 70, "CS50 Shirtificate",align="C")
    pdf.image("shirtificate.png", x=0, y=70)
    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255,255,255)
    pdf.cell(-190, 250,name + " took CS50",align="C")
    pdf.output("shirtificate.pdf")



main()


