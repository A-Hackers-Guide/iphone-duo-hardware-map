# `MTLFunctionStitchingGraph`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSString" _functionName;
@"NSArray" _nodes;
@"MTLFunctionStitchingFunctionNode" _outputNode;
@"NSArray" _attributes;
```

## Properties

```
@property (T@"NSString",C,N,V_functionName) functionName;
@property (T@"NSArray",C,N,V_nodes) nodes;
@property (T@"MTLFunctionStitchingFunctionNode",&,N,V_outputNode) outputNode;
@property (T@"NSArray",C,N,V_attributes) attributes;
```

## Instance methods

```
-[MTLFunctionStitchingGraph setFunctionName:];
-[MTLFunctionStitchingGraph functionName];
-[MTLFunctionStitchingGraph nodes];
-[MTLFunctionStitchingGraph formattedDescription:];
-[MTLFunctionStitchingGraph init];
-[MTLFunctionStitchingGraph dealloc];
-[MTLFunctionStitchingGraph setAttributes:];
-[MTLFunctionStitchingGraph hash];
-[MTLFunctionStitchingGraph description];
-[MTLFunctionStitchingGraph attributes];
-[MTLFunctionStitchingGraph copyWithZone:];
-[MTLFunctionStitchingGraph isEqual:];
-[MTLFunctionStitchingGraph setNodes:];
-[MTLFunctionStitchingGraph outputNode];
-[MTLFunctionStitchingGraph initWithFunctionName:nodes:outputNode:attributes:];
-[MTLFunctionStitchingGraph setOutputNode:];
```
