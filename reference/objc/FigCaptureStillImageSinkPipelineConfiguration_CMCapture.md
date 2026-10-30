# `FigCaptureStillImageSinkPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureBaseStillImageSinkPipelineConfiguration`
- Protocols: `NSSecureCoding`
- 7 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
i _clientPID;
@"NSDictionary" _stillImageColorInfoForFramesOriginatingFromVideoStream;
B _stillImageISPChromaNoiseReductionEnabled;
B _stereoFusionSupported;
B _isIrisSupported;
B _hdrSupported;
B _gnrHDRSupported;
```

## Class methods

```
+[FigCaptureStillImageSinkPipelineConfiguration supportsSecureCoding];
```

## Instance methods

```
-[FigCaptureStillImageSinkPipelineConfiguration dealloc];
-[FigCaptureStillImageSinkPipelineConfiguration encodeWithCoder:];
-[FigCaptureStillImageSinkPipelineConfiguration initWithCoder:];
-[FigCaptureStillImageSinkPipelineConfiguration isEqual:];
```
