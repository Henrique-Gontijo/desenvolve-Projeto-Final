from urllib import parse

print("Digite o texto que você deseja converter:")
text = input("")

parsed_text = parse.quote_plus(text)

with open("parsed_url.txt", "w") as file:
    file.write(parsed_text)

print("Texto convertido e salvo em 'parsed_url.txt'")