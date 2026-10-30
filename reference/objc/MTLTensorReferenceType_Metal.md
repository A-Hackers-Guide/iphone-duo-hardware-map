# `MTLTensorReferenceType`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLType`
- 6 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _dataType;
q _tensorDataType;
Q _indexType;
@"MTLTensorExtents" _dimensions;
@"NSArray" _auxiliaryPlanes;
Q _access;
```

## Properties

```
@property (Tq,R,V_tensorDataType) tensorDataType;
@property (TQ,R,V_indexType) indexType;
@property (T@"MTLTensorExtents",R,V_dimensions) dimensions;
@property (T@"NSArray",R,V_auxiliaryPlanes) auxiliaryPlanes;
@property (TQ,R,V_access) access;
```

## Instance methods

```
-[MTLTensorReferenceType indexType];
-[MTLTensorReferenceType dimensions];
-[MTLTensorReferenceType dealloc];
-[MTLTensorReferenceType access];
-[MTLTensorReferenceType formattedDescription:withPrintedTypes:];
-[MTLTensorReferenceType dataType];
-[MTLTensorReferenceType isEqual:];
-[MTLTensorReferenceType auxiliaryPlanes];
-[MTLTensorReferenceType initWithTensorDataType:indexType:dimensions:access:auxiliaryPlanes:];
-[MTLTensorReferenceType tensorDataType];
```
