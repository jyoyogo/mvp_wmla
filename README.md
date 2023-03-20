# mvp_wmla

### 1. Environment
```
$ python -m venv my_env
$ . myenv/bin/activate
(my_env)$ pip install -r requirements.txt
```

### 2. Prepare Credential
```
(my_env)$ python generate_credential.py --userid admin --name admin --password admin123 --email admin@domain.com
```

### 3. Run Webapp
```
(my_env)$ run 🏠_Home.py --server.port ${PORT_NUM}
```

### Part to Edit
```
#/pathdir/pages/1_🌎_Translator.py
#41 line result = request.post(xxx)
#42 line hypotheses = {"translatedText":[{"translated":"(월요일 발행 기사 중복, 본문 변경 없음) 8월 15일 로이터=런던) 호주 우라늄 광부 아우라 에너지는 9월 말까지 런던 증시의 AIM 시장에 주식을 상장할 계획이며 285만 파운드(37억 달러)를 목표로 하고 있다고 월요일 밝혔다."}]}
```
