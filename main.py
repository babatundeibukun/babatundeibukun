from flask import Flask, render_template
import datetime
import calendar
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME']  # Optional to ignore certain files
app.config['FREEZER_RELATIVE_URLS'] = True  # Ensure URLs are relative


# Define your @freezer.register_generator
@freezer.register_generator
def project_details():
    for project_id in projects.keys():
        yield {'project_id': project_id}


# Define your project data
projects = {
    1: {
        'title': 'Chatbot for Riad Kitchen',
        'date': 'April 24, 2017',
        'description': """
                    <p>The project is a chatbot designed specifically for Riad's Kitchen, a Moroccan culinary store.
                    This innovative chatbot has been integrated with Telegram, offering users a seamless and intuitive 
                    way to interact with the menu and manage their orders using natural language.</p>

                    <h3>Key Features of the Chatbot:</h3> <ul> <li><strong>Order Placement:</strong> Users can 
                    effortlessly place orders from the menu by simply conversing with the chatbot in natural 
                    language.</li> <li><strong>Order Modification:</strong> The chatbot enables users to add 
                    additional items to their orders, enhancing their ordering experience without the need for manual 
                    updates.</li> <li><strong>Order Customization:</strong> If users decide to modify their orders, 
                    such as removing an item, they can do so through a natural language request, e.g., 
                    "Remove Chicken Tagine".</li> <li><strong>Order Confirmation and Tracking:</strong> After placing 
                    an order, the details are processed and stored in an SQL database, which automatically calculates 
                    the total amount and communicates it back to the user. Additionally, users can track their orders 
                    in real-time, receiving updates on the preparation and delivery status.</li> 
                    <li><strong>Real-time Updates:</strong> The chatbot keeps users informed about their order 
                    status, whether it's being prepared or is in transit, ensuring a transparent and reassuring 
                    ordering process.</li> </ul> """
        ,
        'image': 'static/images/chatbot.png',
        'technologies': ['Python', 'NLP technologies', 'Telegram API for integrating into the bot into telegram',
                         'MySQL Workbench '
                         'for database '
                         'management',
                         'Google Dialogflow for conversational user interfaces'],
        'github_url': 'https://github.com/babatundeibukun/FoodChatBot',
        'video_url': 'https://www.youtube.com/embed/g_Le3rak6lI'
    },
    2: {
        'title': 'End-2-End ML Price Prediction Project',
        'date': 'July 15, 2020',
        "description": """
        <p>I developed a comprehensive <strong>end-to-end machine learning project</strong> designed to predict real estate prices in India, encompassing both the front end and back end. This ambitious endeavor has been one of my most challenging yet rewarding experiences, significantly enhancing my technical skills and industry readiness.</p>
        
        <h3>Key Highlights of the Project:</h3>
        
        <h4>1. Data Cleaning & Feature Engineering:</h4>
        <ul>
        <li>Preprocessed and transformed a real estate dataset from Kaggle to ensure its usability.</li>
        <li>Implemented advanced feature engineering techniques, including feature creation and dimensionality reduction.</li>
        </ul>
        
        <h4>2. Model Building & Optimization:</h4>
        <ul>
        <li>Conducted a rigorous evaluation of multiple models using <strong>K-Fold Cross Validation</strong> and <strong>Grid Search CV</strong>.</li>
        <li>Achieved an impressive <strong>91% accuracy</strong> with Linear Regression as the final model.</li>
        </ul>
        
        <h4>3. Advanced Outlier Detection:</h4>
        <ul>
        <li>Applied domain-specific knowledge to identify and remove anomalies, maintaining the dataset's integrity.</li>
        </ul>
        
        <h4>4. Full System Development:</h4>
        <ul>
        <li>Designed a <strong>user-friendly frontend</strong> that allows users to input property details and instantly receive price predictions.</li>
        <li>Built a robust backend using <strong>Flask</strong> to manage data processing and deliver accurate predictions seamlessly.</li>
        </ul>
        
        <h4>5. Deployment to Cloud</h4>
        <ul>
        <li> Deployed the project to the cloud using AWS EC 2</li>
        """
        ,
        'image': 'static/images/ml_price_prediction.png',
        'technologies': ['Python', 'Pandas & NumPy', 'Scikit-learn',
                         'Flask : A Python web framework for creating the backend API and serving predictions',
                         'HTML, CSS, and JavaScript :The fundamental technologies for building the user interface',
                         'AWS EC2 for hosting flask application',
                         'Nginx: As a reverse proxy and web server for handling static files and routing requests'],
        'github_url': 'https://github.com/babatundeibukun/price_predict_ML_project',
        'video_url': 'https://www.youtube.com/embed/9hgH8S1tzWc'  # Add video URL here
    },
    3: {
        'title': 'Deep Learning Project: AI-Powered Image Classification for Potato Leaf Disease Detection',
        'date': 'July 15, 2020',
        "description": """
            <h2>AI-Powered Image Classification for Potato Leaf Disease Detection</h2>
            <p>This project presents an advanced <strong>deep learning solution</strong> designed to revolutionize agricultural disease management. By leveraging state-of-the-art convolutional neural networks (CNNs), the system classifies potato leaves into three categories: <strong>Healthy</strong>, <strong>Early Blight</strong>, and <strong>Late Blight</strong>. The solution features a robust, end-to-end pipeline encompassing model development, deployment, and cross-platform accessibility, delivering real-time and scalable performance.</p>
            
            <h3>Key Highlights of the Project:</h3>
            
            <h4>1. State-of-the-Art Model Architecture:</h4>
            <ul>
                <li>Designed and trained a TensorFlow-based CNN with optimized input pipelines.</li>
                <li>Implemented data augmentation techniques to enhance the model's generalization and handle complex datasets.</li>
            </ul>
            
            <h4>2. Edge-Compatible Deployment:</h4>
            <ul>
                <li>Deployed the model using TensorFlow Lite with model quantization, ensuring seamless operation on edge devices for real-time disease detection.</li>
            </ul>
            
            <h4>3. Cross-Platform Accessibility:</h4>
            <ul>
                <li>Developed a <strong>ReactJS-powered web interface</strong> and a <strong>React Native mobile app</strong>, offering user-friendly, real-time disease detection for farmers and agricultural experts.</li>
            </ul>
            
            <h4>4. Scalable Cloud Infrastructure:</h4>
            <ul>
                <li>Hosted the backend on <strong>Google Cloud Platform (GCP)</strong>, utilizing <strong>FastAPI</strong> and <strong>TensorFlow Serving</strong> for efficient model inference and API interactions.</li>
            </ul>
            
            <h4>5. End-to-End Integration:</h4>
            <ul>
                <li>Delivered a comprehensive solution that integrates modern AI with practical agricultural applications, enabling advanced disease monitoring and control.</li>
            </ul>
            
            <p>This project demonstrates my expertise in <strong>deep learning</strong>, <strong>edge computing</strong>, <strong>cloud deployment</strong>, and <strong>full-stack development</strong> while showcasing the tangible impact AI can have on agricultural innovation.</p>
            """
        ,
        'image': 'static/images/ml_price_prediction.png',
        'technologies': ['Python', 'NumPy', 'Tensorflow ', 'Tensorflow Lite',
                         'TensorFlow input pipelines', 'TensorFlow Serving', 'FastAPI',
                         'HTML, CSS, and React JavaScript :The fundamental technologies for building the user '
                         'interface',
                         'GCP for hosting flask application',
                         ],
        'github_url': 'https://github.com/babatundeibukun/potato-diease-classification-using-tensorflow-cnn',
        'video_url': 'https://www.youtube.com/embed/y9VtRK5jeLA'  # Add video URL here
        # Add more projects here,
    },
    4: {
        "title": "Farewell, But Not Goodbye",
        "date": "March 2024",
        "description": """
            Saying goodbye is never easy, especially when it’s to colleagues who’ve become like family. 
            As I bid farewell, I wanted this moment to reflect the vibrant memories we’ve shared and the 
            bonds we’ve built.

            In parting, I embarked on a fascinating project as part of my NLP class presentation. Drawing 
            inspiration from our WhatsApp group conversations, I analyzed our interactions to create a 
            digital reflection of our time together.

            ### The Journey Behind the Data
            It all began with extracting and cleaning WhatsApp data—a challenge I tackled using Regex. 
            From this cleaned data, I generated a word cloud, revealing frequently used words that sparked 
            nostalgia. Unsurprisingly, words like "class," "thank you," and "poll" topped the list, 
            symbolizing our collective spirit. Our class decisions often hinged on polls, as we humorously 
            avoided centralizing power in a single class representative for most of the program!

            Beyond word frequencies, I explored contributions within the group. To my surprise, 
            Ghizlane Rehioui emerged as the most active participant, despite spending just a year with us. 
            She was followed by Chaymae Bennouri, who later became our class representative, and myself 
            (yes, I had my fair share of contributions too!). My data analysis revealed:
            - Total messages sent,
            - Media shared,
            - Links posted,
            ...and much more—detailed insights are in my presentation slides.

            ### Unveiling Our Conversations
            I delved deeper into when and how we communicated, uncovering peaks in activity during heated 
            discussions about deadlines or tests. One unforgettable moment was the debate on whether a key 
            exam should be held in December 2023 or January 2024—our group was truly on fire that day!

            Additionally, I mapped response patterns to identify interaction dynamics within the group. 
            Leveraging NMF for topic modeling, I uncovered recurring themes in our conversations, providing 
            a richer understanding of our shared journey.

            ### A Fond Farewell
            To my UM6P School of Collective Intelligence Class of 2024: you’ve made these years 
            unforgettable. This analysis, shared with your permission, is just a glimpse into our collective 
            experience.

            While this marks the end of one chapter, it’s also the start of another. I’ll be using weekends 
            to share my ongoing and completed projects. So, this isn’t just a goodbye—it’s Week 1 of a new 
            journey! Stay tuned, and thank you for being such an integral part of my story.

            With love and gratitude,  
            **[Your Name]**
        """,
        "video_url": None,  # No video associated with this project
        "slides_url": """<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ0KRaBLJizPQWO4JZpiu2lGmCeC9SuOR726SBnmMg-6rBMp7OeP6VLAgHklak-ktuRAQMZaFv5Fks_/embed?start=true&loop=true&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>""",
        "technologies": ["Regex", "Natural Language Processing (NLP)", "Word Cloud", "Topic Modeling", "NMF"],
        "methodologies": [
            "Data extraction and cleaning using Regex.",
            "Word frequency analysis to identify prominent terms.",
            "Visualization with word clouds to capture conversational highlights.",
            "Interaction analysis to map response patterns and activity peaks.",
            "Topic modeling using Non-negative Matrix Factorization (NMF) for thematic insights."
        ],
        "key_findings": [
            "Frequent words like 'class,' 'thank you,' and 'poll' showcased class dynamics.",
            "Most active contributors were Ghizlane Rehioui, Chaymae Bennouri, and the author.",
            "Analyzed group communication peaks during significant debates and events.",
            "Uncovered key conversational themes through topic modeling.",
            "Mapped detailed insights into interaction patterns and media sharing."
        ],
        "github_url": "https://colab.research.google.com/drive/1CQDjWPg3limekAs7UYeLtdTLIgxyQLUK?usp=sharing"
    },

    5: {
        'title': 'How NLP Unpacked 200 Years of American Politics',
        'description': 'This groundbreaking project employs advanced Natural Language Processing (NLP) techniques '
                       'to analyze over two centuries of American political discourse. '
                       'Spanning from George Washington’s address in 1790 to Donald Trump’s in 2019, the project '
                       'uncovers thematic shifts in presidential speeches '
                       'through rigorous data analysis and modeling. It reveals patterns in political priorities '
                       'such as healthcare, economy, and education, demonstrating '
                       'the evolution of American leadership across eras.',
        'methodologies': [
            'Data Collection & Cleaning: Acquired and prepared a comprehensive dataset from Kaggle.',
            'Feature Engineering: Applied Bag-of-Words and TF-IDF techniques to refine text analysis.',
            'Topic Modeling: Leveraged Latent Semantic Indexing (LSI) and Latent Dirichlet Allocation (LDA) to '
            'extract key themes. '
        ],
        'key_findings': [
            'Uncovered recurring themes like healthcare, economy, and security.',
            'Visualized the shifting focus of congressional speeches across presidencies.'
        ],
        'github_url': "https://colab.research.google.com/drive/1lIwptcb2HDitn2sdjTBG_ZuqVfmkfLTC?usp=sharing",
        'technologies': ['Python', 'NLP', 'TF-IDF', 'LDA', 'LSI'],
        'slides_url': '<iframe src="https://docs.google.com/presentation/d/e/2PACX'
                      '-1vQ0KRaBLJizPQWO4JZpiu2lGmCeC9SuOR726SBnmMg-6rBMp7OeP6VLAgHklak-ktuRAQMZaFv5Fks_/embed'
                      '?start=true&loop=true&delayms=3000" '
                      'frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>',
    },
    6: {
        "title": "Review-X: A Controllable Multi-Agent AI System for Research Automation",
        "date": "December 2024",
        "description": """
            My latest project, Review-X, addresses the challenge of controllability in generative AI 
            by creating a multi-agent research assistant bot. This bot automates the research process 
            while ensuring user control through a human-in-the-loop system.

            ### The Core of Review-X
            Review-X utilizes large language models (LLMs) to create a dynamic team of AI analysts 
            focusing on specific sub-topics within a broader research area. Each AI agent operates as 
            a persona, engaging in simulated "interviews" to gather insights from a variety of sources, 
            including Wikipedia, external documents, and web searches.

            The system incorporates a human-in-the-loop process for validation and refinement, 
            allowing users to guide the AI’s research direction. This ensures that the resulting research 
            is aligned with the user’s goals and provides a high degree of autonomy over the final outcome.

            ### How It Works
            I designed Review-X using the LangChain framework, which enables the coordination of multiple 
            agents and tasks. The agents collaborate by conducting parallel interviews, leveraging a 
            map-reduce paradigm to maximize research efficiency. This design allows for the seamless extraction 
            and synthesis of insights from various data sources.

            ### Key Features
            - **Multi-Agent System:** Specialized AI agents, each focusing on a distinct sub-topic.
            - **Human-in-the-Loop:** Ensures user control over research direction and validation.
            - **Simulated Interviews:** AI agents engage in simulated interviews with external sources to gather data.
            - **Parallel Processing:** Efficient use of map-reduce for data gathering and synthesis.
            - **Customizable Output:** Flexible report formatting for diverse research needs.

            ### A New Era of Research Automation
            This project demonstrates my commitment to advancing AI research tools, with a focus on 
            creating practical, controllable AI systems. Review-X is a step forward in research automation, 
            offering a dynamic, user-controlled approach to tackling complex research problems.

            **Stay tuned for future developments, as I continue to share my AI projects and solutions!**
        """,
        "video_url": None,  # No video associated with this project
        "slides_url": None,  # Add slides URL here if available
        "technologies": ["Large Language Models (LLMs)", "LangChain Framework", "Multi-Agent Systems",
                         "Human-in-the-Loop", "Map-Reduce Paradigm", "Wikipedia", "Tavily API", "Python",
                         "Flask"],
        "methodologies": [
            "Human-in-the-loop process for research validation and refinement.",
            "Parallel processing of research tasks using map-reduce paradigm.",
            "Dynamic AI personas with specialized knowledge on specific sub-topics.",
            "Use of large language models (LLMs) for knowledge extraction and conversational agents.",
            "Incorporating multiple data sources like Wikipedia and Tavily API for diversified insights."
        ],
        "key_findings": [
            "Successfully automated research workflows using a multi-agent AI system.",
            "Empowered users to define research topics and control AI analysis through human-in-the-loop refinement.",
            "Achieved efficient data gathering and synthesis through parallel processing.",
            "Demonstrated the flexibility of AI agents in conducting simulated interviews and extracting insights from external sources.",
            "Provided a customizable output that aligns with diverse research needs."
        ],
        "github_url": "https://colab.research.google.com/drive/19zM5XZ71yA8S4DLayFDAMHkScQECfCVE?usp=sharing"
    },
}


@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    month_name = calendar.month_name[current_month]  # This will get the full month name
    return render_template("index.html", year=current_year, month=month_name, day=current_day)


# @app.route("/project/<int:project_id>")
# def project_details(project_id):
#     project = projects.get(project_id)
#     if project:
#         return render_template("project.html", project=project)
#     else:
#         return "Project not found", 404
@app.route("/project/<int:project_id>/")
def project_details(project_id):
    project = projects.get(project_id)
    if project:
        return render_template("project.html", project=project)
    else:
        return "Project not found", 404


@app.route("/publications/")
def publication_details():
    return render_template("publications.html")


@app.route("/cv/")
def academic_cv():
    return render_template("cv.html")


@app.route("/news/")
def news():
    return render_template("news.html")


@app.route("/talks/")
def talks():
    return render_template("talks.html")


if __name__ == "__main__":
    # app.run(debug=True)  # For local development
    # Uncomment the line below when you want to freeze the app
    freezer.freeze()
