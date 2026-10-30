# `CWFWiFiNetworkSharingEventID`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CWFEventID`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"CWFWiFiNetworkSharingClientID" _clientID;
@"NSData" _networkListUpdateEventPredicateData;
@"NSData" _connectedAPUpdateEventPredicateData;
```

## Properties

```
@property (T@"CWFWiFiNetworkSharingClientID",C,V_clientID) clientID;
@property (T@"NSData",C,N,V_networkListUpdateEventPredicateData) networkListUpdateEventPredicateData;
@property (T@"NSData",C,N,V_connectedAPUpdateEventPredicateData) connectedAPUpdateEventPredicateData;
```

## Class methods

```
+[CWFWiFiNetworkSharingEventID supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingEventID clientID];
-[CWFWiFiNetworkSharingEventID setClientID:];
-[CWFWiFiNetworkSharingEventID setConnectedAPUpdateEventPredicateData:];
-[CWFWiFiNetworkSharingEventID connectedAPUpdateEventPredicateData];
-[CWFWiFiNetworkSharingEventID isEqualToWiFiNetworkSharingEventID:];
-[CWFWiFiNetworkSharingEventID encodeWithCoder:];
-[CWFWiFiNetworkSharingEventID hash];
-[CWFWiFiNetworkSharingEventID description];
-[CWFWiFiNetworkSharingEventID initWithCoder:];
-[CWFWiFiNetworkSharingEventID setNetworkListUpdateEventPredicateData:];
-[CWFWiFiNetworkSharingEventID copyWithZone:];
-[CWFWiFiNetworkSharingEventID isEqual:];
-[CWFWiFiNetworkSharingEventID networkListUpdateEventPredicateData];
```
