import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
import pyfiglet

g = '\033[32m'
banner = pyfiglet.figlet_format("NumInFO", font='slant')
print(g+banner)

print('coded by Voilater v0.1 ',"\n")

number = phonenumbers.parse("+918438123013")
 
timezone = timezone.time_zones_for_number(number)
print("Timezone :",timezone,"\n")

country = geocoder.description_for_number (number,'en')
print("Country : ",country,"\n")

valid = phonenumbers.is_valid_number(number)
print("Valid :",valid,"\n")

isb = carrier.name_for_number(number,'en')
print("ISB provider :",isb,"\n")
