# `TURoute`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 33 instance variables, 42 properties, 87 instance methods, 5 class methods

## Instance variables

```
B _A2DPRoute;
B _currentlyPicked;
B _defaultRoute;
B _receiver;
B _speaker;
B _wiredHeadphones;
B _wiredHeadset;
B _wirelessHeadset;
B _airTunes;
B _carAudio;
B _guest;
B _bluetooth;
B _bluetoothLE;
B _bluetoothManaged;
B _inEarDetectionEnabled;
B _inEarDetectionSupported;
B _preferred;
B _preferredAndActive;
B _partnerRouteRoutable;
B _siblingRoutePresent;
B _supportsHighQualityVoiceWithMedia;
B _supportsSharePlay;
B _supportsRelay;
B _recommended;
B _disabled;
B _inTipiWithCompanion;
B _smartRoutedTo;
@"NSString" _uniqueIdentifier;
@"NSString" _name;
@"NSString" _modelIdentifier;
q _deviceType;
q _bluetoothEndpointType;
@"NSArray" _identifiersOfOtherConnectedDevices;
```

## Properties

```
@property (TB,N,GisA2DPRoute,V_A2DPRoute) A2DPRoute;
@property (TB,N,GisAirTunes,V_airTunes) airTunes;
@property (TB,N,GisCarAudio,V_carAudio) carAudio;
@property (TB,N,GisCurrentlyPicked,V_currentlyPicked) currentlyPicked;
@property (TB,N,GisBluetooth,V_bluetooth) bluetooth;
@property (Tq,N,V_bluetoothEndpointType) bluetoothEndpointType;
@property (TB,N,GisBluetoothLE,V_bluetoothLE) bluetoothLE;
@property (TB,N,GisBluetoothManaged,V_bluetoothManaged) bluetoothManaged;
@property (TB,N,GisDefaultRoute,V_defaultRoute) defaultRoute;
@property (Tq,N,V_deviceType) deviceType;
@property (T@"NSString",C,N,V_modelIdentifier) modelIdentifier;
@property (TB,N,GisGuest,V_guest) guest;
@property (T@"NSArray",C,N,V_identifiersOfOtherConnectedDevices) identifiersOfOtherConnectedDevices;
@property (TB,N,GisInTipiWithCompanion,V_inTipiWithCompanion) inTipiWithCompanion;
@property (TB,N,GisSmartRoutedTo,V_smartRoutedTo) smartRoutedTo;
@property (TB,N,GisInEarDetectionEnabled,V_inEarDetectionEnabled) inEarDetectionEnabled;
@property (TB,N,GisInEarDetectionSupported,V_inEarDetectionSupported) inEarDetectionSupported;
@property (T@"NSString",C,N,V_name) name;
@property (TB,N,GisPreferred,V_preferred) preferred;
@property (TB,N,GisPreferredAndActive,V_preferredAndActive) preferredAndActive;
@property (TB,N,GisReceiver,V_receiver) receiver;
@property (TB,N,GisSpeaker,V_speaker) speaker;
@property (TB,N,V_supportsHighQualityVoiceWithMedia) supportsHighQualityVoiceWithMedia;
@property (TB,N,V_supportsRelay) supportsRelay;
@property (T@"NSString",C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (TB,N,GisWiredHeadphones,V_wiredHeadphones) wiredHeadphones;
@property (TB,N,GisWiredHeadset,V_wiredHeadset) wiredHeadset;
@property (TB,N,GisWirelessHeadset,V_wirelessHeadset) wirelessHeadset;
@property (TB,N,GisPartnerRouteRoutable,V_partnerRouteRoutable) partnerRouteRoutable;
@property (TB,N,GisSiblingRoutePresent,V_siblingRoutePresent) siblingRoutePresent;
@property (TB,N,V_supportsSharePlay) supportsSharePlay;
@property (TB,N,GisRecommended,V_recommended) recommended;
@property (TB,N,GisDisabled,V_disabled) disabled;
@property (TB,R,N,GisCarKitRoute) carKitRoute;
@property (TB,R,N,GisHomePodFamily) homePodFamily;
@property (TB,R,N) isAirPodsRoute;
@property (TB,R,N,GisInEarDetected) inEarDetected;
@property (TB,R,N) supportsPreferredAndActive;
@property (TB,R,N,GisTipiParticipant) tipiParticipant;
@property (TB,R,N,GisTriangleParticipant) triangleParticipant;
@property (TB,R,N,GisAuxiliary) auxiliary;
@property (T@"NSString",R,C,N) localizedDisabledReason;
```

## Class methods

```
+[TURoute supportsSecureCoding];
+[TURoute predicateForInEarRouteInTipiWithCompanionWatch];
+[TURoute predicateForInEarAudioRoute];
+[TURoute predicateForPreferredRoute];
+[TURoute predicateForInEarRouteInTipiWithAndSmartRoutedToCompanionWatch];
```

## Instance methods

```
-[TURoute isAuxiliary];
-[TURoute customDescription];
-[TURoute setDeviceType:];
-[TURoute setRecommended:];
-[TURoute isEqualToRoute:];
-[TURoute setDefaultRoute:];
-[TURoute localizedDisabledReason];
-[TURoute isRecommended];
-[TURoute isBluetoothLE];
-[TURoute setSpeaker:];
-[TURoute setPreferred:];
-[TURoute isCarKitRoute];
-[TURoute setInEarDetectionEnabled:];
-[TURoute isInEarDetected];
-[TURoute setReceiver:];
-[TURoute mutableCopyWithZone:];
-[TURoute isPreferred];
-[TURoute setSupportsHighQualityVoiceWithMedia:];
-[TURoute modelIdentifier];
-[TURoute setInTipiWithCompanion:];
-[TURoute setA2DPRoute:];
-[TURoute supportsPreferredAndActive];
-[TURoute setBluetoothManaged:];
-[TURoute isSiblingRoutePresent];
-[TURoute deviceType];
-[TURoute isCarAudio];
-[TURoute setBluetoothLE:];
-[TURoute setPreferredAndActive:];
-[TURoute setBluetooth:];
-[TURoute isCurrentlyPicked];
-[TURoute setAirTunes:];
-[TURoute setWirelessHeadset:];
-[TURoute setUniqueIdentifier:];
-[TURoute isDefaultRoute];
-[TURoute isEqualToRouteIgnoringIsRecommended:];
-[TURoute supportsHighQualityVoiceWithMedia];
-[TURoute isWiredHeadphones];
-[TURoute isGuest];
-[TURoute isInEarDetectionEnabled];
-[TURoute uniqueIdentifier];
-[TURoute identifiersOfOtherConnectedDevices];
-[TURoute isDisabled];
-[TURoute isTriangleParticipant];
-[TURoute isSpeaker];
-[TURoute supportsRelay];
-[TURoute setCarAudio:];
-[TURoute setBluetoothEndpointType:];
-[TURoute isTipiParticipant];
-[TURoute setSmartRoutedTo:];
-[TURoute isPartnerRouteRoutable];
-[TURoute isBluetooth];
-[TURoute initWithUniqueIdentifier:name:];
-[TURoute encodeWithCoder:];
-[TURoute setGuest:];
-[TURoute isInEarDetectionSupported];
-[TURoute isInTipiWithCompanion];
-[TURoute hash];
-[TURoute description];
-[TURoute setName:];
-[TURoute initWithCoder:];
-[TURoute isA2DPRoute];
-[TURoute isPreferredAndActive];
-[TURoute setWiredHeadphones:];
-[TURoute setPartnerRouteRoutable:];
-[TURoute isReceiver];
-[TURoute setModelIdentifier:];
-[TURoute setCurrentlyPicked:];
-[TURoute isBluetoothManaged];
-[TURoute setInEarDetectionSupported:];
-[TURoute copyWithZone:];
-[TURoute initWithRoute:];
-[TURoute isWiredHeadset];
-[TURoute setSupportsRelay:];
-[TURoute isAirTunes];
-[TURoute isSmartRoutedTo];
-[TURoute isEqual:];
-[TURoute setIdentifiersOfOtherConnectedDevices:];
-[TURoute isAirPodsRoute];
-[TURoute setDisabled:];
-[TURoute name];
-[TURoute setSupportsSharePlay:];
-[TURoute supportsSharePlay];
-[TURoute bluetoothEndpointType];
-[TURoute isHomePodFamily];
-[TURoute setSiblingRoutePresent:];
-[TURoute setWiredHeadset:];
-[TURoute isWirelessHeadset];
```
