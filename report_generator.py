from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        """Header for the PDF document."""
        self.set_font("Arial", "B", 16)
        self.cell(200, 10, "Financial Risk Analysis Report", ln=True, align="C")
        self.ln(10)

    def add_section(self, title, content):
        """Add a section to the PDF report."""
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_pdf_report(output_path, std_dev, beta, treynor_ratio, var_95):
    """Generate a PDF report summarizing the risk analysis."""
    pdf = PDFReport()
    pdf.add_page()

    pdf.add_section("Standard Deviation (Volatility)", f"{std_dev:.4f}")
    pdf.add_section("Beta (Market Risk)", f"{beta:.4f}")
    pdf.add_section("Treynor Ratio", f"{treynor_ratio:.4f}")
    pdf.add_section("Value at Risk (95%)", f"{var_95:.4f}")

    pdf.output(output_path)
    print(f"PDF Report saved: {output_path}")

if __name__ == "__main__":
    generate_pdf_report("reports/risk_report.pdf", 0.02, 1.2, 0.05, -0.03)
