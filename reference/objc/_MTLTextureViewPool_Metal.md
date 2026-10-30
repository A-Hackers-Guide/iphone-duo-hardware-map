# `_MTLTextureViewPool`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLResourceViewPool`
- Protocols: `MTLTextureViewPoolGGDSPI`
- 0 instance variables, 8 properties, 4 instance methods, 0 class methods

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
-[_MTLTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:];
-[_MTLTextureViewPool setBufferView:descriptor:offset:bytesPerRow:atIndex:];
-[_MTLTextureViewPool setTextureView:atIndex:];
-[_MTLTextureViewPool setTextureView:descriptor:atIndex:];
```
