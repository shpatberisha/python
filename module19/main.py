if selected_author != "All"
    filtered_books_df = filtered-books_df[filtered_books_df['Author'] == selected_author]
if selected_year != "All":
        filtered_books_df = filtered - books_df[filtered_books_df['Year'] == selected_year]
if selected_genre != "All"
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
