# Nanobot Defense System - Visualization Dashboard

## Project Overview
This represents the "Cyber-Organic Noir" interface for the Nanobot Cancer Visualization.
It is a static site built with Vite.

## Setup
1. **Install Dependencies**:
   ```bash
   npm install
   ```

2. **Run Development Server**:
   ```bash
   npm run dev
   ```
   Open the link provided (usually `http://localhost:5173`).

## Project Structure
- `index.html`: Home page with Intelligence Cards and Ticker.
- `visualization.html`: The Tactical Visualization Lab.
- `mission.html`: The Mission Theatre (Video Gallery).
- `assets/videos/`: **Drop your MP4/WebM mission videos here.**
- `assets/visualizations/`: **Drop generated charts here.**
- `generate_plots.py`: Python script to generate the 8D Feature Vector chart and GATv2 Heatmap.

## How to use the Python Script
Ensure you have Python installed with `matplotlib` and `numpy`.
```bash
pip install matplotlib numpy
python generate_plots.py
```
This will create simulated charts in `assets/visualizations/` which you can then reference in the HTML (currently they are hardcoded SVG placeholders, but you can swap the `<img>` tags in `visualization.html` to point to the PNGs if you prefer static images over code).
