from threading import Thread


def main():

    def run_redis():
        from mirrulations_server.redis_manager import run
        run()

    def run_flask():
        from mirrulations_server.flask_manager import run
        run()

    def run_work():
        from mirrulations_server.work_manager import run
        run()

    Thread(target=run_redis).start()
    Thread(target=run_flask).start()
    Thread(target=run_work).start()


if __name__ == '__main__':
    main()
