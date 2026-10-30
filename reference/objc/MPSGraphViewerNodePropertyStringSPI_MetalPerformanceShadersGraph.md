# `MPSGraphViewerNodePropertyStringSPI`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `MPSGraphViewerNodePropertySPI`
- 3 instance variables, 2 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"NSData" _stringUTF8Data;
@"NSString" _name;
@"NSString" _stringValue;
```

## Properties

```
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSString",R,N,V_stringValue) stringValue;
```

## Class methods

```
+[MPSGraphViewerNodePropertyStringSPI type];
```

## Instance methods

```
-[MPSGraphViewerNodePropertyStringSPI stringValue];
-[MPSGraphViewerNodePropertyStringSPI shape];
-[MPSGraphViewerNodePropertyStringSPI dataLength];
-[MPSGraphViewerNodePropertyStringSPI jsonDictionary];
-[MPSGraphViewerNodePropertyStringSPI dataType];
-[MPSGraphViewerNodePropertyStringSPI initWithName:value:];
-[MPSGraphViewerNodePropertyStringSPI name];
-[MPSGraphViewerNodePropertyStringSPI isEnum];
-[MPSGraphViewerNodePropertyStringSPI initWithJSONDictionary:];
-[MPSGraphViewerNodePropertyStringSPI enumCases];
-[MPSGraphViewerNodePropertyStringSPI isSplat];
-[MPSGraphViewerNodePropertyStringSPI dataWithRange:];
```
