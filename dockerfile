FROM python:3.11.6

WORKDIR /app

#로컬에서 requirements.txt파일을 컨테이너의 /app 디렉터리로 복사
COPY requirements.txt /app/

#컨테이너 내부에서 requirements.txt를 기반으로 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app

#FastAPI앱 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
