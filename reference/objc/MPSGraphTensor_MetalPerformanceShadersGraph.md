# `MPSGraphTensor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 8 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
{Value="impl"^{ValueImpl}} _value;
@"MPSGraphOperation" _operation;
@"MPSGraph" _graph;
@"MPSGraphBlock" _parentBlock;
I _dataType;
Q _index;
@"NSArray" _shape;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T{Value=^{ValueImpl}},R,N,V_value) value;
@property (TQ,R,N,V_index) index;
@property (T@"NSArray",R,C,N,V_shape) shape;
@property (TI,R,N,V_dataType) dataType;
@property (T@"MPSGraphOperation",R,W,N,V_operation) operation;
```

## Instance methods

```
-[MPSGraphTensor operation];
-[MPSGraphTensor debugDescription];
-[MPSGraphTensor shape];
-[MPSGraphTensor value];
-[MPSGraphTensor index];
-[MPSGraphTensor dataType];
-[MPSGraphTensor copyWithZone:];
-[MPSGraphTensor name];
-[MPSGraphTensor initTensorWithOperation:value:graph:];
-[MPSGraphTensor initTensorWithOperation:value:graph:name:];
-[MPSGraphTensor initTensorWithOperation:value:graph:parentBlock:name:];
-[MPSGraphTensor initTensorWithValue:graph:];
```
