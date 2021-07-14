LOGGING = {
    #バージョンは 「1」 固定
    'version': 1,
    #既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    #ログフォーマット
    'formatters': {
        #開発⽤
        'develop': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d '
                        '%(message)s'
        },
    },
    #ハンドラ
    'handlers': {
        #コンソール出⼒⽤ハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'develop', 
        },
    },
    #ロガー
    'loggers': {
        #⾃作アプリケーション全般のログを拾うロガー
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        #Django本体が出すログ全般を拾うロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        #発⾏される SQL⽂を出⼒するための設定
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
