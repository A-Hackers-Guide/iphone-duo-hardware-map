# `BWSecureMetadataOutputConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 28 instance variables, 29 properties, 62 instance methods, 0 class methods

## Instance variables

```
B _objectDetectionEnabled;
@"NSSet" _enabledDetectedObjectTypes;
f _objectDetectionTargetFrameRate;
B _attentionDetectionEnabled;
B _faceOcclusionDetectionEnabled;
@"NSSet" _perceptionThumbnailChannelMetadataObjectTypes;
f _perceptionThumbnailChannelTargetFrameRate;
B _perceptionTestModeEnabled;
B _faceTrackingEnabled;
i _faceTrackingMaxNumTrackedFaces;
f _faceTrackingNetworkFailureThresholdMultiplier;
f _faceTrackingFailureFieldOfViewModifier;
B _eyeReliefStatusDetectionEnabled;
B _motionToWakeEnabled;
f _motionToWakeTargetFrameRate;
B _faceIDReadinessEnabled;
B _faceIDReadinessPeriocularEnabled;
B _faceIDReadinessAttentionRequired;
B _rawFrameDeliveryEnabled;
B _faceIDEnabled;
@"NSDictionary" _faceIDConfiguration;
B _colorCameraAssistEnabled;
B _deviceProximityDetectionEnabled;
@"NSSet" _deviceProximityDetectionDeviceTypes;
f _deviceProximityDetectionTargetFrameRate;
B _lightSourceEstimationEnabled;
I _lightSourceEstimationAmbientLuminance;
f _lightSourceEstimationTargetFrameRate;
```

## Properties

```
@property (TB,N,V_objectDetectionEnabled) objectDetectionEnabled;
@property (T@"NSSet",C,N,V_enabledDetectedObjectTypes) enabledDetectedObjectTypes;
@property (TB,N,V_attentionDetectionEnabled) attentionDetectionEnabled;
@property (TB,N,V_faceOcclusionDetectionEnabled) faceOcclusionDetectionEnabled;
@property (T@"NSSet",C,N,V_perceptionThumbnailChannelMetadataObjectTypes) perceptionThumbnailChannelMetadataObjectTypes;
@property (TB,N,V_perceptionTestModeEnabled) perceptionTestModeEnabled;
@property (Tf,N,V_objectDetectionTargetFrameRate) objectDetectionTargetFrameRate;
@property (TB,N,V_faceTrackingEnabled) faceTrackingEnabled;
@property (Ti,N,V_faceTrackingMaxNumTrackedFaces) faceTrackingMaxNumTrackedFaces;
@property (Tf,N,V_faceTrackingNetworkFailureThresholdMultiplier) faceTrackingNetworkFailureThresholdMultiplier;
@property (Tf,N,V_faceTrackingFailureFieldOfViewModifier) faceTrackingFailureFieldOfViewModifier;
@property (TB,N,V_eyeReliefStatusDetectionEnabled) eyeReliefStatusDetectionEnabled;
@property (TB,N,V_motionToWakeEnabled) motionToWakeEnabled;
@property (Tf,N,V_motionToWakeTargetFrameRate) motionToWakeTargetFrameRate;
@property (TB,N,V_faceIDReadinessEnabled) faceIDReadinessEnabled;
@property (TB,N,V_faceIDReadinessPeriocularEnabled) faceIDReadinessPeriocularEnabled;
@property (TB,N,V_faceIDReadinessAttentionRequired) faceIDReadinessAttentionRequired;
@property (TB,N,V_rawFrameDeliveryEnabled) rawFrameDeliveryEnabled;
@property (TB,N,V_faceIDEnabled) faceIDEnabled;
@property (T@"NSDictionary",C,N,V_faceIDConfiguration) faceIDConfiguration;
@property (TB,N,V_colorCameraAssistEnabled) colorCameraAssistEnabled;
@property (TB,N,V_deviceProximityDetectionEnabled) deviceProximityDetectionEnabled;
@property (T@"NSSet",C,N,V_deviceProximityDetectionDeviceTypes) deviceProximityDetectionDeviceTypes;
@property (Tf,N,V_deviceProximityDetectionTargetFrameRate) deviceProximityDetectionTargetFrameRate;
@property (TB,N,V_lightSourceEstimationEnabled) lightSourceEstimationEnabled;
@property (TI,N,V_lightSourceEstimationAmbientLuminance) lightSourceEstimationAmbientLuminance;
@property (Tf,N,V_lightSourceEstimationTargetFrameRate) lightSourceEstimationTargetFrameRate;
@property (T@"NSDictionary",R,N) metadataOutputConfigurationDictionary;
@property (TB,R,N) isEmpty;
```

## Instance methods

```
-[BWSecureMetadataOutputConfiguration setFaceIDReadinessAttentionRequired:];
-[BWSecureMetadataOutputConfiguration setRawFrameDeliveryEnabled:];
-[BWSecureMetadataOutputConfiguration setFaceTrackingMaxNumTrackedFaces:];
-[BWSecureMetadataOutputConfiguration faceIDReadinessAttentionRequired];
-[BWSecureMetadataOutputConfiguration faceIDEnabled];
-[BWSecureMetadataOutputConfiguration faceIDReadinessEnabled];
-[BWSecureMetadataOutputConfiguration faceIDReadinessPeriocularEnabled];
-[BWSecureMetadataOutputConfiguration setLightSourceEstimationAmbientLuminance:];
-[BWSecureMetadataOutputConfiguration motionToWakeTargetFrameRate];
-[BWSecureMetadataOutputConfiguration init];
-[BWSecureMetadataOutputConfiguration setPerceptionThumbnailChannelTargetFrameRate:];
-[BWSecureMetadataOutputConfiguration setAttentionDetectionEnabled:];
-[BWSecureMetadataOutputConfiguration setMotionToWakeEnabled:];
-[BWSecureMetadataOutputConfiguration setPerceptionThumbnailChannelMetadataObjectTypes:];
-[BWSecureMetadataOutputConfiguration lightSourceEstimationAmbientLuminance];
-[BWSecureMetadataOutputConfiguration faceTrackingMaxNumTrackedFaces];
-[BWSecureMetadataOutputConfiguration dealloc];
-[BWSecureMetadataOutputConfiguration perceptionThumbnailChannelMetadataObjectTypes];
-[BWSecureMetadataOutputConfiguration deviceProximityDetectionDeviceTypes];
-[BWSecureMetadataOutputConfiguration enabledDetectedObjectTypes];
-[BWSecureMetadataOutputConfiguration lightSourceEstimationTargetFrameRate];
-[BWSecureMetadataOutputConfiguration setColorCameraAssistEnabled:];
-[BWSecureMetadataOutputConfiguration setLightSourceEstimationTargetFrameRate:];
-[BWSecureMetadataOutputConfiguration attentionDetectionEnabled];
-[BWSecureMetadataOutputConfiguration setEnabledDetectedObjectTypes:];
-[BWSecureMetadataOutputConfiguration eyeReliefStatusDetectionEnabled];
-[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionTargetFrameRate:];
-[BWSecureMetadataOutputConfiguration setFaceIDEnabled:];
-[BWSecureMetadataOutputConfiguration deviceProximityDetectionTargetFrameRate];
-[BWSecureMetadataOutputConfiguration faceIDConfiguration];
-[BWSecureMetadataOutputConfiguration rawFrameDeliveryEnabled];
-[BWSecureMetadataOutputConfiguration perceptionThumbnailChannelTargetFrameRate];
-[BWSecureMetadataOutputConfiguration setLightSourceEstimationEnabled:];
-[BWSecureMetadataOutputConfiguration isEmpty];
-[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionDeviceTypes:];
-[BWSecureMetadataOutputConfiguration faceTrackingFailureFieldOfViewModifier];
-[BWSecureMetadataOutputConfiguration colorCameraAssistEnabled];
-[BWSecureMetadataOutputConfiguration lightSourceEstimationEnabled];
-[BWSecureMetadataOutputConfiguration setEyeReliefStatusDetectionEnabled:];
-[BWSecureMetadataOutputConfiguration setPerceptionTestModeEnabled:];
-[BWSecureMetadataOutputConfiguration setObjectDetectionEnabled:];
-[BWSecureMetadataOutputConfiguration setFaceOcclusionDetectionEnabled:];
-[BWSecureMetadataOutputConfiguration setFaceIDReadinessEnabled:];
-[BWSecureMetadataOutputConfiguration setFaceTrackingFailureFieldOfViewModifier:];
-[BWSecureMetadataOutputConfiguration setFaceIDReadinessPeriocularEnabled:];
-[BWSecureMetadataOutputConfiguration faceTrackingEnabled];
-[BWSecureMetadataOutputConfiguration deviceProximityDetectionEnabled];
-[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionEnabled:];
-[BWSecureMetadataOutputConfiguration copyWithZone:];
-[BWSecureMetadataOutputConfiguration motionToWakeEnabled];
-[BWSecureMetadataOutputConfiguration perceptionTestModeEnabled];
-[BWSecureMetadataOutputConfiguration setFaceIDConfiguration:];
-[BWSecureMetadataOutputConfiguration isEqual:];
-[BWSecureMetadataOutputConfiguration setFaceTrackingNetworkFailureThresholdMultiplier:];
-[BWSecureMetadataOutputConfiguration objectDetectionEnabled];
-[BWSecureMetadataOutputConfiguration faceOcclusionDetectionEnabled];
-[BWSecureMetadataOutputConfiguration setObjectDetectionTargetFrameRate:];
-[BWSecureMetadataOutputConfiguration setMotionToWakeTargetFrameRate:];
-[BWSecureMetadataOutputConfiguration setFaceTrackingEnabled:];
-[BWSecureMetadataOutputConfiguration faceTrackingNetworkFailureThresholdMultiplier];
-[BWSecureMetadataOutputConfiguration metadataOutputConfigurationDictionary];
-[BWSecureMetadataOutputConfiguration objectDetectionTargetFrameRate];
```
