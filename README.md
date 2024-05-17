
# Advanced RAG control flow:

This repository contains a refactored version of the original [LangChain's Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain),

tailored towards developers and production-oriented applications for learning LangGraph🦜🕸️.

Implemenation of Reflective RAG, Self-RAG & Adaptive RAG

See Original YouTube video:

[Advance RAG control flow with Mistral and LangChain: Corrective RAG, Self-RAG, Adaptive RAG](https://www.youtube.com/watch?v=sgnrL7yo1TE)


![Logo](https://github.com/emarco177/langgaph-course/blob/main/static/langgraph_adaptive_rag.png)
[![udemy](https://img.shields.io/badge/LangGraph%20Udemy%20Course-Coupon%20%2412.99-brightgreen)](https://www.udemy.com/course/langgraph/?referralCode=FEA50E8CBA24ECD48212)


## Features

- **Refactored Notebooks**: The original LangChain notebooks have been refactored to enhance readability, maintainability, and usability for developers.
- **Production-Oriented**: The codebase is designed with a focus on production readiness, allowing developers to seamlessly transition from experimentation to deployment.
- **Test Coverage**: Comprehensive test coverage ensures the reliability and stability of the application, enabling developers to validate their implementations effectively.
- **Documentation**: Detailed documentation and branches guides developers through setting up the environment, understanding the codebase, and utilizing LangGraph effectively.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/langgraph-course`

`OPENAI_API_KEY`

`TAVILY_API_KEY`

## Run Locally

Clone the project

```bash
  git clone https://github.com/emarco177/langgraph-course.git
```

Go to the project directory

```bash
  cd langgraph-course
```

Install dependencies

```bash
  poetry install
```

Start the flask server

```bash
  poetry run app.py
```


## Running Tests

To run tests, run the following command

```bash
  poetry run pytest . -s -v
```
## Acknowledgements

Original LangChain repository: [LangChain Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain)
![Logo](https://github.com/emarco177/langgaph-course/blob/main/static/LangChain-logo.png)




## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.udemy.com/course/langgraph/?referralCode=FEA50E8CBA24ECD48212)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.udemy.com/user/eden-marco/)