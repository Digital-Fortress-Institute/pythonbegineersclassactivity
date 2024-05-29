import tkinter as tk
from tkinter import *
from tkinter import messagebox
# from tkinter import ttk
import sqlite3  # This invokes SQL.
from tkinter.ttk import Combobox


def create_table():
    sigmawolf = sqlite3.connect('wave_reg_form.db')
    waveclass = sigmawolf.cursor()
    waveclass.execute('''
      CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT NOT NULL,
                            firstname TEXT NOT NULL,
                            middlename TEXT NOT NULL,
                            lastname TEXT NOT NULL,
                            address1 TEXT NOT NULL,
                            address2 TEXT NOT NULL,
                            lga TEXT NOT NULL,
                            state TEXT NOT NULL,
                            country TEXT NOT NULL,
                            gender TEXT NOT NULL,
                            birthmonth TEXT NOT NULL,
                            birthdate TEXT NOT NULL,
                            birthyear TEXT NOT NULL,
                            nin TEXT NOT NULL,
                            employment TEXT NOT NULL
          )
      ''')
    sigmawolf.commit()
    sigmawolf.close()


def result():
    fn_key = fn_entry.get()
    mn_key = mn_entry.get()
    ln_key = ln_entry.get()
    add1_key = add_entry.get()
    add2_key = add_2_entry.get()
    lga_key = lga_entry.get()
    state_key = s_combo.get()
    country_key = c_combo.get()
    email_key = email_entry.get()
    gender_key = combo.get()
    month_key = month_entry.get()
    date_key = date_entry.get()
    year_key = year_entry.get()
    nin_key = nin_entry.get()
    em_key = em_entry.get()

    fnr = Label(root, text=fn_key)
    fnr.grid()
    mnr = Label(root, text=mn_key)
    mnr.grid()
    lnr = Label(root, text=ln_key)
    lnr.grid()
    add1r = Label(root, text=add1_key)
    add1r.grid()
    add2r = Label(root, text=add2_key)
    add2r.grid()
    lgar = Label(root, text=lga_key)
    lgar.grid()
    state_r = Label(root, text=state_key)
    state_r.grid()
    countryr = Label(root, text=country_key)
    countryr.grid()
    emr = Label(root, text=email_key)
    emr.grid()
    gendr = Label(root, text=gender_key)
    gendr.grid()
    monr = Label(root, text=month_key)
    monr.grid()
    dater = Label(root, text=date_key)
    dater.grid()
    yearr = Label(root, text=year_key)
    yearr.grid()
    ninr = Label(root, text=nin_key)
    ninr.grid()
    employr = Label(root, text=em_key)
    employr.grid()

def savedata():
    email = email_entry.get()
    firstname = fn_entry.get()
    middlename = mn_entry.get()
    lastname = ln_entry.get()
    address1 = add_entry.get()
    address2 = add_2_entry.get()
    lga = lga_entry.get()
    state = s_combo.get()
    country = c_combo.get()
    gender = combo.get()
    birthmonth = month_entry.get()
    birthdate = date_entry.get()
    birthyear = year_entry.get()
    nin = nin_entry.get()
    employment = em_entry.get()

    if email and firstname and middlename and lastname and address1 and address2 and lga and state and country and gender and birthmonth and birthdate and birthyear\
            and nin and employment:
        sigmawolf = sqlite3.connect('wave_reg_form.db')
        waveclass = sigmawolf.cursor()
        waveclass.execute("INSERT INTO users (email, firstname, middlename, lastname, address1, address2, lga, state, country, gender, birthmonth,birthdate, birthyear, nin, employment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (email, firstname, middlename, lastname, address1, address2, lga, state, country, gender, birthmonth,
                        birthdate, birthyear, nin, employment))
        sigmawolf.commit()
        sigmawolf.close()

        messagebox.showinfo('Successfully registered')
    else:
        messagebox.showerror('Credentials not successfully saved')

root = tk.Tk()
root.title('Job Application Form')
# root.geometry('600x1200')
root.iconbitmap(r'job.ico')

# First Name
label_firstname = Label(root, text="First Name:")
label_firstname.grid(row=0, column=0, padx=5, pady=5)
fn_entry = Entry(root, width=30)
fn_entry.grid(row=0, column=1, padx=5, pady=5)
# Middle Name
label_middlename = Label(root, text="Middle Name(optional):")
label_middlename.grid(row=1, column=0, padx=5, pady=5)
mn_entry = Entry(root, width=30)
mn_entry.grid(row=1, column=1, padx=5, pady=5)
# Last Name
label_lastname = Label(root, text="Last Name:")
label_lastname.grid(row=2, column=0, padx=5, pady=5)
ln_entry = Entry(root, width=30)
ln_entry.grid(row=2, column=1, padx=5, pady=5)

label_address1 = Label(root, text="Address 1:")
label_address1.grid(row=3, column=0, padx=5, pady=5)
add_entry = Entry(root, width=30)
add_entry.grid(row=3, column=1, padx=5, pady=5)

label_address2 = Label(root, text="Address 2:")
label_address2.grid(row=4, column=0, padx=5, pady=5)
add_2_entry = Entry(root, width=30)
add_2_entry.grid(row=4, column=1, padx=5, pady=5)

label_lga = Label(root, text="L.G.A.:")
label_lga.grid(row=5, column=0, padx=5, pady=5)
lga_entry = Entry(root, width=30)
lga_entry.grid(row=5, column=1, padx=5, pady=5)

label_state = Label(root, text="State:")
label_state.grid(row=6, column=0, padx=5, pady=5)
s_combo = Combobox(justify='left', width=29, values=[
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
s_combo.grid(row=6, column=1, padx=5, pady=5)

label_country = Label(root, text="Country:")
label_country.grid(row=7, column=0, padx=5, pady=5)
c_combo = Combobox(width=29, justify='left', values=["Afghanistan",
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
c_combo.grid(row=7, column=1, padx=5, pady=5)

label_email = Label(root, text="E-mail:")
label_email.grid(row=8, column=0, padx=5, pady=5)
email_entry = Entry(root, width=30)
email_entry.grid(row=8, column=1, padx=5, pady=5)

label_gender = Label(root, text="Gender:")
label_gender.grid(row=9, column=0, padx=5, pady=5)
combo = Combobox(state='readonly', width=29, justify='right', values=['Male', 'Female', 'Transgender', 'Not Specified'])
combo.grid(row=9, column=1, padx=5, pady=5)
# gender_entry = Entry(root, width=30)
# gender_entry.grid(row=8, column=1, pady=5)

label_dob = Label(root, text="D.O.B:")
label_dob.grid(row=10, column=0, padx=5, pady=5)

label_birthmonth = Label(root, text='Month')
label_birthmonth.grid(row=10, column=1, padx=5, pady=5)

month_entry = Combobox(width=6, justify='left', values=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
month_entry.grid(row=10, column=2, padx=5, pady=5)

label_birthdate = Label(root, text='Date')
label_birthdate.grid(row=10, column=3, padx=5, pady=5)
date_entry = Combobox(width=4, justify='left', values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                                                    '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                                                    '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'])
date_entry.grid(row=10, column=4, padx=5, pady=5)

label_birthyear = Label(root, text='Year')
label_birthyear.grid(row=10, column=5, padx=5, pady=5)
year_entry = Combobox(width=4, justify='left', values=['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
                                                    '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
                                                    '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021',
                                                    '2022', '2023', '2024'])
year_entry.grid(row=10, column=6, padx=5, pady=5)

# dob_entry = Entry(root, width=30)
# dob_entry.grid(row=10, column=1, pady=5)

label_nin = Label(root, text="NIN:")
label_nin.grid(row=11, column=0, padx=5, pady=5)
nin_entry = Entry(root, width=30)
nin_entry.grid(row=11, column=1, padx=5, pady=5)

label_employment_stat = Label(root, text="Choose your employment :")
label_employment_stat.grid(row=12, column=0, padx=5, pady=5)
em_entry = Combobox(width=29, justify='left', values=['Employed', 'Unemployed', 'Self-employed', 'Student'])
em_entry.grid(row=12, column=1, padx=5, pady=5)
# em_stat_entry = Entry(root, width=30)
# em_stat_entry.grid(row=12, column=1, pady=5)

submit = Button(root, text='Submit', command=result)
submit.grid(row=13, columnspan=2,  padx=5, pady=5)

saveinfo = Button(root, text="Save Data", command=savedata)
saveinfo.grid(row=14, columnspan=2,  padx=5, pady=5)

create_table()

root.mainloop()