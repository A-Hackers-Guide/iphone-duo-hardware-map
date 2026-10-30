# `BWStillImageSampleBufferSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWSinkNode`
- 13 instance variables, 1 properties, 25 instance methods, 1 class methods

## Instance variables

```
@? _sampleBufferAvailableHandler;
i _stillImageCapturePipeliningMode;
B _deferredPhotoProcessorEnabled;
B _clientIsCameraOrDerivative;
B _captureTimePhotosCurationSupported;
@"NSArray" _propagatedAttachedMediaKeys;
B _focusPixelBlurScoreEnabled;
@"BWStillImageSampleBufferSinkNodeAnalyticsConfiguration" _analyticsConfiguration;
B _cameraSupportsFlash;
q _lastCaptureRequestTime;
q _lastReportedSettingsID;
@"BWStillImageAnalyticsPayloadCommon" _cachedAnalyticsPayloadForPortraitFailures;
@"BWStillImageFrameCoordinatorNode" _frameCoordinatorNode;
```

## Properties

```
@property (T@?,C,N,V_sampleBufferAvailableHandler) sampleBufferAvailableHandler;
```

## Class methods

```
+[BWStillImageSampleBufferSinkNode initialize];
```

## Instance methods

```
-[BWStillImageSampleBufferSinkNode initWithSinkID:];
-[BWStillImageSampleBufferSinkNode stillImageCapturePipeliningMode];
-[BWStillImageSampleBufferSinkNode focusPixelBlurScoreEnabled];
-[BWStillImageSampleBufferSinkNode captureTimePhotosCurationSupported];
-[BWStillImageSampleBufferSinkNode setPropagatedAttachedMediaKeys:];
-[BWStillImageSampleBufferSinkNode setFocusPixelBlurScoreEnabled:];
-[BWStillImageSampleBufferSinkNode deferredPhotoProcessorEnabled];
-[BWStillImageSampleBufferSinkNode setCameraSupportsFlash:];
-[BWStillImageSampleBufferSinkNode renderSampleBuffer:forInput:];
-[BWStillImageSampleBufferSinkNode cameraSupportsFlash];
-[BWStillImageSampleBufferSinkNode clientIsCameraOrDerivative];
-[BWStillImageSampleBufferSinkNode setDeferredPhotoProcessorEnabled:];
-[BWStillImageSampleBufferSinkNode setClientIsCameraOrDerivative:];
-[BWStillImageSampleBufferSinkNode dealloc];
-[BWStillImageSampleBufferSinkNode setCaptureTimePhotosCurationSupported:];
-[BWStillImageSampleBufferSinkNode setStillImageCapturePipeliningMode:];
-[BWStillImageSampleBufferSinkNode analyticsConfiguration];
-[BWStillImageSampleBufferSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWStillImageSampleBufferSinkNode propagatedAttachedMediaKeys];
-[BWStillImageSampleBufferSinkNode sampleBufferAvailableHandler];
-[BWStillImageSampleBufferSinkNode nodeSubType];
-[BWStillImageSampleBufferSinkNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStillImageSampleBufferSinkNode handleNodeError:forInput:];
-[BWStillImageSampleBufferSinkNode setSampleBufferAvailableHandler:];
-[BWStillImageSampleBufferSinkNode setAnalyticsConfiguration:];
```
