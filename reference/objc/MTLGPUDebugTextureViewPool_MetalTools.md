# `MTLGPUDebugTextureViewPool`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsTextureViewPool`
- 1 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
{vector<id<MTLGPUDebugViewable>, std::allocator<id<MTLGPUDebugViewable>>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} viewables;
```

## Instance methods

```
-[MTLGPUDebugTextureViewPool dealloc];
-[MTLGPUDebugTextureViewPool setTextureViewFromBuffer:descriptor:offset:bytesPerRow:atIndex:];
-[MTLGPUDebugTextureViewPool copyResourceStatesFromPool:sourceRange:destinationLocation:];
-[MTLGPUDebugTextureViewPool copyResourceViewsFromPool:sourceRange:destinationIndex:];
-[MTLGPUDebugTextureViewPool setTextureView:atIndex:];
-[MTLGPUDebugTextureViewPool setTextureView:descriptor:atIndex:];
-[MTLGPUDebugTextureViewPool initWithTextureViewPool:device:];
-[MTLGPUDebugTextureViewPool getViewableAt:];
-[MTLGPUDebugTextureViewPool setView:resourceID:type:index:];
```
