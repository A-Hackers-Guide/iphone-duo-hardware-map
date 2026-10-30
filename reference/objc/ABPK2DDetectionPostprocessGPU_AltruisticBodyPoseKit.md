# `ABPK2DDetectionPostprocessGPU`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _nChannels;
@"<MTLDevice>" _device;
@"<MTLCommandQueue>" _commandQueue;
@"<MTLComputePipelineState>" _pipelineStateInterpolate;
@"<MTLComputePipelineState>" _pipelineStateMaxFilter;
@"<MTLBuffer>" _input;
@"<MTLBuffer>" _intermediate;
@"<MTLBuffer>" _output;
@"<MTLLibrary>" _library;
```

## Instance methods

```
-[ABPK2DDetectionPostprocessGPU init];
-[ABPK2DDetectionPostprocessGPU dealloc];
-[ABPK2DDetectionPostprocessGPU _copyToInputAsFloat16:shape:];
-[ABPK2DDetectionPostprocessGPU initWithNumberOfChannels:];
-[ABPK2DDetectionPostprocessGPU process:counter:shape:];
```
