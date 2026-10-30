# `_MTLDepthStencilState`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLDepthStencilStateSPI`
- 2 instance variables, 13 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"NSString" _label;
```

## Properties

```
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",R,V_label) label;
@property (TB,R) readsDepth;
@property (TB,R) writesDepth;
@property (TB,R) readsStencil;
@property (TB,R) writesStencil;
@property (TQ,R) uniqueIdentifier;
@property (TQ,R,N) resourceIndex;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLDepthStencilState resourceIndex];
-[_MTLDepthStencilState formattedDescription:];
-[_MTLDepthStencilState device];
-[_MTLDepthStencilState label];
-[_MTLDepthStencilState dealloc];
-[_MTLDepthStencilState uniqueIdentifier];
-[_MTLDepthStencilState description];
-[_MTLDepthStencilState gpuResourceID];
-[_MTLDepthStencilState initWithDevice:depthStencilDescriptor:];
-[_MTLDepthStencilState readsDepth];
-[_MTLDepthStencilState readsStencil];
-[_MTLDepthStencilState writesDepth];
-[_MTLDepthStencilState writesStencil];
```
