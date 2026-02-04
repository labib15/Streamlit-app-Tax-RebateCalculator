import streamlit as st

#st.markdown( """ <style> div[data-baseweb="input"] input { font-size: 21px; /* Change number input text size */ } </style> """, unsafe_allow_html=True )
st.title("Tax & Rebate Calculator")

options = ["Private Job", "Govt Job", "Other"]
st.markdown("<div style='font-size:20px; font-weight:bold;margin-bottom:0;'> Please select your profession </div>",
                unsafe_allow_html=True)
selected_option = st.selectbox("Job Type:",options)
st.write(f"You selected: :orange[{selected_option}]")

def income_tax(income):
    if income <= 375000:
        tax_due = 0
    elif income <= 675000:
        tax_due = (income - 375000) * 0.10
    elif income <= 1075000:
        tax_due = (300000 * 0.10) + ((income - 675000) * 0.15)
    elif income <= 1575000:
        tax_due = (300000 * 0.10) + (400000 * 0.15) + ((income - 1075000) * 0.20)
    elif income <= 3575000:
        tax_due = (300000 * 0.10) + (400000 * 0.15) + (500000 * 0.20) + ((income - 1575000) * 0.25)
    else:
        tax_due = (300000 * 0.10) + (400000 * 0.15) + (500000 * 0.20) + (2000000 * 0.25) + ((income - 3575000) * 0.30)

    return tax_due



if selected_option == "Private Job":
    st.markdown("<div style='font-size:18px; font-weight:bold;margin-bottom:0;'>Please input the total yearly income from job </div>",
                unsafe_allow_html=True)
    total_amount = st.number_input(
        "Tk:",
        min_value=0,
        step=10000
    )
    taxable_amount = int(total_amount - min(500000, int((1 / 3) * total_amount)))


if selected_option == "Govt Job":
    st.markdown(
        "<div style='font-size:18px; font-weight:bold;margin-bottom:0;'>Please input the total yearly income from job </div>",
        unsafe_allow_html=True)
    total_amount = st.number_input(
        "Tk:",
        min_value=0,
        step=10000
    )
    taxable_amount = int(total_amount - min(500000, int((1 / 3) * total_amount)))

if selected_option == "Other":
    st.markdown(
        "<div style='font-size:18px; font-weight:bold;margin-bottom:0;'>Please input the total yearly income from 'Other' sources</div>",
        unsafe_allow_html=True)
    total_amount = st.number_input(
        "TK:",
        min_value=0,
        step=10000
    )
    taxable_amount = total_amount




# Show maximum rebate and required investment
if taxable_amount > 0:
    max_rebate = taxable_amount * 0.03
    max_investment_needed = int(max_rebate / 0.15)

    st.write(f"**Total Taxable income:** TK {taxable_amount:,.2f}")
    st.write(f"**Total Tax Due:** :red[Tk {income_tax(taxable_amount):,.2f}]")
    st.write(f"**Maximum possible rebate through investment:** :green[TK {max_rebate:,.2f}]")
    st.write(f"**Minimum investment required for this rebate:** :blue[TK {max_investment_needed:,.2f}]")

    st.markdown("---")
    st.header("Rebate-able Investment Data")

    # DPS input
    st.markdown("<div style='font-size:18px; font-weight:bold;margin-bottom:0;'> 1) Please input the DPS amount</div>",
                unsafe_allow_html=True)
    dps_amount = st.number_input("DPS = Deposit Pension Scheme. Monthly Investment", min_value=0, step=500)
    dps_amount_approved = min(120000, dps_amount)
    st.write(f"Approved DPS amount for rebate investment: TK {dps_amount_approved:,}")
    if (dps_amount > 120000):
        st.write("*DPS investment is capped at Tk. 1,20,000*")




    # Savings Certificate input
    st.markdown("<div style='font-size:18px; font-weight:bold;margin-bottom:0;'> 2) Please input the Savings Certificate (SanchayPatra) investment amount</div>",
                unsafe_allow_html=True)
    savingsCertificate_amount = st.number_input("Savings Certificate = Government FDR. One time investment for fixed time", min_value=0, step=10000)
    savingsCertificate_amount_approved = min(500000, savingsCertificate_amount)
    st.write(f"Approved Savings Certificate amount for rebate investment: TK {savingsCertificate_amount_approved:,}")
    if (savingsCertificate_amount > 500000):
        st.write("*Savings Certificate investment is capped at Tk. 5,00,000*")

    # Provident Fund input
    st.markdown(
        "<div style='font-size:18px; font-weight:bold;margin-bottom:0;'> 3) Please input the provident fund amount (employer + employee contribution)</div>",
        unsafe_allow_html=True)
    pf_amount = st.number_input("", min_value=0, step=1000)
    pf_amount_approved = pf_amount
    st.write(f"Approved Provident Fund amount for rebate investment: TK {pf_amount_approved:,}")

    # Total rebatable investment
    total_rebatable_investment = dps_amount_approved + savingsCertificate_amount_approved + pf_amount_approved

    st.markdown("---")
    st.header("Rebate Calculation")

    actual_rebate = min(
        taxable_amount * 0.03,
        total_rebatable_investment * 0.15,
        1000000
    )

   # st.error(f"**Total Income Tax Due:** TK {income_tax(taxable_amount):,}")
    st.info(f"**Total Rebatable Investment:** TK {total_rebatable_investment:,}")
    st.success(f"**Actual rebate received:** TK {actual_rebate:,.2f}")



    st.markdown("-----")
    st.header("Final Tax Calculation")
    # Source TaxProvident Fund input
    st.markdown(
        "<div style='font-size:18px; font-weight:bold;margin-bottom:0;'> Please input the total source tax </div>",
        unsafe_allow_html=True)
    st_amount = st.number_input("Source Tax = Tax cut at source of payment", min_value=0, step=10)
    st_amount_approved = st_amount
    st.write(f"Total Source Tax: TK {st_amount_approved:,}")

    st.write(f"Total Rebate: TK {actual_rebate:,.2f}")

    st.write(f"Total Income Tax Due: TK {income_tax(taxable_amount):,}")


    st.error(f"Net Tax to be paid: TK {max(income_tax(taxable_amount) - actual_rebate - st_amount_approved,0):,.2f}")
