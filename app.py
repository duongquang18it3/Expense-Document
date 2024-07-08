import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="")

# Create a placeholder for the uploaded image
uploaded_image = None

# Create the two-column layout
col1, col2 = st.columns([4, 6])

# Subcategory options
subcategory_options = [
    "Expense categories", "Food and Groceries", "Healthcare", "Insurance", 
    "Marketing and Advertising", "Meals and Entertainment", "Mortgage", 
    "Office Supplies & Expenses", "Other expenses", "Professional Services", 
    "Rent", "Salaries and Wages", "Subscriptions", "Taxes", "Tools & Hardware", 
    "Training and Education", "Transportation and Travel", "Utilities", 
    "Vehicles and Gas"
]

# Subcategory options
currency_options = [
    "AFN - Afghan afghani",
    "ALL - Albanian lek",
    "DZD - Algerian dinar",
    "AOA - Angolan kwanza",
    "ARS - Argentine peso",
    "AMD - Armenian dram",
    "AWG - Aruban florin",
    "AUD - Australian dollar",
    "AZN - Azerbaijani manat",
    "BSD - Bahamian dollar",
    "BHD - Bahraini dinar",
    "BDT - Bangladeshi taka",
    "BBD - Barbadian dollar",
    "BYN - Belarusian ruble",
    "BZD - Belize dollar",
    "BMD - Bermudian dollar",
    "BTN - Bhutanese ngultrum",
    "BOB - Bolivian boliviano",
    "BAM - Bosnia and Herzegovina convertible mark",
    "BWP - Botswana pula",
    "BRL - Brazilian real",
    "BND - Brunei dollar",
    "BGN - Bulgarian lev",
    "MMK - Burmese kyat",
    "BIF - Burundian franc",
    "XPF - CFP franc",
    "KHR - Cambodian riel",
    "CAD - Canadian dollar",
    "CVE - Cape Verdean escudo",
    "KYD - Cayman Islands dollar",
    "XAF - Central African CFA franc",
    "CLP - Chilean peso",
    "COP - Colombian peso",
    "KMF - Comorian franc",
    "CDF - Congolese franc",
    "CRC - Costa Rican colón",
    "HRK - Croatian kuna",
    "CUC - Cuban convertible peso",
    "CUP - Cuban peso",
    "CZK - Czech koruna",
    "DKK - Danish krone",
    "DJF - Djiboutian franc",
    "DOP - Dominican peso",
    "XCD - Eastern Caribbean dollar",
    "EGP - Egyptian pound",
    "ERN - Eritrean nakfa",
    "ETB - Ethiopian birr",
    "EUR - Euro",
    "FKP - Falkland Islands pound",
    "FJD - Fijian dollar",
    "GMD - Gambian dalasi",
    "GEL - Georgian lari",
    "GHS - Ghanaian cedi",
    "GIP - Gibraltar pound",
    "XAU - Gold (troy ounce)",
    "GTQ - Guatemalan quetzal",
    "GGP - Guernsey pound",
    "GNF - Guinean franc",
    "GYD - Guyanese dollar",
    "HTG - Haitian gourde",
    "HNL - Honduran lempira",
    "HKD - Hong Kong dollar",
    "HUF - Hungarian forint",
    "ISK - Icelandic króna",
    "INR - Indian rupee",
    "IDR - Indonesian rupiah",
    "IRR - Iranian rial",
    "IQD - Iraqi dinar",
    "ILS - Israeli new shekel",
    "JMD - Jamaican dollar",
    "JPY - Japanese yen",
    "JEP - Jersey pound",
    "JOD - Jordanian dinar",
    "KZT - Kazakhstani tenge",
    "KES - Kenyan shilling",
    "KWD - Kuwaiti dinar",
    "KGS - Kyrgyzstani som",
    "LAK - Lao kip",
    "LBP - Lebanese pound",
    "LSL - Lesotho loti",
    "LRD - Liberian dollar",
    "LYD - Libyan dinar",
    "MOP - Macanese pataca",
    "MKD - Macedonian denar",
    "MGA - Malagasy ariary",
    "MWK - Malawian kwacha",
    "MYR - Malaysian ringgit",
    "MVR - Maldivian rufiyaa",
    "IMP - Manx pound",
    "MRU - Mauritanian ouguiya",
    "MUR - Mauritian rupee",
    "MXN - Mexican peso",
    "MDL - Moldovan leu",
    "MNT - Mongolian tögrög",
    "MAD - Moroccan dirham",
    "MZN - Mozambican metical",
    "NAD - Namibian dollar",
    "NPR - Nepalese rupee",
    "ANG - Netherlands Antillean guilder",
    "TWD - New Taiwan dollar",
    "NZD - New Zealand dollar",
    "NIO - Nicaraguan córdoba",
    "NGN - Nigerian naira",
    "NOK - Norwegian krone",
    "OMR - Omani rial",
    "PKR - Pakistani rupee",
    "PAB - Panamanian balboa",
    "PGK - Papua New Guinean kina",
    "PYG - Paraguayan guaraní",
    "PEN - Peruvian sol",
    "PHP - Philippine peso",
    "PLN - Polish złoty",
    "GBP - Pound sterling",
    "QAR - Qatari riyal",
    "CNY - Renminbi",
    "RON - Romanian leu",
    "RUB - Russian ruble",
    "RWF - Rwandan franc",
    "SHP - Saint Helena pound",
    "SVC - Salvadoran colón",
    "WST - Samoan tālā",
    "SAR - Saudi riyal",
    "RSD - Serbian dinar",
    "SCR - Seychellois rupee",
    "SLL - Sierra Leonean leone",
    "XAG - Silver (troy ounce)",
    "SGD - Singapore dollar",
    "SBD - Solomon Islands dollar",
    "SOS - Somali shilling",
    "ZAR - South African rand",
    "KRW - South Korean won",
    "SSP - South Sudanese pound",
    "XDR - Special drawing rights",
    "LKR - Sri Lankan rupee",
    "SDG - Sudanese pound",
    "SRD - Surinamese dollar",
    "SZL - Swazi lilangeni",
    "SEK - Swedish krona",
    "CHF - Swiss franc",
    "SYP - Syrian pound",
    "STN - São Tomé and Príncipe dobra",
    "TJS - Tajikistani somoni",
    "TZS - Tanzanian shilling",
    "USDT - Tether",
    "THB - Thai baht",
    "TOP - Tongan paʻanga",
    "TTD - Trinidad and Tobago dollar",
    "TND - Tunisian dinar",
    "TRY - Turkish lira",
    "TMT - Turkmenistan manat",
    "USDC - USD Coin",
    "UGX - Ugandan shilling",
    "UAH - Ukrainian hryvnia",
    "AED - United Arab Emirates dirham",
    "USD - United States dollar",
    "UYU - Uruguayan peso",
    "UZS - Uzbekistani soʻm",
    "VUV - Vanuatu vatu",
    "VES - Venezuelan bolívar",
    "VND - Vietnamese đồng",
    "XOF - West African CFA franc",
    "YER - Yemeni rial",
    "ZMW - Zambian kwacha",
    "ZWL - Zimbabwean dollar"
]

# Create the form in the left column
with col1:
    with st.form("expense_report_form"):
        

        merchant = st.text_input(label="Merchant", value="")
        date = st.date_input(label="Date")
        document_category = st.selectbox(
            label="Document Category",
            options=["Expenses", "Income", "Bank statements", "Documents"]
        )
        subcategory = st.selectbox(label="Subcategory", options=subcategory_options)

        # Show text input for other subcate gory if 'Other' is selected
        
        new_subcategory = st.text_input("Please specify other subcategory if necessary")

        payment_method = st.text_input(label="Payment Method", value="")
        reference = st.text_input(label="Reference", value="")
        tax_calculation = st.radio(label="Tax Calculation", options=["Tax Included", "Tax Excluded"])  
        value = st.number_input(label="Value", value=0.00)
        tax_amount = st.number_input(label="Tax amount", value=0.00)
        # Calculate tax percentage
        tax_percentage = (tax_amount / value) * 100 if value != 0 else 0

        # Display tax percentage
        st.write(f"= {tax_percentage:.2f}%")
        currency = st.selectbox(label="Currency", options=currency_options)
        detail = st.text_input(label="Detail", value="")
        document_tag = st.text_input(label="Document tags", value="")
        
        submitted = st.form_submit_button("Submit")
        # Check if the form has been submitted
        if submitted:
            # Get the form values
            form_data = {
                "Merchant": merchant,
                "Date": date,
                "Document Category": document_category,
                "Subcategory": subcategory,
                "Payment Method": payment_method,
                "Reference": reference,
                "Tax Calculation": tax_calculation,
                "Value": value,
                "Currency": currency
            }

            # Process the form data
            # ...

            # Display a message to the user
            st.success("Expense report submitted successfully!")

# Create the image upload section in the right column
with col2:
    image_file = st.file_uploader("Upload Invoice or Receipt", type=["jpg", "jpeg", "png"])

    if image_file is not None:
        uploaded_image = Image.open(image_file)
        st.image(uploaded_image, width=800)
