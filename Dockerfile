FROM python:3.11

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
COPY groundwater_data.csv /app/

CMD streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0