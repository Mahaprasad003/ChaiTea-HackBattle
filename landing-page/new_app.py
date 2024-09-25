from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return (
        Style("""
            :root {
                --primary-color: #4a90e2;
                --secondary-color: #50e3c2;
                --text-color: #333;
                --light-bg: #f9f9f9;
                --dark-bg: #1a2a3a;
            }
            body {
                font-family: 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.6;
                color: var(--text-color);
                margin: 0;
                padding: 0;
                background-color: var(--dark-bg);
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 0 20px;
            }
            .header {
                background-color: white;
                padding: 1rem 0;
            }
            .header-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .logo {
                font-size: 1.5rem;
                font-weight: bold;
                color: var(--primary-color);
            }
            .nav a {
                color: var(--text-color);
                text-decoration: none;
                margin-left: 1.5rem;
            }
            .hero {
                background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
                color: white;
                padding: 4rem 0;
            }
            .hero-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .hero-text {
                max-width: 50%;
            }
            .hero h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
                line-height: 1.2;
            }
            .hero p {
                font-size: 1.1rem;
                margin-bottom: 2rem;
                opacity: 0.9;
            }
            .cta-button {
                display: inline-block;
                background-color: white;
                color: var(--primary-color);
                padding: 0.8rem 2rem;
                border-radius: 5px;
                text-decoration: none;
                font-weight: bold;
                transition: background-color 0.3s, color 0.3s;
            }
            .cta-button:hover {
                background-color: var(--secondary-color);
                color: white;
            }
            .hero-image {
                max-width: 45%;
            }
            .hero-image img {
                max-width: 100%;
                height: auto;
                border-radius: 10px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            }
            .features {
                background-color: white;
                padding: 4rem 0;
            }
            .features h2 {
                text-align: center;
                margin-bottom: 3rem;
                color: var(--primary-color);
            }
            .feature-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
            }
            .feature-card {
                background-color: var(--light-bg);
                border-radius: 8px;
                padding: 2rem;
                text-align: center;
                transition: transform 0.3s;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
            .feature-card h3 {
                color: var(--primary-color);
                margin-bottom: 1rem;
            }
            .feature-icon {
                font-size: 3rem;
                color: var(--secondary-color);
                margin-bottom: 1rem;
            }
            .stats {
                background-color: var(--dark-bg);
                color: white;
                padding: 4rem 0;
                text-align: center;
            }
            .stats h2 {
                margin-bottom: 3rem;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 2rem;
            }
            .stat-item h4 {
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
                color: var(--secondary-color);
            }
            .stat-item p {
                font-size: 1rem;
                opacity: 0.8;
                
            .footer {
                background-color: var(--dark-bg);
                color: white;
                padding: 3rem 0;
                text-align: center;
            }
            .footer-content {
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
            }
            .footer-logo {
                font-size: 1.2rem;
                font-weight: bold;
                color: var(--secondary-color);
            }
            .footer-links a {
                color: white;
                text-decoration: none;
                margin: 0 1rem;
            }
            .footer-contact {
                margin-top: 1rem;
            }
            .footer-contact a {
                color: var(--secondary-color);
                text-decoration: none;
            }
            .footer-social {
                margin-top: 1rem;
            }
            .footer-social a {
                color: white;
                text-decoration: none;
                margin: 0 0.5rem;
                font-size: 1.2rem;
            }
        """),
        Div(
            Div(
                Div(
                    Div("SkinSense AI", cls="logo"),
                    Div(
                        A("Features", href="#features"),
                        cls="nav"
                    ),
                    cls="header-content"
                ),
                cls="container"
            ),
            cls="header"
        ),
        Div(
            Div(
                Div(
                    Div(
                        H1("Unlock Your Skin's Potential with AI-Powered Analysis"),
                        P("Experience personalized skincare recommendations with our innovative Chrome extension. Upload photos, chat with our AI, and shop smarter - all while keeping your data private."),
                        A("Download Extension", href="#", cls="cta-button"),
                        cls="hero-text"
                    ),
                    Div(
                        Img(src="test.webp", alt="SkinSense AI Interface"),
                        cls="hero-image"
                    ),
                    cls="hero-content"
                ),
                cls="container"
            ),
            cls="hero"
        ),
        Div(
            Div(
                H2("Key Features", id="features"),
                Div(
                    Div(
                        Div("📷", cls="feature-icon"),
                        H3("Local Image Analysis"),
                        P("Analyze skin images privately, right in your browser.")
                    , cls="feature-card"),
                    Div(
                        Div("💬", cls="feature-icon"),
                        H3("Interactive Chatbot"),
                        P("Get personalized skincare advice through AI-powered conversations.")
                    , cls="feature-card"),
                    Div(
                        Div("🧪", cls="feature-icon"),
                        H3("Ingredient Analysis"),
                        P("Understand product ingredients and their effects on your skin.")
                    , cls="feature-card"),
                    Div(
                        Div("📊", cls="feature-icon"),
                        H3("Real-Time Evaluation"),
                        P("Receive instant feedback on product suitability while shopping.")
                    , cls="feature-card"),
                    Div(
                        Div("🔒", cls="feature-icon"),
                        H3("Privacy-First Approach"),
                        P("Enjoy all features without accounts or data collection.")
                    , cls="feature-card"),
                    Div(
                        Div("📚", cls="feature-icon"),
                        H3("Skincare Education"),
                        P("Learn about effective compounds and practices for skin health.")
                    , cls="feature-card"),
                cls="feature-grid"),
                cls="container"
            ),
            cls="features"
        ),
        Div(
            Div(
                H2("Empowering Users Worldwide"),
                Div(
                    Div(
                        H4("100K+"),
                        P("Active Users")
                    , cls="stat-item"),
                    Div(
                        H4("1M+"),
                        P("Skin Analyses")
                    , cls="stat-item"),
                    Div(
                        H4("95%"),
                        P("User Satisfaction")
                    , cls="stat-item"),
                cls="stats-grid"),
                cls="container"
            ),
            cls="stats"
        ),
        Div(
            Div(
                Div(
                    Div(
                        cls="footer-links"
                    ),
                    cls="footer-content"
                ),
                Div(
                    P("Contact us: Team ChaiTea"),
                    cls="footer-contact"
                ),

                P("© 2024 SkinSense AI. All rights reserved.", cls="footer-copyright"),
                cls="container",
                id="contact"
            ),
            cls="footer"
        ),
    )

serve()