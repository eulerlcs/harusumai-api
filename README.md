# harusumai-api ハルスマ  


## 処理概要  
  社員情報管理システム  


## 実行環境  
### windows  
#### 事前準備  
  - python 3.11  
#### サービス起動  
```bash
uvicorn app.main:app --host 0.0.0.0 --port 9527 --log-config=config/log_config.yml
```

### docker  
#### dockerイメージ作成  
```bash
docker build -t harusumai-api:0.0.1-dev
```
#### docker-compose-sample.yml   
```yaml
services:
  harusamai-api:
    build:
      context: ./
      dockerfile: Dockerfile
    image:
      harusumai-api:0.0.1-dev
    container_name: harusumai-api
    restart: unless-stopped
    environment:
      TZ: "Asia/Tokyo"
      
      DB_HOST: 
      DB_USERNAME: 
      DB_PASSWORD: 
    ports:
    - 9527:80
```

## UI（api doc）
  - http://localhost:9527/docs  
  - http://localhost:9527/redoc  


## 参考資料  
  - [FastAPI始めました](https://zenn.dev/kou_kawa/articles/07-first-fastapi)  
  - [FastAPIでMySQLのデータベースCRUD操作](https://zenn.dev/kou_kawa/articles/08-first-mysql-fastapi)  
  - [FastAPIとSQLAlchemyでリレーショナルデータベースからの複雑なデータ取得](https://zenn.dev/kou_kawa/articles/09-second-mysql-fastapi)  
  - [FastAPIでOAuth2.0認証](https://zenn.dev/kou_kawa/articles/10-oauth20-fastapi)  
