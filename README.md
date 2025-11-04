# Enhancing Threat Detection with SIEM Tool Using GNN

## Overview
This project leverages Graph Neural Networks (GNNs) to enhance threat detection capabilities in Security Information and Event Management (SIEM) systems. By analyzing relationships between security events, the system detects threats with improved accuracy and reduced false positives.

---

## Workflow Steps in the Workflow

1. **Windows Host (Winlogbeat)**:
   - Collect Windows Event Logs.
   - Send structured logs to Elasticsearch.

2. **Elasticsearch**:
   - Log indexing and storage.
   - Retrieve logs for processing and analysis.

3. **Flask API**:
   - Retrieve logs from Elasticsearch.
   - Process logs and pass them to the GNN model.

4. **GNN Model**:
   - Analyze logs in graph format for threat detection.
   - Return enriched results.

5. **Kibana**:
   - Visualize the enriched results for easy analysis.

---

## Features

- Collection and processing of Windows Event Logs using Winlogbeat.
- Log indexing and querying using Elasticsearch.
- GNN model for advanced threat detection and analysis.
- Visualization of results using Kibana.


## Setup Instructions

### Prerequisites
- Python 3.8+
- Elasticsearch and Kibana
- Git
- Libraries: PyTorch, Flask, Pandas, Matplotlib


## Screenshots
<p align="center">
  <img src="[d9db1db3-a3b9-44ee-b5d3-2d4d7df9e81c.png" alt="Workflow Diagram" width="400](https://github.com/user-attachments/assets/da609bac-ef21-4396-9289-e6794ed02033)"/>
  <br>
  <em>Figure: Workflow of the project</em>
</p>
