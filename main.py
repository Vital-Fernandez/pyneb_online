import pyneb
import streamlit as st

import streamlit as st
import pyneb as pn

st.title("PyNeb Emissivity Calculator")

# Ion selection
ion_label = st.selectbox(
    "Select an ion (e.g. O3, N2, S2, H1):",
    ["O3", "N2", "S2", "H1", "He1", "Ar3", "Ne3"]
)

# Temperature and density inputs
tem = st.number_input("Electron Temperature (K)", min_value=100.0, max_value=30000.0, value=10000.0, step=100.0)
den = st.number_input("Electron Density (cm⁻³)", min_value=1.0, max_value=1e6, value=100.0, step=10.0)

# Line label input
line_label = st.text_input("Line label (e.g. 5007, 6584, 6563):", value="5007")

# Compute emissivity
if st.button("Compute Emissivity"):

    # Load appropriate ion type
    if ion_label in ["H1", "He1", "He2"]:
        ion = pn.RecAtom(ion_label[0], int(ion_label[1]))
    else:
        ion = pn.Atom(ion_label[:-1], int(ion_label[-1]))

    emissivity = ion.getEmissivity(tem=tem, den=den, wave=float(line_label))

    st.success(f"Emissivity for {ion_label} λ{line_label} at T={tem} K, n={den} cm⁻³: {emissivity:.2e} erg cm³ s⁻¹")



    # try:
    #     # Load appropriate ion type
    #     if ion_label in ["H1", "He1", "He2"]:
    #         ion = pn.RecAtom(ion_label[0], int(ion_label[1]))
    #     else:
    #         ion = pn.Atom(ion_label[:-1], int(ion_label[-1]))
    #
    #     emissivity = ion.getEmissivity(tem=tem, den=den, wave=line_label)
    #
    #     st.success(f"Emissivity for {ion_label} λ{line_label} at T={tem} K, n={den} cm⁻³: {emissivity:.2e} erg cm³ s⁻¹")
    # except Exception as e:
    #     st.error(f"Error: {e}")
