# `TUCallCapabilitiesState`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`, `TUPubliclyAccessibleCopying`
- 24 instance variables, 29 properties, 56 instance methods, 1 class methods

## Instance variables

```
B _supportsPrimaryCalling;
B _supportsBasebandCalling;
B _supportsCellularData;
B _supportsDisplayingTelephonyCalls;
B _supportsDisplayingFaceTimeAudioCalls;
B _supportsDisplayingFaceTimeVideoCalls;
B _faceTimeAudioAvailable;
B _faceTimeVideoAvailable;
B _ctCapabilitiesValid;
B _accountsMatchForSecondaryCalling;
B _accountsSupportSecondaryCalling;
B _supportsRelayCalling;
B _relayCallingEnabled;
B _relayCallingFeaturesEnabled;
B _supportsTelephonyRelayCalling;
B _supportsFaceTimeAudioRelayCalling;
B _supportsFaceTimeVideoRelayCalling;
B _emergencyCallbackModeEnabled;
B _emergencyCallbackPossible;
i _relayCallingAvailability;
@"NSDictionary" _relayCallingDisabledForDeviceID;
@"NSString" _outgoingRelayCallerID;
@"NSArray" _cloudCallingDevices;
@"NSDictionary" _senderIdentityCapabilitiesStateByUUID;
```

## Properties

```
@property (TB,N,V_supportsPrimaryCalling) supportsPrimaryCalling;
@property (TB,N,V_supportsBasebandCalling) supportsBasebandCalling;
@property (TB,N,V_supportsCellularData) supportsCellularData;
@property (TB,N,V_supportsDisplayingTelephonyCalls) supportsDisplayingTelephonyCalls;
@property (TB,N,V_supportsDisplayingFaceTimeAudioCalls) supportsDisplayingFaceTimeAudioCalls;
@property (TB,N,V_supportsDisplayingFaceTimeVideoCalls) supportsDisplayingFaceTimeVideoCalls;
@property (TB,N,GisFaceTimeAudioAvailable,V_faceTimeAudioAvailable) faceTimeAudioAvailable;
@property (TB,N,GisFaceTimeVideoAvailable,V_faceTimeVideoAvailable) faceTimeVideoAvailable;
@property (TB,N,GareCTCapabilitiesValid,V_ctCapabilitiesValid) ctCapabilitiesValid;
@property (TB,N,V_accountsMatchForSecondaryCalling) accountsMatchForSecondaryCalling;
@property (TB,N,V_accountsSupportSecondaryCalling) accountsSupportSecondaryCalling;
@property (TB,N,V_supportsRelayCalling) supportsRelayCalling;
@property (TB,N,GisRelayCallingEnabled,V_relayCallingEnabled) relayCallingEnabled;
@property (TB,N,GareRelayCallingFeaturesEnabled,V_relayCallingFeaturesEnabled) relayCallingFeaturesEnabled;
@property (Ti,N,V_relayCallingAvailability) relayCallingAvailability;
@property (T@"NSDictionary",C,N,V_relayCallingDisabledForDeviceID) relayCallingDisabledForDeviceID;
@property (T@"NSString",C,N,V_outgoingRelayCallerID) outgoingRelayCallerID;
@property (TB,N,V_supportsTelephonyRelayCalling) supportsTelephonyRelayCalling;
@property (TB,N,V_supportsFaceTimeAudioRelayCalling) supportsFaceTimeAudioRelayCalling;
@property (TB,N,V_supportsFaceTimeVideoRelayCalling) supportsFaceTimeVideoRelayCalling;
@property (T@"NSArray",C,N,V_cloudCallingDevices) cloudCallingDevices;
@property (T@"TUCloudCallingDevice",R,N) defaultPairedDevice;
@property (TB,N,GisEmergencyCallbackModeEnabled,V_emergencyCallbackModeEnabled) emergencyCallbackModeEnabled;
@property (TB,N,GisEmergencyCallbackPossible,V_emergencyCallbackPossible) emergencyCallbackPossible;
@property (T@"NSDictionary",C,N,V_senderIdentityCapabilitiesStateByUUID) senderIdentityCapabilitiesStateByUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCallCapabilitiesState supportsSecureCoding];
```

## Instance methods

```
-[TUCallCapabilitiesState accountsMatchForSecondaryCalling];
-[TUCallCapabilitiesState supportsFaceTimeVideoRelayCalling];
-[TUCallCapabilitiesState setRelayCallingEnabled:];
-[TUCallCapabilitiesState setSupportsBasebandCalling:];
-[TUCallCapabilitiesState setAccountsMatchForSecondaryCalling:];
-[TUCallCapabilitiesState setRelayCallingFeaturesEnabled:];
-[TUCallCapabilitiesState setSenderIdentityCapabilitiesStateByUUID:];
-[TUCallCapabilitiesState isEmergencyCallbackModeEnabled];
-[TUCallCapabilitiesState publiclyAccessibleCopyWithZone:];
-[TUCallCapabilitiesState publiclyAccessibleCopy];
-[TUCallCapabilitiesState init];
-[TUCallCapabilitiesState setAccountsSupportSecondaryCalling:];
-[TUCallCapabilitiesState isRelayCallingEnabled];
-[TUCallCapabilitiesState setCtCapabilitiesValid:];
-[TUCallCapabilitiesState supportsDisplayingTelephonyCalls];
-[TUCallCapabilitiesState outgoingRelayCallerID];
-[TUCallCapabilitiesState supportsFaceTimeAudioRelayCalling];
-[TUCallCapabilitiesState setSupportsTelephonyRelayCalling:];
-[TUCallCapabilitiesState areCTCapabilitiesValid];
-[TUCallCapabilitiesState setSupportsDisplayingFaceTimeAudioCalls:];
-[TUCallCapabilitiesState isEmergencyCallbackPossible];
-[TUCallCapabilitiesState setCloudCallingDevices:];
-[TUCallCapabilitiesState defaultPairedDevice];
-[TUCallCapabilitiesState relayCallingAvailability];
-[TUCallCapabilitiesState supportsTelephonyRelayCalling];
-[TUCallCapabilitiesState areRelayCallingFeaturesEnabled];
-[TUCallCapabilitiesState setSupportsPrimaryCalling:];
-[TUCallCapabilitiesState isFaceTimeVideoAvailable];
-[TUCallCapabilitiesState setRelayCallingAvailability:];
-[TUCallCapabilitiesState setEmergencyCallbackModeEnabled:];
-[TUCallCapabilitiesState encodeWithCoder:];
-[TUCallCapabilitiesState isFaceTimeAudioAvailable];
-[TUCallCapabilitiesState supportsDisplayingFaceTimeVideoCalls];
-[TUCallCapabilitiesState supportsBasebandCalling];
-[TUCallCapabilitiesState setOutgoingRelayCallerID:];
-[TUCallCapabilitiesState supportsCellularData];
-[TUCallCapabilitiesState description];
-[TUCallCapabilitiesState setFaceTimeAudioAvailable:];
-[TUCallCapabilitiesState setSupportsDisplayingTelephonyCalls:];
-[TUCallCapabilitiesState supportsRelayCalling];
-[TUCallCapabilitiesState cloudCallingDevices];
-[TUCallCapabilitiesState supportsDisplayingFaceTimeAudioCalls];
-[TUCallCapabilitiesState initWithCoder:];
-[TUCallCapabilitiesState setSupportsCellularData:];
-[TUCallCapabilitiesState relayCallingDisabledForDeviceID];
-[TUCallCapabilitiesState senderIdentityCapabilitiesStateByUUID];
-[TUCallCapabilitiesState copyWithZone:];
-[TUCallCapabilitiesState setEmergencyCallbackPossible:];
-[TUCallCapabilitiesState setRelayCallingDisabledForDeviceID:];
-[TUCallCapabilitiesState supportsPrimaryCalling];
-[TUCallCapabilitiesState setSupportsFaceTimeAudioRelayCalling:];
-[TUCallCapabilitiesState setFaceTimeVideoAvailable:];
-[TUCallCapabilitiesState setSupportsDisplayingFaceTimeVideoCalls:];
-[TUCallCapabilitiesState setSupportsFaceTimeVideoRelayCalling:];
-[TUCallCapabilitiesState accountsSupportSecondaryCalling];
-[TUCallCapabilitiesState setSupportsRelayCalling:];
```
