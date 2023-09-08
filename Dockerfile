FROM python:3.11

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y libfreetype6-dev libxft-dev && \
    pip install numpy scipy matplotlib

WORKDIR /usr/src/app
COPY . /usr/src/app


RUN python -c "import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt; import numpy as np; from scipy.optimize import curve_fit; import warnings; warnings.filterwarnings('ignore', category=UserWarning)"

CMD ["python3","./main.py"]
