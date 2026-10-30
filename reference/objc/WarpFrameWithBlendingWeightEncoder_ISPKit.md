# `WarpFrameWithBlendingWeightEncoder`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 3 instance methods, 0 class methods

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
-[WarpFrameWithBlendingWeightEncoder initWithDevice:];
-[WarpFrameWithBlendingWeightEncoder computePipelineState];
-[WarpFrameWithBlendingWeightEncoder encodeToCommandBuffer:inputYTexture:inputUVTexture:sxsyTexture:outputYTexture:outputUVTexture:blendingWeightTexture:homography:warpHomographyOnly:];
```
