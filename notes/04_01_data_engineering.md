<br />
<div align="center">
  <a href="#">
    <img src="./assets/analytics_engineering.png" alt="Analytics Engineering Diagram"  height="275">
  </a>

<h1 align = "center">
<b><i>Analytics Engineering</i></b>
</h1>

  <p align="center">
  </p>
</div>
<br />

## Roles in a Data Team

- Data Engineer: preparing and maintaining infrastructure that hosts data
- Data Analysts: uses the data to answer the questions and solve business problems
- Analytics Engineer: introduces good software engineering practices to the efforts of data analysts and data scientists

![](assets/data_team_roles.png)

## Data Modelling Concepts

- ETL: Longer to implement, as data is transformed before it is loaded with higher storage and compute costs.
- ELT: Faster and more flexible with lower cost and maintenance.

[](assets/elt_vs_etl.png)

## Kimball's Dimensional Modelling

Dimensional modeling is a technique introduced by Ralph Kimball in 1996 with his book, The Data Warehouse Toolkit. The
goal of dimensional modeling is to take raw data and transform it into Fact and Dimension tables that represent the
business.

### Objective

- Deliver data understandable to the business user
- Deliver fast query performance

### Approach

Prioritize user understandability and query performance over non-redundant data (3NF - 3rd Normal Form)

### Elements

- **Fact Tables**: Corresponds to a business process (measurements, metrics or facts). "Verbs".
- **Dimension Tables**: Corresponds to a business entity. "Nouns".

### Architecture

- **Staging Area**: Contains the raw data, not meant to be exposed to everyone.
- **Processing Area**: From raw data to data models. Focuses in efficiency and ensures standards are met.
- **Presentation Area**: Final presentation of the data. Exposure to the business stakeholders.

![](assets/kimball_architecture.png)

