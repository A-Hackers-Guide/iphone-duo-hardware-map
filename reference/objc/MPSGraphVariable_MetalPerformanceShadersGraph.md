# `MPSGraphVariable`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 5 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSData" _data;
@"NSMutableArray" _mpsndarrays;
{Value="impl"^{ValueImpl}} _value;
I _dataType;
@"NSArray" _shape;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_shape) shape;
@property (TI,R,N,V_dataType) dataType;
@property (T{Value=^{ValueImpl}},R,N,V_value) value;
```

## Class methods

```
+[MPSGraphVariable newVariableWithData:dataType:shape:];
```

## Instance methods

```
-[MPSGraphVariable shape];
-[MPSGraphVariable value];
-[MPSGraphVariable dataType];
-[MPSGraphVariable copyWithZone:];
-[MPSGraphVariable initVariableWithData:dataType:shape:];
-[MPSGraphVariable initVariableWithData:value:];
-[MPSGraphVariable initVariableWithMPSNDArray:value:];
-[MPSGraphVariable mpsNDArrayWithDevice:];
```
