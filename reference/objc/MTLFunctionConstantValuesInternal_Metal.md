# `MTLFunctionConstantValuesInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLFunctionConstantValues`
- Protocols: `MTLFunctionConstantSPI`
- 1 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
^v _constantStorage;
```

## Instance methods

```
-[MTLFunctionConstantValuesInternal newNamedConstantArray];
-[MTLFunctionConstantValuesInternal init];
-[MTLFunctionConstantValuesInternal constantValueWithFunctionConstant:];
-[MTLFunctionConstantValuesInternal dealloc];
-[MTLFunctionConstantValuesInternal newConstantScriptForFunction:name:specializedName:errorMessage:];
-[MTLFunctionConstantValuesInternal reset];
-[MTLFunctionConstantValuesInternal newIndexedConstantArray];
-[MTLFunctionConstantValuesInternal setConstantValue:type:atIndex:];
-[MTLFunctionConstantValuesInternal setConstantValue:type:withName:];
-[MTLFunctionConstantValuesInternal serializedConstantDataForFunction:dataSize:errorMessage:];
-[MTLFunctionConstantValuesInternal hash];
-[MTLFunctionConstantValuesInternal description];
-[MTLFunctionConstantValuesInternal copyWithZone:];
-[MTLFunctionConstantValuesInternal isEqual:];
-[MTLFunctionConstantValuesInternal setConstantValues:type:withRange:];
```
