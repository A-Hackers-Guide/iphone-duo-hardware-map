# `CWFWiFiNetworkSharingConnectedAPUpdate`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _connectedAPs;
Q _connectedAPsUpdateCounter;
```

## Properties

```
@property (T@"NSArray",C,V_connectedAPs) connectedAPs;
@property (TQ,V_connectedAPsUpdateCounter) connectedAPsUpdateCounter;
```

## Class methods

```
+[CWFWiFiNetworkSharingConnectedAPUpdate supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingConnectedAPUpdate encodeWithCoder:];
-[CWFWiFiNetworkSharingConnectedAPUpdate hash];
-[CWFWiFiNetworkSharingConnectedAPUpdate description];
-[CWFWiFiNetworkSharingConnectedAPUpdate initWithCoder:];
-[CWFWiFiNetworkSharingConnectedAPUpdate copyWithZone:];
-[CWFWiFiNetworkSharingConnectedAPUpdate isEqual:];
-[CWFWiFiNetworkSharingConnectedAPUpdate connectedAPs];
-[CWFWiFiNetworkSharingConnectedAPUpdate connectedAPsUpdateCounter];
-[CWFWiFiNetworkSharingConnectedAPUpdate isEqualToWiFiNetworkSharingConnectedAPUpdate:];
-[CWFWiFiNetworkSharingConnectedAPUpdate setConnectedAPs:];
-[CWFWiFiNetworkSharingConnectedAPUpdate setConnectedAPsUpdateCounter:];
```
