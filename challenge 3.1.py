def LinearSearchProduct(producrlist, targetproduct):
  indices = [] 
  for index, product in enumerate(producrlist):
    if product == targetproduct:
      indices.append(index)

  return indices

products = ["shoes","boost","toafer","shoes","sandel","shoes"]
target = "shoes"
result = LinearSearchProduct(products, target) 
print(result)