from setuptools import setup, find_packages

setup(
    name="stock_risk_analysis",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "yfinance",
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn"
    ],
    entry_points={
        "console_scripts": [
            "stock-analysis=stock_risk_analysis.main:main",
        ]
    },
    author="M1000",
    description="A Python tool for stock history analysis and risk assessment",
    url="https://github.com/your-username/stock-risk-analysis",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
