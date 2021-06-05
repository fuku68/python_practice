#ベースイメージの設定
FROM ubuntu:16.04

# Nginx のインストール
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nginx

# ポート指定
EXPOSE 80

# サーバの実行
CMD ["nginx", "-g", "daemon off;"]
