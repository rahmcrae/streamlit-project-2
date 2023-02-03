import streamlit as st

def page_1():
    st.title("This is page 1")
    return
def page_2():
    st.title("This is page 2")
    return
def page_3():
    st.title("This is page 3")
    return
def page_4():
    st.title("This is page 4")
    return
def page_5():
    st.title("This is page 5")
    return
def navigation_menu():
    menu = ["Page 1", "Page 2", "Page 3", "Page 4", "Page 5",]
    selection = st.sidebar.selectbox("Select a page", menu)
    if selection == "Page 1":
        page_1()
    elif selection == "Page 2":
        page_2()
    elif selection == "Page 3":
        page_3()
    elif selection == "Page 4":
        page_4()
    elif selection == "Page 5":
        page_5()            
        return
    
if __name__ == "__main__":
    navigation_menu()

