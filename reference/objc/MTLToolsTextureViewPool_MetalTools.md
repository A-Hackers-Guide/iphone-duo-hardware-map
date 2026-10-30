# `MTLToolsTextureViewPool`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLTextureViewPoolGGDSPI`
- 0 instance variables, 8 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T{MTLResourceID=Q},R,N) baseResourceID;
@property (TQ,R,N) resourceViewCount;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R,N) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsTextureViewPool label];
-[MTLToolsTextureViewPool dealloc];
-[MTLToolsTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:];
-[MTLToolsTextureViewPool baseResourceID];
-[MTLToolsTextureViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:];
-[MTLToolsTextureViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:];
-[MTLToolsTextureViewPool initWithBaseObject:parent:];
-[MTLToolsTextureViewPool resourceViewCount];
-[MTLToolsTextureViewPool setTextureView:atIndex:];
-[MTLToolsTextureViewPool setTextureView:descriptor:atIndex:];
```
