# `MTLIOAccelBuffer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLIOAccelResource`
- 8 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
^v _pointer;
@? _deallocator;
@"MTLIOAccelBuffer" _masterBuffer;
s _masterHeapIndex;
s _masterBufferIndex;
Q _masterBufferOffset;
Q _length;
^{__IOSurface=} _iosurface;
```

## Properties

```
@property (TQ,R) length;
@property (T^v,R,N) contents;
@property (T^{__IOSurface=},R,V_iosurface) iosurface;
@property (TQ,R) allocatedSize;
```

## Instance methods

```
-[MTLIOAccelBuffer didModifyRange:];
-[MTLIOAccelBuffer iosurface];
-[MTLIOAccelBuffer removeAllDebugMarkers];
-[MTLIOAccelBuffer copyAnnotations];
-[MTLIOAccelBuffer initWithHeap:resource:offset:length:];
-[MTLIOAccelBuffer setOwnerWithIdentity:];
-[MTLIOAccelBuffer _aneIOSurface];
-[MTLIOAccelBuffer addDebugMarker:range:];
-[MTLIOAccelBuffer newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:];
-[MTLIOAccelBuffer initWithDevice:iosurface:args:argsSize:];
-[MTLIOAccelBuffer initWithDevice:pointer:length:options:sysMemSize:vidMemSize:args:argsSize:deallocator:];
-[MTLIOAccelBuffer contents];
-[MTLIOAccelBuffer formattedDescription:];
-[MTLIOAccelBuffer allocatedSize];
-[MTLIOAccelBuffer dealloc];
-[MTLIOAccelBuffer length];
-[MTLIOAccelBuffer description];
-[MTLIOAccelBuffer initWithDevice:pointer:length:options:sysMemSize:vidMemSize:gpuAddress:args:argsSize:deallocator:];
-[MTLIOAccelBuffer initWithMasterBuffer:heapIndex:bufferIndex:bufferOffset:length:args:argsSize:];
```
