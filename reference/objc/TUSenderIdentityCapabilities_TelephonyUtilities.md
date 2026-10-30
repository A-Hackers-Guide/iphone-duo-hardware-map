# `TUSenderIdentityCapabilities`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 36 properties, 51 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _senderIdentityUUID;
@"NSString" _thumperCallingLocalDeviceID;
@"TUSenderIdentityCapabilitiesState" _state;
@"TUCallCapabilitiesXPCClient" _client;
```

## Properties

```
@property (T@"TUSenderIdentityCapabilitiesState",R,C,N,V_state) state;
@property (T@"TUCallCapabilitiesXPCClient",R,N,V_client) client;
@property (T@"TUCTCapabilityInfo",R,N) voLTECallingCapabilityInfo;
@property (T@"TUCTCapabilityInfo",R,N) wiFiCallingCapabilityInfo;
@property (T@"TUCTCapabilityInfo",R,N) thumperCallingCapabilityInfo;
@property (T@"NSUUID",R,C,N,V_senderIdentityUUID) senderIdentityUUID;
@property (TB,R,N) supportsSimultaneousVoiceAndData;
@property (TB,R,N) canAttemptTelephonyCallsWithoutCellularConnection;
@property (TB,R,N) canAttemptEmergencyCallsWithoutCellularConnection;
@property (TB,R,N,GisCSCallingCurrentlyAvailable) csCallingCurrentlyAvailable;
@property (TB,R,N) supportsVoLTECalling;
@property (TB,R,N,GisVoLTECallingEnabled) voLTECallingEnabled;
@property (TB,R,N,GisVoLTECallingCurrentlyAvailable) voLTECallingCurrentlyAvailable;
@property (TB,R,N) supportsWiFiCalling;
@property (TB,R,N,GisWiFiCallingEnabled) wiFiCallingEnabled;
@property (TB,R,N) supportsWiFiCallingRoaming;
@property (TB,R,N,GisWiFiCallingRoamingEnabled) wiFiCallingRoamingEnabled;
@property (TB,R,N,GisWiFiCallingCurrentlyAvailable) wiFiCallingCurrentlyAvailable;
@property (TB,R,N) supportsEmergencyWiFiCalling;
@property (TB,R,N,GisEmergencyWiFiCallingCurrentlyAvailable) emergencyWiFiCallingCurrentlyAvailable;
@property (Ti,R,N) wiFiCallingProvisioningStatus;
@property (T@"NSURL",R,C,N) wiFiCallingProvisioningURL;
@property (TB,R,N,GisWiFiCallingProvisioningURLInvalid) wiFiCallingProvisioningURLInvalid;
@property (T@"NSData",R,C,N) wiFiCallingProvisioningPostData;
@property (TB,R,N) supportsThumperCalling;
@property (TB,R,N) canEnableThumperCalling;
@property (TB,R,N,GisThumperCallingAllowedForCurrentDevice) thumperCallingAllowedForCurrentDevice;
@property (TB,R,N,GisThumperCallingEnabled) thumperCallingEnabled;
@property (TB,R,N,GisThumperCallingCurrentlyAvailable) thumperCallingCurrentlyAvailable;
@property (TB,R,N) supportsThumperCallingOverCellularData;
@property (T@"NSString",C,N,V_thumperCallingLocalDeviceID) thumperCallingLocalDeviceID;
@property (Ti,R,N) thumperCallingProvisioningStatus;
@property (T@"NSURL",R,C,N) thumperCallingProvisioningURL;
@property (TB,R,N,GisThumperCallingProvisioningURLInvalid) thumperCallingProvisioningURLInvalid;
@property (T@"NSData",R,C,N) thumperCallingProvisioningPostData;
@property (TB,R,N,GisThumperCallingAllowedOnDefaultPairedSecondaryDevice) thumperCallingAllowedOnDefaultPairedSecondaryDevice;
```

## Instance methods

```
-[TUSenderIdentityCapabilities wiFiCallingCapabilityInfo];
-[TUSenderIdentityCapabilities isWiFiCallingProvisioningURLInvalid];
-[TUSenderIdentityCapabilities isEmergencyWiFiCallingCurrentlyAvailable];
-[TUSenderIdentityCapabilities voLTECallingCapabilityInfo];
-[TUSenderIdentityCapabilities debugDescription];
-[TUSenderIdentityCapabilities thumperCallingLocalDeviceID];
-[TUSenderIdentityCapabilities supportsEmergencyWiFiCalling];
-[TUSenderIdentityCapabilities supportsSimultaneousVoiceAndData];
-[TUSenderIdentityCapabilities _sendNotificationsAndCallbacksComparingToOldSenderIdentityCapabilities:];
-[TUSenderIdentityCapabilities wiFiCallingProvisioningPostData];
-[TUSenderIdentityCapabilities canAttemptTelephonyCallsWithoutCellularConnection];
-[TUSenderIdentityCapabilities isThumperCallingProvisioningURLInvalid];
-[TUSenderIdentityCapabilities cancelPinRequestFromPrimaryDeviceForThumperCalling];
-[TUSenderIdentityCapabilities setWiFiCallingEnabled:];
-[TUSenderIdentityCapabilities invalidateAndRefreshWiFiCallingProvisioningURL];
-[TUSenderIdentityCapabilities invalidateAndRefreshThumperCallingProvisioningURL];
-[TUSenderIdentityCapabilities thumperCallingProvisioningPostData];
-[TUSenderIdentityCapabilities supportsThumperCallingOverCellularData];
-[TUSenderIdentityCapabilities isWiFiCallingCurrentlyAvailable];
-[TUSenderIdentityCapabilities setThumperCallingLocalDeviceID:];
-[TUSenderIdentityCapabilities isCSCallingCurrentlyAvailable];
-[TUSenderIdentityCapabilities supportsVoLTECalling];
-[TUSenderIdentityCapabilities isVoLTECallingCurrentlyAvailable];
-[TUSenderIdentityCapabilities canEnableThumperCalling];
-[TUSenderIdentityCapabilities setVoLTECallingEnabled:];
-[TUSenderIdentityCapabilities requestPinFromPrimaryDeviceForThumperCalling];
-[TUSenderIdentityCapabilities thumperCallingCapabilityInfo];
-[TUSenderIdentityCapabilities isWiFiCallingEnabled];
-[TUSenderIdentityCapabilities isVoLTECallingEnabled];
-[TUSenderIdentityCapabilities wiFiCallingProvisioningURL];
-[TUSenderIdentityCapabilities setThumperCallingEnabled:];
-[TUSenderIdentityCapabilities initWithSenderIdentityUUID:state:client:];
-[TUSenderIdentityCapabilities isThumperCallingAllowedOnDefaultPairedSecondaryDevice];
-[TUSenderIdentityCapabilities canAttemptEmergencyCallsWithoutCellularConnection];
-[TUSenderIdentityCapabilities supportsWiFiCallingRoaming];
-[TUSenderIdentityCapabilities thumperCallingProvisioningStatus];
-[TUSenderIdentityCapabilities wiFiCallingProvisioningStatus];
-[TUSenderIdentityCapabilities setThumperCallingAllowedOnDefaultPairedSecondaryDevice:];
-[TUSenderIdentityCapabilities isWiFiCallingRoamingEnabled];
-[TUSenderIdentityCapabilities senderIdentityUUID];
-[TUSenderIdentityCapabilities supportsThumperCalling];
-[TUSenderIdentityCapabilities thumperCallingProvisioningURL];
-[TUSenderIdentityCapabilities setThumperCallingAllowed:onSecondaryDeviceWithID:];
-[TUSenderIdentityCapabilities isThumperCallingAllowedOnSecondaryDeviceWithID:];
-[TUSenderIdentityCapabilities client];
-[TUSenderIdentityCapabilities isThumperCallingEnabled];
-[TUSenderIdentityCapabilities supportsWiFiCalling];
-[TUSenderIdentityCapabilities state];
-[TUSenderIdentityCapabilities setWiFiCallingRoamingEnabled:];
-[TUSenderIdentityCapabilities isThumperCallingCurrentlyAvailable];
-[TUSenderIdentityCapabilities isThumperCallingAllowedForCurrentDevice];
```
