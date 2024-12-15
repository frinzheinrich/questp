#koreanerrorprocess
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

def koreanep(data_dict, tabs, sig):
    errors = []

    if 'NO Family Name_a' in data_dict:
        name = str(data_dict['NO Family Name_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Surname should contain only letters and spaces")

    if 'OF Given Names_a' in data_dict:
        name = str(data_dict['OF Given Names_a'])
        if not name.replace(' ', '').isalpha():
            errors.append("Given and middle names should contain only letters and spaces")

    if '1.4 Date of Birth (yyyy/mm/dd)_a' in data_dict:
        birthdate = str(data_dict['1.4 Date of Birth (yyyy/mm/dd)_a'])
        if not re.match(r'^\d{4}/\d{2}/\d{2}$', birthdate):
            errors.append("Date of birth should be in YYYY/MM/DD format")
        else:
            year, month, day = map(int, birthdate.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024): 
                errors.append("Invalid date of birth")

    if '1.6 Country of Birth_a' in data_dict:
        name = str(data_dict['1.6 Country of Birth_a'])
        if name.rstrip().lower() not in countries:
            errors.append("Invalid Country on Place of birth")

    if '1.5 Nationality_a' in data_dict:
        name = str(data_dict['1.5 Nationality_a'])
        if name.rstrip().lower() not in nationalities:
            errors.append("Invalid Country on Nationality")

    if '1.7 National Identity No._a' in data_dict:
        id_number = data_dict['1.7 National Identity No._a']
        try:
            int(id_number)
        except ValueError:
            if id_number.upper() == 'N/A' or id_number.upper() == 'NA':
                # ID number is 'N/A' or 'NA'
                pass
            else:
                errors.append("ID number must be an integer, 'N/A', or 'NA'")

    if '1.2 ****_a' in data_dict:
        section_1_2 = data_dict['1.2 ****_a'].strip()
        if not section_1_2:
            errors.append("Section 1.2 must not be empty")

    if '/Male_a' in data_dict and '/Female_a' in data_dict:
        if not ((data_dict['/Male[_a'] == 'X' and data_dict['/Female[_a'] == '') or (data_dict['/Male[_a'] == '' and data_dict['/Female[_a'] == 'X')):
            errors.append("Exactly one of 'Male' or 'Female' must be selected")

    if 'Yes_a' in data_dict and 'No_a' in data_dict:
        if not ((data_dict['Yes_a'] == 'X' and data_dict['No_a'] == '') or (data_dict['Yes_a'] == '' and data_dict['No_a'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")

    if 'Yes2_a' in data_dict and 'No2_a' in data_dict:
        if not ((data_dict['Yes2_a'] == 'X' and data_dict['No2_a'] == '') or (data_dict['Yes2_a'] == '' and data_dict['No2_a'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected")

    if 'Yes_a' in data_dict and "If 'Yes' please write the countries_a" in data_dict:
        name = str(data_dict['Yes_a'])
        if name == 'X':
            val = data_dict["If 'Yes' please write the countries_a"].strip()
            if not val:
                errors.append("Section 1.9 must not be empty")
        else:
            pass

    if 'Yes2_a' in data_dict and 'OR Given Name_a' in data_dict:
        name = str(data_dict['Yes2_a'])
        if name == 'X':
            val = data_dict['OR Given Name_a'].strip()
            if not val:
                errors.append("Section 1.8 must not be empty")
        else:
            pass

    if 'Long-term Stay over 90 days_a' in data_dict and 'Short-term Stay less than 90 days_a' in data_dict:
        if not ((data_dict['Long-term Stay over 90 days_a'] == 'X' and data_dict['Short-term Stay less than 90 days_a'] == '') or (data_dict['Long-term Stay over 90 days_a'] == '' and data_dict['Short-term Stay less than 90 days_a'] == 'X')):
            errors.append("Period of stay must be selected")

    if '2.2 Status of Stay_a' in data_dict:
        section = data_dict['2.2 Status of Stay_a'].replace('-', '')
        if not re.match(r'[A-Za-z]\d{1,2}', section):
            errors.append("Section 2 must be in the format of a letter followed by one or two numbers")

    if all(key in data_dict for key in ['Diplomatic_b', 'Official_b', 'Regular_b', 'Other_b']):
        if not sum(data_dict[key] == 'X' for key in ['Diplomatic_b', 'Official_b', 'Regular_b', 'Other_b']) == 1:
            errors.append("Exactly one Passport Type must be selected")

    if '3.2 Passport No._b' in data_dict:
        passport_number = data_dict['3.2 Passport No._b']
        if len(passport_number) != 9 or not all(char.isalnum() for char in passport_number):
            errors.append("Passport number must be 9 characters long and contain only letters and numbers")

    if '3.3 Country of Passport_b' in data_dict:
        name = str(data_dict['3.3 Country of Passport_b'])
        if name.rstrip().lower() not in countries:
            errors.append("Invalid Country of passport")

    if '3.4 Place of Issue_b' in data_dict:
        name = str(data_dict['3.4 Place of Issue_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Place of Issue should contain only letters and spaces")

    if '3.5 Date of Issue_b' in data_dict:
        date = str(data_dict['3.5 Date of Issue_b'])
        if not re.match(r'^\d{4}/\d{2}/\d{2}$', date):
            errors.append("Date of issue should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            year, month, day = map(int, date.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024): 
                errors.append("Invalid date of issue")

    if '3.6 Date of Expiry_b' in data_dict:
        date = str(data_dict['3.6 Date of Expiry_b'])
        if not re.match(r'^\d{4}/\d{2}/\d{2}$', date):
            errors.append("Date of expiry should be in DD/MM/YYYY format")
        else:
            # Validate if it's a real date
            year, month, day = map(int, date.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2040): 
                errors.append("Invalid date of expiry")

    if '4.1 Home Country Address of the applicant_b' in data_dict: 
        name = str(data_dict['4.1 Home Country Address of the applicant_b'])
        if not name:
                errors.append("Section 1.8 must not be empty")

    if 'Telephone No._b' in data_dict:
        telno = data_dict['Telephone No._b'].replace('-', '')
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel No. must be an integer or 'N/A' or 'NA'")

    if 'Cell Phone No._b' in data_dict:
        telno = data_dict['Cell Phone No._b'].replace('-', '')
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Cell No. must be an integer or 'N/A' or 'NA'")

    if '4.4 E-Mail_b' in data_dict:
        email = data_dict['4.4 E-Mail_b']
        if '@' not in email or email.count('@') != 1:
            errors.append("Invalid email address")

    if 'a) Full Name in English_b' in data_dict:
        name = str(data_dict['a) Full Name in English_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Emergency contact name should contain only letters and spaces")

    if 'b) Country of Residence_b' in data_dict:
        name = str(data_dict['b) Country of Residence_b'])
        if name.rstrip().lower() not in countries:
            errors.append("Invalid Country on Emergency Contact")

    if 'c) Telephone No._b' in data_dict:
        telno = data_dict['c) Telephone No._b'].replace('-', '')
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel No. 2 in page 2 must be an integer or 'N/A' or 'NA'")

    if 'd) Relationship to the applicant_b' in data_dict:
        name = str(data_dict['d) Relationship to the applicant_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Emergency contact relationship should contain only letters and spaces")

    if all(key in data_dict for key in ['Married_b', 'Single_b', 'Divorced_b']):
        if not sum(data_dict[key] == 'X' for key in ['Married_b', 'Single_b', 'Divorced_b']) == 1:
            errors.append("Exactly one of 'Single', 'Married', or 'Divorced' must be selected")

    if 'Married_b' in data_dict and 'a) ID Family Name (in English)_b':
        name = str(data_dict['Married_b'])
        newn = str(data_dict['a) ID Family Name (in English)_b'])
        if name =='X':
            if not newn:
                errors.append("Spouse information must be filled")

    if 'Yes2_b' in data_dict and 'No2_b' in data_dict:
        if not ((data_dict['Yes2_b'] == 'X' and data_dict['No2_b'] == '') or (data_dict['Yes2_b'] == '' and data_dict['No2_b'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected for children")

    if 'Yes2_b' in data_dict and 'Number of children_b' in data_dict:
        if data_dict['Yes2_b'] == 'X':
            try:
                int(data_dict['Number of children_b'])
            except ValueError:
                errors.append("Number of children must be an integer")

    if all(key in data_dict for key in ["Master' S /Doctoral Degree_b", 'High School Diploma_b', 'Other2_b',"Bachelor' S Degree_b"]):
        if not sum(data_dict[key] == 'X' for key in ["Master' S /Doctoral Degree_b", 'High School Diploma_b', 'Other2_b',"Bachelor' S Degree_b"]) == 1:
            errors.append("Exactly one highest degree must be selected")

    if '6.2 Name of School_b' in data_dict:
        name = str(data_dict['6.2 Name of School_b'])
        if not name.replace(' ', '').isalpha():
            errors.append("Name of School should contain only letters and spaces")

    if '6.3 Location of School(city/province/country)_b' in data_dict:
        location = str(data_dict['6.3 Location of School(city/province/country)_b']).replace(',', '')
        if not location.replace(' ', '').isalpha():
            errors.append("Location of School should contain only letters and spaces")

    jobkeys = ['Self-Employed_c', 'Employed_c', 'Unemployed_c', 'Other_c', 'Student_c', 'Entrepreneur_c', 'Retired_c', 'Civil Servant_c']

    purposekeys = ['Medical Tourism_c', 'Tourism/Transit_c', 'Conference_c', 'Work_c', 'Marriage Migrant_c', 'Diplomatic/Official_c', 'Trade/Investment/Intra-Corporate Transferee_c', 'Study/Training_c', 'Other2_c', 'Business Trip_c']

    if all(key in data_dict for key in jobkeys):
        job_count = sum(data_dict.get(key, '') == 'X' for key in jobkeys)
        if job_count != 1:
            errors.append("Exactly one of the employment status options must be selected")

    if all(key in data_dict for key in purposekeys):
        purpose_count = sum(data_dict.get(key, '') == 'X' for key in purposekeys)
        if purpose_count != 1:
            errors.append("Exactly one of the purpose of visit options must be selected")

    if 'Name of Company/Institute/School_c' in data_dict:
        name = str(data_dict['Name of Company/Institute/School_c'])
        if not name.replace(' ', '').isalpha():
            errors.append("Name of Insitute should contain only letters and spaces")

    if 'b) Position/Course_c' in data_dict:
        name = str(data_dict['b) Position/Course_c'])
        if not name.replace(' ', '').isalpha():
            errors.append("Position/Course should contain only letters and spaces")

    if 'c) Address of Company/Institute/School_c' in data_dict:
        address = str(data_dict['c) Address of Company/Institute/School_c']).replace(',', '')
        if not address.replace(' ', '').isalpha():
            errors.append("Address of Institute should contain only letters and spaces")

    if 'd) Telephone No._c' in data_dict:
        telno = data_dict['d) Telephone No._c'].replace('-', '')
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel No. in 7.2 must be an integer or 'N/A' or 'NA'")

    if '8.2 Intended Period of Stay_c' in data_dict:
        name = str(data_dict['8.2 Intended Period of Stay_c'])
        if not name.replace(' ', '').isalpha():
            errors.append("Period of stay should contain only letters and spaces")

    if '8.3 Intended Date of Entry_c' in data_dict:
        date = str(data_dict['8.3 Intended Date of Entry_c'])
        if not re.match(r'^\d{4}/\d{2}/\d{2}$', date):
            errors.append("Date of Entry should be in YYYY/MM/DD format")
        else:
            year, month, day = map(int, date.split('/'))
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2024): 
                errors.append("Invalid date of entry")

    if '8.4 ) Address in Korea (including hotels)_c' in data_dict:
        location = str(data_dict['8.4 ) Address in Korea (including hotels)_c']).replace(',', '')
        if not location.replace(' ', '').isalpha():
            errors.append("Korean Address should contain only letters and spaces")

    if '8.5 Contact No. in Korea_c' in data_dict:
        telno = data_dict['8.5 Contact No. in Korea_c'].replace('-', '')
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel No. in 8.5 must be an integer or 'N/A' or 'NA'")

    if 'Yes_c' in data_dict and 'No_c' in data_dict:
        if not ((data_dict['Yes_c'] == 'X' and data_dict['No_c'] == '') or (data_dict['Yes_c'] == '' and data_dict['No_c'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected for previous visits")

    if 'Yes_c' in data_dict and 'Table 6' in tabs:
        if data_dict['Yes_c'] == 'X':
            if not tabs['Table 6'][1][1].strip():
                errors.append("Previous vistits must be filled if Yes is selected")

    if 'Yes2_c' in data_dict and 'No2_c' in data_dict:
        if not ((data_dict['Yes2_c'] == 'X' and data_dict['No2_c'] == '') or (data_dict['Yes2_c'] == '' and data_dict['No2_c'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected for previous travels")

    if 'Yes2_c' in data_dict and 'Table 7' in tabs:
        if data_dict['Yes2_c'] == 'X':
            if not tabs['Table 7'][1][1].strip():
                errors.append("Other travels must be filled if Yes is selected")

    if 'Yes_d' in data_dict and 'No_d' in data_dict:
        if not ((data_dict['Yes_d'] == 'X' and data_dict['No_d'] == '') or (data_dict['Yes_d'] == '' and data_dict['No_d'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected in 8.8")

    if 'Yes_d' in data_dict and 'Table 8' in tabs:
        if data_dict['Yes_d'] == 'X':
            if not tabs['Table 8'][1][1].strip():
                errors.append("Table 8.8 must be filled")

    if 'Yes2_d' in data_dict and 'No2_d' in data_dict:
        if not ((data_dict['Yes2_d'] == 'X' and data_dict['No2_d'] == '') or (data_dict['Yes2_d'] == '' and data_dict['No2_d'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected in 8.9")

    if 'Yes2_d' in data_dict and 'Table 9' in tabs:
        if data_dict['Yes2_d'] == 'X':
            if not tabs['Table 9'][1][1].strip():
                errors.append("Table 8.9 must be filled")

    if 'Yes3_d' in data_dict and 'No3_d' in data_dict:
        if not ((data_dict['Yes3_d'] == 'X' and data_dict['No3_d'] == '') or (data_dict['Yes3_d'] == '' and data_dict['No3_d'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected in 9.1")

    if 'a) Name of inviting person/organization (Korean, foreign resident in Korea, company, or institute)_d' in data_dict and 'Yes3_d' in data_dict:
        if data_dict['Yes3_d'] == 'X':
            name = data_dict['a) Name of inviting person/organization (Korean, foreign resident in Korea, company, or institute)_d'].strip()
            if not name:
                errors.append("Name of inviting person/organization must not be empty if Yes is selected")

    if 'Yes4_d' in data_dict and 'No4_d' in data_dict:
        if not ((data_dict['Yes4_d'] == 'X' and data_dict['No4_d'] == '') or (data_dict['Yes4_d'] == '' and data_dict['No4_d'] == 'X')):
            errors.append("Exactly one of 'Yes' or 'No' must be selected in 11.1")

    if 'Yes4_d' in data_dict and 'Table 10' in tabs:
        if data_dict['Yes4_d'] == 'X':
            if not tabs['Table 10'][1][1].strip():
                errors.append("Table 11 must be filled")

    if 'Estimated travel costs(in US dollars)_d' in data_dict:
        cost = data_dict['Estimated travel costs(in US dollars)_d'].strip()
        if not cost:
            errors.append("Estimated travel costs must not be empty")
    
    if 'b) Relationship to the applicant_d' in data_dict:
        cost = data_dict['b) Relationship to the applicant_d'].strip()
        if not cost:
            errors.append("10.b Relationship to applicant must not be empty")

    if 'c) Type of Support_d' in data_dict:
        cost = data_dict['c) Type of Support_d'].strip()
        if not cost:
            errors.append("10.c Type of support must not be empty")

    if 'd) Contact No._d' in data_dict:
        telno = data_dict['d) Contact No._d'].replace('-', '')
        if telno.lower() not in ['n/a', 'na']:
            try:
                int(telno)
            except ValueError:
                errors.append("Tel No. in 10.2d must be an integer or 'N/A' or 'NA'")

    if 'Applicant Name_e' in data_dict:
        name = str(data_dict['Applicant Name_e'])
        if not name.replace(' ', '').isalpha():
            errors.append("Name of applicant must be filled and should contain only letters and spaces")

    if 'Signature' in sig:
        sign = sig['Signature']
        if not sign == 'Detected':
            errors.append("No signature is detected in the form")

    validform = ['Form is complete and valid']

    if errors:
        return errors
    else:
        return validform