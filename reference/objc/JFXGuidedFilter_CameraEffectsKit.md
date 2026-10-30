# `JFXGuidedFilter`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"MPSImageGuidedFilter" _osGuidedFilter;
B _useCPU;
@"<MTLDevice>" _device;
@"<MTLCommandQueue>" _commandQueue;
^{__CVPixelBufferPool=} _coeffPool;
^{__CVMetalTextureCache=} _textureCache;
Q _guideImageWidth;
Q _guideImageHeight;
```

## Instance methods

```
-[JFXGuidedFilter dealloc];
-[JFXGuidedFilter initWithDiameter:];
-[JFXGuidedFilter scaleImage:guidanceImage:destinationImage:];
```
