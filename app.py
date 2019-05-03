from dotenv import load_dotenv

from common import strings, load_links

load_dotenv(".env")

if __name__ == '__main__':
    strings.refresh()
    load_links.refresh()
    from main import main
    main()
