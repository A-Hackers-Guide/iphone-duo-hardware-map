# `MPSGraphIntermediateIdentifier`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
Q _parentIdentifier;
@"NSString" _operationNamespace;
Q _operationIdentifier;
@"NSNumber" _index;
```

## Properties

```
@property (TQ,V_parentIdentifier) parentIdentifier;
@property (T@"NSString",&,V_operationNamespace) operationNamespace;
@property (TQ,V_operationIdentifier) operationIdentifier;
@property (T@"NSNumber",&,V_index) index;
```

## Instance methods

```
-[MPSGraphIntermediateIdentifier parentIdentifier];
-[MPSGraphIntermediateIdentifier index];
-[MPSGraphIntermediateIdentifier setParentIdentifier:];
-[MPSGraphIntermediateIdentifier setIndex:];
-[MPSGraphIntermediateIdentifier hash];
-[MPSGraphIntermediateIdentifier description];
-[MPSGraphIntermediateIdentifier copyWithZone:];
-[MPSGraphIntermediateIdentifier isEqual:];
-[MPSGraphIntermediateIdentifier isEqualToIntermediateIdentifier:];
-[MPSGraphIntermediateIdentifier operationIdentifier];
-[MPSGraphIntermediateIdentifier operationNamespace];
-[MPSGraphIntermediateIdentifier setOperationIdentifier:];
-[MPSGraphIntermediateIdentifier setOperationNamespace:];
```
