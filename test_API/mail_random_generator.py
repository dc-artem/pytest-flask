import random
import string

__all__ = ['generate_random_email']

domains = [ "ksdfhj.com", "sdhfs.ru", "sdfjgs.com", "khdfs.com" , "sdjfgksad.ru", "sdfslk.ru"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_email(length):
    return get_random_name(letters, length) + '@' + get_random_domain(domains)


def main():
    print(generate_random_email(7))

if __name__ == "__main__":
    main()