import streamlit as st

def page_4_hypothesis_and_validation_body():

    st.write("### Project Hypothesis and Validation")
	
    st.info(
    f"Before the analysis, we knew we wanted this page to describe "
    f"each project hypothesis, the conclusions, and how we validated "
    f"each. After the data analysis, we can report that: \n\n "
	)
    st.success(
    f"1 - We suspect houses with larger square footing may have had "
    f"a higher sales price.\n "
	f"* Correct. There is a strong correlation between the two. "
    f"The correlation study on the House Sale Price Study "
    f"supports this hypothesis.\n\n"
    f"2 - We suspect that between houses with similar square footing, "
    f"those with a more recent Year Built date may have had a higher "
    f"sales price.\n "
	f"* Correct. There is moderate correlation between the two. "
    f"The correlation study on the House Sale Price Study supports this. "
    f"It's worth noting that houses with a more recent Year Built date are "
    f"typically higher in Overall Quality which has much stronger correlation"
    f"to Sale Price.\n\n"
    f"3 - We suspect that between houses with similar square footing and "
    f"year built date, those with a more recent Remodel date may have had a "
    f"higher sales price.\n"
	f"* Correct. There is weak to moderate correlation between the two. "
    f"Again, it is worth noting that there is a relationship between houses "
    f"with a more recent Remodel date being higher in Overall Quality\n\n"
    f"4 - We suspect that between houses with similar square footing, "
    f"those with higher quality and condition scores may have had a higher "
    f"sales price.\n "
	f"* Correct. There is a strong correlation between the two variables."
    f"The correlation study on the House Sale Price Study supports this hypothesis."
    )