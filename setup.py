import string
import random


SYMBOLS = string.ascii_letters + string.digits

def main():

    with open(".env", "w", encoding="utf-8") as file:
       file.write(f"""



POSTGRES_USER=root
POSTGRES_PASSWORD={"".join(random.choices(SYMBOLS, k=100))}





""".strip())
       
if __name__ == "__main__":
    main()