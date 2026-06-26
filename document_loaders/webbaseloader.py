from langchain_community.document_loaders import WebBaseLoader

url = 'https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mw123hn-a/p/itm08069ed2395aa?pid=COMH9ZWQDGMTF3HA&lid=LSTCOMH9ZWQDGMTF3HAIAWW11&hl_lid=&marketplace=FLIPKART&fm=eyJ3dHAiOiJyZWNvIiwicHJwdCI6InBwIiwibWlkIjoicHJvZHVjdFJlY29tbWVuZGF0aW9uL2FzcGVjdFNpbWlsYXIifQ%3D%3D&pageUID=1782476319593'

loader = WebBaseLoader(url)

docs = loader.load()

print(len(docs))

print(docs)