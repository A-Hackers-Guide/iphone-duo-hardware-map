# `MTKMeshBufferAllocator`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MDLMeshBufferAllocator`
- 1 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
```

## Properties

```
@property (T@"<MTLDevice>",R,N,V_device) device;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTKMeshBufferAllocator initWithDevice:];
-[MTKMeshBufferAllocator device];
-[MTKMeshBufferAllocator isEqual:];
-[MTKMeshBufferAllocator newBuffer:type:];
-[MTKMeshBufferAllocator newBufferWithData:type:];
-[MTKMeshBufferAllocator newBufferFromZone:data:type:];
-[MTKMeshBufferAllocator newBufferFromZone:length:type:];
-[MTKMeshBufferAllocator newZone:];
-[MTKMeshBufferAllocator newZoneForBuffersWithSize:andType:];
```
