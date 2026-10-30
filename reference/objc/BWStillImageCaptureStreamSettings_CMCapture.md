# `BWStillImageCaptureStreamSettings`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 25 instance variables, 18 properties, 71 instance methods, 1 class methods

## Instance variables

```
@"NSString" _portType;
@"NSString" _sensorIDString;
i _captureType;
Q _captureFlags;
@"BWBracketSettings" _bracketSettings;
@"NSArray" _validBracketedCaptureSequenceNumbers;
{?="value"q"timescale"i"flags"I"epoch"q} _preferredTimeMachinePTS;
i _timeMachineFrameCount;
i _referenceFrameIndex;
@"NSArray" _timeMachineBracketedCaptureParams;
@"NSDictionary" _preBracketFrameCaptureParams;
@"NSArray" _unifiedBracketedCaptureParams;
@"NSArray" _captureFrameInfos;
B _lensStabilizationEnabledForClientBracket;
B _usesUltraHighResolutionBuffersForStandardResolution;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _adaptiveBracketingLock;
@"<BWAdaptiveBracketingParameters>" _adaptiveBracketingParameters;
@"NSArray" _adaptiveBracketingSphereOffsets;
@"NSMutableArray" _adaptiveBracketingFrameParameters;
@"NSMutableArray" _adaptiveTimeMachineBracketedCaptureParams;
@"NSMutableArray" _adaptivePreBracketFrameCaptureParams;
@"NSMutableArray" _adaptiveUnifiedBracketedCaptureParams;
@"NSMutableArray" _adaptiveCaptureFrameInfos;
B _reachedEndOfAdaptiveBracketing;
{?="value"q"timescale"i"flags"I"epoch"q} _adaptiveBracketingLastFramePTS;
```

## Properties

```
@property (T@"NSString",R,N,V_portType) portType;
@property (T@"NSString",&,N,V_sensorIDString) sensorIDString;
@property (Ti,R,N,V_captureType) captureType;
@property (TQ,R,N,V_captureFlags) captureFlags;
@property (T@"BWBracketSettings",R,N,V_bracketSettings) bracketSettings;
@property (T@"NSArray",R,N,V_validBracketedCaptureSequenceNumbers) validBracketedCaptureSequenceNumbers;
@property (TB,R,N) hasValidFrames;
@property (Ti,R,N) expectedFrameCount;
@property (Ti,R,N) expectedFrameCaptureCount;
@property (T{?=iii},R,N) expectedFrameCaptureCounts;
@property (Ti,R,N) expectedUltraHighResFrameCaptureCount;
@property (TB,R,N) expectPreBracketFrame;
@property (T{?=qiIq},N,V_preferredTimeMachinePTS) preferredTimeMachinePTS;
@property (Ti,R,N,V_timeMachineFrameCount) timeMachineFrameCount;
@property (Ti,R,N) expectedTimeMachineFrameCaptureCount;
@property (TB,R,N) isYUVCapture;
@property (TB,R,N) isSensorRawCapture;
@property (Ti,R,N) resolutionFlavor;
```

## Class methods

```
+[BWStillImageCaptureStreamSettings supportsSecureCoding];
```

## Instance methods

```
-[BWStillImageCaptureStreamSettings sensorIDString];
-[BWStillImageCaptureStreamSettings portType];
-[BWStillImageCaptureStreamSettings updateForLearnedNRMissingEVZero:missingEVMinus:];
-[BWStillImageCaptureStreamSettings setPreferredTimeMachinePTS:];
-[BWStillImageCaptureStreamSettings timeMachineReferenceFrameIndex];
-[BWStillImageCaptureStreamSettings captureFrameInfoForFrame:];
-[BWStillImageCaptureStreamSettings timeMachineFrameCount];
-[BWStillImageCaptureStreamSettings isUnifiedBracketingErrorRecoveryFrame:isReferenceFrame:];
-[BWStillImageCaptureStreamSettings cannotProcessDeepFusionEnhancedResolution];
-[BWStillImageCaptureStreamSettings adaptiveBracketingSphereOffsetsForNextGroupWithFrameCount:];
-[BWStillImageCaptureStreamSettings timeMachineBracketedCaptureParams];
-[BWStillImageCaptureStreamSettings preferredTimeMachinePTS];
-[BWStillImageCaptureStreamSettings updateForFusionMissingEVMinus:missingHDRErrorRecoveryEVZero:];
-[BWStillImageCaptureStreamSettings dealloc];
-[BWStillImageCaptureStreamSettings captureFlags];
-[BWStillImageCaptureStreamSettings adaptiveBracketingLastFramePTS];
-[BWStillImageCaptureStreamSettings adaptiveUnifiedBracketedCaptureParams];
-[BWStillImageCaptureStreamSettings expectedFrameCaptureCounts];
-[BWStillImageCaptureStreamSettings expectedLongFrameCount];
-[BWStillImageCaptureStreamSettings captureFrameInfos];
-[BWStillImageCaptureStreamSettings isFirstAdaptiveBracketingFrame:];
-[BWStillImageCaptureStreamSettings adaptiveBracketingParameters];
-[BWStillImageCaptureStreamSettings referenceFrameIndex];
-[BWStillImageCaptureStreamSettings expectedFrameCount];
-[BWStillImageCaptureStreamSettings expectedAdaptiveBracketedTimeMachineFrameCountUsingGroup:];
-[BWStillImageCaptureStreamSettings currentExpectedAdaptiveBracketedFrameCount];
-[BWStillImageCaptureStreamSettings expectedAdaptiveBracketedTimeMachineFrameCaptureCountUsingGroup:];
-[BWStillImageCaptureStreamSettings currentExpectedAdaptiveBracketedFrameCaptureCount];
-[BWStillImageCaptureStreamSettings expectedTimeMachineFrameCaptureCount];
-[BWStillImageCaptureStreamSettings setLensStabilizationEnabledForClientBracket:];
-[BWStillImageCaptureStreamSettings captureType];
-[BWStillImageCaptureStreamSettings adaptiveBracketingGroupCaptureCount];
-[BWStillImageCaptureStreamSettings lensStabilizationEnabledForClientBracket];
-[BWStillImageCaptureStreamSettings adaptiveBracketingFrameParametersForFrame:];
-[BWStillImageCaptureStreamSettings initWithPortType:captureType:captureFlags:referenceFrameIndex:timeMachineBracketedCaptureParams:preBracketFrameCaptureParams:unifiedBracketedCaptureParams:frameInfos:];
-[BWStillImageCaptureStreamSettings sensorRawCapturedForFinalImageProcessing];
-[BWStillImageCaptureStreamSettings setSensorIDString:];
-[BWStillImageCaptureStreamSettings addAdaptiveBracketingMetadataIfNeededForFrame:];
-[BWStillImageCaptureStreamSettings encodeWithCoder:];
-[BWStillImageCaptureStreamSettings adaptiveTimeMachineBracketedCaptureParams];
-[BWStillImageCaptureStreamSettings expectPreBracketFrame];
-[BWStillImageCaptureStreamSettings disableAWBReflow];
-[BWStillImageCaptureStreamSettings expectedReferenceFrameCandidateCount];
-[BWStillImageCaptureStreamSettings hash];
-[BWStillImageCaptureStreamSettings resolutionFlavor];
-[BWStillImageCaptureStreamSettings description];
-[BWStillImageCaptureStreamSettings isSensorRawCapture];
-[BWStillImageCaptureStreamSettings isFrameCapturedForProcessing:];
-[BWStillImageCaptureStreamSettings hasValidFrames];
-[BWStillImageCaptureStreamSettings initWithCoder:];
-[BWStillImageCaptureStreamSettings addAdaptiveBracketingFrameParameters:timeMachineBracketedCaptureParams:preBracketFrameCaptureParams:unifiedBracketedCaptureParams:captureFrameInfos:];
-[BWStillImageCaptureStreamSettings initWithPortType:captureType:captureFlags:referenceFrameIndex:adaptiveBracketingParameters:sphereOffsets:];
-[BWStillImageCaptureStreamSettings reachedEndOfAdaptiveBracketing];
-[BWStillImageCaptureStreamSettings expectedFrameCaptureCount];
-[BWStillImageCaptureStreamSettings expectedAdaptiveBracketedFrameCaptureCountUsingGroup:];
-[BWStillImageCaptureStreamSettings preBracketFrameCaptureParams];
-[BWStillImageCaptureStreamSettings unifiedBracketedCaptureParams];
-[BWStillImageCaptureStreamSettings expectedEVZeroFrameCount];
-[BWStillImageCaptureStreamSettings cannotProcessDepthPhotos];
-[BWStillImageCaptureStreamSettings expectedUltraHighResFrameCaptureCount];
-[BWStillImageCaptureStreamSettings isEqual:];
-[BWStillImageCaptureStreamSettings isYUVCapture];
-[BWStillImageCaptureStreamSettings usesUltraHighResolutionBuffersForStandardResolution];
-[BWStillImageCaptureStreamSettings setAdaptiveBracketingLastFramePTS:];
-[BWStillImageCaptureStreamSettings bracketSettings];
-[BWStillImageCaptureStreamSettings hasCaptureFrameInfoWithMainFlags:sifrFlags:];
-[BWStillImageCaptureStreamSettings setReachedEndOfAdaptiveBracketing:];
-[BWStillImageCaptureStreamSettings setUsesUltraHighResolutionBuffersForStandardResolution:];
-[BWStillImageCaptureStreamSettings validBracketedCaptureSequenceNumbers];
-[BWStillImageCaptureStreamSettings adaptivePreBracketFrameCaptureParams];
-[BWStillImageCaptureStreamSettings initWithPortType:captureType:captureFlags:timeMachineFrameCount:bracketSettings:validBracketedCaptureSequenceNumbers:];
```
