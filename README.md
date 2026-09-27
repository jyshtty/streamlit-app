# Streamlit Demo Application

A simple, interactive demo application showcasing various Streamlit features including data visualization, interactive widgets, and UI components.

## Features

### 📊 Data Visualization
- Interactive line charts
- Area charts with multiple series
- Dynamic data tables with sample data
- Real-time data rendering

### 🎮 Interactive Widgets
- **Input Controls**: Sliders, text inputs, and checkboxes
- **Selection Controls**: Dropdown menus, radio buttons, and multi-select
- **Date/Time**: Date picker for temporal data
- **Sidebar**: Personalized user input section

### 📝 Text & Media
- Markdown formatting support
- Code syntax highlighting
- Status messages (success, info, warning, error)
- Metrics display with delta indicators
- Organized tab-based layout

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jyshtty/streamlit-app.git
cd streamlit-app
```

2. Install the required dependencies:
```bash
pip install streamlit pandas numpy
```

## Running the Application

Start the Streamlit server:
```bash
streamlit run app.py
```

Or using Python module:
```bash
python3 -m streamlit run app.py
```

The application will automatically open in your default web browser at:
- Local URL: http://localhost:8501
- Network URL: Available on your local network

## Usage

Once the application is running:

1. **Enter your name** in the sidebar to personalize your experience
2. **Navigate through tabs**:
   - **Data Visualization**: View dynamic charts and data tables
   - **Interactive Widgets**: Experiment with various input controls
   - **Text & Media**: See different formatting and display options
3. **Interact with widgets**: Adjust sliders, select options, and see real-time updates

## Project Structure

```
streamlit-app/
├── app.py              # Main Streamlit application
├── pyproject.toml      # Project dependencies and metadata
└── README.md           # This file
```

## Dependencies

- **streamlit** (>=1.28.0): Web framework for data apps
- **pandas** (>=2.0.0): Data manipulation and analysis
- **numpy** (>=1.24.0): Numerical computing

## Configuration

Streamlit can be configured using command-line options:

```bash
# Run on a different port
streamlit run app.py --server.port 8502

# Run in headless mode
streamlit run app.py --server.headless true
```

## Features Showcase

### Metrics Display
The app displays key metrics with delta indicators showing trends:
- Temperature monitoring
- Revenue tracking
- User analytics

### Data Generation
Sample data is generated using NumPy's random functions to demonstrate:
- Time series visualization
- Multi-series comparisons
- Tabular data presentation

### Responsive Layout
- Multi-column layouts for efficient space usage
- Wide page layout for better data visibility
- Organized content in collapsible tabs

## Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run app.py --server.port 8502
```

### Module Not Found
Ensure all dependencies are installed:
```bash
pip install --upgrade streamlit pandas numpy
```

### Performance Optimization
For better performance, install watchdog:
```bash
pip install watchdog
```

## Learn More

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit API Reference](https://docs.streamlit.io/library/api-reference)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [Streamlit Community](https://discuss.streamlit.io)

## License

This is a demo application for educational purposes.

## Author

Built with Streamlit

---

**Note**: This is a demonstration application showcasing Streamlit's capabilities. Feel free to modify and extend it for your specific use case.
