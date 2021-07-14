LOGGING = {
    #バージョンは 「1」 固定
    'version': 1,
    #既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    #ログフォーマット
    'formatters': {
        # 本番用
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                        '%(pathname)s:%(lineno)d %(message)s'
        },
    },
    # ハンドラ
    'handlers': {
        #ファイル出⼒⽤ハンドラ
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': './logs/app.log',
            'formatter': 'production',
        },
    },
    # ロガー
    'loggers':{
        # ⾃作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        # Django本体が出すログ全般を拾うロガー
        'Django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
