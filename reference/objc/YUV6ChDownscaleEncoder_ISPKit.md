# `YUV6ChDownscaleEncoder`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"NSObject<OS_os_log>" _logger;
@"<MTLComputePipelineState>" _computePipelineState;
```

## Properties

```
@property (T@"<MTLComputePipelineState>",R,N,V_computePipelineState) computePipelineState;
```

## Instance methods

```
-[YUV6ChDownscaleEncoder initWithDevice:];
-[YUV6ChDownscaleEncoder computePipelineState];
-[YUV6ChDownscaleEncoder encodeToCommandBuffer:inputYUV6CH:outputDownscaled:];
-[YUV6ChDownscaleEncoder encodeToCommandBuffer:inputYUV6CH:outputDownscaled:gamma:];
```
