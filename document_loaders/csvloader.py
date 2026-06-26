from langchain_community.document_loaders import CSVLoader


loader = CSVLoader('/Users/apple/Desktop/Artificial Intelligence/GEN AI/document_loader/Social_Network_Ads.csv')

docs = loader.load()

print(len(docs))

print(docs[0])