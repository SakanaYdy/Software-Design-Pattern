from codeFactory import CodeFactoryLazy, CodeFactoryEager, CodeFactoryNew


# Lazy Test
print("Testing Lazy Singleton:")
factory1 = CodeFactoryLazy.getCodeFactory()
factory2 = CodeFactoryLazy.getCodeFactory()
factory1.printCodeFactory()
print(f"factory1 is factory2: {factory1 is factory2}")

# Eager Test
print("\nTesting Eager Singleton:")
factory3 = CodeFactoryEager.getCodeFactory()
factory4 = CodeFactoryEager.getCodeFactory()
factory3.printCodeFactory()
print(f"factory3 is factory4: {factory3 is factory4}")

print("\nTesting New Singleton:")
factory5 = CodeFactoryNew()
factory6 = CodeFactoryNew()
factory5.printCodeFactory()
print(f"factory5 is factory6: {factory5 is factory6}")  

