def featuredProduct(products):
    # Write your code here
    my_dict = {i:products.count(i) for i in products}
    ordered=[v[0] for v in sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)]
    return ordered[0]

print(featuredProduct(['rS','gP','rS','oS','bP','bP']))