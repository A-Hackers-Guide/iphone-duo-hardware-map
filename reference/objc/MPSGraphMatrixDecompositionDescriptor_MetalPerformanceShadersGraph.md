# `MPSGraphMatrixDecompositionDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
I _dataType;
Q _decompositionType;
```

## Properties

```
@property (TQ,N,V_decompositionType) decompositionType;
@property (TI,N,V_dataType) dataType;
```

## Class methods

```
+[MPSGraphMatrixDecompositionDescriptor descriptorWithDecompositionType:dataType:];
```

## Instance methods

```
-[MPSGraphMatrixDecompositionDescriptor setDataType:];
-[MPSGraphMatrixDecompositionDescriptor dataType];
-[MPSGraphMatrixDecompositionDescriptor copyWithZone:];
-[MPSGraphMatrixDecompositionDescriptor decompositionType];
-[MPSGraphMatrixDecompositionDescriptor setDecompositionType:];
```
