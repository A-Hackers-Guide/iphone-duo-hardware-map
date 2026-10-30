# `BWCoreImageIntermediateAllocator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CIContextIntermediateAllocator`
- 3 instance variables, 9 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<MTLDeviceSPI>" _device;
@"FigMetalAllocator" _metalAllocator;
Q _poolID;
```

## Properties

```
@property (T@"FigMetalAllocator",R,V_metalAllocator) metalAllocator;
@property (TQ,R,V_poolID) poolID;
@property (T@"<MTLDeviceSPI>",R,V_device) device;
@property (TQ,R) totalSize;
@property (TQ,R) maxAvailableAllocationSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWCoreImageIntermediateAllocator device];
-[BWCoreImageIntermediateAllocator dealloc];
-[BWCoreImageIntermediateAllocator totalSize];
-[BWCoreImageIntermediateAllocator bufferForContextIntermediateCommitted:];
-[BWCoreImageIntermediateAllocator bufferForContextIntermediateCompleted:];
-[BWCoreImageIntermediateAllocator maxAvailableAllocationSize];
-[BWCoreImageIntermediateAllocator newBufferForContextIntermediate:usingHint:identifier:];
-[BWCoreImageIntermediateAllocator initWithBackend:allocatorBackend:memoryPool:];
-[BWCoreImageIntermediateAllocator metalAllocator];
-[BWCoreImageIntermediateAllocator poolID];
```
