# `BWNRFProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 15 instance variables, 16 properties, 27 instance methods, 0 class methods

## Instance variables

```
i _resolutionFlavor;
i _fusionMode;
@"<BWNRFProcessorInputDelegate>" _delegate;
@"NSMutableArray" _frames;
^{__CVBuffer=} _gainMapPixelBuffer;
B _keepFrames;
i _receivedFrames;
B _receivedAllFrames;
^{opaqueCMSampleBuffer=} _referenceFrame;
^{opaqueCMSampleBuffer=} _errorRecoveryFrame;
I _remainingProcessingCount;
i _adaptiveBracketingStopFrameCount;
@"NSMutableDictionary" _oisRecenteringLoggingData;
i _ispMotionHighPassFilterConvergenceFlags;
@"NSDictionary" _referenceFrameAttachments;
```

## Properties

```
@property (Ti,R,N,V_resolutionFlavor) resolutionFlavor;
@property (Ti,R,N) expectedFrameCount;
@property (T^{opaqueCMSampleBuffer=},R,N) originalImage;
@property (T@"<BWNRFProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (TB,N) keepFrames;
@property (T@"NSMutableDictionary",R,N) oisRecenteringLoggingData;
@property (Ti,R,N) ispMotionHighPassFilterConvergenceFlags;
@property (TB,R,N) learnedNRProxyProcessingUsingDeepFusionProxy;
@property (T@"NSDictionary",C,N,V_referenceFrameAttachments) referenceFrameAttachments;
@property (Ti,R,N) receivedFrames;
@property (TB,R,N) receivedAllFrames;
@property (T^{opaqueCMSampleBuffer=},R,N) referenceFrame;
@property (T^{opaqueCMSampleBuffer=},R,N) evMinusReferenceFrame;
@property (T^{opaqueCMSampleBuffer=},R,N) errorRecoveryFrame;
@property (Ti,N,V_fusionMode) fusionMode;
@property (TI,N,V_remainingProcessingCount) remainingProcessingCount;
```

## Instance methods

```
-[BWNRFProcessorInput fusionMode];
-[BWNRFProcessorInput evMinusReferenceFrame];
-[BWNRFProcessorInput setRemainingProcessingCount:];
-[BWNRFProcessorInput setKeepFrames:];
-[BWNRFProcessorInput dealloc];
-[BWNRFProcessorInput setReferenceFrameAttachments:];
-[BWNRFProcessorInput referenceFrame];
-[BWNRFProcessorInput receivedAllFrames];
-[BWNRFProcessorInput oisRecenteringLoggingData];
-[BWNRFProcessorInput setDelegate:];
-[BWNRFProcessorInput expectedFrameCount];
-[BWNRFProcessorInput learnedNRProxyProcessingUsingDeepFusionProxy];
-[BWNRFProcessorInput keepFrames];
-[BWNRFProcessorInput originalImage];
-[BWNRFProcessorInput setFusionMode:];
-[BWNRFProcessorInput initWithSettings:portType:resolutionFlavor:];
-[BWNRFProcessorInput delegate];
-[BWNRFProcessorInput resolutionFlavor];
-[BWNRFProcessorInput setProcessedRawErrorRecoveryFrame:proxy:];
-[BWNRFProcessorInput description];
-[BWNRFProcessorInput ispMotionHighPassFilterConvergenceFlags];
-[BWNRFProcessorInput referenceFrameAttachments];
-[BWNRFProcessorInput stopAdaptiveBracketingWithGroup:];
-[BWNRFProcessorInput remainingProcessingCount];
-[BWNRFProcessorInput receivedFrames];
-[BWNRFProcessorInput addFrame:];
-[BWNRFProcessorInput errorRecoveryFrame];
```
