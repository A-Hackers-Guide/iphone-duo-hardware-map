# `MPSGraphViewerNodePropertyDataSPI`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `MPSGraphViewerNodePropertySPI`
- 5 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _isSplat;
@"NSData" _raw;
I _dataType;
@"NSString" _name;
@"NSArray" _shape;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (TI,R,N,V_dataType) dataType;
@property (T@"NSArray",R,N,V_shape) shape;
```

## Class methods

```
+[MPSGraphViewerNodePropertyDataSPI type];
```

## Instance methods

```
-[MPSGraphViewerNodePropertyDataSPI shape];
-[MPSGraphViewerNodePropertyDataSPI dataLength];
-[MPSGraphViewerNodePropertyDataSPI jsonDictionary];
-[MPSGraphViewerNodePropertyDataSPI setValue:];
-[MPSGraphViewerNodePropertyDataSPI dataType];
-[MPSGraphViewerNodePropertyDataSPI name];
-[MPSGraphViewerNodePropertyDataSPI isEnum];
-[MPSGraphViewerNodePropertyDataSPI initWithJSONDictionary:];
-[MPSGraphViewerNodePropertyDataSPI enumCases];
-[MPSGraphViewerNodePropertyDataSPI isSplat];
-[MPSGraphViewerNodePropertyDataSPI dataWithRange:];
-[MPSGraphViewerNodePropertyDataSPI initWithName:dataType:shape:];
-[MPSGraphViewerNodePropertyDataSPI setSplatValue:];
```
