# `YPyramidEncoder`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"NSObject<OS_os_log>" _logger;
@"<MTLComputePipelineState>" _computePipelineState;
@"<MTLComputePipelineState>" _computePipelineStateHalfRes;
```

## Properties

```
@property (T@"<MTLComputePipelineState>",R,N,V_computePipelineState) computePipelineState;
@property (T@"<MTLComputePipelineState>",R,N,V_computePipelineStateHalfRes) computePipelineStateHalfRes;
```

## Instance methods

```
-[YPyramidEncoder initWithDevice:];
-[YPyramidEncoder computePipelineState];
-[YPyramidEncoder computePipelineStateHalfRes];
-[YPyramidEncoder encodeToCommandBuffer:inputYUV6CH:outputPyramid:];
```
