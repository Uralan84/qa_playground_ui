import os

class Links:

    STAGE = "https://release-crm.qa-playground.com" if os.environ["STAGE"] == "release" else "https://dev-crm.qa-playground.com"


    CONTACTS_PAGE = f"{STAGE}/#/contacts"
    CONTACT_CARD_PAGE = f"{STAGE}/#/contacts/create"
    DEALS_PAGE = f"{STAGE}/#/deals"
