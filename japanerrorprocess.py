import re

countries = ["afghanistan", "albania", "algeria", "andorra", "angola", "antigua and barbuda", "argentina", "armenia", 
            "australia", "austria", "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados", "belarus", "belgium", 
            "belize", "benin", "bhutan", "bolivia", "bosnia and herzegovina", "botswana", "brazil", "brunei", "bulgaria", 
            "burkina faso", "burundi", "cabo verde", "cambodia", "cameroon", "canada", "central african republic", "chad", 
            "chile", "china", "colombia", "comoros", "congo", "costa rica", "croatia", "cuba", "cyprus", "czech republic", 
            "democratic republic of the congo", "denmark", "djibouti", "dominica", "dominican republic", "ecuador", "egypt", 
            "el salvador", "equatorial guinea", "eritrea", "estonia", "eswatini", "ethiopia", "fiji", "finland", "france", 
            "gabon", "gambia", "georgia", "germany", "ghana", "greece", "grenada", "guatemala", "guinea", "guinea-bissau", 
            "guyana", "haiti", "honduras", "hungary", "iceland", "india", "indonesia", "iran", "iraq", "ireland", "israel", 
            "italy", "ivory coast", "jamaica", "japan", "jordan", "kazakhstan", "kenya", "kiribati", "kuwait", "kyrgyzstan", 
            "laos", "latvia", "lebanon", "lesotho", "liberia", "libya", "liechtenstein", "lithuania", "luxembourg", 
            "madagascar", "malawi", "malaysia", "maldives", "mali", "malta", "marshall islands", "mauritania", "mauritius", 
            "mexico", "micronesia", "moldova", "monaco", "mongolia", "montenegro", "morocco", "mozambique", "myanmar", 
            "namibia", "nauru", "nepal", "netherlands", "new zealand", "nicaragua", "niger", "nigeria", "north korea", 
            "north macedonia", "norway", "oman", "pakistan", "palau", "palestine", "panama", "papua new guinea", "paraguay", 
            "peru", "philippines", "poland", "portugal", "qatar", "romania", "russia", "rwanda", "saint kitts and nevis", 
            "saint lucia", "saint vincent and the grenadines", "samoa", "san marino", "sao tome and principe", "saudi arabia", 
            "senegal", "serbia", "seychelles", "sierra leone", "singapore", "slovakia", "slovenia", "solomon islands", 
            "somalia", "south africa", "south korea", "south sudan", "spain", "sri lanka", "sudan", "suriname", "sweden", 
            "switzerland", "syria", "taiwan", "tajikistan", "tanzania", "thailand", "timor-leste", "togo", "tonga", 
            "trinidad and tobago", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda", "ukraine", "united arab emirates", 
            "united kingdom", "united states", "uruguay", "uzbekistan", "vanuatu", "vatican city", "venezuela", "vietnam", 
            "yemen", "zambia", "zimbabwe"]
nationalities = ["afghan", "albanian", "algerian", "american", "andorran", "angolan", "antiguan", "argentine", "armenian", "australian", "austrian", "azerbaijani", "bahamian", "bahraini", "bangladeshi", "barbadian", "belarusian", "belgian", "belizean", "beninese", "bhutanese", "bolivian", "bosnian", "botswanan", "brazilian", "british", "bruneian", "bulgarian", "burkinabe", "burmese", "burundian", "cambodian", "cameroonian", "canadian", "cape verdean", "central african", "chadian", "chilean", "chinese", "colombian", "comoran", "congolese", "costa rican", "croatian", "cuban", "cypriot", "czech", "danish", "djiboutian", "dominican", "dutch", "east timorese", "ecuadorian", "egyptian", "emirian", "equatorial guinean", "eritrean", "estonian", "ethiopian", "fijian", "filipino", "finnish", "french", "gabonese", "gambian", "georgian", "german", "ghanaian", "greek", "grenadian", "guatemalan", "guinean", "guyanese", "haitian", "honduran", "hungarian", "icelandic", "indian", "indonesian", "iranian", "iraqi", "irish", "israeli", "italian", "ivorian", "jamaican", "japanese", "jordanian", "kazakhstani", "kenyan", "kiribati", "korean", "kuwaiti", "kyrgyz", "laotian", "latvian", "lebanese", "lesothan", "liberian", "libyan", "liechtensteiner", "lithuanian", "luxembourgish", "macedonian", "malagasy", "malawian", "malaysian", "maldivian", "malian", "maltese", "marshallese", "mauritanian", "mauritian", "mexican", "micronesian", "moldovan", "monacan", "mongolian", "montenegrin", "moroccan", "mozambican", "namibian", "nauruan", "nepalese", "new zealander", "nicaraguan", "nigerian", "nigerien", "norwegian", "omani", "pakistani", "palauan", "palestinian", "panamanian", "papua new guinean", "paraguayan", "peruvian", "polish", "portuguese", "qatari", "romanian", "russian", "rwandan", "saint kitts and nevis", "saint lucian", "saint vincent and the grenadines", "samoan", "san marinese", "sao tomean", "saudi", "senegalese", "serbian", "seychellois", "sierra leonean", "singaporean", "slovak", "slovenian", "solomon islander", "somali", "south african", "south sudanese", "spanish", "sri lankan", "sudanese", "surinamese", "swazi", "swedish", "swiss", "syrian", "tajik", "tanzanian", "thai", "togolese", "tongan", "trinidadian and tobagonian", "tunisian", "turkish", "turkmen", "tuvaluan", "ugandan", "ukrainian", "uruguayan", "uzbek", "vanuatuan", "vatican", "venezuelan", "vietnamese", "yemeni", "zambian", "zimbabwean"]


def japanep(data_dict, sig):
    errors = []

    if 'Surname (as shown in passport)_a' in data_dict:
        name = str(data_dict['Surname (as shown in passport)_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Surname should contain only letters and spaces")

    if 'Given and middle names (as shown in passport)_a' in data_dict:
        name = str(data_dict['Given and middle names (as shown in passport)_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Given and middle names should contain only letters and spaces")
    
    if 'Date of birth_a' in data_dict:
        birthdate = str(data_dict['Date of birth_a'])
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', birthdate):
            errors.append("Date of birth should be in DD/MM/YYYY format")
        else:
            day, month, year = map(int, birthdate.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024): 
                errors.append("Invalid date of birth")

    if '(Country)_a' in data_dict:
        name = str(data_dict['(Country)_a'])
        if name.rstrip().lower() not in countries:
            errors.append("Invalid Country on Place of birth")

    if 'Nationality or citizenship_a' in data_dict:
        name = str(data_dict['Nationality or citizenship_a'])
        if name.rstrip().lower() not in countries:
            errors.append("Invalid Country on Nationality")

    if 'Male_a' in data_dict and 'Female_a' in data_dict:
        if not ((data_dict['Male_a'] == 'X' and data_dict['Female_a'] == '') or (data_dict['Male_a'] == '' and data_dict['Female_a'] == 'X')):
            errors.append("Exactly one of 'Male' or 'Female' must be selected")

    if all(key in data_dict for key in ['Married_a', 'Single_a', 'Widowed_a', 'Divorced_a']):
        if not sum(data_dict[key] == 'X' for key in ['Married_a', 'Single_a', 'Widowed_a', 'Divorced_a']) == 1:
            errors.append("Exactly one of 'Single', 'Married', 'Widowed', or 'Divorced' must be selected")

    if 'ID No. issued to you by your government_a' in data_dict:
        id_number = data_dict['ID No. issued to you by your government_a']
        try:
            int(id_number)
        except ValueError:
            if id_number.upper() == 'N/A' or id_number.upper() == 'NA':
                # ID number is 'N/A' or 'NA'
                pass
            else:
                errors.append("ID number must be an integer, 'N/A', or 'NA'")

    if all(key in data_dict for key in ['Diplomatic_a', 'Official_a', 'Ordinary_a', 'Other_a']):
        if not sum(data_dict[key] == 'X' for key in ['Diplomatic_a', 'Official_a', 'Ordinary_a', 'Other_a']) == 1:
            errors.append("Exactly one Passport Type must be selected")

    if 'Date of issue_a' in data_dict:
        date = str(data_dict['Date of issue_a'])
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', date):
            errors.append("Date of issue should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            day, month, year = map(int, date.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024): 
                errors.append("Invalid date of issue")

    if 'Date of expiry_a' in data_dict:
        date = str(data_dict['Date of expiry_a'])
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', date):
            errors.append("Date of expiry should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            day, month, year = map(int, date.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2040): 
                errors.append("Invalid date of expiry")

    if 'Place of issue_a' in data_dict:
        name = str(data_dict['Place of issue_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Place of issue should contain only letters and spaces")

    if 'Issuing authority_a' in data_dict:
        name = str(data_dict['Issuing authority_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Issuing authority should contain only letters and spaces")

    if 'Certificate of Eligibility No._a' in data_dict:
        id_number = data_dict['Certificate of Eligibility No._a']
        try:
            int(id_number)
        except ValueError:
            if id_number.upper() == 'N/A' or id_number.upper() == 'NA':
                pass
            else:
                errors.append("Certificate of Eligibility No. must be an integer, 'N/A', or 'NA'")

    if 'Passport No._a' in data_dict:
        passport_number = data_dict['Passport No._a']
        if len(passport_number) != 9 or not all(char.isalnum() for char in passport_number):
            errors.append("Passport number must be 9 characters long and contain only letters and numbers")

    if 'Date of arrival in Japan_a' in data_dict:
        date = str(data_dict['Date of expiry_a'])
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', date):
            errors.append("Date of arrival should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            day, month, year = map(int, date.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2040): 
                errors.append("Invalid date of arrival")

    if 'Intended length of stay in Japan_a' in data_dict:
        name = str(data_dict['Intended length of stay in Japan_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Length of stay should contain only letters and spaces")

    if 'Port of entry into Japan_a' in data_dict:
        name = str(data_dict['Port of entry into Japan_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Port of entry should contain only letters and spaces")

    if 'Name of ship or airline_a' in data_dict:
        name = str(data_dict['Name of ship or airline_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Ship/Airline should contain only letters and spaces")

    if 'Name_a' in data_dict:
        name = str(data_dict['Name_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Name should contain only letters and spaces")

    if 'Name2_a' in data_dict:
        name = str(data_dict['Name2_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Name 2 should contain only letters and spaces")

    if 'Address_a' in data_dict:
        name = str(data_dict['Address_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Address should contain only letters and spaces")

    if 'Address2_a' in data_dict:
        name = str(data_dict['Address2_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Address 2 should contain only letters and spaces")

    if 'Address3_a' in data_dict:
        name = str(data_dict['Address3_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Address 3 should contain only letters and spaces")

    if 'Tel._a' in data_dict:
        telno = data_dict['Tel._a']
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel. must be an integer or 'N/A' or 'NA'")

    if 'Tel.2_a' in data_dict:
        telno = data_dict['Tel.2_a']
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel. 2 must be an integer or 'N/A' or 'NA'")

    if 'Tel.3_a' in data_dict:
        telno = data_dict['Tel.3_a']
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel. 3 must be an integer or 'N/A' or 'NA'")

    if 'Mobile No._a' in data_dict:
        telno = data_dict['Mobile No._a']
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Mobile No. must be an integer or 'N/A' or 'NA'")

    if 'E-Mail_a' in data_dict:
        email = data_dict['E-Mail_a']
        if '@' not in email or email.count('@') != 1:
            errors.append("Invalid email address")
    
    if 'Current profession or occupation and position_a' in data_dict:
        name = str(data_dict['Current profession or occupation and position_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Profession should contain only letters and spaces")

    if 'Date of application_b' in data_dict:
        date = str(data_dict['Date of application_b'])
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', date):
            errors.append("Date of expiry should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            day, month, year = map(int, date.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2040): 
                errors.append("Invalid date of application")

    if 'Name_b' in data_dict:
        name = str(data_dict['Name_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Name in page2 should contain only letters and spaces")

    if 'Name2_b' in data_dict:
        name = str(data_dict['Name2_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Name 2 in page2 should contain only letters and spaces")

    if 'Tel._b' in data_dict:
        telno = data_dict['Tel._b']
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel. in page 2 must be an integer or 'N/A' or 'NA'")

    if 'Tel.2_b' in data_dict:
        telno = data_dict['Tel.2_b']
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel. 2 in page 2 must be an integer or 'N/A' or 'NA'")

    if 'Address_b' in data_dict:
        name = str(data_dict['Address_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Address in page 2 should contain only letters and spaces")

    if 'Address2_b' in data_dict:
        name = str(data_dict['Address2_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Address 2 in page 2 should contain only letters and spaces")

    if 'Date of birth_b' in data_dict:
        birthdate = str(data_dict['Date of birth_b'])
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', birthdate):
            errors.append("Date of birth in page 2 should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            day, month, year = map(int, birthdate.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024): 
                errors.append("Invalid date of birth in page 2")

    if 'Date of birth2_b' in data_dict:
        birthdate = str(data_dict['Date of birth2_b'])
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', birthdate):
            errors.append("Date of birth in page 2 should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            day, month, year = map(int, birthdate.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024): 
                errors.append("Invalid date of birth 2 in page 2")  

    if 'Relationship to applicant_b' in data_dict:
        name = str(data_dict['Relationship to applicant_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Relationship to applicant in page2 should contain only letters and spaces")

    if 'Relationship to applicant2_b' in data_dict:
        name = str(data_dict['Relationship to applicant2_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Relationship to applicant 2 in page2 should contain only letters and spaces")

    if 'Profession or occupation and position_b' in data_dict:
        name = str(data_dict['Profession or occupation and position_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Profession in page2 should contain only letters and spaces")

    if 'Profession or occupation and position2_b' in data_dict:
        name = str(data_dict['Profession or occupation and position2_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Profession 2 in page2 should contain only letters and spaces")

    if 'Nationality or immigration status_b' in data_dict:
        name = str(data_dict['Nationality or immigration status_b'])
        if name.rstrip().lower() not in nationalities:
            errors.append("Invalid Nationality on page 2")

    if 'Nationality or immigration status2_b' in data_dict:
        name = str(data_dict['Nationality or immigration status2_b'])
        if name.rstrip().lower() not in nationalities:
            errors.append("Invalid Nationality 2 on page 2")

    if 'Male_b' in data_dict and 'Female_b' in data_dict:
        if not ((data_dict['Male_b'] == 'X' and data_dict['Female_b'] == '') or (data_dict['Male_b'] == '' and data_dict['Female_b'] == 'X')):
            errors.append("Exactly one of 'Male' or 'Female' in page 2 must be selected")

    if 'Male2_b' in data_dict and 'Female2_b' in data_dict:
        if not ((data_dict['Male2_b'] == 'X' and data_dict['Female2_b'] == '') or (data_dict['Male2_b'] == '' and data_dict['Female2_b'] == 'X')):
            errors.append("Exactly one of 'Male' or 'Female' in page 2 must be selected")

    if 'Yes_b' in data_dict and 'No_b' in data_dict:
        if not ((data_dict['Yes_b'] == 'X' and data_dict['No_b'] == '') or (data_dict['Yes_b'] == '' and data_dict['No_b'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")

    if 'Yes2_b' in data_dict and 'No2_b' in data_dict:
        if not ((data_dict['Yes2_b'] == 'X' and data_dict['No2_b'] == '') or (data_dict['Yes2_b'] == '' and data_dict['No2_b'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")

    if 'Yes3_b' in data_dict and 'No3_b' in data_dict:
        if not ((data_dict['Yes3_b'] == 'X' and data_dict['No3_b'] == '') or (data_dict['Yes3_b'] == '' and data_dict['No3_b'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")

    if 'Yes4_b' in data_dict and 'No4_b' in data_dict:
        if not ((data_dict['Yes4_b'] == 'X' and data_dict['No4_b'] == '') or (data_dict['Yes4_b'] == '' and data_dict['No4_b'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")
            
    if 'Yes5_b' in data_dict and 'No5_b' in data_dict:
        if not ((data_dict['Yes5_b'] == 'X' and data_dict['No5_b'] == '') or (data_dict['Yes5_b'] == '' and data_dict['No5_b'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")
    
    if 'Yes6_b' in data_dict and 'No6_b' in data_dict:
        if not ((data_dict['Yes6_b'] == 'X' and data_dict['No6_b'] == '') or (data_dict['Yes6_b'] == '' and data_dict['No6_b'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")

    if any(data_dict.get(key, '') == 'X' for key in ['Yes_b', 'Yes2_b', 'Yes3_b', 'Yes4_b', 'Yes5_b','Yes6_b']):
        if not data_dict.get('If you answered "Yes" to any of the above questions, please provide relevant details._b', ''):
            errors.append("Optional field cannot be empty if at least one Yes is selected")

    if 'Signature' in sig:
        sign = sig['Signature']
        if not sign == 'Detected':
            errors.append("No signature is detected in the form")

    validform = ['Form is complete and valid']

    if errors:
        #return f"The following error/s has been found: {', '.join(errors)}"
        return errors
    else:
        return validform


