# `MDLMeshBuffer` (protocol)

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 4 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) length;
@property (T@"<MDLMeshBufferAllocator>",R,&,N) allocator;
@property (T@"<MDLMeshBufferZone>",R,&,N) zone;
@property (TQ,R,N) type;
```

## Instance methods

```
-[MDLMeshBuffer allocator];
-[MDLMeshBuffer zone];
-[MDLMeshBuffer length];
-[MDLMeshBuffer type];
-[MDLMeshBuffer map];
-[MDLMeshBuffer fillData:offset:];
```
