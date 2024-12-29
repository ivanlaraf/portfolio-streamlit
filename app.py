import streamlit as st
import streamlit_shadcn_ui as ui



profile_pic="assets/profile-pic.png"
resume_file="assets/resume_ivanlara.pdf"
resume_file_name="CV_ivanlara.pdf"

#Gotta Read the PDF File

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#Page configuration
layout = "centered"
page_title = "My Webpage | Ivan Lara"
page_icon= "☁️"
name="Hi 👋"
description="""
    My name is Ivan, a passionate and Skilled future DevOps Engineer with knowledge in infrastructure, provisioning, automation and monitoring. I have completed and been certified by AWS, Hashicorp and LPI. Have hands on pojects working with tools such as Terraform, AWS Console, Python, Linux and Git as well as maintaining best practices using the cloud. I enjoy meeting new people and see new perspectives, i like discussing new technologies and other things, for me, there is a lot to learn, a lot of problems to be solved, and much more to build on, so far and for what I've got, I'm very grateful.
"""""
email="ivan.corporate@hotmail.com"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
css_file="styles/main.css"
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    """,
    unsafe_allow_html=True,
)

proyectos = {
    "🏆 Lets Deploy a static website using S3 Bucket, CloudFront, Amplify and let's add a fail routing policy":
    "https://www.youtube.com",
     "🏆 How I beated the Learn to Cloud Challenge":
    "https://www.google.com.py",
     "🏆 Let's use Amazon Connect to create a contact center":
    "https://www.google.com.py",
     "🏆 Create a chatbot using AWS":
    "https://www.google.com.py"

}



social_media = {
    "GitHub": {"url": "https://github.com", "icon": "fab fa-github"},
    "All Projects": {"url": "https://twitter.com", "icon": "fa-brands fa-dev"},
    "LinkedIn": {"url": "https://linkedin.com", "icon": "fab fa-linkedin"},
}

st.markdown(
    """
    <div class="social-buttons">
    """,
    unsafe_allow_html=True,
)



cols = st.columns(len(social_media))
for index, (platform, info) in enumerate(social_media.items()):
    with cols[index]:
        st.markdown( f"""
            <a href="{info['url']}" target="_blank" style="text-decoration:none;">
                <button style="
                    display: flex; 
                    align-items: center; 
                    gap: 10px; 
                    padding: 10px 20px; 
                    border: none; 
                    background-color: #007BFF; 
                    color: white; 
                    border-radius: 5px; 
                    font-size: 16px; 
                    cursor: pointer;">
                    <i class="{info['icon']}" style="font-size:20px;"></i>
                    {platform}
                </button>
            </a>
            """,
            unsafe_allow_html=True,)

st.markdown(
    """
    </div>
    """,
    unsafe_allow_html=True,
)

      
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="image-container">', unsafe_allow_html=True)
    st.image(profile_pic, width=230)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.write(name)
    st.write(description)
    st.download_button(
        label="📄 Download CV",
        data=PDFbyte,
        file_name=resume_file_name,
        mime="application/pdf"
    )
    st.write("📭",email)

st.write('##')
st.subheader("Take a look some of my projects")
st.write("---")

for project, link in proyectos.items():
    st.write(f"[{project}]({link})")


st.write('##')
st.subheader('Tech Skills & Certifications')
st.write('---')
st.write(
    """
-  🐍 Programming language & Framework : <i class="fab fa-python" style="font-size:20px;"></i> Python, <i class="fab fa-react" style="font-size:20px;"></i> Streamlit
-  ☁️ Cloud Provider : <i class="fab fa-aws" style="font-size:20px;"></i> Amazon Web Services
-  ⚙️ DevOps Tools : <i class="fas fa-tools" style="font-size:20px;"></i> Terraform, <i class="fa-brands fa-github"></i> Github, <i class="fab fa-github-square"></i>GithubActions, <i class="fa-brands fa-watchman-monitoring"></i> Prometheus & Grafana
-  🏆 Certifications : 
    <ul>
        <li><i class="fas fa-certificate" style="color:gold;"></i> <a href="https://www.credly.com/badges/8dc744b5-dd71-4ed8-8a78-5a04c0aa9326/linked_in_profile" target="_blank" style="text-decoration:none; color:#0073e6;">AWS Solutions Architect - Associate</a></li>
        <li><i class="fas fa-certificate" style="color:gold;"></i> <a href="https://cs.lpi.org/caf/Xamman/certification/verify/LPI000605289/f2tpemw4xj" target="_blank" style="text-decoration:none; color:#0073e6;">LPI Linux Essentials</a></li>
        <li><i class="fas fa-certificate" style="color:gold;"></i> <a href="https://www.credly.com/badges/a2b0c42c-268e-4a9a-ba0d-720059bd91f8/linked_in_profile" target="_blank" style="text-decoration:none; color:#0073e6;">HashiCorp Certified: Terraform Associate</a></li>
        <li><i class="fas fa-certificate" style="color:gold;"></i> <a href="https://www.credly.com/badges/7cc75f9d-915f-48c2-97f5-e21ff371935a/linked_in_profile" target="_blank" style="text-decoration:none; color:#0073e6;">AWS Cloud Practitioner</a></li>

    </ul>
    """,
    
    unsafe_allow_html=True,

)

st.write('##')
st.subheader("Experience")
st.write('---')

st.write("💼","**Senior IT Analyst - Anheusher Busch Inbev**")
st.write("Present")
st.write(
    """
- ▶️ Amazon Connect Administration
- ▶️ Review Cloudwatch logs
- ▶️ Salesforce Administration Create, delete and grant permission to users
- ▶️ Solve tickets using ServiceNow
- ▶️ PRTG Monitoring
- ▶️ Azure AD administration, Create, delete and disable Users
- ▶️ Hardware and Software Diagnostic
- ▶️ Maintain inventory of user devices

    """
)

st.write("💼","**IT Helpdesk - TEISA**")
st.write("08/2022 - 06/2023")
st.write(
    """
- ▶️ Forti Mail Administration
- ▶️ Forti EMS: Managing endpoints, status, vulnerabilities and antivirus
- ▶️ Documentation of Most common problems
- ▶️ SAP Administration and Troubleshooting
- ▶️ Install and Update Software
- ▶️ Synology NAS Administration

    """
)


st.write("💼","**IT Support - Frigorifico Guarani**")
st.write("05/2020 - 08/2022")
st.write(
    """
- ▶️ Repair Laptops and PCs
- ▶️ Antivirus administration
- ▶️ Mikrotik Router administration
- ▶️ Huawei Cloud administration
- ▶️ Active Directory Administration

    """
)

st.write("💼","**IT Trainee - Inflight Catering**")
st.write("02/2018 - 03/2020")
st.write(
    """
- ▶️ Cpanel Administration
- ▶️ Repair Laptops and PCs
- ▶️ Unifi devices configuration
- ▶️ Documentation of most common problems for the user

    """
)
