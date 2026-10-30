# `BWUBNRFProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- Protocols: `BWNoiseReductionAndFusionProcessorInput`
- 14 instance variables, 24 properties, 24 instance methods, 0 class methods

## Instance variables

```
i _fusionMode;
@"<BWUBNRFProcessorInputDelegate>" _delegate;
@"NSMutableArray" _frames;
^{__CVBuffer=} _gainMapPixelBuffer;
B _keepFrames;
i _receivedFrames;
B _receivedAllFrames;
^{opaqueCMSampleBuffer=} _referenceFrame;
^{opaqueCMSampleBuffer=} _errorRecoveryFrame;
B _emitErrorRecoveryFrame;
I _remainingProcessingCount;
i _adaptiveBracketingStopFrameCount;
@"NSMutableDictionary" _oisRecenteringLoggingData;
i _ispMotionHighPassFilterConvergenceFlags;
```

## Properties

```
@property (Ti,R,N) expectedFrameCount;
@property (T^{opaqueCMSampleBuffer=},R,N) originalImage;
@property (T@"<BWUBNRFProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (TB,N) keepFrames;
@property (T@"NSMutableDictionary",R,N) oisRecenteringLoggingData;
@property (Ti,R,N) ispMotionHighPassFilterConvergenceFlags;
@property (T@"BWStillImageSettings",R,N) stillImageSettings;
@property (T@"FigCaptureStillImageSettings",R,N) settings;
@property (T@"BWStillImageCaptureSettings",R,N) captureSettings;
@property (T@"BWStillImageCaptureStreamSettings",R,N) captureStreamSettings;
@property (TB,R,N) isMaster;
@property (T@"NSString",R,N) portType;
@property (Ti,R,N) receivedFrames;
@property (TB,R,N) receivedAllFrames;
@property (T^{opaqueCMSampleBuffer=},R,N) referenceFrame;
@property (T^{opaqueCMSampleBuffer=},R,N) evMinusReferenceFrame;
@property (T^{opaqueCMSampleBuffer=},R,N) errorRecoveryFrame;
@property (Ti,N,V_fusionMode) fusionMode;
@property (TB,N,V_emitErrorRecoveryFrame) emitErrorRecoveryFrame;
@property (TI,N,V_remainingProcessingCount) remainingProcessingCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWUBNRFProcessorInput fusionMode];
-[BWUBNRFProcessorInput evMinusReferenceFrame];
-[BWUBNRFProcessorInput setRemainingProcessingCount:];
-[BWUBNRFProcessorInput setKeepFrames:];
-[BWUBNRFProcessorInput dealloc];
-[BWUBNRFProcessorInput referenceFrame];
-[BWUBNRFProcessorInput receivedAllFrames];
-[BWUBNRFProcessorInput oisRecenteringLoggingData];
-[BWUBNRFProcessorInput setDelegate:];
-[BWUBNRFProcessorInput expectedFrameCount];
-[BWUBNRFProcessorInput keepFrames];
-[BWUBNRFProcessorInput originalImage];
-[BWUBNRFProcessorInput setFusionMode:];
-[BWUBNRFProcessorInput delegate];
-[BWUBNRFProcessorInput description];
-[BWUBNRFProcessorInput ispMotionHighPassFilterConvergenceFlags];
-[BWUBNRFProcessorInput stopAdaptiveBracketingWithGroup:];
-[BWUBNRFProcessorInput remainingProcessingCount];
-[BWUBNRFProcessorInput initWithSettings:portType:];
-[BWUBNRFProcessorInput receivedFrames];
-[BWUBNRFProcessorInput addFrame:];
-[BWUBNRFProcessorInput errorRecoveryFrame];
-[BWUBNRFProcessorInput emitErrorRecoveryFrame];
-[BWUBNRFProcessorInput setEmitErrorRecoveryFrame:];
```
