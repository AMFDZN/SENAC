import urllib.robotparser


def verificar_robots_txt(url):
    try:
        parser = urllib.robotparser.RobotFileParser()

        endereco_robots = f"{url.rstrip('/')}/robots.txt"

        parser.set_url(endereco_robots)
        parser.read()

        return parser.can_fetch("*", url)

    except Exception:
        return False
