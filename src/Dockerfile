# Usa un immagine di Python leggera
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /helloworld

# Copia ed installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

# Copia il codice dell'applicazione e definisci il comando di avvio
COPY app.py .

# Il container è in ascolto sulla porta 5000
EXPOSE 5000

# Comando di avvio
CMD ["python", "app.py"]