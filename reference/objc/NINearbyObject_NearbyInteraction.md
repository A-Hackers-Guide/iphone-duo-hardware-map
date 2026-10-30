# `NINearbyObject`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 41 instance variables, 41 properties, 100 instance methods, 3 class methods

## Instance variables

```
C _remoteTxAntennaMask;
B _requiresBiasCorrection;
C _nbRxStatus;
C _mmsRxStatus;
B _canInteract;
B _vioMajorRelocalization;
B _resetARSession;
B _revokeFindingExperience;
f _distance;
f _horizontalAngle;
f _azimuth;
f _elevation;
f _horizontalAngleAccuracy;
f _suggestedNearbyThreshold;
f _boundedRegionRange;
f _horizontalDistance;
f _rawRange;
@"NIDiscoveryToken" _discoveryToken;
q _verticalDirectionEstimate;
Q _relationship;
@"NSString" _deviceIdentifier;
d _timestamp;
q _distanceMeasurementQuality;
q _motionState;
@"NSString" _name;
@"NSNumber" _spatialScore;
@"NSData" _bluetoothAdvertisingAddress;
@"NSUUID" _bluetoothPeerIdentifier;
d _signalStrength;
d _rangeBiasEstimate;
d _rangeUncertainty;
@"UWBSignalFeatures" _uwbSignalFeatures;
d _nbRssi;
q _algorithmSource;
@"NSString" _debugDisplayInfo;
q _itemState;
@"NILocation" _location;
q _vioTrackingState;
_direction;
{?="vector"} _quaternion;
_worldPosition;
```

## Properties

```
@property (T@"NIDiscoveryToken",C,N,V_discoveryToken) discoveryToken;
@property (Tf,N,V_distance) distance;
@property (T,N,V_direction) direction;
@property (T{?=},N,V_quaternion) quaternion;
@property (Tf,N,V_azimuth) azimuth;
@property (Tf,N,V_elevation) elevation;
@property (TQ,N,V_relationship) relationship;
@property (T@"NSString",C,N,V_deviceIdentifier) deviceIdentifier;
@property (Td,N,V_timestamp) timestamp;
@property (Tq,N,V_distanceMeasurementQuality) distanceMeasurementQuality;
@property (Tq,N,V_motionState) motionState;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSNumber",C,N,V_spatialScore) spatialScore;
@property (T@"NSData",C,N,V_bluetoothAdvertisingAddress) bluetoothAdvertisingAddress;
@property (T@"NSUUID",C,N,V_bluetoothPeerIdentifier) bluetoothPeerIdentifier;
@property (Tq,N,V_verticalDirectionEstimate) verticalDirectionEstimate;
@property (Tf,N,V_horizontalAngle) horizontalAngle;
@property (Tf,N,V_horizontalAngleAccuracy) horizontalAngleAccuracy;
@property (Tf,N,V_suggestedNearbyThreshold) suggestedNearbyThreshold;
@property (Td,N,V_signalStrength) signalStrength;
@property (Td,N,V_rangeBiasEstimate) rangeBiasEstimate;
@property (Td,N,V_rangeUncertainty) rangeUncertainty;
@property (TC,N,V_remoteTxAntennaMask) remoteTxAntennaMask;
@property (T,N,V_worldPosition) worldPosition;
@property (TB,N,V_requiresBiasCorrection) requiresBiasCorrection;
@property (T@"UWBSignalFeatures",C,N,V_uwbSignalFeatures) uwbSignalFeatures;
@property (TC,N,V_nbRxStatus) nbRxStatus;
@property (TC,N,V_mmsRxStatus) mmsRxStatus;
@property (Td,N,V_nbRssi) nbRssi;
@property (TB,N,V_canInteract) canInteract;
@property (Tf,N,V_boundedRegionRange) boundedRegionRange;
@property (Tq,N,V_algorithmSource) algorithmSource;
@property (T@"NSString",C,N,V_debugDisplayInfo) debugDisplayInfo;
@property (Tf,N,V_horizontalDistance) horizontalDistance;
@property (Tq,N,V_itemState) itemState;
@property (T@"NILocation",C,N,V_location) location;
@property (Tf,N,V_rawRange) rawRange;
@property (Tq,N,V_vioTrackingState) vioTrackingState;
@property (TB,N,V_vioMajorRelocalization) vioMajorRelocalization;
@property (TB,N,V_resetARSession) resetARSession;
@property (TB,N,V_revokeFindingExperience) revokeFindingExperience;
```

## Class methods

```
+[NINearbyObject supportsSecureCoding];
+[NINearbyObject new];
+[NINearbyObject fauxObjectWithDiscoveryToken:name:deviceIdentifier:];
```

## Instance methods

```
-[NINearbyObject motionState];
-[NINearbyObject signalStrength];
-[NINearbyObject distance];
-[NINearbyObject setTimestamp:];
-[NINearbyObject setDeviceIdentifier:];
-[NINearbyObject setRelationship:];
-[NINearbyObject setDistance:];
-[NINearbyObject initWithToken:];
-[NINearbyObject init];
-[NINearbyObject descriptionInternal];
-[NINearbyObject location];
-[NINearbyObject timestamp];
-[NINearbyObject setDirection:];
-[NINearbyObject setMotionState:];
-[NINearbyObject direction];
-[NINearbyObject deviceIdentifier];
-[NINearbyObject setLocation:];
-[NINearbyObject encodeWithCoder:];
-[NINearbyObject hash];
-[NINearbyObject description];
-[NINearbyObject setName:];
-[NINearbyObject initWithCoder:];
-[NINearbyObject copyWithZone:];
-[NINearbyObject relationship];
-[NINearbyObject isEqual:];
-[NINearbyObject name];
-[NINearbyObject itemState];
-[NINearbyObject quaternion];
-[NINearbyObject setItemState:];
-[NINearbyObject azimuth];
-[NINearbyObject setAzimuth:];
-[NINearbyObject horizontalAngle];
-[NINearbyObject setHorizontalAngle:];
-[NINearbyObject elevation];
-[NINearbyObject setSignalStrength:];
-[NINearbyObject setQuaternion:];
-[NINearbyObject setElevation:];
-[NINearbyObject setWorldPosition:];
-[NINearbyObject worldPosition];
-[NINearbyObject horizontalDistance];
-[NINearbyObject setHorizontalDistance:];
-[NINearbyObject algorithmSource];
-[NINearbyObject deviceIdentifer];
-[NINearbyObject setBluetoothAdvertisingAddress:];
-[NINearbyObject setCanInteract:];
-[NINearbyObject setMmsRxStatus:];
-[NINearbyObject bluetoothAdvertisingAddress];
-[NINearbyObject bluetoothPeerIdentifier];
-[NINearbyObject boundedRegionRange];
-[NINearbyObject canInteract];
-[NINearbyObject debugDisplayInfo];
-[NINearbyObject discoveryToken];
-[NINearbyObject distanceMeasurementQuality];
-[NINearbyObject horizontalAngleAccuracy];
-[NINearbyObject initWithNearbyObject:];
-[NINearbyObject mmsRxStatus];
-[NINearbyObject nbRssi];
-[NINearbyObject nbRxStatus];
-[NINearbyObject overrideDirection:];
-[NINearbyObject overrideDistance:];
-[NINearbyObject overrideDistanceMeasurementQuality:];
-[NINearbyObject overrideMotionState:];
-[NINearbyObject overrideRelationship:];
-[NINearbyObject overrideSpatialScore:];
-[NINearbyObject overrideTimestamp:];
-[NINearbyObject rangeBiasEstimate];
-[NINearbyObject rangeUncertainty];
-[NINearbyObject rawRange];
-[NINearbyObject remoteTxAntennaMask];
-[NINearbyObject requiresBiasCorrection];
-[NINearbyObject resetARSession];
-[NINearbyObject revokeFindingExperience];
-[NINearbyObject setAlgorithmSource:];
-[NINearbyObject setBluetoothPeerIdentifier:];
-[NINearbyObject setBoundedRegionRange:];
-[NINearbyObject setDebugDisplayInfo:];
-[NINearbyObject setDiscoveryToken:];
-[NINearbyObject setDistanceMeasurementQuality:];
-[NINearbyObject setHorizontalAngleAccuracy:];
-[NINearbyObject setNbRssi:];
-[NINearbyObject setNbRxStatus:];
-[NINearbyObject setRangeBiasEstimate:];
-[NINearbyObject setRangeUncertainty:];
-[NINearbyObject setRawRange:];
-[NINearbyObject setRemoteTxAntennaMask:];
-[NINearbyObject setRequiresBiasCorrection:];
-[NINearbyObject setResetARSession:];
-[NINearbyObject setRevokeFindingExperience:];
-[NINearbyObject setSpatialScore:];
-[NINearbyObject setSuggestedNearbyThreshold:];
-[NINearbyObject setUwbSignalFeatures:];
-[NINearbyObject setVerticalDirectionEstimate:];
-[NINearbyObject setVioMajorRelocalization:];
-[NINearbyObject setVioTrackingState:];
-[NINearbyObject spatialScore];
-[NINearbyObject suggestedNearbyThreshold];
-[NINearbyObject uwbSignalFeatures];
-[NINearbyObject verticalDirectionEstimate];
-[NINearbyObject vioMajorRelocalization];
-[NINearbyObject vioTrackingState];
```
