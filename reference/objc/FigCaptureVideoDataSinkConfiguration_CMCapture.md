# `FigCaptureVideoDataSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkConfiguration`
- 13 instance variables, 13 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _discardsLateVideoFrames;
B _optimizedForPreview;
B _sceneStabilityMetadataEnabled;
@"NSArray" _requestedBufferAttachments;
@"FigCaptureTrie" _requestedBufferAttachmentsTrie;
B _cinematicFramingSupported;
B _cinematicFramingEnabled;
B _temporalFilterLowLightBandingMitigationEnabled;
B _preparesCellularRadioForNetworkConnection;
B _ringLightEnabled;
B _preservesDynamicHDRMetadata;
B _panoRecordingInProgress;
B _cinematicVideoMetadataCaptureEnabled;
```

## Properties

```
@property (TB,N,V_discardsLateVideoFrames) discardsLateVideoFrames;
@property (TB,N,V_optimizedForPreview) optimizedForPreview;
@property (TB,N,V_sceneStabilityMetadataEnabled) sceneStabilityMetadataEnabled;
@property (T@"NSArray",&,N) requestedBufferAttachments;
@property (T@"FigCaptureTrie",R,N) requestedBufferAttachmentsTrie;
@property (TB,N,V_cinematicFramingSupported) cinematicFramingSupported;
@property (TB,N,V_cinematicFramingEnabled) cinematicFramingEnabled;
@property (TB,N,V_temporalFilterLowLightBandingMitigationEnabled) temporalFilterLowLightBandingMitigationEnabled;
@property (TB,N,V_preparesCellularRadioForNetworkConnection) preparesCellularRadioForNetworkConnection;
@property (TB,N,V_preservesDynamicHDRMetadata) preservesDynamicHDRMetadata;
@property (TB,N,V_panoRecordingInProgress) panoRecordingInProgress;
@property (TB,N,V_ringLightEnabled) ringLightEnabled;
@property (TB,N,V_cinematicVideoMetadataCaptureEnabled) cinematicVideoMetadataCaptureEnabled;
```

## Instance methods

```
-[FigCaptureVideoDataSinkConfiguration cinematicFramingEnabled];
-[FigCaptureVideoDataSinkConfiguration cinematicFramingSupported];
-[FigCaptureVideoDataSinkConfiguration setCinematicVideoMetadataCaptureEnabled:];
-[FigCaptureVideoDataSinkConfiguration sinkType];
-[FigCaptureVideoDataSinkConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureVideoDataSinkConfiguration setOptimizedForPreview:];
-[FigCaptureVideoDataSinkConfiguration setCinematicFramingEnabled:];
-[FigCaptureVideoDataSinkConfiguration optimizedForPreview];
-[FigCaptureVideoDataSinkConfiguration preservesDynamicHDRMetadata];
-[FigCaptureVideoDataSinkConfiguration setPreparesCellularRadioForNetworkConnection:];
-[FigCaptureVideoDataSinkConfiguration setPreservesDynamicHDRMetadata:];
-[FigCaptureVideoDataSinkConfiguration requestedBufferAttachments];
-[FigCaptureVideoDataSinkConfiguration panoRecordingInProgress];
-[FigCaptureVideoDataSinkConfiguration dealloc];
-[FigCaptureVideoDataSinkConfiguration setSceneStabilityMetadataEnabled:];
-[FigCaptureVideoDataSinkConfiguration setRingLightEnabled:];
-[FigCaptureVideoDataSinkConfiguration setPanoRecordingInProgress:];
-[FigCaptureVideoDataSinkConfiguration setTemporalFilterLowLightBandingMitigationEnabled:];
-[FigCaptureVideoDataSinkConfiguration sceneStabilityMetadataEnabled];
-[FigCaptureVideoDataSinkConfiguration discardsLateVideoFrames];
-[FigCaptureVideoDataSinkConfiguration preparesCellularRadioForNetworkConnection];
-[FigCaptureVideoDataSinkConfiguration copyXPCEncoding];
-[FigCaptureVideoDataSinkConfiguration description];
-[FigCaptureVideoDataSinkConfiguration cinematicVideoMetadataCaptureEnabled];
-[FigCaptureVideoDataSinkConfiguration initWithXPCEncoding:];
-[FigCaptureVideoDataSinkConfiguration ringLightEnabled];
-[FigCaptureVideoDataSinkConfiguration temporalFilterLowLightBandingMitigationEnabled];
-[FigCaptureVideoDataSinkConfiguration copyWithZone:];
-[FigCaptureVideoDataSinkConfiguration setCinematicFramingSupported:];
-[FigCaptureVideoDataSinkConfiguration setRequestedBufferAttachments:];
-[FigCaptureVideoDataSinkConfiguration isEqual:];
-[FigCaptureVideoDataSinkConfiguration requestedBufferAttachmentsTrie];
-[FigCaptureVideoDataSinkConfiguration setDiscardsLateVideoFrames:];
```
