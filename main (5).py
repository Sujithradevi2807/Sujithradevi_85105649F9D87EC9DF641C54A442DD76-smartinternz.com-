def linearSearchProduct(productList, targetProduct):
  indices = []
  for index,product in enumerate(productList):
    if product==targetProduct:
      indices. append(index)
  return indices 
products = ["shoes","boot","losfer","shoes","sandal","shoes"]
target="shoes"
result = linearSearchProduct (products, target)
print(result)
