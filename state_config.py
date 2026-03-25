"""
State configuration for this AlabamaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "AL"
STATE_NAME = "Alabama"
APP_NAME = "AlabamaDischargeWatch"
APP_TAGLINE = "Alabama Discharge Monitoring"
DOMAIN = "alabamadischargewatch.org"
DATA_FILE = "al_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@alabamadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 4
