FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy frontend files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app with sidebar nav off
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--client.showSidebarNavigation", "false"]
