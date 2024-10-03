from page_generation import *


def main():
    static_to_public("static", "public", True)
    generate_pages_recursive("content", template, "public")










main()
