from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os
styles = getSampleStyleSheet()

def generate_report(data, bowl):

    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = "reports/IPL_Report.pdf"

    doc = SimpleDocTemplate(filename)

    elements = []

    elements.append(
        Paragraph("IPL Analysis Dashboard Report", styles["Title"])
    )

    elements.append(
        Paragraph(
            f"Generated on : {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1,20))

    elements.append(
        Paragraph("<b>Dataset Summary</b>", styles["Heading2"])
    )

    elements.append(
        Paragraph(f"Batting Records : {len(data)}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Bowling Records : {len(bowl)}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Batting Columns : {len(data.columns)}", styles["BodyText"])
    )

    elements.append(
        Paragraph(f"Bowling Columns : {len(bowl.columns)}", styles["BodyText"])
    )

    elements.append(Spacer(1,15))

    elements.append(
        Paragraph("<b>Batting Analysis</b>", styles["Heading2"])
    )

    top_run = data.loc[data["Runs"].idxmax()]

    elements.append(
        Paragraph(
            f"Highest Run Scorer : {top_run['Player']} ({top_run['Runs']} Runs)",
            styles["BodyText"]
        )
    )

    best_avg = data.loc[data["Avg"].idxmax()]

    elements.append(
        Paragraph(
            f"Highest Average : {best_avg['Player']} ({best_avg['Avg']})",
            styles["BodyText"]
        )
    )

    best_sr = data.loc[data["SR"].idxmax()]

    elements.append(
        Paragraph(
            f"Highest Strike Rate : {best_sr['Player']} ({best_sr['SR']})",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1,15))

    elements.append(
        Paragraph("<b>Bowling Analysis</b>", styles["Heading2"])
    )

    most_wkts = bowl.loc[bowl["Wkts"].idxmax()]

    elements.append(
        Paragraph(
            f"Most Wickets : {most_wkts['Player']} ({most_wkts['Wkts']} Wickets)",
            styles["BodyText"]
        )
    )

    best_econ = bowl.loc[bowl["Econ"].idxmin()]

    elements.append(
        Paragraph(
            f"Best Economy : {best_econ['Player']} ({best_econ['Econ']})",
            styles["BodyText"]
        )
    )

    elements.append(Spacer(1,15))

    elements.append(
        Paragraph("<b>Key Insights</b>", styles["Heading2"])
    )

    insights = [
        f"The leading run scorer is {top_run['Player']}.",
        f"{most_wkts['Player']} has taken the highest number of wickets.",
        f"{best_sr['Player']} has the highest strike rate.",
        f"{best_econ['Player']} has the best bowling economy."
    ]

    for i in insights:
        elements.append(
            Paragraph("• " + i, styles["BodyText"])
        )

    doc.build(elements)

    return filename