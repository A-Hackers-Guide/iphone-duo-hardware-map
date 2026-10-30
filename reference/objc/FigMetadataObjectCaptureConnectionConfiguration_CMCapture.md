# `FigMetadataObjectCaptureConnectionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureConnectionConfiguration`
- 24 instance variables, 24 properties, 55 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _metadataIdentifiers;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _metadataRectOfInterest;
i _faceTrackingMaxFaces;
B _faceTrackingUsesFaceRecognition;
B _faceTrackingPlusEnabled;
B _faceTrackingSuspended;
f _faceTrackingNetworkFailureThresholdMultiplier;
f _faceTrackingFailureFieldOfViewModifier;
B _attentionDetectionEnabled;
B _periocularForFaceIDReadinessEnabled;
B _attentionForFaceIDReadinessRequired;
B _faceOcclusionDetectionEnabled;
B _rawFrameDeliveryEnabled;
@"NSDictionary" _faceIDConfiguration;
@"NSArray" _metadataIdentifiersForPerceptionThumbnailChannel;
B _perceptionTestModeEnabled;
@"NSArray" _deviceProximityDetectionDeviceTypes;
f _deviceProximityDetectionTargetFrameRate;
f _motionToWakeTargetFrameRate;
f _objectDetectionTargetFrameRate;
I _lightSourceEstimationAmbientLuminance;
f _lightSourceEstimationTargetFrameRate;
B _attachMetadataToVideoBuffers;
B _emitsEmptyObjectDetectionMetadata;
```

## Properties

```
@property (T@"NSArray",C,N,V_metadataIdentifiers) metadataIdentifiers;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_metadataRectOfInterest) metadataRectOfInterest;
@property (Ti,N,V_faceTrackingMaxFaces) faceTrackingMaxFaces;
@property (TB,N,V_faceTrackingUsesFaceRecognition) faceTrackingUsesFaceRecognition;
@property (TB,N,V_faceTrackingPlusEnabled) faceTrackingPlusEnabled;
@property (TB,N,V_faceTrackingSuspended) faceTrackingSuspended;
@property (Tf,N,V_faceTrackingNetworkFailureThresholdMultiplier) faceTrackingNetworkFailureThresholdMultiplier;
@property (Tf,N,V_faceTrackingFailureFieldOfViewModifier) faceTrackingFailureFieldOfViewModifier;
@property (TB,N,V_attentionDetectionEnabled) attentionDetectionEnabled;
@property (TB,N,V_periocularForFaceIDReadinessEnabled) periocularForFaceIDReadinessEnabled;
@property (TB,N,V_attentionForFaceIDReadinessRequired) attentionForFaceIDReadinessRequired;
@property (TB,N,V_faceOcclusionDetectionEnabled) faceOcclusionDetectionEnabled;
@property (TB,N,V_rawFrameDeliveryEnabled) rawFrameDeliveryEnabled;
@property (T@"NSDictionary",C,N,V_faceIDConfiguration) faceIDConfiguration;
@property (T@"NSArray",C,N,V_metadataIdentifiersForPerceptionThumbnailChannel) metadataIdentifiersForPerceptionThumbnailChannel;
@property (TB,N,V_perceptionTestModeEnabled) perceptionTestModeEnabled;
@property (T@"NSArray",C,N,V_deviceProximityDetectionDeviceTypes) deviceProximityDetectionDeviceTypes;
@property (Tf,N,V_deviceProximityDetectionTargetFrameRate) deviceProximityDetectionTargetFrameRate;
@property (Tf,N,V_motionToWakeTargetFrameRate) motionToWakeTargetFrameRate;
@property (TI,N,V_lightSourceEstimationAmbientLuminance) lightSourceEstimationAmbientLuminance;
@property (Tf,N,V_lightSourceEstimationTargetFrameRate) lightSourceEstimationTargetFrameRate;
@property (Tf,N,V_objectDetectionTargetFrameRate) objectDetectionTargetFrameRate;
@property (TB,N,V_attachMetadataToVideoBuffers) attachMetadataToVideoBuffers;
@property (TB,N,V_emitsEmptyObjectDetectionMetadata) emitsEmptyObjectDetectionMetadata;
```

## Instance methods

```
-[FigMetadataObjectCaptureConnectionConfiguration setRawFrameDeliveryEnabled:];
-[FigMetadataObjectCaptureConnectionConfiguration metadataIdentifiersForPerceptionThumbnailChannel];
-[FigMetadataObjectCaptureConnectionConfiguration setEmitsEmptyObjectDetectionMetadata:];
-[FigMetadataObjectCaptureConnectionConfiguration attentionForFaceIDReadinessRequired];
-[FigMetadataObjectCaptureConnectionConfiguration periocularForFaceIDReadinessEnabled];
-[FigMetadataObjectCaptureConnectionConfiguration reasonForNotEqualingConfiguration:];
-[FigMetadataObjectCaptureConnectionConfiguration emitsEmptyObjectDetectionMetadata];
-[FigMetadataObjectCaptureConnectionConfiguration setMetadataIdentifiers:];
-[FigMetadataObjectCaptureConnectionConfiguration setLightSourceEstimationAmbientLuminance:];
-[FigMetadataObjectCaptureConnectionConfiguration motionToWakeTargetFrameRate];
-[FigMetadataObjectCaptureConnectionConfiguration setAttentionDetectionEnabled:];
-[FigMetadataObjectCaptureConnectionConfiguration lightSourceEstimationAmbientLuminance];
-[FigMetadataObjectCaptureConnectionConfiguration dealloc];
-[FigMetadataObjectCaptureConnectionConfiguration deviceProximityDetectionDeviceTypes];
-[FigMetadataObjectCaptureConnectionConfiguration setMetadataRectOfInterest:];
-[FigMetadataObjectCaptureConnectionConfiguration lightSourceEstimationTargetFrameRate];
-[FigMetadataObjectCaptureConnectionConfiguration faceTrackingPlusEnabled];
-[FigMetadataObjectCaptureConnectionConfiguration setLightSourceEstimationTargetFrameRate:];
-[FigMetadataObjectCaptureConnectionConfiguration setAttentionForFaceIDReadinessRequired:];
-[FigMetadataObjectCaptureConnectionConfiguration setMetadataIdentifiersForPerceptionThumbnailChannel:];
-[FigMetadataObjectCaptureConnectionConfiguration faceTrackingUsesFaceRecognition];
-[FigMetadataObjectCaptureConnectionConfiguration attentionDetectionEnabled];
-[FigMetadataObjectCaptureConnectionConfiguration attachMetadataToVideoBuffers];
-[FigMetadataObjectCaptureConnectionConfiguration setDeviceProximityDetectionTargetFrameRate:];
-[FigMetadataObjectCaptureConnectionConfiguration deviceProximityDetectionTargetFrameRate];
-[FigMetadataObjectCaptureConnectionConfiguration faceIDConfiguration];
-[FigMetadataObjectCaptureConnectionConfiguration rawFrameDeliveryEnabled];
-[FigMetadataObjectCaptureConnectionConfiguration faceTrackingSuspended];
-[FigMetadataObjectCaptureConnectionConfiguration setDeviceProximityDetectionDeviceTypes:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceTrackingSuspended:];
-[FigMetadataObjectCaptureConnectionConfiguration copyXPCEncoding];
-[FigMetadataObjectCaptureConnectionConfiguration faceTrackingFailureFieldOfViewModifier];
-[FigMetadataObjectCaptureConnectionConfiguration metadataIdentifiers];
-[FigMetadataObjectCaptureConnectionConfiguration description];
-[FigMetadataObjectCaptureConnectionConfiguration metadataRectOfInterest];
-[FigMetadataObjectCaptureConnectionConfiguration initWithXPCEncoding:];
-[FigMetadataObjectCaptureConnectionConfiguration setPerceptionTestModeEnabled:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceTrackingPlusEnabled:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceOcclusionDetectionEnabled:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceTrackingFailureFieldOfViewModifier:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceTrackingUsesFaceRecognition:];
-[FigMetadataObjectCaptureConnectionConfiguration copyWithZone:];
-[FigMetadataObjectCaptureConnectionConfiguration setAttachMetadataToVideoBuffers:];
-[FigMetadataObjectCaptureConnectionConfiguration perceptionTestModeEnabled];
-[FigMetadataObjectCaptureConnectionConfiguration setPeriocularForFaceIDReadinessEnabled:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceIDConfiguration:];
-[FigMetadataObjectCaptureConnectionConfiguration isEqual:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceTrackingNetworkFailureThresholdMultiplier:];
-[FigMetadataObjectCaptureConnectionConfiguration setFaceTrackingMaxFaces:];
-[FigMetadataObjectCaptureConnectionConfiguration faceOcclusionDetectionEnabled];
-[FigMetadataObjectCaptureConnectionConfiguration setObjectDetectionTargetFrameRate:];
-[FigMetadataObjectCaptureConnectionConfiguration setMotionToWakeTargetFrameRate:];
-[FigMetadataObjectCaptureConnectionConfiguration faceTrackingNetworkFailureThresholdMultiplier];
-[FigMetadataObjectCaptureConnectionConfiguration objectDetectionTargetFrameRate];
-[FigMetadataObjectCaptureConnectionConfiguration faceTrackingMaxFaces];
```
