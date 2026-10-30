# `AGXG19FamilySparseHeap`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLHeap`
- Protocols: `MTLHeapSPI`
- 8 instance variables, 22 properties, 16 instance methods, 0 class methods

## Instance variables

```
{vector<IOGPUMetalResource *, std::allocator<IOGPUMetalResource *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} _resources;
@"IOGPUMetalDevice<MTLDevice>" _device;
@"IOGPUMetalBuffer<MTLBuffer>" _sparse_pages_buffer;
@"IOGPUMetalBuffer<MTLBuffer>" _sparse_queue_buffer;
Q _size;
Q sparse_page_queue_addr;
I sparse_page_size;
I sparse_page_queue_alignment_padding;
```

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (TQ,R) size;
@property (TQ,R) usedSize;
@property (T@"IOGPUMetalResource",R) sparsePagesResource;
@property (T@"IOGPUMetalResource",R) sparseQueueResource;
@property (TQ,R) sparsePageQueueAddress;
@property (TQ,R) currentAllocatedSize;
@property (TQ,R) unfilteredResourceOptions;
@property (TQ,?,R,N) gpuAddress;
@property (TQ,?,R,N) protectionOptions;
@property (TQ,R,N) memoryPoolId;
@property (T@"NSString",C) label;
@property (TQ,R) storageMode;
@property (TQ,R) cpuCacheMode;
@property (TQ,R) hazardTrackingMode;
@property (TQ,R) resourceOptions;
@property (Tq,R) type;
@property (TQ,R) allocatedSize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilySparseHeap currentAllocatedSize];
-[AGXG19FamilySparseHeap usedSize];
-[AGXG19FamilySparseHeap initWithDevice:descriptor:];
-[AGXG19FamilySparseHeap newTextureWithDescriptor:atOffset:];
-[AGXG19FamilySparseHeap device];
-[AGXG19FamilySparseHeap dealloc];
-[AGXG19FamilySparseHeap newTextureWithDescriptor:];
-[AGXG19FamilySparseHeap size];
-[AGXG19FamilySparseHeap setPurgeableState:];
-[AGXG19FamilySparseHeap newBufferWithLength:options:atOffset:];
-[AGXG19FamilySparseHeap maxAvailableSizeWithAlignment:];
-[AGXG19FamilySparseHeap newBufferWithLength:options:];
-[AGXG19FamilySparseHeap removeTexture:];
-[AGXG19FamilySparseHeap sparsePageQueueAddress];
-[AGXG19FamilySparseHeap sparsePagesResource];
-[AGXG19FamilySparseHeap sparseQueueResource];
```
