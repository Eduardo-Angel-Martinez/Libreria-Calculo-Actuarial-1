# firstact — Dockerfile
# Imagen base con Python
FROM python:3.11-slim

# Metadata
LABEL maintainer="firstact"
LABEL description="Libreria de matematicas actuariales: firstact"
LABEL version="0.2.0"

# Directorio de trabajo
WORKDIR /app

# Instalar firstact desde PyPI
RUN pip install --no-cache-dir firstact matplotlib pandas jupyter

# Copiar ejemplos y tests
COPY examples/ ./examples/
COPY tests/ ./tests/

# Exponer puerto para Jupyter
EXPOSE 8888

# Comando por default: correr los tests
CMD ["python", "tests/test_firstact.py"]
