## 📈**Card Consumption Pattern Analysis Dashboard**📋
### **Project** : Data Visualization Dashboard with 📈**Plotly** & 📋**Dash**
### **DATASET** : 📂Card spending data
### 🐍**Conda Virtual Environment**

    python==3.8.16
    plotly==5.18.0
    dash==2.14.2
    dash-bootstrap-components 1.5.0 
    flask==2.2.5

---
#### **Usually**, behavior such as DB connection, Data preprocessing, and Modeling must be developed from Backend with Python or Java etc. and Web visualization should have been developed from Frontend with Javascript(e.g. Vue.js, React).
#### **In the process of web charts visualizing**, The web chart is implemented in FrontEnd in one language(e.g. chart.js on javascript) and The chart source is provided in BackEnd in another language(e.g. django on python). But Plotly & Dash can visualize chart on the web only in Python, without having to use two languages. So, the results of Data analysis or Modeling implemented in Python can be viewed as they are.

#### **Modularization** : This dashboard is implemented by combining different chart components. Modularization increases the maintenance of code in large applications and makes each component easier to work with individually.
### **About** 📈[**Plotly**](https://github.com/plotly/plotly.py)
#### - Graphy library made of Python can replace matplotlib's functionality
#### - Supports variety of chart formats & Modern and Interactive graph
#### - Open Source of MIT License
### **About** 📋[**Dash**](https://github.com/plotly/dash)  
#### - Library to develop Web Services based on Plotly can replace Flask+matplotlib 
#### - Low-code framework for rapidly building data apps
####  - Open Source of MIT License
---