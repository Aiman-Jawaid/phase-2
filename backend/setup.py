from setuptools import setup, find_packages

setup(
    name="todo-api-backend",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.115.0",
        "sqlmodel>=0.0.22",
        "uvicorn[standard]==0.32.0",
        "python-jose[cryptography]==3.3.0",
        "python-dotenv==1.0.0",
        "pydantic==2.12.5",
        "pydantic-settings==2.1.0",
        "passlib[bcrypt]==1.7.4",
    ],
    author="Todo App Team",
    author_email="todo@example.com",
    description="Secure Todo Management Backend with JWT Authentication",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aiman-Jawaid/phase-2-hackathon2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)