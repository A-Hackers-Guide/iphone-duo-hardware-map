# `_CLRangingPeer`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 2 properties, 15 instance methods, 3 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (TQ,R,N) macAddress;
@property (T@"NSData",R,C,N) secureRangingKeyID;
```

## Class methods

```
+[_CLRangingPeer supportsSecureCoding];
+[_CLRangingPeer hexStringMacAddressFromUInt:];
+[_CLRangingPeer uintMacAddressFromString:];
```

## Instance methods

```
-[_CLRangingPeer macAddress];
-[_CLRangingPeer init];
-[_CLRangingPeer dealloc];
-[_CLRangingPeer encodeWithCoder:];
-[_CLRangingPeer hash];
-[_CLRangingPeer description];
-[_CLRangingPeer initWithCoder:];
-[_CLRangingPeer copyWithZone:];
-[_CLRangingPeer isEqual:];
-[_CLRangingPeer getMacAddressAsString];
-[_CLRangingPeer initWithMacAddressAsData:secureRangingKeyID:];
-[_CLRangingPeer initWithMacAddressAsString:secureRangingKeyID:];
-[_CLRangingPeer initWithMacAddressAsUInt:secureRangingKeyID:];
-[_CLRangingPeer isEqualToPeer:];
-[_CLRangingPeer secureRangingKeyID];
```
