import streamlit as st
import pandas as pd
import plotly. export as px

from module14.bar_chart import filtered_df

if selected_author != "All":
    filtered_books_df = filtered-books_df[filtered_books_df['Author'] == selected_author]
if selected_year != "All":
        filtered_books_df = filtered - books_df[filtered_books_df['Year'] == selected_year]
if selected_genre != "All":
    filtered_books_df = filtered-books_df[filtered_books_df['Author'] == selected_genre]

filtered_books_df = filtered_books_df[
    (filtered_books_df['User Rating'] >= min_rating) & (filtered_books_df['Price'] <= max_price)

]

st.subheader("Summary Statistcs")
total_books = filtered_books_df.shape[0]
unique.titles = filtered_books_df['Name'].nunique()
average_rating = filtered_books_df['User Rating'].mean()
average_prive = filtered_books_df['Price'].mean()



col1 , col2 , col4 = st.columns(4)
col1.metric("Total Books" , total_books)
col2.metric("Total Titles" , total_titles)
col3.metric("Total Rating" , total_rating)
col4.metric("Total Price" , total_price)

st.subheader("Datasat Privew")
st.write(filtered_books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 selling books")
    top_titles = filtered_books_df['Name'].value_counts().head(10)
    st.bar_charts(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_titles = filtered_books_df['Author'].value_counts().head(10)
    st.bar_charts(top_authors)

st.subheader("Genre Distribution")
fig = px.pie(filtered_books_df, names='Genre', title='Most Liked Genre  (2009-2022', color='Genre',
             color_discrete_sequence=px.colors.sequntial.Plasma)
st.plotly_chart(fig)

st.subheader("Number of Fiction vs BNon-Fiction Books Over the Years")
size = filtered_books_df.groupby(['Year', 'Genre']).size().reset_index(name='Counts')
fig = px.bar(size, x='Year', y='Counts', color='Genre', title="Number of Fiction vs Non-Fiction Book from 2009-2022",
             color_discrete_sequence=px.colors.sequntial.Plasma, barmode='group')
st.plotly_chart(fig)

st.subheader("Top 15 authors by counts of books published (2009-2022)")
top_authors = filtered_books_df['Authors'].value.counts().head(15).reset_index()
top_authors.columns = ['Author' , 'Counts']
fig = px.bar(top_authors , x='Counts' , y='Author' , orientation='h',
            title = 'Top 15 authors by counts of books published',
            lables={'Count': 'Counts of books published' , 'Author': 'Author'},
            color = 'Count', color_countinous_scale=px.colors.sequntial.Plasma)
st.plotly_chart(fig)

st.subheader('Filter Data by Genre')
genre_filter = st.selectbox("Select Genre", filtered_books_df['Genre'].unique())
filtered_genre_df = filtered_books_df[filtered_books_df['Genre'] == genre_filter]
st.write(filtered_genre_df)










