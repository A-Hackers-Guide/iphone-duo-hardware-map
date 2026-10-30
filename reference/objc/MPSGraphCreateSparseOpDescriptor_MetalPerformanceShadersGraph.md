# `MPSGraphCreateSparseOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
I _dataType;
Q _sparseStorageType;
```

## Properties

```
@property (TQ,N,V_sparseStorageType) sparseStorageType;
@property (TI,N,V_dataType) dataType;
```

## Class methods

```
+[MPSGraphCreateSparseOpDescriptor descriptorWithStorageType:dataType:];
```

## Instance methods

```
-[MPSGraphCreateSparseOpDescriptor setDataType:];
-[MPSGraphCreateSparseOpDescriptor dataType];
-[MPSGraphCreateSparseOpDescriptor copyWithZone:];
-[MPSGraphCreateSparseOpDescriptor setSparseStorageType:];
-[MPSGraphCreateSparseOpDescriptor sparseStorageType];
```
