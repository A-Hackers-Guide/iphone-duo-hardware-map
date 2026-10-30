# `CWFWiFiNetworkSharingNetworkListUpdate`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isAskToShareNetworkAvailable;
B _isAskToShareRequestFromAppPending;
@"NSArray" _networkList;
Q _networkListUpdateCounter;
```

## Properties

```
@property (T@"NSArray",C,V_networkList) networkList;
@property (TQ,V_networkListUpdateCounter) networkListUpdateCounter;
@property (TB,V_isAskToShareNetworkAvailable) isAskToShareNetworkAvailable;
@property (TB,V_isAskToShareRequestFromAppPending) isAskToShareRequestFromAppPending;
```

## Class methods

```
+[CWFWiFiNetworkSharingNetworkListUpdate supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingNetworkListUpdate encodeWithCoder:];
-[CWFWiFiNetworkSharingNetworkListUpdate hash];
-[CWFWiFiNetworkSharingNetworkListUpdate description];
-[CWFWiFiNetworkSharingNetworkListUpdate initWithCoder:];
-[CWFWiFiNetworkSharingNetworkListUpdate copyWithZone:];
-[CWFWiFiNetworkSharingNetworkListUpdate isEqual:];
-[CWFWiFiNetworkSharingNetworkListUpdate setNetworkList:];
-[CWFWiFiNetworkSharingNetworkListUpdate networkList];
-[CWFWiFiNetworkSharingNetworkListUpdate isAskToShareNetworkAvailable];
-[CWFWiFiNetworkSharingNetworkListUpdate isAskToShareRequestFromAppPending];
-[CWFWiFiNetworkSharingNetworkListUpdate isEqualToWiFiNetworkSharingNetworksUpdate:];
-[CWFWiFiNetworkSharingNetworkListUpdate networkListUpdateCounter];
-[CWFWiFiNetworkSharingNetworkListUpdate setIsAskToShareNetworkAvailable:];
-[CWFWiFiNetworkSharingNetworkListUpdate setIsAskToShareRequestFromAppPending:];
-[CWFWiFiNetworkSharingNetworkListUpdate setNetworkListUpdateCounter:];
```
