#crosscheck
#def jcompare_dictionaries(iddict, formdict):
from datetime import datetime

def parse_date(date_string):
    # Try parsing the date in different formats
    for fmt in ("%d %b %Y", "%m/%d/%y", "%Y/%m/%d"):
        try:
            # Parse the date and then format it as a string
            dt = datetime.strptime(date_string, fmt)
            return dt.strftime("%Y-%m-%d")  # Format the output as YYYY-MM-DD
        except ValueError:
            continue
    return None

def jcompare_dict_values(iddict, formdict):
    mismatches = []

    if iddict.get('FIRST_NAME').lower() != formdict.get('Given and middle names (as shown in passport)_a').lower():
        mismatches.append(f"First Name Mismatch: '{iddict.get('FIRST_NAME')}' vs '{formdict.get('Given and middle names (as shown in passport)_a')}'")

    if iddict.get('LAST_NAME').lower() != formdict.get('Surname (as shown in passport)_a').lower():
        mismatches.append(f"Last Name Mismatch: '{iddict.get('LAST_NAME')}' vs '{formdict.get('Surname (as shown in passport)_a')}'")
    
    if parse_date(iddict.get('DATE_OF_BIRTH')) != parse_date(formdict.get('Date of birth_a')):
        mismatches.append(f"Date of Birth Mismatch: '{iddict.get('DATE_OF_BIRTH')}' vs '{formdict.get('Date of birth_a')}'")

    if parse_date(iddict.get('DATE_OF_ISSUE')) != parse_date(formdict.get('Date of issue_a')):
        mismatches.append(f"Date of Issue Mismatch: '{iddict.get('DATE_OF_ISSUE')}' vs '{formdict.get('Date of issue_a')}'")

    if parse_date(iddict.get('EXPIRATION_DATE')) != parse_date(formdict.get('Date of expiry_a')):
        mismatches.append(f"Date of Expiry Mismatch: '{iddict.get('EXPIRATION_DATE')}' vs '{formdict.get('Date of expiry_a')}'")

    if iddict.get('DOCUMENT_NUMBER') != formdict.get('Passport No._a'):
        mismatches.append(f"Passport No. Mismatch: '{iddict.get('DOCUMENT_NUMBER')}' vs '{formdict.get('Passport No._a')}'")
    
    # Return appropriate message
    nomis =['ID matches information in the application form']
    if mismatches:
        return mismatches
    else:
        return nomis
    

def kcompare_dict_values(iddict, formdict):
    mismatches = []

    if 'OF Given Names_a' in formdict:
        if iddict.get('FIRST_NAME').lower() != formdict.get('OF Given Names_b').lower():
            mismatches.append(f"First Name Mismatch: '{iddict.get('FIRST_NAME')}' vs '{formdict.get('OF Given Names_b')}'")
    else:
        mismatches.append(f"Given Name is not detected in VAF")

    if 'NO Family Name_a' in formdict:
        if iddict.get('LAST_NAME').lower() != formdict.get('NO Family Name_b').lower():
            mismatches.append(f"Last Name Mismatch: '{iddict.get('LAST_NAME')}' vs '{formdict.get('NO Family Name_b')}'")
    else:
        mismatches.append(f"Last Name is not detected in VAF")
        
    if parse_date(iddict.get('DATE_OF_BIRTH')) != parse_date(formdict.get('1.4 Date of Birth (yyyy/mm/dd)_b')):
        mismatches.append(f"Date of Birth Mismatch: '{iddict.get('DATE_OF_BIRTH')}' vs '{formdict.get('1.4 Date of Birth (yyyy/mm/dd)_b')}'")

    if parse_date(iddict.get('DATE_OF_ISSUE')) != parse_date(formdict.get('Date of issue_a')):
        mismatches.append(f"Date of Issue Mismatch: '{iddict.get('DATE_OF_ISSUE')}' vs '{formdict.get('3.5 Date of Issue_a')}'")

    if parse_date(iddict.get('EXPIRATION_DATE')) != parse_date(formdict.get('3.6 Date Of Expiry_a')):
        mismatches.append(f"Date of Expiry Mismatch: '{iddict.get('EXPIRATION_DATE')}' vs '{formdict.get('3.6 Date Of Expiry_a')}'")

    if iddict.get('DOCUMENT_NUMBER') != formdict.get('Passport No._a'):
        mismatches.append(f"Passport No. Mismatch: '{iddict.get('DOCUMENT_NUMBER')}' vs '{formdict.get('3.2 Passport No._a')}'")
    
    # Return appropriate message
    nomis =['ID matches information in the application form']
    if mismatches:
        return mismatches
    else:
        return nomis