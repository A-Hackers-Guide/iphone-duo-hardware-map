# `MTLFunction` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) functionType;
@property (TQ,R) patchType;
@property (Tq,R) patchControlPointCount;
@property (T@"NSArray",R) vertexAttributes;
@property (T@"NSArray",R) stageInputAttributes;
@property (T@"NSString",R) name;
@property (T@"NSDictionary",R) functionConstantsDictionary;
@property (TQ,R) options;
```

## Instance methods

```
-[MTLFunction functionType];
-[MTLFunction stageInputAttributes];
-[MTLFunction device];
-[MTLFunction label];
-[MTLFunction functionConstantsDictionary];
-[MTLFunction vertexAttributes];
-[MTLFunction setLabel:];
-[MTLFunction patchType];
-[MTLFunction newArgumentEncoderWithBufferIndex:];
-[MTLFunction options];
-[MTLFunction newArgumentEncoderWithBufferIndex:reflection:];
-[MTLFunction name];
-[MTLFunction patchControlPointCount];
```
