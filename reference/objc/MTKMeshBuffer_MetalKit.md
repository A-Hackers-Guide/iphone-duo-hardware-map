# `MTKMeshBuffer`

- Image: [`/System/Library/Frameworks/MetalKit.framework/MetalKit`](../userland/System__Library__Frameworks__MetalKit.framework__MetalKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MDLMeshBuffer`, `MDLNamed`
- 6 instance variables, 11 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"MTKMeshBufferZone" _zone;
Q _length;
@"MTKMeshBufferAllocator" _allocator;
@"<MTLBuffer>" _buffer;
Q _offset;
Q _type;
```

## Properties

```
@property (TQ,R,N,V_length) length;
@property (T@"MTKMeshBufferAllocator",R,N,V_allocator) allocator;
@property (T@"<MDLMeshBufferZone>",R,N,V_zone) zone;
@property (T@"<MTLBuffer>",R,N,V_buffer) buffer;
@property (TQ,R,N,V_offset) offset;
@property (TQ,R,N,V_type) type;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",C,N) name;
```

## Instance methods

```
-[MTKMeshBuffer buffer];
-[MTKMeshBuffer allocator];
-[MTKMeshBuffer zone];
-[MTKMeshBuffer dealloc];
-[MTKMeshBuffer length];
-[MTKMeshBuffer type];
-[MTKMeshBuffer setName:];
-[MTKMeshBuffer map];
-[MTKMeshBuffer copyWithZone:];
-[MTKMeshBuffer name];
-[MTKMeshBuffer offset];
-[MTKMeshBuffer fillData:offset:];
-[MTKMeshBuffer _initWithLength:allocator:type:];
-[MTKMeshBuffer _initWithBytes:length:offset:allocator:zone:type:];
-[MTKMeshBuffer _initWithData:allocator:type:];
-[MTKMeshBuffer _initWithLength:offset:zone:type:];
-[MTKMeshBuffer _newMap];
```
