<div align="center">
This repository contains different examples and use cases showcased in the book <a href="https://appswithgpt.com">Developing Apps with GPT-4 and ChatGPT</a>.
<img src="./images/book_cover.png" alt="Book cover" width="300"/>
</div>

📘 Developing Apps with GPT-4 and ChatGPT — Code Examples
Welcome! 👋
This repository contains all the example projects and code snippets featured in the book Developing Apps with GPT-4 and ChatGPT.

Whether you're new to coding or exploring AI development for the first time, this repo is designed to help you learn by doing.

📖 About This Repository
If you're coming from the first edition of the book:

The code in this repo has been updated to use a newer version of the official OpenAI Python library.

You’ll also find additional examples not included in the first edition.

The chapter numbers and example structure remain the same across book editions for easy navigation.

To view the original version of the code (first edition), switch to the appropriate tag using Git:


git checkout [tag_name]
🚀 Getting Started
1. Clone the Repository
If you haven’t already, clone the repository to your local machine:


git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install the Required Packages
Make sure you have Python installed. Then, install the dependencies for all examples:


pip install -r requirements.txt
💡 Tip: It’s a good idea to use a virtual environment to manage your Python packages.

🧪 How to Run the Examples
Each example is stored in its own folder and contains either a Jupyter Notebook (.ipynb) or a Python script (run.py).

To run an example:

python [example_folder]/run.py
Or open the .ipynb file in a Jupyter environment like VS Code or Google Colab.

⚙️ Examples That Need Extra Setup
Some examples need a bit more configuration to work. Here's a quick guide:

📄 Chapter 3.03 — Question Answering on PDFs
This example uses Redis, a fast in-memory database.

To start Redis using Docker:


docker-compose up -d
Make sure Docker is installed and running on your machine. Learn more about Docker here.

🎙️ Chapter 3.04 — Voice Assistant with Gradio
This example launches a simple voice assistant interface using Gradio.

After running the script, you’ll see a link in your terminal. Open it in your browser to use the assistant.

🧠 Chapter 5.04 — Customizing with LlamaIndex and Weaviate
This example demonstrates how to customize LlamaIndex with a vector database called Weaviate.

You can start Weaviate locally using Docker:


docker-compose up -d
Or run it directly via Docker without using docker-compose:


docker run -p 8080:8080 -p 50051:50051 cr.weaviate.io/semitechnologies/weaviate:1.24.9
If needed, customize the docker-compose.yml file to suit your setup.

🙋 Need Help?
If you're stuck, feel free to:

Open an issue

Check the official OpenAI API documentation

Google the error message — it's what all devs do 😄

✅ Contributing
Beginner contributions are welcome!
If you improve the documentation or fix an error in the code, feel free to make a pull request.

⭐️ Show Some Love
If you found this helpful, please give the repo a ⭐️ on GitHub! It helps others discover it — and gives you credit on your profile too.

