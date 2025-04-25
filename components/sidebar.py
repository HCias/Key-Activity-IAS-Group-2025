import streamlit as st

def apply_sidebar_css():
    """Apply CSS styling for sidebar"""
    st.markdown("""
    <style>
        section[data-testid="stSidebar"] > div {
            background-color: #f8f9fa;
            padding: 1rem;
        }
        
        /* Menu title styling */
        .menu-header {
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 15px;
            color: #333;
            padding-left: 10px;
        }
        
        /* Custom button styling for menu */
        div[data-testid="element-container"] div[data-testid="stHorizontalBlock"] {
            gap: 0 !important;  
        }
        
        /* Target button specifically */
        button[kind="secondary"] p, button[kind="primary"] p {
            text-align: left !important;
            width: 100%;
            margin-left: 0;
        }
        
        div[data-testid="stVerticalBlock"] button[kind] {
            display: block;
            text-align: left;
            width: 100%;
            border-radius: 4px;
            margin-bottom: 8px;
            padding: 10px !important;
        }
        
        /* Specific alignment for text inside button */
        button[kind] div[data-testid="stMarkdownContainer"] {
            text-align: left !important; 
            display: block;
            width: 100%;
        }
        
        button[kind] div[data-testid="stMarkdownContainer"] p {
            text-align: left !important;
            width: 100%;
            margin-left: 0;
        }
    </style>
    """, unsafe_allow_html=True)

def sidebar():
    """Create sidebar with navigation menu"""
    with st.sidebar:
        # Judul Menu
        st.markdown('<div class="menu-header">Menu</div>', unsafe_allow_html=True)
        
        # Inisialisasi session state jika belum ada
        if 'menu' not in st.session_state:
            st.session_state['menu'] = "Dashboard"
        
        # Daftar menu
        menu_items = ["Dashboard", "Detail", "Capaian Deskriptif"]
        
        # Gunakan tombol sederhana
        for item in menu_items:
            selected = st.session_state['menu'] == item
            button_style = "primary" if selected else "secondary"
            
            # st.write di depan tombol untuk menambah padding kiri
            cols = st.columns([0.05, 0.95])
            with cols[1]:
                if st.button(
                    item,
                    key=f"menu_{item}",
                    use_container_width=True,
                    type=button_style
                ):
                    st.session_state['menu'] = item
                    st.rerun()
    
    return st.session_state['menu']
