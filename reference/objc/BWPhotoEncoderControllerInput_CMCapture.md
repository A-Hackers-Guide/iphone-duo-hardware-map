# `BWPhotoEncoderControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 21 instance variables, 21 properties, 37 instance methods, 0 class methods

## Instance variables

```
I _expectedFramesCount;
B _requiresPhotosAdjustment;
I _receivedFramesCount;
^{opaqueCMSampleBuffer=} _sbufToProcess;
^{opaqueCMSampleBuffer=} _primarySampleBuffer;
q _reservedPrimaryImageHandle;
q _gainMapHandle;
q _toneMapAlternateGroupHandle;
B _fatalErrorOccurred;
B _processingCanceled;
{?="mono"q"left"q"right"q} _stereoPhotoImageHandles;
Q _monoImageLocationType;
@"NSDictionary" _decompressStyledBufferAttributes;
@"NSMutableSet" _encodedAttachedMediaKeys;
@"NSMutableDictionary" _stashedAttacheMediaSampleBuffersByAttachedMediaKey;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stashedAttachedMediaSampleBuffersLock;
@"NSDictionary" _primaryImageMetadataForPrewarming;
I _processingFlagsForPrewarming;
B _fsincMasksPrewarmedForCurrentEncoding;
B _deltaMapIsValid;
i _textOrientationSuggestedExifOrientation;
```

## Properties

```
@property (TB,R,N,V_requiresPhotosAdjustment) requiresPhotosAdjustment;
@property (T^{opaqueCMSampleBuffer=},R,N,V_sbufToProcess) sbufToProcess;
@property (Tq,R,N) settingsID;
@property (TI,R,N,V_receivedFramesCount) receivedFramesCount;
@property (T^{opaqueCMSampleBuffer=},R,N,V_primarySampleBuffer) primarySampleBuffer;
@property (TB,V_processingCanceled) processingCanceled;
@property (TB,N,V_fatalErrorOccurred) fatalErrorOccurred;
@property (Tq,N,V_reservedPrimaryImageHandle) reservedPrimaryImageHandle;
@property (Tq,N,V_gainMapHandle) gainMapHandle;
@property (Tq,N,V_toneMapAlternateGroupHandle) toneMapAlternateGroupHandle;
@property (TB,R,N) isStereoPhotoCapture;
@property (T{?=qqq},N,V_stereoPhotoImageHandles) stereoPhotoImageHandles;
@property (TQ,N,V_monoImageLocationType) monoImageLocationType;
@property (TB,N,V_deltaMapIsValid) deltaMapIsValid;
@property (Ti,R,N,V_textOrientationSuggestedExifOrientation) textOrientationSuggestedExifOrientation;
@property (T@"NSMutableSet",R,N,V_encodedAttachedMediaKeys) encodedAttachedMediaKeys;
@property (T@"NSDictionary",R,N,V_primaryImageMetadataForPrewarming) primaryImageMetadataForPrewarming;
@property (TI,R,N,V_processingFlagsForPrewarming) processingFlagsForPrewarming;
@property (TB,N,V_fsincMasksPrewarmedForCurrentEncoding) fsincMasksPrewarmedForCurrentEncoding;
@property (T@"NSDictionary",&,N,V_decompressStyledBufferAttributes) decompressStyledBufferAttributes;
@property (TB,R,N) receivedAllFramesInSingleContainer;
```

## Instance methods

```
-[BWPhotoEncoderControllerInput decompressStyledBufferAttributes];
-[BWPhotoEncoderControllerInput setMonoImageLocationType:];
-[BWPhotoEncoderControllerInput primarySampleBuffer];
-[BWPhotoEncoderControllerInput setStereoPhotoImageHandles:];
-[BWPhotoEncoderControllerInput gainMapHandle];
-[BWPhotoEncoderControllerInput fsincMasksPrewarmedForCurrentEncoding];
-[BWPhotoEncoderControllerInput encodedAttachedMediaKeys];
-[BWPhotoEncoderControllerInput setFsincMasksPrewarmedForCurrentEncoding:];
-[BWPhotoEncoderControllerInput primaryImageMetadataForPrewarming];
-[BWPhotoEncoderControllerInput addSampleBuffer:];
-[BWPhotoEncoderControllerInput dealloc];
-[BWPhotoEncoderControllerInput setReservedPrimaryImageHandle:];
-[BWPhotoEncoderControllerInput settingsID];
-[BWPhotoEncoderControllerInput sbufToProcess];
-[BWPhotoEncoderControllerInput receivedFramesCount];
-[BWPhotoEncoderControllerInput processingCanceled];
-[BWPhotoEncoderControllerInput toneMapAlternateGroupHandle];
-[BWPhotoEncoderControllerInput addSbufForPiecemealEncoding:attachedMediakey:primaryImageMetadata:processingFlags:];
-[BWPhotoEncoderControllerInput setFatalErrorOccurred:];
-[BWPhotoEncoderControllerInput setProcessingCanceled:];
-[BWPhotoEncoderControllerInput isStereoPhotoCapture];
-[BWPhotoEncoderControllerInput setDecompressStyledBufferAttributes:];
-[BWPhotoEncoderControllerInput setDeltaMapIsValid:];
-[BWPhotoEncoderControllerInput fatalErrorOccurred];
-[BWPhotoEncoderControllerInput setToneMapAlternateGroupHandle:];
-[BWPhotoEncoderControllerInput reservedPrimaryImageHandle];
-[BWPhotoEncoderControllerInput description];
-[BWPhotoEncoderControllerInput finishedProcessingSbuf];
-[BWPhotoEncoderControllerInput setGainMapHandle:];
-[BWPhotoEncoderControllerInput stereoPhotoImageHandles];
-[BWPhotoEncoderControllerInput requiresPhotosAdjustment];
-[BWPhotoEncoderControllerInput processingFlagsForPrewarming];
-[BWPhotoEncoderControllerInput textOrientationSuggestedExifOrientation];
-[BWPhotoEncoderControllerInput receivedFrame:isPrimary:];
-[BWPhotoEncoderControllerInput deltaMapIsValid];
-[BWPhotoEncoderControllerInput monoImageLocationType];
-[BWPhotoEncoderControllerInput receivedAllFramesInSingleContainer];
```
