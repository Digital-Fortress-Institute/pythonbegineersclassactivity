import tkinter.ttk
from tkinter import *

import tk

root = Tk()
root.title('Job Application Form')
root.geometry('800x1200')
root.iconbitmap(r'job.ico')

# First Name
fn = Label(root, text="First Name:")
fn.grid(row=0, column=0, padx=10)
fn_entry = Entry(root, width=30)
fn_entry.grid(row=0, column=1, pady=5)
# Middle Name
mn = Label(root, text="Middle Name(optional):")
mn.grid(row=1, column=0)
mn_entry = Entry(root, width=30)
mn_entry.grid(row=1, column=1, pady=5)
# Last Name
ln = Label(root, text="Last Name:")
ln.grid(row=2, column=0, padx=10)
ln_entry = Entry(root, width=30)
ln_entry.grid(row=2, column=1, pady=5)

add = Label(root, text="Address 1:")
add.grid(row=3, column=0, padx=10)
add_entry = Entry(root, width=30)
add_entry.grid(row=3, column=1, pady=5)

add_2 = Label(root, text="Address 2:")
add_2.grid(row=4, column=0, padx=10)
add_2_entry = Entry(root, width=30)
add_2_entry.grid(row=4, column=1, pady=5)

lga = Label(root, text="L.G.A.:")
lga.grid(row=5, column=0, padx=10)
lga_entry = Entry(root, width=30)
lga_entry.grid(row=5, column=1, pady=5)

state = Label(root, text="State:")
state.grid(row=6, column=0, padx=10)
s_combo = tkinter.ttk.Combobox(justify='left', width=29, values=[
  "Abia",
  "Adamawa",
  "Akwa Ibom",
  "Anambra",
  "Bauchi",
  "Bayelsa",
  "Benue",
  "Borno",
  "Cross River",
  "Delta",
  "Ebonyi",
  "Edo",
  "Ekiti",
  "Enugu",
  "FCT - Abuja",
  "Gombe",
  "Imo",
  "Jigawa",
  "Kaduna",
  "Kano",
  "Katsina",
  "Kebbi",
  "Kogi",
  "Kwara",
  "Lagos",
  "Nasarawa",
  "Niger",
  "Ogun",
  "Ondo",
  "Osun",
  "Oyo",
  "Plateau",
  "Rivers",
  "Sokoto",
  "Taraba",
  "Yobe",
  "Zamfara"
])
s_combo.grid(row=6, column=1, pady=5)

country = Label(root, text="Country:")
country.grid(row=7, column=0, padx=10)
c_combo = tkinter.ttk.Combobox(width=29, justify='right', values=["Afghanistan",
    "Åland Islands",
    "Albania",
    "Algeria",
    "American Samoa",
    "Andorra",
    "Angola",
    "Anguilla",
    "Antarctica",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Aruba",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bermuda",
    "Bhutan",
    "Bolivia (Plurinational State of)",
    "Bonaire, Sint Eustatius and Saba",
    "Bosnia and Herzegovina",
    "Botswana",
    "Bouvet Island",
    "Brazil",
    "British Indian Ocean Territory",
    "United States Minor Outlying Islands",
    "Virgin Islands (British)",
    "Virgin Islands (U.S.)",
    "Brunei Darussalam",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cabo Verde",
    "Cayman Islands",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Christmas Island",
    "Cocos (Keeling) Islands",
    "Colombia",
    "Comoros",
    "Congo",
    "Congo (Democratic Republic of the)",
    "Cook Islands",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Curaçao",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Falkland Islands (Malvinas)",
    "Faroe Islands",
    "Fiji",
    "Finland",
    "France",
    "French Guiana",
    "French Polynesia",
    "French Southern Territories",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Gibraltar",
    "Greece",
    "Greenland",
    "Grenada",
    "Guadeloupe",
    "Guam",
    "Guatemala",
    "Guernsey",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Heard Island and McDonald Islands",
    "Holy See",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Côte d'Ivoire",
    "Iran (Islamic Republic of)",
    "Iraq",
    "Ireland",
    "Isle of Man",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jersey",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Kuwait",
    "Kyrgyzstan",
    "Lao People's Democratic Republic",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macao",
    "Macedonia (the former Yugoslav Republic of)",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Martinique",
    "Mauritania",
    "Mauritius",
    "Mayotte",
    "Mexico",
    "Micronesia (Federated States of)",
    "Moldova (Republic of)",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Montserrat",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Caledonia",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Niue",
    "Norfolk Island",
    "Korea (Democratic People's Republic of)",
    "Northern Mariana Islands",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine, State of",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Pitcairn",
    "Poland",
    "Portugal",
    "Puerto Rico",
    "Qatar",
    "Republic of Kosovo",
    "Réunion",
    "Romania",
    "Russian Federation",
    "Rwanda",
    "Saint Barthélemy",
    "Saint Helena, Ascension and Tristan da Cunha",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Martin (French part)",
    "Saint Pierre and Miquelon",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Sint Maarten (Dutch part)",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Georgia and the South Sandwich Islands",
    "Korea (Republic of)",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Svalbard and Jan Mayen",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syrian Arab Republic",
    "Taiwan",
    "Tajikistan",
    "Tanzania, United Republic of",
    "Thailand",
    "Timor-Leste",
    "Togo",
    "Tokelau",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Turks and Caicos Islands",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom of Great Britain and Northern Ireland",
    "United States of America",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Venezuela (Bolivarian Republic of)",
    "Viet Nam",
    "Wallis and Futuna",
    "Western Sahara",
    "Yemen",
    "Zambia",
    "Zimbabwe"])
c_combo.grid(row=7, column=1, pady=5)

email = Label(root, text="E-mail:")
email.grid(row=8, column=0, padx=10)
email_entry = Entry(root, width=30)
email_entry.grid(row=8, column=1, pady=5)

gender = Label(root, text="Gender:")
gender.grid(row=9, column=0, padx=10)
combo = tkinter.ttk.Combobox(state='readonly', width=29, justify='right', values=['Male', 'Female', 'Transgender', 'Not Specified'])
combo.grid(row=9, column=1, pady=5)
# gender_entry = Entry(root, width=30)
# gender_entry.grid(row=8, column=1, pady=5)

dob = Label(root, text="D.O.B:")
dob.grid(row=10, column=0)
month = Label(root, text='Month')
month.grid(row=10, column=1)
month_entry = tkinter.ttk.Combobox(width=6, justify='left', values=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
month_entry.grid(row=10, column=2)

date = Label(root, text='Date')
date.grid(row=10, column=3)
date_entry = tkinter.ttk.Combobox(width=4, justify='left', values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                                   '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                                                   '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])
date_entry.grid(row=10, column=4)

year = Label(root, text='Year')
year.grid(row=10, column=5)
date_entry = tkinter.ttk.Combobox(width=4, justify='left', values=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
                                                                   '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                                                                   '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021',
                                                                   '2022', '2023', '2024'])
date_entry.grid(row=10, column=6)

# dob_entry = Entry(root, width=30)
# dob_entry.grid(row=10, column=1, pady=5)

nin = Label(root, text="NIN:")
nin.grid(row=11, column=0, padx=10)
nin_entry = Entry(root, width=30)
nin_entry.grid(row=11, column=1, pady=5)

employment_status = Label(root, text="Choose your employment :")
employment_status.grid(row=12, column=0, padx=10)
em_entry = tkinter.ttk.Combobox(width=29, justify='left', values=['Employed', 'Unemployed', 'Self-employed', 'Student'])
em_entry.grid(row=12, column=1)
# em_stat_entry = Entry(root, width=30)
# em_stat_entry.grid(row=12, column=1, pady=5)

submit = Button(root,
                text='Submit',
                bd=2,
                activebackground='blue',
                justify='center')
submit.grid(row=13, column=1,  padx=5, pady=5)
# mybutton = Button(root, text='Submit')
# mybutton.grid(row=1, column=0, padx=20, pady=10)
root.mainloop()

