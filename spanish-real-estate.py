import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for housing prices over the past decade
years = list(range(2012, 2023))
housing_prices = [150000, 160000, 170000, 180000, 190000, 200000, 210000, 220000, 230000, 240000, 250000]

# Sample data for potential impact of global factors
factors = ['Global Economic Climate', 'Brexit Negotiations', 'Housing Affordability', 'Overdevelopment', 'Climate Change']
impact_scores = [3, 2, 4, 3, 5]

# Create a DataFrame
data = {'Year': years, 'Housing Prices (€)': housing_prices}
df_prices = pd.DataFrame(data)

# Sidebar with information from the article
st.sidebar.title('Spanish Real Estate Market Concerns')
st.sidebar.image('https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Flag_of_Spain.svg/1200px-Flag_of_Spain.svg.png', use_column_width=True)
st.sidebar.markdown("""
The Spanish real estate market has been through various challenges over the past decade. 
Some major concerns include the potential impact of the global economic climate, Brexit negotiations, housing affordability, overdevelopment, and climate change.
""")

# Main content
st.title('Spanish Real Estate Market Analysis')

# Line chart for housing prices
st.subheader('Housing Prices Over the Past Decade')
fig_prices, ax_prices = plt.subplots()
ax_prices.plot(df_prices['Year'], df_prices['Housing Prices (€)'], marker='o')
ax_prices.set_xlabel('Year')
ax_prices.set_ylabel('Housing Prices (€)')
st.pyplot(fig_prices)

# Bar chart for potential impact of global factors
st.subheader('Potential Impact of Global Factors')
fig_factors, ax_factors = plt.subplots()
ax_factors.bar(factors, impact_scores, color='skyblue')
ax_factors.set_xlabel('Factors')
ax_factors.set_ylabel('Impact Score')
ax_factors.set_ylim(0, 5)
# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')
st.pyplot(fig_factors)

# Conclusion
st.subheader('Conclusion')
st.markdown("""
The Spanish real estate market is facing challenges such as housing affordability, overdevelopment, and the impact of global factors like the economic climate and Brexit negotiations. 
Stakeholders must closely monitor these issues to mitigate potential market impacts.
""")

# Additional information
st.sidebar.markdown("""
* Article: [Link to the Article](https://medium.com/@ddanon_37094/spanish-real-estate-over-the-next-10-years-11eba3aec858)

* Author: [David Danon](https://medium.com/@ddanon_37094)
""")
