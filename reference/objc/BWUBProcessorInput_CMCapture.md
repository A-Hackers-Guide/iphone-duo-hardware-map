# `BWUBProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- Protocols: `BWNoiseReductionAndFusionProcessorInput`
- 12 instance variables, 22 properties, 21 instance methods, 0 class methods

## Instance variables

```
i _fusionMode;
@"<BWUBProcessorInputDelegate>" _delegate;
@"NSMutableArray" _frames;
B _keepFrames;
i _receivedFrames;
B _receivedAllFrames;
^{opaqueCMSampleBuffer=} _referenceFrame;
^{opaqueCMSampleBuffer=} _errorRecoveryFrame;
B _emitErrorRecoveryFrame;
I _remainingProcessingCount;
i _adaptiveBracketingStopFrameCount;
@"NSMutableDictionary" _oisRecenteringLoggingData;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R,N) originalImage;
@property (T@"<BWUBProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (TB,N) keepFrames;
@property (T@"NSMutableDictionary",R,N) oisRecenteringLoggingData;
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
-[BWUBProcessorInput fusionMode];
-[BWUBProcessorInput evMinusReferenceFrame];
-[BWUBProcessorInput setRemainingProcessingCount:];
-[BWUBProcessorInput setKeepFrames:];
-[BWUBProcessorInput dealloc];
-[BWUBProcessorInput referenceFrame];
-[BWUBProcessorInput receivedAllFrames];
-[BWUBProcessorInput oisRecenteringLoggingData];
-[BWUBProcessorInput setDelegate:];
-[BWUBProcessorInput keepFrames];
-[BWUBProcessorInput originalImage];
-[BWUBProcessorInput setFusionMode:];
-[BWUBProcessorInput delegate];
-[BWUBProcessorInput stopAdaptiveBracketingWithGroup:];
-[BWUBProcessorInput remainingProcessingCount];
-[BWUBProcessorInput initWithSettings:portType:];
-[BWUBProcessorInput receivedFrames];
-[BWUBProcessorInput addFrame:];
-[BWUBProcessorInput errorRecoveryFrame];
-[BWUBProcessorInput emitErrorRecoveryFrame];
-[BWUBProcessorInput setEmitErrorRecoveryFrame:];
```
