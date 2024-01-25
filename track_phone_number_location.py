import phonenumbers
from phonenumbers import geocoder

def get_phone_number_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        country = geocoder.description_for_number(parsed_number, "en")
        return country
    except phonenumbers.NumberParseException as e:
        print(f"Error parsing phone number: {e}")
        return None

phone_number = "+923457134603"
result = get_phone_number_info(phone_number)

if result:
    print(f"Country: {result}")
else:
    print("Failed to retrieve phone number information.")