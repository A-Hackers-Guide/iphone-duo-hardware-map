# `NINearbyPeerConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NIConfiguration`
- 8 instance variables, 8 properties, 29 instance methods, 4 class methods

## Instance variables

```
B _cameraAssistanceEnabled;
B _extendedDistanceMeasurementEnabled;
B _useCaseCameraAssistanceInClientProcess;
B _longRangeEnabled;
@"NIDiscoveryToken" _peerDiscoveryToken;
q _useCase;
q _backgroundMode;
@"NSDictionary" _debugParameters;
```

## Properties

```
@property (T@"NIDiscoveryToken",C,N,V_peerDiscoveryToken) peerDiscoveryToken;
@property (Tq,N,V_useCase) useCase;
@property (TB,N,V_useCaseCameraAssistanceInClientProcess) useCaseCameraAssistanceInClientProcess;
@property (TB,N,GisLongRangeEnabled,V_longRangeEnabled) longRangeEnabled;
@property (Tq,N,V_backgroundMode) backgroundMode;
@property (T@"NSDictionary",C,V_debugParameters) debugParameters;
@property (TB,N,GisCameraAssistanceEnabled,V_cameraAssistanceEnabled) cameraAssistanceEnabled;
@property (TB,N,GisExtendedDistanceMeasurementEnabled,V_extendedDistanceMeasurementEnabled) extendedDistanceMeasurementEnabled;
```

## Class methods

```
+[NINearbyPeerConfiguration supportsSecureCoding];
+[NINearbyPeerConfiguration new];
+[NINearbyPeerConfiguration createSOSBeaconSearcherConfigWithSessionKey:selfData:peerData:usingCameraAssistance:];
+[NINearbyPeerConfiguration createSOSBeaconSubjectConfigWithSessionKey:selfData:peerData:];
```

## Instance methods

```
-[NINearbyPeerConfiguration useCase];
-[NINearbyPeerConfiguration setCameraAssistanceEnabled:];
-[NINearbyPeerConfiguration init];
-[NINearbyPeerConfiguration descriptionInternal];
-[NINearbyPeerConfiguration setUseCase:];
-[NINearbyPeerConfiguration encodeWithCoder:];
-[NINearbyPeerConfiguration _internalIsCameraAssistanceEnabled];
-[NINearbyPeerConfiguration hash];
-[NINearbyPeerConfiguration isCameraAssistanceEnabled];
-[NINearbyPeerConfiguration description];
-[NINearbyPeerConfiguration initWithCoder:];
-[NINearbyPeerConfiguration copyWithZone:];
-[NINearbyPeerConfiguration isEqual:];
-[NINearbyPeerConfiguration backgroundMode];
-[NINearbyPeerConfiguration setBackgroundMode:];
-[NINearbyPeerConfiguration debugParameters];
-[NINearbyPeerConfiguration _internalIsCameraAssistanceInClientProcess];
-[NINearbyPeerConfiguration _internalIsExtendedDistanceMeasurementEnabled];
-[NINearbyPeerConfiguration _internalIsPowerAssertionRequired];
-[NINearbyPeerConfiguration initWithPeerToken:];
-[NINearbyPeerConfiguration isExtendedDistanceMeasurementEnabled];
-[NINearbyPeerConfiguration isLongRangeEnabled];
-[NINearbyPeerConfiguration peerDiscoveryToken];
-[NINearbyPeerConfiguration setDebugParameters:];
-[NINearbyPeerConfiguration setExtendedDistanceMeasurementEnabled:];
-[NINearbyPeerConfiguration setLongRangeEnabled:];
-[NINearbyPeerConfiguration setPeerDiscoveryToken:];
-[NINearbyPeerConfiguration setUseCaseCameraAssistanceInClientProcess:];
-[NINearbyPeerConfiguration useCaseCameraAssistanceInClientProcess];
```
