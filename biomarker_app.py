# Import library 
import tkinter as tk 
from tkinter import messagebox 
 
# Extended biomarker-disease mapping with details 
biomarker_dict = { 
    "CA-125": { 
        "disease": "Ovarian Cancer", 
        "symptoms": "Abdominal bloating, pelvic pain, frequent urination", 
        "cause": "Uncontrolled growth of ovarian cells", 
        "risk": "Genetic mutations (BRCA1/2), family history, age", 
        "treatment": "Surgery, chemotherapy, targeted therapy", 
        "pathways": { 
            "Cell cycle regulation": "Uncontrolled division of ovarian epithelial cells.", 
            "Apoptosis signaling": "Defective cell death pathways allow cancer 
progression.", 
            "Angiogenesis pathway": "Promotes tumor growth by forming new blood 
vessels." 
        }, 
        "drugs": { 
            "Carboplatin": "Platinum-based chemotherapy targeting ovarian cancer.", 
            "Paclitaxel": "Inhibits cell division by stabilizing microtubules.", 
            "Bevacizumab": "Monoclonal antibody inhibiting tumor angiogenesis." 
        }, 
        "publications": [ 
            {"name": "CA-125 as a Biomarker in Ovarian Cancer", "id": 
"PMID:456789", "link": "https://pubmed.ncbi.nlm.nih.gov/456789"}, 
            {"name": "Role of Angiogenesis in Ovarian Tumors", "id": 
"PMID:567890", "link": "https://pubmed.ncbi.nlm.nih.gov/567890"} 
        ] 
    }, 
    "AFP": { 
        "disease": "Liver Cancer (Hepatocellular Carcinoma)", 
        "symptoms": "Jaundice, abdominal swelling, weight loss", 
        "cause": "Chronic hepatitis B/C, cirrhosis", 
        "risk": "Alcohol abuse, viral infections, fatty liver disease", 
        "treatment": "Surgical resection, liver transplant, targeted therapy", 
        "pathways": { 
            "Wnt/β-catenin pathway": "Regulates tumor growth in hepatocellular 
carcinoma.", 
            "PI3K/AKT pathway": "Promotes survival and proliferation of liver cancer 
cells.", 
            "Angiogenesis": "Supports tumor vascularization for rapid growth." 
        }, 
        "drugs": { 
            "Sorafenib": "Tyrosine kinase inhibitor targeting angiogenesis in liver 
cancer.", 
            "Lenvatinib": "Blocks VEGF and FGF receptors to suppress tumor 
growth.", 
            "Nivolumab": "Immunotherapy drug enhancing T-cell mediated response." 
        }, 
        "publications": [ 
            {"name": "AFP as a Biomarker in Liver Cancer", "id": "PMID:678901", 
"link": "https://pubmed.ncbi.nlm.nih.gov/678901"}, 
            {"name": "Targeted Therapy in HCC", "id": "PMID:789012", "link": 
"https://pubmed.ncbi.nlm.nih.gov/789012"} 
        ] 
    }, 
    "HbA1c": { 
        "disease": "Diabetes Mellitus", 
        "symptoms": "Increased thirst, frequent urination, fatigue, blurred vision", 
        "cause": "Insulin resistance or low insulin production", 
        "risk": "Obesity, sedentary lifestyle, family history", 
        "treatment": "Insulin therapy, oral hypoglycemic drugs, diet and exercise", 
        "pathways": { 
            "Insulin signaling pathway": "Regulates glucose uptake and metabolism.", 
            "AGE-RAGE pathway": "High glucose leads to advanced glycation end 
products causing complications.", 
            "Glucose metabolism pathway": "Disrupted glucose regulation in diabetes." 
        }, 
        "drugs": { 
            "Metformin": "Improves insulin sensitivity and lowers glucose 
production.", 
            "Insulin": "Replaces or supplements body’s own insulin.", 
            "SGLT2 inhibitors": "Increase glucose excretion via urine." 
        }, 
        "publications": [ 
            {"name": "HbA1c as a Diagnostic Biomarker", "id": "PMID:890123", 
"link": "https://pubmed.ncbi.nlm.nih.gov/890123"}, 
            {"name": "Complications of Diabetes and HbA1c", "id": "PMID:901234", 
"link": "https://pubmed.ncbi.nlm.nih.gov/901234"} 
        ] 
    }, 
    "Troponin": { 
        "disease": "Heart Attack (Myocardial Infarction)", 
        "symptoms": "Chest pain, shortness of breath, fatigue", 
        "cause": "Blocked coronary artery due to plaque", 
        "risk": "Smoking, high cholesterol, high blood pressure", 
        "treatment": "Angioplasty, blood thinners, lifestyle changes", 
        "pathways": { 
            "Cardiac muscle contraction pathway": "Regulates heart muscle contraction 
through calcium ion signaling.", 
            "Oxidative stress pathway": "Overproduction of ROS damages cardiac 
tissue during heart attack.", 
            "Calcium signaling pathway": "Controls heart rhythm and contraction 
strength.", 
            "Inflammatory response pathway": "Immune system response leads to 
tissue injury and repair.", 
            "Mitochondrial dysfunction pathway": "Impaired ATP production weakens 
cardiac cells." 
        }, 
        "drugs": { 
            "Aspirin": "Prevents platelet aggregation and reduces clot formation.", 
            "Clopidogrel": "Inhibits ADP-induced platelet aggregation to prevent artery 
blockage.", 
            "Atorvastatin": "Lowers cholesterol and stabilizes arterial plaque.", 
            "Heparin": "Prevents blood clot formation by activating antithrombin.", 
            "Beta-blockers": "Reduce heart rate and blood pressure by blocking 
adrenaline effects." 
        }, 
        "publications": [ 
            {"name": "Role of Troponin in Myocardial Infarction", "id": 
"PMID:123456", "link": "https://pubmed.ncbi.nlm.nih.gov/123456"}, 
            {"name": "Calcium Pathways in Cardiac Arrest", "id": "PMID:234567", 
"link": "https://pubmed.ncbi.nlm.nih.gov/234567"}, 
            {"name": "Drug Therapy for Acute Heart Attack", "id": "PMID:345678", 
"link": "https://pubmed.ncbi.nlm.nih.gov/345678"} 
        ] 
    }, 
"PSA": { 
        "disease": "Prostate Cancer", 
        "symptoms": "Difficulty urinating, pelvic pain, blood in urine", 
        "cause": "Abnormal growth of prostate cells", 
        "risk": "Age, family history, hormonal imbalance", 
        "treatment": "Surgery, radiation therapy, hormone therapy", 
        "pathways": { 
            "Androgen receptor signaling": "Drives growth of prostate cancer cells.", 
            "Cell proliferation pathway": "Uncontrolled division of prostate cells.", 
            "Apoptosis inhibition": "Cancer cells evade programmed cell death." 
        }, 
        "drugs": { 
            "Leuprolide": "Hormone therapy reducing testosterone levels.", 
            "Bicalutamide": "Blocks androgen receptors in prostate cancer.", 
            "Docetaxel": "Chemotherapy drug disrupting cell division." 
        }, 
        "publications": [ 
            {"name": "PSA as a Screening Biomarker", "id": "PMID:912345", "link": 
"https://pubmed.ncbi.nlm.nih.gov/912345"}, 
            {"name": "Hormonal Pathways in Prostate Cancer", "id": "PMID:923456", 
"link": "https://pubmed.ncbi.nlm.nih.gov/923456"} 
        ] 
    } 
} 
 
# --- FUNCTIONS --- 
def show_pathways(details): 
    win = tk.Toplevel(root) 
    win.title("Pathways") 
    win.geometry("600x400") 
    win.config(bg="white") 
 
    tk.Label(win, text=f"Pathways for {details['disease']}", font=("Arial", 14, 
"bold"), fg="darkblue", bg="white").pack(pady=10) 
 
    for pathway, summary in details["pathways"].items(): 
        frame = tk.Frame(win, bg="white", bd=1, relief="solid") 
        frame.pack(padx=10, pady=5, fill="x") 
 
        tk.Label(frame, text=f"• {pathway}", font=("Arial", 12, "bold"), 
fg="darkgreen", bg="white").pack(anchor="w", padx=10, pady=2) 
        tk.Label(frame, text=summary, font=("Arial", 11), bg="white", 
wraplength=500, justify="left").pack(anchor="w", padx=20, pady=2) 
 
        # Network button 
        btn = tk.Button(frame, text="Show Network", bg="#4CAF50", fg="white", 
command=lambda p=pathway: show_network(p)) 
        btn.pack(anchor="e", padx=10, pady=5) 
 
def show_network(pathway): 
    nw = tk.Toplevel(root) 
    nw.title(f"Network - {pathway}") 
    nw.geometry("400x300") 
    nw.config(bg="white") 
    tk.Label(nw, text=f"Network View for {pathway}", font=("Arial", 14, "bold"), 
fg="purple", bg="white").pack(pady=10) 
    tk.Label(nw, text="[Simulated Pathway Network Diagram Here]", 
font=("Arial", 12), bg="white", fg="gray").pack(pady=20) 
 
def show_drugs(details): 
    win = tk.Toplevel(root) 
    win.title("Drugs") 
    win.geometry("600x400") 
    win.config(bg="white") 
 
    tk.Label(win, text=f"Drugs for {details['disease']}", font=("Arial", 14, "bold"), 
fg="darkred", bg="white").pack(pady=10) 
 
    for drug, summary in details["drugs"].items(): 
        frame = tk.Frame(win, bg="white", bd=1, relief="solid") 
        frame.pack(padx=10, pady=5, fill="x") 
 
        tk.Label(frame, text=f"• {drug}", font=("Arial", 12, "bold"), fg="blue", 
bg="white").pack(anchor="w", padx=10, pady=2) 
        tk.Label(frame, text=summary, font=("Arial", 11), bg="white", 
wraplength=500, justify="left").pack(anchor="w", padx=20, pady=2) 
 
def show_publications(details): 
    win = tk.Toplevel(root) 
    win.title("Publications") 
    win.geometry("650x400") 
    win.config(bg="white") 
 
    tk.Label(win, text=f"Publications for {details['disease']}", font=("Arial", 14, 
"bold"), fg="brown", bg="white").pack(pady=10) 
 
    for pub in details["publications"]: 
        frame = tk.Frame(win, bg="white", bd=1, relief="solid") 
        frame.pack(padx=10, pady=5, fill="x") 
 
        tk.Label(frame, text=f"• {pub['name']}", font=("Arial", 12, "bold"), 
fg="darkblue", bg="white").pack(anchor="w", padx=10, pady=2) 
        tk.Label(frame, text=f"ID: {pub['id']}", font=("Arial", 11), 
bg="white").pack(anchor="w", padx=20, pady=2) 
        link = tk.Label(frame, text=pub["link"], font=("Arial", 11, "underline"), 
fg="blue", bg="white", cursor="hand2") 
        link.pack(anchor="w", padx=20, pady=2) 
        link.bind("<Button-1>", lambda e, url=pub["link"]: open_link(url)) 
 
import webbrowser 
def open_link(url): 
    webbrowser.open(url) 
 
def identify_disease(): 
    biomarker = entry.get().strip() 
    details = biomarker_dict.get(biomarker, None) 
 
    if details: 
        detail_win = tk.Toplevel(root) 
        detail_win.title("Disease Information") 
        detail_win.geometry("550x350") 
        detail_win.config(bg="#e8f5e9") 
 
        frame = tk.Frame(detail_win, bg="white", bd=2, relief="groove") 
        frame.pack(padx=20, pady=20, fill="both", expand=True) 
 
        tk.Label(frame, text=f"Disease: {details['disease']}",  
                 font=("Arial", 14, "bold"), bg="white", fg="darkgreen").pack(pady=10, 
anchor="w") 
        tk.Label(frame, text=f"Symptoms: {details['symptoms']}", font=("Arial", 12), 
bg="white").pack(anchor="w", padx=20, pady=5) 
        tk.Label(frame, text=f"Cause: {details['cause']}", font=("Arial", 12), 
bg="white").pack(anchor="w", padx=20, pady=5) 
        tk.Label(frame, text=f"Risk Factors: {details['risk']}", font=("Arial", 12), 
bg="white").pack(anchor="w", padx=20, pady=5) 
        tk.Label(frame, text=f"Treatment: {details['treatment']}", font=("Arial", 12), 
bg="white").pack(anchor="w", padx=20, pady=5) 
 
        # New buttons 
        tk.Button(frame, text="Pathways", command=lambda: 
show_pathways(details), bg="#81C784", fg="white", font=("Arial", 12, 
"bold")).pack(side="left", padx=10, pady=15) 
        tk.Button(frame, text="Drugs", command=lambda: show_drugs(details), 
bg="#64B5F6", fg="white", font=("Arial", 12, "bold")).pack(side="left", padx=10, 
pady=15) 
        tk.Button(frame, text="Publications", command=lambda: 
show_publications(details), bg="#BA68C8", fg="white", font=("Arial", 12, 
"bold")).pack(side="left", padx=10, pady=15) 
 
    else: 
        messagebox.showerror("Error", "Biomarker not found in database.") 
 
# --- MAIN GUI --- 
root = tk.Tk() 
root.title("Disease Identifier from Biomarker") 
root.geometry("450x250") 
root.config(bg="#e8f5e9") 
 
title = tk.Label(root, text="Biomarker → Disease Identifier", font=("Arial", 16, 
"bold"), bg="#e8f5e9", fg="darkgreen") 
title.pack(pady=10) 
 
frame = tk.Frame(root, bg="white", bd=2, relief="groove") 
frame.pack(pady=20, padx=20, fill="x") 
tk.Label(frame, text="Enter Biomarker:", font=("Arial", 12), 
bg="white").grid(row=0, column=0, padx=5, pady=10) 
entry = tk.Entry(frame, font=("Arial", 12), width=20) 
entry.grid(row=0, column=1, padx=5) 
btn = tk.Button(root, text="Identify Disease", command=identify_disease, 
font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", relief="raised") 
btn.pack(pady=15) 
root.mainloop()