# `MPSGraphViewerNodePortSPI`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
I _dataType;
@"NSString" _name;
@"NSArray" _shape;
Q _valueRef;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (TI,R,N,V_dataType) dataType;
@property (T@"NSArray",R,N,V_shape) shape;
@property (TQ,R,N,V_valueRef) valueRef;
```

## Instance methods

```
-[MPSGraphViewerNodePortSPI shape];
-[MPSGraphViewerNodePortSPI jsonDictionary];
-[MPSGraphViewerNodePortSPI dataType];
-[MPSGraphViewerNodePortSPI name];
-[MPSGraphViewerNodePortSPI initWithJSONDictionary:];
-[MPSGraphViewerNodePortSPI valueRef];
-[MPSGraphViewerNodePortSPI initWithName:dataType:shape:valueRef:];
```
