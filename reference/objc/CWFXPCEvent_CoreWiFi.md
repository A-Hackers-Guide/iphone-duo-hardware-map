# `CWFXPCEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 11 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _UUID;
q _type;
q _internalType;
@"CWFWiFiNetworkSharingClientID" _wifiNetworkSharingClientID;
@"NSData" _wifiNetworkSharingNetworkListUpdateEventPredicateData;
@"NSData" _wifiNetworkSharingConnectedAPUpdateEventPredicateData;
@"NSString" _interfaceName;
@"NSDictionary" _info;
@"NSDate" _timestamp;
Q _acknowledgementTimeout;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (Tq,N,V_type) type;
@property (Tq,N,V_internalType) internalType;
@property (T@"CWFWiFiNetworkSharingClientID",C,N,V_wifiNetworkSharingClientID) wifiNetworkSharingClientID;
@property (T@"NSData",C,N,V_wifiNetworkSharingNetworkListUpdateEventPredicateData) wifiNetworkSharingNetworkListUpdateEventPredicateData;
@property (T@"NSData",C,N,V_wifiNetworkSharingConnectedAPUpdateEventPredicateData) wifiNetworkSharingConnectedAPUpdateEventPredicateData;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"NSDictionary",C,N,V_info) info;
@property (T@"NSDate",C,N,V_timestamp) timestamp;
@property (TQ,N,V_acknowledgementTimeout) acknowledgementTimeout;
@property (T@"CWFEventID",R) eventID;
```

## Class methods

```
+[CWFXPCEvent supportsSecureCoding];
```

## Instance methods

```
-[CWFXPCEvent internalType];
-[CWFXPCEvent setWifiNetworkSharingNetworkListUpdateEventPredicateData:];
-[CWFXPCEvent setTimestamp:];
-[CWFXPCEvent wifiNetworkSharingNetworkListUpdateEventPredicateData];
-[CWFXPCEvent setWifiNetworkSharingConnectedAPUpdateEventPredicateData:];
-[CWFXPCEvent eventID];
-[CWFXPCEvent info];
-[CWFXPCEvent wifiNetworkSharingConnectedAPUpdateEventPredicateData];
-[CWFXPCEvent init];
-[CWFXPCEvent setInfo:];
-[CWFXPCEvent setUUID:];
-[CWFXPCEvent UUID];
-[CWFXPCEvent setInterfaceName:];
-[CWFXPCEvent timestamp];
-[CWFXPCEvent interfaceName];
-[CWFXPCEvent isEqualToXPCEvent:];
-[CWFXPCEvent acknowledgementTimeout];
-[CWFXPCEvent wifiNetworkSharingClientID];
-[CWFXPCEvent setType:];
-[CWFXPCEvent type];
-[CWFXPCEvent setInternalType:];
-[CWFXPCEvent encodeWithCoder:];
-[CWFXPCEvent hash];
-[CWFXPCEvent description];
-[CWFXPCEvent setAcknowledgementTimeout:];
-[CWFXPCEvent initWithCoder:];
-[CWFXPCEvent setWifiNetworkSharingClientID:];
-[CWFXPCEvent copyWithZone:];
-[CWFXPCEvent isEqual:];
-[CWFXPCEvent __descriptionForEventType];
```
