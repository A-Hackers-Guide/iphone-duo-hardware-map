# `CWFRemoteInterfaceNetworkInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
i _state;
@"NSString" _SSID;
@"NSString" _BSSID;
Q _securityType;
q _RSSI;
@"NSString" _networkName;
@"NSString" _macAddress;
```

## Properties

```
@property (T@"NSString",C,N,V_SSID) SSID;
@property (Tq,N,V_RSSI) RSSI;
@property (T@"NSString",C,N,V_BSSID) BSSID;
@property (TQ,N,V_securityType) securityType;
@property (Ti,N,V_state) state;
@property (T@"NSString",C,N,V_macAddress) macAddress;
@property (T@"NSString",C,N,V_networkName) networkName;
```

## Class methods

```
+[CWFRemoteInterfaceNetworkInfo supportsSecureCoding];
```

## Instance methods

```
-[CWFRemoteInterfaceNetworkInfo securityType];
-[CWFRemoteInterfaceNetworkInfo networkName];
-[CWFRemoteInterfaceNetworkInfo setSSID:];
-[CWFRemoteInterfaceNetworkInfo BSSID];
-[CWFRemoteInterfaceNetworkInfo SSID];
-[CWFRemoteInterfaceNetworkInfo setState:];
-[CWFRemoteInterfaceNetworkInfo setBSSID:];
-[CWFRemoteInterfaceNetworkInfo macAddress];
-[CWFRemoteInterfaceNetworkInfo setRSSI:];
-[CWFRemoteInterfaceNetworkInfo initWithInterface:];
-[CWFRemoteInterfaceNetworkInfo RSSI];
-[CWFRemoteInterfaceNetworkInfo setMacAddress:];
-[CWFRemoteInterfaceNetworkInfo encodeWithCoder:];
-[CWFRemoteInterfaceNetworkInfo description];
-[CWFRemoteInterfaceNetworkInfo initWithCoder:];
-[CWFRemoteInterfaceNetworkInfo setNetworkName:];
-[CWFRemoteInterfaceNetworkInfo state];
-[CWFRemoteInterfaceNetworkInfo setSecurityType:];
-[CWFRemoteInterfaceNetworkInfo initWithSSID:];
-[CWFRemoteInterfaceNetworkInfo initWithScanResult:];
```
