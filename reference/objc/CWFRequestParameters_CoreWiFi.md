# `CWFRequestParameters`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 28 instance methods, 1 class methods

## Instance variables

```
i _virtualInterfaceRole;
@"NSUUID" _UUID;
@"NSString" _interfaceName;
Q _timeout;
q _qualityOfService;
q _queuePriority;
@"NSString" _wifiNetworkSharingBundleIDOverride;
@"NSString" _wifiNetworkSharingAccessoryID;
@"NSData" _wifiNetworkSharingNetworkListUpdateEventPredicateData;
@"NSData" _wifiNetworkSharingConnectedAPUpdateEventPredicateData;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"NSString",C,N,V_wifiNetworkSharingBundleIDOverride) wifiNetworkSharingBundleIDOverride;
@property (T@"NSString",C,N,V_wifiNetworkSharingAccessoryID) wifiNetworkSharingAccessoryID;
@property (T@"NSData",C,N,V_wifiNetworkSharingNetworkListUpdateEventPredicateData) wifiNetworkSharingNetworkListUpdateEventPredicateData;
@property (T@"NSData",C,N,V_wifiNetworkSharingConnectedAPUpdateEventPredicateData) wifiNetworkSharingConnectedAPUpdateEventPredicateData;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (Ti,N,V_virtualInterfaceRole) virtualInterfaceRole;
@property (TQ,N,V_timeout) timeout;
@property (Tq,N,V_qualityOfService) qualityOfService;
@property (Tq,N,V_queuePriority) queuePriority;
```

## Class methods

```
+[CWFRequestParameters supportsSecureCoding];
```

## Instance methods

```
-[CWFRequestParameters virtualInterfaceRole];
-[CWFRequestParameters setWifiNetworkSharingNetworkListUpdateEventPredicateData:];
-[CWFRequestParameters wifiNetworkSharingNetworkListUpdateEventPredicateData];
-[CWFRequestParameters setWifiNetworkSharingConnectedAPUpdateEventPredicateData:];
-[CWFRequestParameters wifiNetworkSharingConnectedAPUpdateEventPredicateData];
-[CWFRequestParameters setVirtualInterfaceRole:];
-[CWFRequestParameters init];
-[CWFRequestParameters setQueuePriority:];
-[CWFRequestParameters setUUID:];
-[CWFRequestParameters UUID];
-[CWFRequestParameters setInterfaceName:];
-[CWFRequestParameters setQualityOfService:];
-[CWFRequestParameters qualityOfService];
-[CWFRequestParameters interfaceName];
-[CWFRequestParameters timeout];
-[CWFRequestParameters setTimeout:];
-[CWFRequestParameters setWifiNetworkSharingAccessoryID:];
-[CWFRequestParameters encodeWithCoder:];
-[CWFRequestParameters hash];
-[CWFRequestParameters wifiNetworkSharingBundleIDOverride];
-[CWFRequestParameters description];
-[CWFRequestParameters wifiNetworkSharingAccessoryID];
-[CWFRequestParameters initWithCoder:];
-[CWFRequestParameters isEqualToRequestParameters:];
-[CWFRequestParameters queuePriority];
-[CWFRequestParameters setWifiNetworkSharingBundleIDOverride:];
-[CWFRequestParameters copyWithZone:];
-[CWFRequestParameters isEqual:];
```
