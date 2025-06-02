# archivo: main.py

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware



# Cargar modelo entrenado y columnas
model = joblib.load("Modelo2.pkl")  # debes guardarlo antes
columnas = joblib.load("Columnas_Modelo2.pkl")  # también guardas esto

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:8000"] si quieres restringirlo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Definir los campos de entrada
class CampañaInput(BaseModel):
    Age: int
    Income: float
    AdSpend: float
    ClickThroughRate: float
    ConversionRate: float
    WebsiteVisits: int
    PagesPerVisit: float
    TimeOnSite: float
    SocialShares: int
    EmailOpens: int
    EmailClicks: int
    PreviousPurchases: int
    LoyaltyPoints: int
    Gender_Male: int
    CampaignChannel_PPC: int
    CampaignChannel_Referral: int
    CampaignChannel_SEO: int
    CampaignChannel_Social_Media: int
    CampaignType_Consideration: int
    CampaignType_Conversion: int
    CampaignType_Retention: int

@app.post("/predecir")
def predecir(data: CampañaInput):
    df = pd.DataFrame([data.dict()], columns=columnas)
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]
    return {
        "exito": bool(pred),
        "probabilidad_exito": round(prob * 100, 2)
    }

@app.get("/principal", response_class=HTMLResponse)
def principal():
    with open("static/modelo2-vista1.html", "r", encoding="utf-8") as file:
        html = file.read()
    return html

@app.get("/modelo", response_class=HTMLResponse)
def principal():
    with open("static/modelo2-vista2.html", "r", encoding="utf-8") as file:
        html = file.read()
    return html