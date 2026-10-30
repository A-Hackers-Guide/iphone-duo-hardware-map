# `JFXVideoDecoderInterface`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
^{OpaqueVTDecompressionSession=} _session;
d m_expectedFrameRate;
@"NSObject<OS_dispatch_semaphore>" _frameSemaphore;
^{__CVBuffer=} _imageBuffer;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_frameSemaphore) frameSemaphore;
@property (T^{__CVBuffer=},V_imageBuffer) imageBuffer;
```

## Instance methods

```
-[JFXVideoDecoderInterface imageBuffer];
-[JFXVideoDecoderInterface init];
-[JFXVideoDecoderInterface initWithFormatDescription:];
-[JFXVideoDecoderInterface dealloc];
-[JFXVideoDecoderInterface setImageBuffer:];
-[JFXVideoDecoderInterface decodeFrame:];
-[JFXVideoDecoderInterface frameSemaphore];
-[JFXVideoDecoderInterface setFrameSemaphore:];
```
