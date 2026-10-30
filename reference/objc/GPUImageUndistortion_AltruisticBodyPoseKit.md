# `GPUImageUndistortion`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLComputePipelineState>" _pipelineState;
@"<MTLComputePipelineState>" _lutGenerationPipelineState;
@"<MTLTexture>" _lut;
{?="columns"[3]} _fisheyeIntrinsics;
_fisheyeRadialCoefficients;
{?="columns"[3]} _rectilinearIntrinsics;
@"<MTLLibrary>" _library;
```

## Instance methods

```
-[GPUImageUndistortion init];
-[GPUImageUndistortion undistortFisheyeImage:withFisheyeIntrinsics:withFisheyeRadialCoefficients:toRectilinearImage:withRectilinearIntrinsics:];
```
