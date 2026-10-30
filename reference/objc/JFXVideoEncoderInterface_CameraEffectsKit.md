# `JFXVideoEncoderInterface`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
^{HEVCLosslessEncoder=iid^{OpaqueVTCompressionSession}{EncoderConfig=iiiidBBBB}{?=qiIq}III} m_encoder;
^{__CVBuffer=} m_preparedPixelBuffer;
B m_encoderInitialized;
{promise<opaqueCMSampleBuffer *>="__state_"^v} m_sampleBufferPromise;
d m_expectedFrameRate;
^{opaqueCMSampleBuffer=} _currentBuffer;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},V_currentBuffer) currentBuffer;
```

## Instance methods

```
-[JFXVideoEncoderInterface init];
-[JFXVideoEncoderInterface dealloc];
-[JFXVideoEncoderInterface currentBuffer];
-[JFXVideoEncoderInterface closeEncoder];
-[JFXVideoEncoderInterface encodeFrame:presentationTime:frameProperties:];
-[JFXVideoEncoderInterface initWithExpectedFrameRate:];
-[JFXVideoEncoderInterface setCurrentBuffer:];
-[JFXVideoEncoderInterface setupEncoderWithWidth:andHeight:imageFormat:andFramerate:];
-[JFXVideoEncoderInterface skipFrame];
-[JFXVideoEncoderInterface writeSampleBuffer:];
```
