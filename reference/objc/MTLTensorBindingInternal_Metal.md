# `MTLTensorBindingInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLBindingInternal`
- Protocols: `MTLTensorBinding`
- 5 instance variables, 14 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _tensorDataType;
Q _indexType;
@"MTLTensorExtents" _dimensions;
@"NSArray" auxiliaryPlanes;
@"NSArray" _auxiliaryPlanes;
```

## Properties

```
@property (Tq,R,V_tensorDataType) tensorDataType;
@property (TQ,R,V_indexType) indexType;
@property (T@"MTLTensorExtents",R,V_dimensions) dimensions;
@property (T@"NSArray",R,V_auxiliaryPlanes) auxiliaryPlanes;
@property (T@"NSString",R) name;
@property (Tq,R) type;
@property (TQ,R) access;
@property (TQ,R) index;
@property (TB,R,GisUsed) used;
@property (TB,R,GisArgument) argument;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLTensorBindingInternal indexType];
-[MTLTensorBindingInternal dimensions];
-[MTLTensorBindingInternal formattedDescription:];
-[MTLTensorBindingInternal dealloc];
-[MTLTensorBindingInternal description];
-[MTLTensorBindingInternal isEqual:];
-[MTLTensorBindingInternal auxiliaryPlanes];
-[MTLTensorBindingInternal initWithName:access:isActive:locationIndex:arrayLength:dataType:indexType:dimensions:auxiliaryPlanes:];
-[MTLTensorBindingInternal tensorDataType];
```
