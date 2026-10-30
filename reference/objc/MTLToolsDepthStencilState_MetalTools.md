# `MTLToolsDepthStencilState`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLDepthStencilStateSPI`
- 0 instance variables, 13 properties, 11 instance methods, 0 class methods

## Properties

```
@property (TB,R) readsDepth;
@property (TB,R) writesDepth;
@property (TB,R) readsStencil;
@property (TB,R) writesStencil;
@property (TQ,R) uniqueIdentifier;
@property (TQ,R,N) resourceIndex;
@property (T@"NSString",R) label;
@property (T@"<MTLDevice>",R) device;
@property (T{MTLResourceID=Q},R) gpuResourceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsDepthStencilState resourceIndex];
-[MTLToolsDepthStencilState device];
-[MTLToolsDepthStencilState label];
-[MTLToolsDepthStencilState dealloc];
-[MTLToolsDepthStencilState uniqueIdentifier];
-[MTLToolsDepthStencilState gpuResourceID];
-[MTLToolsDepthStencilState readsDepth];
-[MTLToolsDepthStencilState readsStencil];
-[MTLToolsDepthStencilState writesDepth];
-[MTLToolsDepthStencilState writesStencil];
-[MTLToolsDepthStencilState initWithDepthStencilState:descriptor:device:];
```
