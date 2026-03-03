"""
HC Agent Renewal — Configuration
"""
from datetime import date

# Monday.com board
MONDAY_BOARD_ID = 359922413
MONDAY_TERMINATED_GROUP_ID = "new_group79397"

# DFPR (data.illinois.gov)
DFPR_DATASET_ID = "pzzh-kp68"
DFPR_BUSINESS_DBA = "Rivers Realty"

# License renewal cutoff: agents with expiration AFTER this date have renewed
RENEWAL_CUTOFF = date(2026, 4, 30)

# Email
EMAIL_RECIPIENTS = ["dj@kalerealty.com", "rea@kalerealty.com"]
ENTITY_NAME = "HC"

# Google Sheets — agent email list
GOOGLE_SHEET_ID = "1npw5b1MKI7C2Xkg6qrE7NR6x378wxO-tsolKNJXDxn8"
