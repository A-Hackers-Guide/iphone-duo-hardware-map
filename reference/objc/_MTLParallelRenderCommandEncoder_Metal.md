# `_MTLParallelRenderCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLParallelRenderCommandEncoder`
- 16 instance variables, 8 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"<MTLCommandQueue>" _queue;
Q _globalTraceObjectID;
Q _labelTraceID;
@"_MTLCommandBuffer<MTLCommandBuffer>" _commandBuffer;
@"MTLRenderPassDescriptor" _renderPassDescriptor;
{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]} _lock;
Q _commandBuffersSize;
Q _commandBuffersCount;
^@ _commandBuffers;
B _retainedReferences;
B _StatEnabled;
Q _numThisEncoder;
@"<MTLFence>" _progressFence;
B _needsFrameworkAssistedErrorTracking;
@"NSMutableArray" _debugSignposts;
```

## Properties

```
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (TQ,R,D,N,GgetType) type;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",C,D) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTLParallelRenderCommandEncoder insertDebugSignpost:];
-[_MTLParallelRenderCommandEncoder pushDebugGroup:];
-[_MTLParallelRenderCommandEncoder setColorStoreAction:atIndex:];
-[_MTLParallelRenderCommandEncoder popDebugGroup];
-[_MTLParallelRenderCommandEncoder formattedDescription:];
-[_MTLParallelRenderCommandEncoder device];
-[_MTLParallelRenderCommandEncoder endEncoding];
-[_MTLParallelRenderCommandEncoder globalTraceObjectID];
-[_MTLParallelRenderCommandEncoder dealloc];
-[_MTLParallelRenderCommandEncoder setStencilStoreActionOptions:];
-[_MTLParallelRenderCommandEncoder setStencilStoreAction:];
-[_MTLParallelRenderCommandEncoder commandBuffer];
-[_MTLParallelRenderCommandEncoder description];
-[_MTLParallelRenderCommandEncoder setDepthStoreAction:];
-[_MTLParallelRenderCommandEncoder setDepthStoreActionOptions:];
-[_MTLParallelRenderCommandEncoder setColorStoreActionOptions:atIndex:];
-[_MTLParallelRenderCommandEncoder isMemorylessRender];
-[_MTLParallelRenderCommandEncoder _renderCommandEncoderCommon];
-[_MTLParallelRenderCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[_MTLParallelRenderCommandEncoder getDriverUniqueID];
-[_MTLParallelRenderCommandEncoder initWithCommandBuffer:renderPassDescriptor:];
-[_MTLParallelRenderCommandEncoder initializeEnhancedCommandBufferErrors];
-[_MTLParallelRenderCommandEncoder insertSplit];
-[_MTLParallelRenderCommandEncoder preEndEncoding];
-[_MTLParallelRenderCommandEncoder renderCommandEncoder];
-[_MTLParallelRenderCommandEncoder sampledRenderCommandEncoderWithProgramInfoBuffer:capacity:];
```
