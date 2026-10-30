# `MTKMeshBufferZone`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MDLMeshBufferZone`
- 5 instance variables, 7 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMutableOrderedSet" _buffers;
B _destroyInvoked;
@"MTKMeshBufferAllocator" _allocator;
Q _capacity;
@"<MTLBuffer>" _buffer;
```

## Properties

```
@property (TQ,R,N,V_capacity) capacity;
@property (T@"<MDLMeshBufferAllocator>",R,N,V_allocator) allocator;
@property (T@"<MTLBuffer>",R,N,V_buffer) buffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTKMeshBufferZone buffer];
-[MTKMeshBufferZone allocator];
-[MTKMeshBufferZone capacity];
-[MTKMeshBufferZone destroyBuffer:];
-[MTKMeshBufferZone initWithCapacity:allocator:];
-[MTKMeshBufferZone newBufferWithLength:type:];
```
