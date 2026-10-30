# `BWAssistiveOverlayNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<MTLCommandQueue>" _metalCommandQueue;
@"BWAssistiveOverlayRenderer" _overlayRenderer;
@"NSObject<OS_dispatch_queue>" _renderQueue;
B _cycleDiagnosticOverlaysWhenRendererIsReady;
i _maxLossyCompressionLevel;
@"BWPixelBufferPool" _unpackedOutputPool;
@"BWPixelBufferPool" _highFrameRateOutputPool;
B _detectedHighFrameRate;
{?="value"q"timescale"i"flags"I"epoch"q} _previousPresentationTimeStamp;
```

## Class methods

```
+[BWAssistiveOverlayNode initialize];
```

## Instance methods

```
-[BWAssistiveOverlayNode renderSampleBuffer:forInput:];
-[BWAssistiveOverlayNode dealloc];
-[BWAssistiveOverlayNode setFocusPeakingOverlayState:];
-[BWAssistiveOverlayNode setSubstrateState:];
-[BWAssistiveOverlayNode setExposureClippingOverlayState:];
-[BWAssistiveOverlayNode nodeSubType];
-[BWAssistiveOverlayNode didSelectFormat:forInput:];
-[BWAssistiveOverlayNode initWithMetalCommandQueue:maxLossyCompressionLevel:];
-[BWAssistiveOverlayNode nodeType];
```
