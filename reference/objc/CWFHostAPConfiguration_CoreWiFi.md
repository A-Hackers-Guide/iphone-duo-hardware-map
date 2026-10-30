# `CWFHostAPConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 14 instance variables, 14 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _forceHiddenMode;
B _forceBeaconInterval100ms;
B _mfpc;
i _PHYMode;
i _bridgeMode;
i _bridgeType;
@"NSData" _SSID;
@"CWFChannel" _channel;
Q _securityType;
@"NSString" _password;
@"NSData" _IEList;
@"NSString" _bridgeInterfaceName;
q _h2eonly;
q _transitiondisabledflags;
```

## Properties

```
@property (T@"NSData",C,N,V_SSID) SSID;
@property (T@"CWFChannel",C,N,V_channel) channel;
@property (TQ,N,V_securityType) securityType;
@property (T@"NSString",C,N,V_password) password;
@property (Ti,N,V_PHYMode) PHYMode;
@property (T@"NSData",C,N,V_IEList) IEList;
@property (TB,N,V_forceHiddenMode) forceHiddenMode;
@property (TB,N,V_forceBeaconInterval100ms) forceBeaconInterval100ms;
@property (Ti,N,V_bridgeMode) bridgeMode;
@property (Ti,N,V_bridgeType) bridgeType;
@property (T@"NSString",C,N,V_bridgeInterfaceName) bridgeInterfaceName;
@property (Tq,N,V_h2eonly) h2eonly;
@property (Tq,N,V_transitiondisabledflags) transitiondisabledflags;
@property (TB,N,V_mfpc) mfpc;
```

## Class methods

```
+[CWFHostAPConfiguration supportsSecureCoding];
```

## Instance methods

```
-[CWFHostAPConfiguration securityType];
-[CWFHostAPConfiguration setChannel:];
-[CWFHostAPConfiguration channel];
-[CWFHostAPConfiguration PHYMode];
-[CWFHostAPConfiguration setSSID:];
-[CWFHostAPConfiguration SSID];
-[CWFHostAPConfiguration encodeWithCoder:];
-[CWFHostAPConfiguration hash];
-[CWFHostAPConfiguration description];
-[CWFHostAPConfiguration initWithCoder:];
-[CWFHostAPConfiguration setPassword:];
-[CWFHostAPConfiguration copyWithZone:];
-[CWFHostAPConfiguration isEqual:];
-[CWFHostAPConfiguration password];
-[CWFHostAPConfiguration setPHYMode:];
-[CWFHostAPConfiguration setSecurityType:];
-[CWFHostAPConfiguration h2eonly];
-[CWFHostAPConfiguration IEList];
-[CWFHostAPConfiguration forceHiddenMode];
-[CWFHostAPConfiguration bridgeInterfaceName];
-[CWFHostAPConfiguration bridgeMode];
-[CWFHostAPConfiguration bridgeType];
-[CWFHostAPConfiguration forceBeaconInterval100ms];
-[CWFHostAPConfiguration isEqualToHostAPConfiguration:];
-[CWFHostAPConfiguration mfpc];
-[CWFHostAPConfiguration setBridgeInterfaceName:];
-[CWFHostAPConfiguration setBridgeMode:];
-[CWFHostAPConfiguration setBridgeType:];
-[CWFHostAPConfiguration setForceBeaconInterval100ms:];
-[CWFHostAPConfiguration setForceHiddenMode:];
-[CWFHostAPConfiguration setH2eonly:];
-[CWFHostAPConfiguration setIEList:];
-[CWFHostAPConfiguration setMfpc:];
-[CWFHostAPConfiguration setTransitiondisabledflags:];
-[CWFHostAPConfiguration transitiondisabledflags];
```
