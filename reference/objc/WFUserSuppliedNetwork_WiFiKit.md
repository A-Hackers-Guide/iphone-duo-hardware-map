# `WFUserSuppliedNetwork`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFNetworkListRecord`
- 5 instance variables, 9 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSString" _ssid;
q _security;
@"NSString" _username;
@"NSString" _password;
^{__SecIdentity=} _TLSIdentity;
```

## Properties

```
@property (T@"NSString",C,N,V_ssid) ssid;
@property (Tq,N,V_security) security;
@property (T@"NSString",C,N,V_username) username;
@property (T@"NSString",C,N,V_password) password;
@property (T^{__SecIdentity=},N,V_TLSIdentity) TLSIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WFUserSuppliedNetwork rssi];
-[WFUserSuppliedNetwork signalBars];
-[WFUserSuppliedNetwork ssid];
-[WFUserSuppliedNetwork setSsid:];
-[WFUserSuppliedNetwork isSecure];
-[WFUserSuppliedNetwork isEnterprise];
-[WFUserSuppliedNetwork scaledRSSI];
-[WFUserSuppliedNetwork subtitle];
-[WFUserSuppliedNetwork username];
-[WFUserSuppliedNetwork isAdhoc];
-[WFUserSuppliedNetwork title];
-[WFUserSuppliedNetwork isInstantHotspot];
-[WFUserSuppliedNetwork security];
-[WFUserSuppliedNetwork setUsername:];
-[WFUserSuppliedNetwork setPassword:];
-[WFUserSuppliedNetwork password];
-[WFUserSuppliedNetwork setSecurity:];
-[WFUserSuppliedNetwork setTLSIdentity:];
-[WFUserSuppliedNetwork TLSIdentity];
-[WFUserSuppliedNetwork canBeDisplayedAsCurrent];
-[WFUserSuppliedNetwork hotspotBatteryLife];
-[WFUserSuppliedNetwork hotspotCellularProtocol];
-[WFUserSuppliedNetwork hotspotSignalStrength];
-[WFUserSuppliedNetwork iOSHotspot];
-[WFUserSuppliedNetwork isUnconfiguredAccessory];
```
