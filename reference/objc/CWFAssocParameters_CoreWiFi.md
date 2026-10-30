# `CWFAssocParameters`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 11 instance variables, 11 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _rememberUponSuccessfulAssociation;
B _forceBSSID;
B _has6GHzOnlyBSS;
B _findAndJoinNetwork;
@"CWFScanResult" _scanResult;
@"CWFNetworkProfile" _knownNetworkProfile;
@"NSString" _password;
@"CWFEAPCredentials" _EAPCredentials;
q _bandPreference;
@"NSString" _colocatedScopeID;
@"SFRemoteHotspotDevice" _remoteHotspotDevice;
```

## Properties

```
@property (T@"CWFScanResult",C,N,V_scanResult) scanResult;
@property (T@"CWFNetworkProfile",C,N,V_knownNetworkProfile) knownNetworkProfile;
@property (T@"NSString",C,N,V_password) password;
@property (T@"CWFEAPCredentials",C,N,V_EAPCredentials) EAPCredentials;
@property (TB,N,V_rememberUponSuccessfulAssociation) rememberUponSuccessfulAssociation;
@property (Tq,N,V_bandPreference) bandPreference;
@property (T@"NSString",C,N,V_colocatedScopeID) colocatedScopeID;
@property (TB,N,V_forceBSSID) forceBSSID;
@property (TB,N,V_has6GHzOnlyBSS) has6GHzOnlyBSS;
@property (T@"SFRemoteHotspotDevice",&,N,V_remoteHotspotDevice) remoteHotspotDevice;
@property (TB,N,V_findAndJoinNetwork) findAndJoinNetwork;
```

## Class methods

```
+[CWFAssocParameters supportsSecureCoding];
```

## Instance methods

```
-[CWFAssocParameters setColocatedScopeID:];
-[CWFAssocParameters knownNetworkProfile];
-[CWFAssocParameters setKnownNetworkProfile:];
-[CWFAssocParameters colocatedScopeID];
-[CWFAssocParameters encodeWithCoder:];
-[CWFAssocParameters hash];
-[CWFAssocParameters description];
-[CWFAssocParameters initWithCoder:];
-[CWFAssocParameters setPassword:];
-[CWFAssocParameters copyWithZone:];
-[CWFAssocParameters isEqual:];
-[CWFAssocParameters password];
-[CWFAssocParameters EAPCredentials];
-[CWFAssocParameters bandPreference];
-[CWFAssocParameters findAndJoinNetwork];
-[CWFAssocParameters forceBSSID];
-[CWFAssocParameters has6GHzOnlyBSS];
-[CWFAssocParameters isEqualToAssocParameters:];
-[CWFAssocParameters rememberUponSuccessfulAssociation];
-[CWFAssocParameters remoteHotspotDevice];
-[CWFAssocParameters scanResult];
-[CWFAssocParameters setBandPreference:];
-[CWFAssocParameters setEAPCredentials:];
-[CWFAssocParameters setFindAndJoinNetwork:];
-[CWFAssocParameters setForceBSSID:];
-[CWFAssocParameters setHas6GHzOnlyBSS:];
-[CWFAssocParameters setRememberUponSuccessfulAssociation:];
-[CWFAssocParameters setRemoteHotspotDevice:];
-[CWFAssocParameters setScanResult:];
```
