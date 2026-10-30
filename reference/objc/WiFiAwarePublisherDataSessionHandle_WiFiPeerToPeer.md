# `WiFiAwarePublisherDataSessionHandle`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
C _datapathID;
@"WiFiMACAddress" _initiatorDataAddress;
```

## Properties

```
@property (TC,R,N,V_datapathID) datapathID;
@property (T@"WiFiMACAddress",R,N,V_initiatorDataAddress) initiatorDataAddress;
```

## Class methods

```
+[WiFiAwarePublisherDataSessionHandle supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePublisherDataSessionHandle encodeWithCoder:];
-[WiFiAwarePublisherDataSessionHandle hash];
-[WiFiAwarePublisherDataSessionHandle description];
-[WiFiAwarePublisherDataSessionHandle initWithCoder:];
-[WiFiAwarePublisherDataSessionHandle isEqual:];
-[WiFiAwarePublisherDataSessionHandle datapathID];
-[WiFiAwarePublisherDataSessionHandle initiatorDataAddress];
-[WiFiAwarePublisherDataSessionHandle initWithDatapathID:initiatorDataAddress:];
```
