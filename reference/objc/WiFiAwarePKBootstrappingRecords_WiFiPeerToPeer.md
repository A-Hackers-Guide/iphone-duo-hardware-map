# `WiFiAwarePKBootstrappingRecords`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSDate" _expiration;
@"NSSet" _bootstrappingRecords;
```

## Properties

```
@property (T@"NSDate",R,N,V_expiration) expiration;
@property (T@"NSSet",R,N,V_bootstrappingRecords) bootstrappingRecords;
```

## Class methods

```
+[WiFiAwarePKBootstrappingRecords supportsSecureCoding];
```

## Instance methods

```
-[WiFiAwarePKBootstrappingRecords expiration];
-[WiFiAwarePKBootstrappingRecords encodeWithCoder:];
-[WiFiAwarePKBootstrappingRecords description];
-[WiFiAwarePKBootstrappingRecords initWithCoder:];
-[WiFiAwarePKBootstrappingRecords bootstrappingRecords];
-[WiFiAwarePKBootstrappingRecords initWithExpiration:bootstrappingRecords:];
```
