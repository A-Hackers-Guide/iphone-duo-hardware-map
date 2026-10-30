# `BWHVSFrame`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 37 instance variables, 31 properties, 57 instance methods, 1 class methods

## Instance variables

```
B _isPauseFrame;
B _isManualCapture;
f _pauseDurationInSec;
i _segmentIdx;
i _frameID;
I _sessionID;
f _frameScore;
f _cropPenalty;
f _petCropPenalty;
{?="value"q"timescale"i"flags"I"epoch"q} _timestamp;
f _auxScore;
f _finalCropRectLaplacianVariance;
f _deviceSharpnessSlope;
f _deviceSharpnessIntercept;
f _maxFaceProminence;
@"NSDictionary" _metadata;
^{__CVBuffer=} _yuvPixelBuffer;
{?="width"i"height"i} _yuvDimensions;
I _yuvPixelFormat;
^{opaqueCMSampleBuffer=} _rawEV0SampleBuffer;
^{opaqueCMSampleBuffer=} _rawSIFRSampleBuffer;
i _ev0RawCaptureID;
i _sifrRawCaptureID;
I _orientation;
Q _stillImageSceneFlags;
@"BWFrameStatisticsByPortType" _frameStatisticsByPortType;
@"BWStillImageCaptureMetadata" _stillImageCaptureMetadata;
@"NSData" _originalCameraIntrinsicMatrix;
@"NSDictionary" _originalCameraIntrinsicMatrixReferenceDimensions;
{?="value"q"timescale"i"flags"I"epoch"q} _sbufPresentationTimestamp;
q _captureSettingsID;
@"NSDictionary" _frameTrackingEntry;
@"NSData" _personMaskPNGData;
@"NSArray" _faceObservations;
@"NSArray" _pets;
@"NSArray" _people;
@"BWHVSEmbeddingAnalysisResult" _unifiedEmbeddingsOutput;
```

## Properties

```
@property (TB,N,V_isPauseFrame) isPauseFrame;
@property (TB,N,V_isManualCapture) isManualCapture;
@property (Tf,N,V_pauseDurationInSec) pauseDurationInSec;
@property (Ti,N,V_segmentIdx) segmentIdx;
@property (Ti,N,V_frameID) frameID;
@property (TI,R,N,V_sessionID) sessionID;
@property (Tf,R,N,V_frameScore) frameScore;
@property (T{?=qiIq},R,N,V_timestamp) timestamp;
@property (T^{opaqueCMSampleBuffer=},N) rawEV0SampleBuffer;
@property (T^{opaqueCMSampleBuffer=},N,V_rawSIFRSampleBuffer) rawSIFRSampleBuffer;
@property (T^{__CVBuffer=},R,N) hueMapPixelBuffer;
@property (Ti,R,N) ev0RawCaptureID;
@property (Ti,R,N) sifrRawCaptureID;
@property (T@"NSArray",R,N,V_faceObservations) faceObservations;
@property (T@"NSArray",R,N,V_pets) pets;
@property (T@"NSArray",R,N,V_people) people;
@property (T@"BWHVSEmbeddingAnalysisResult",R,N,V_unifiedEmbeddingsOutput) unifiedEmbeddingsOutput;
@property (T@"NSDictionary",R,N) metadataRepresentation;
@property (TB,R,N) hrEnabled;
@property (Td,R,N) exposureTime;
@property (Td,R,N) currentFrameRate;
@property (Tf,R,N,V_finalCropRectLaplacianVariance) finalCropRectLaplacianVariance;
@property (TQ,R,N,V_stillImageSceneFlags) stillImageSceneFlags;
@property (T@"BWFrameStatisticsByPortType",R,N,V_frameStatisticsByPortType) frameStatisticsByPortType;
@property (T@"BWStillImageCaptureMetadata",R,N,V_stillImageCaptureMetadata) stillImageCaptureMetadata;
@property (T@"NSData",R,N,V_originalCameraIntrinsicMatrix) originalCameraIntrinsicMatrix;
@property (T@"NSDictionary",R,N,V_originalCameraIntrinsicMatrixReferenceDimensions) originalCameraIntrinsicMatrixReferenceDimensions;
@property (T{?=qiIq},N,V_sbufPresentationTimestamp) sbufPresentationTimestamp;
@property (Tq,N,V_captureSettingsID) captureSettingsID;
@property (T@"NSDictionary",&,N,V_frameTrackingEntry) frameTrackingEntry;
@property (T@"NSData",&,N,V_personMaskPNGData) personMaskPNGData;
```

## Class methods

```
+[BWHVSFrame initialize];
```

## Instance methods

```
-[BWHVSFrame setFrameID:];
-[BWHVSFrame sessionID];
-[BWHVSFrame people];
-[BWHVSFrame dealloc];
-[BWHVSFrame timestamp];
-[BWHVSFrame hrEnabled];
-[BWHVSFrame exposureTime];
-[BWHVSFrame frameID];
-[BWHVSFrame currentFrameRate];
-[BWHVSFrame faceObservations];
-[BWHVSFrame description];
-[BWHVSFrame frameStatisticsByPortType];
-[BWHVSFrame frameScore];
-[BWHVSFrame ev0RawCaptureID];
-[BWHVSFrame isManualCapture];
-[BWHVSFrame _computeCropPenaltyForFaceRects:bodyRects:faceEdgeThreshold:bodyEdgeThreshold:minBodyAreaRatio:finalCropRect:];
-[BWHVSFrame _computeCropPenaltyWithFaceEdgeThreshold:bodyEdgeThreshold:minBodyAreaRatio:percentOfLargestFace:minFaceArea:finalCropRect:];
-[BWHVSFrame _computeMaskedFaceSharpnessWithPercentOfLargestFace:minFaceArea:threshold:capRange:sensitivity:normalizeMax:];
-[BWHVSFrame _computePetCropPenaltyWithFaceEdgeThreshold:bodyEdgeThreshold:minBodyAreaRatio:finalCropRect:];
-[BWHVSFrame _faceCombinedFactor:mlvLow:mlvHigh:bonusRange:maxBonus:];
-[BWHVSFrame _mapAndNormalizeScore:threshold:capRange:sensitivity:normalizeMax:];
-[BWHVSFrame _normalizeAuxScore:statsDict:];
-[BWHVSFrame _normalizeDeviceSharpness:];
-[BWHVSFrame _normalizeGlobalSharpness:divisor:multiplier:];
-[BWHVSFrame captureSettingsID];
-[BWHVSFrame finalCropRectLaplacianVariance];
-[BWHVSFrame frameTrackingEntry];
-[BWHVSFrame hueMapPixelBuffer];
-[BWHVSFrame initWithSampleBuffer:hvsFrameMetadata:hvsConfig:sessionID:];
-[BWHVSFrame initWithYUVSampleBuffer:rawEV0SampleBuffer:rawSIFRSampleBuffer:inputNetworkOutput:inputFaceObservations:pinnedSubjectsArray:hvsConfig:sessionID:sharpnessResults:cacheYUVPixelBuffer:];
-[BWHVSFrame isPauseFrame];
-[BWHVSFrame metadataRepresentation];
-[BWHVSFrame newMutableCopiedRawEV0SampleBuffer];
-[BWHVSFrame newMutableCopiedRawSIFRSampleBuffer];
-[BWHVSFrame originalCameraIntrinsicMatrix];
-[BWHVSFrame originalCameraIntrinsicMatrixReferenceDimensions];
-[BWHVSFrame pauseDurationInSec];
-[BWHVSFrame personMaskPNGData];
-[BWHVSFrame pets];
-[BWHVSFrame rawEV0SampleBuffer];
-[BWHVSFrame rawSIFRSampleBuffer];
-[BWHVSFrame sbufPresentationTimestamp];
-[BWHVSFrame segmentIdx];
-[BWHVSFrame setCaptureSettingsID:];
-[BWHVSFrame setFrameTrackingEntry:];
-[BWHVSFrame setIsManualCapture:];
-[BWHVSFrame setIsPauseFrame:];
-[BWHVSFrame setPauseDurationInSec:];
-[BWHVSFrame setPersonMaskPNGData:];
-[BWHVSFrame setRawEV0SampleBuffer:];
-[BWHVSFrame setRawSIFRSampleBuffer:];
-[BWHVSFrame setSbufPresentationTimestamp:];
-[BWHVSFrame setSegmentIdx:];
-[BWHVSFrame sifrRawCaptureID];
-[BWHVSFrame stillImageCaptureMetadata];
-[BWHVSFrame stillImageSceneFlags];
-[BWHVSFrame unifiedEmbeddingsOutput];
```
