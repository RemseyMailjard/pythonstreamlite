import streamlit as st

# Titel van de applicatie
st.title("Dagelijkse Hydratatie Checklist")

# Lijst met hydratatietaken
checklist_items = [
    "07:00 - Drink 1 groot glas water",
    "09:00 - Drink 1 glas water",
    "10:30 - Drink 1 glas water",
    "12:00 - Drink 1 groot glas water tijdens de lunch",
    "14:00 - Drink 1 glas water",
    "15:30 - Drink 1 glas water",
    "17:00 - Drink 1 glas water",
    "19:00 - Drink 1 groot glas water tijdens het avondeten",
    "20:30 - Drink 1 glas water",
    "22:00 - Drink 1 glas water",
    "23:00 - Drink 1 glas water",
    "Tijdens de nacht - Drink water als je wakker wordt om naar het toilet te gaan",
    "Bij sporten - Drink extra water om vochtverlies te compenseren"
]

# Opslaan van afvinkstatussen
checked_items = [st.checkbox(item) for item in checklist_items]

# Controleer de voortgang
if st.button("Checklist Controleren"):
    incomplete_items = [item for item, checked in zip(checklist_items, checked_items) if not checked]
    if incomplete_items:
        st.warning("Je hebt nog niet alles afgevinkt:\n" + "\n".join(incomplete_items))
    else:
        st.success("Je hebt alles afgevinkt. Goed gedaan!")
