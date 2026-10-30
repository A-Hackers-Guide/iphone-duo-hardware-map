# `MPSGraphViewerNodePropertyEnumSPI`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `MPSGraphViewerNodePropertySPI`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSString" _name;
@"NSString" _enumType;
@"NSArray" _enumCases;
Q _enumValue;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_enumType) enumType;
@property (T@"NSArray",R,N,V_enumCases) enumCases;
@property (TQ,R,N,V_enumValue) enumValue;
```

## Class methods

```
+[MPSGraphViewerNodePropertyEnumSPI type];
```

## Instance methods

```
-[MPSGraphViewerNodePropertyEnumSPI shape];
-[MPSGraphViewerNodePropertyEnumSPI dataLength];
-[MPSGraphViewerNodePropertyEnumSPI jsonDictionary];
-[MPSGraphViewerNodePropertyEnumSPI dataType];
-[MPSGraphViewerNodePropertyEnumSPI name];
-[MPSGraphViewerNodePropertyEnumSPI isEnum];
-[MPSGraphViewerNodePropertyEnumSPI initWithJSONDictionary:];
-[MPSGraphViewerNodePropertyEnumSPI enumValue];
-[MPSGraphViewerNodePropertyEnumSPI enumCases];
-[MPSGraphViewerNodePropertyEnumSPI isSplat];
-[MPSGraphViewerNodePropertyEnumSPI dataWithRange:];
-[MPSGraphViewerNodePropertyEnumSPI enumType];
-[MPSGraphViewerNodePropertyEnumSPI initWithName:type:cases:value:];
```
