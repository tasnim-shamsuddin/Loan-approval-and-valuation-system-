from app.loader import load_model
from app.utils import build_applicant_from_dict

cls_path="models\loan_approval_classifier.pkl"
reg_path="models\loan_approval_regressor.pkl"

cls,reg=load_model(cls_path, reg_path)

def run_cli():
    data= {
    'no_of_dependents': 0,
    'education': 1,
    'self_employed': 0,
    'income_annum': 50000,
    'loan_amount': 200000,
    'loan_term': 360,
    'cibil_score': 700,
    'residential_assets_value': 100000,
    'commercial_assets_value': 50000,
    'luxury_assets_value': 20000,
    'bank_asset_value': 150000  
    }

    df=build_applicant_from_dict(data, list(cls.feature_names_in_)


if __name__ == "__main__":
    run_cli()