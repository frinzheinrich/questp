# error processing
import re

data_dict = {
    "Given Name": "John",
    "Last Name": "Doe",
    "Age": 30,
    "Date of Birth": "15 Sep 1993",
    "Gender": "Male",
    "Place of Issue": "Manila",
    "Issuing Authority": "DFAManila",
    "Passport": "Philippines",
    "Passport_number": "123456789",
    "Country of Birth": "Philippines",
    "Date of Issue": "10 Nov 2023",
    "Date of Expiry": "10 Nov 2028",
    "Cellphone Number": "09345678900",
    "Email": "jd@email.com",
    "Arrival": "20 Dec 2024",
    "Residential Address": "Ateneo",
    "Job Description": "Worker",
    "Employer": "Emp",
    "Marital Status": "Married",
    "Intended Stay": "17 days",
    "Citizenship": "Filipino"
}


errors = []
VALID_MS=["Married", "Single","Divorced","Widowed"]
VALID_CITIZENSHIPS = ["Japanese","Filipino"]
VALID_GENDERS = {"male", "female", "m", "f"}
VALID_COUNTRIES = {"Japan","Philippines"}

def is_valid_email(email: str) -> bool:
    if '@' not in email or email.count('@') != 1:
        errors.append(f"Invalid email address: {email}. It must contain exactly one '@' symbol.")
        return False
    return True

def is_valid_citizenship(citizenship: str) -> bool:
    if citizenship not in VALID_CITIZENSHIPS:
        errors.append(f"Invalid citizenship: {citizenship}")
        return False
    return True

def is_valid_ms(ms: str) -> bool:
    if ms not in VALID_MS:
        errors.append(f"Invalid marital status: {ms}")
        return False
    return True

def is_valid_countrybirth(countrybirth: str) -> bool:
    if countrybirth not in VALID_COUNTRIES:
        errors.append(f"Invalid country of birth: {countrybirth}")
        return False
    return True

def is_valid_passport(passport: str) -> bool:
    if passport not in VALID_COUNTRIES:
        errors.append(f"Invalid country of passport: {passport}")
        return False
    return True

def is_valid_age(age: int) -> bool:
    if not (0 <= age <= 120):  # Valid age range
        errors.append(f"Invalid age: {age}")
        return False
    return True

def is_valid_passport_number(passport_number: str) -> bool:
    if len(passport_number) != 9 or not passport_number.isalnum():
        errors.append(f"Invalid passport number: {passport_number}")
        return False
    return True

def is_valid_address(address: str) -> bool:
    if not address.isalpha():
        errors.append(f"Invalid address: {address}. It must contain only letters.")
        return False
    return True

def is_valid_job(job: str) -> bool:
    if not job.isalpha():
        errors.append(f"Invalid job: {job}. It must contain only letters.")
        return False
    return True

def is_valid_employer(employer: str) -> bool:
    if not employer.isalpha():
        errors.append(f"Invalid employer: {employer}. It must contain only letters.")
        return False
    return True

def is_valid_given_name(given_name: str) -> bool:
    if not given_name.isalpha():
        errors.append(f"Invalid given name: {given_name}. It must contain only letters.")
        return False
    return True

def is_valid_last_name(last_name: str) -> bool:
    if not last_name.isalpha():
        errors.append(f"Invalid last name: {last_name}. It must contain only letters.")
        return False
    return True

def is_valid_date_of_birth(date_of_birth: str) -> bool:
    # Check if the date is in the format dd/mm/yyyy
    try:
        day, month, year = map(int, date_of_birth.split('/'))
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024):  # Adjust year range as needed
            errors.append(f"Invalid date of birth: {date_of_birth}. Date must be in dd/mm/yyyy format.")
            return False
        return True
    except ValueError:
        errors.append(f"Invalid date of birth: {date_of_birth}. Date must be in dd/mm/yyyy format.")
        return False

def is_valid_gender(gender: str) -> bool:
    if gender.lower() not in VALID_GENDERS:
        errors.append(f"Invalid gender: {gender}. Valid options are male, female, m, or f.")
        return False
    return True

def is_valid_place_of_issue(place_of_issue: str) -> bool:
    if not place_of_issue.isalpha():
        errors.append(f"Invalid place of issue: {place_of_issue}. It must contain only letters.")
        return False
    return True

def is_valid_issuing_authority(issuing_authority: str) -> bool:
    if not issuing_authority.isalpha():
        errors.append(f"Invalid issuing authority: {issuing_authority}. It must contain only letters.")
        return False
    return True

def is_valid_cellphone_number(cellphone_number: str) -> bool:
    if not (cellphone_number.isdigit() and len(cellphone_number) == 11):  # Adjust length as needed
        errors.append(f"Invalid cellphone number: {cellphone_number}. It must be a 11-digit number.")
        return False
    return True


def validate_form(data: dict) -> bool:
    errors.clear()  # Clear any previous errors
    
    valid = True
    
    # Validate each field
    valid &= is_valid_citizenship(data.get("Citizenship", ""))
    valid &= is_valid_age(data.get("Age", -1))
    valid &= is_valid_passport_number(data.get("Passport_number", ""))
    valid &= is_valid_given_name(data.get("Given Name", ""))
    valid &= is_valid_last_name(data.get("Last Name", ""))
    valid &= is_valid_date_of_birth(data.get("Date of Birth", ""))
    valid &= is_valid_gender(data.get("Gender", ""))
    valid &= is_valid_place_of_issue(data.get("Place of Issue", ""))
    valid &= is_valid_issuing_authority(data.get("Issuing Authority", ""))
    valid &= is_valid_cellphone_number(data.get("Cellphone Number", ""))
    valid &= is_valid_countrybirth(data.get("Country of Birth", ""))
    valid &= is_valid_passport(data.get("Passport", ""))
    valid &= is_valid_ms(data.get("Marital Status", ""))
    valid &= is_valid_address(data.get("Residential Address", ""))
    valid &= is_valid_job(data.get("Job Description", ""))
    valid &= is_valid_employer(data.get("Employer", ""))
    valid &= is_valid_email(data.get("Email", ""))
    
    return valid




if not validate_form(data_dict):
    print("Errors found:")
    for error in errors:
        print(error)
else:
    print("Form is valid.")
