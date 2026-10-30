# `THThreadNetwork`

- Image: [`/System/Library/Frameworks/ThreadNetwork.framework/ThreadNetwork`](../userland/System__Library__Frameworks__ThreadNetwork.framework__ThreadNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSString" _networkName;
@"NSData" _extendedPANID;
```

## Properties

```
@property (T@"NSString",R,N,V_networkName) networkName;
@property (T@"NSData",R,N,V_extendedPANID) extendedPANID;
```

## Class methods

```
+[THThreadNetwork supportsSecureCoding];
```

## Instance methods

```
-[THThreadNetwork networkName];
-[THThreadNetwork encodeWithCoder:];
-[THThreadNetwork initWithCoder:];
-[THThreadNetwork extendedPANID];
-[THThreadNetwork initWithName:extendedPANID:];
```
