def search_tab():
    import streamlit as st
    import requests

    st.header("🌐 Web Search Assistant")

    query = st.text_input("What do you want to search for?")
    search = st.button("Search Web")

    if search and query:
        with st.spinner("Searching the web..."):
            try:
                # Using DuckDuckGo instant answer API
                response = requests.get(
                    "https://api.duckduckgo.com/",
                    params={"q": query, "format": "json", "no_redirect": 1}
                )
                data = response.json()
                abstract = data.get("AbstractText") or "No direct summary found."

                st.subheader("Summary:")
                st.write(abstract)

                if "RelatedTopics" in data:
                    st.subheader("Related Links:")
                    for topic in data["RelatedTopics"][:5]:
                        if "Text" in topic and "FirstURL" in topic:
                            st.markdown(f"- [{topic['Text']}]({topic['FirstURL']})")
            except Exception as e:
                st.error(f"Web search failed: {e}")
