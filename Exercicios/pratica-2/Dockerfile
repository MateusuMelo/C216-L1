#Para funcionar esta imagem deve estar na mesma pasta que o exercicio anterior :)
FROM python:3.12
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ .

CMD ["python3", "sistema_faculdade.py"]
