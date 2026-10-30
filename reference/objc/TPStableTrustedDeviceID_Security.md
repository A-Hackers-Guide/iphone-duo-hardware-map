# `TPStableTrustedDeviceID`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSString" _sdid;
@"NSString" _lduid;
@"NSString" _idMSTrustTimestamp;
```

## Properties

```
@property (T@"NSString",R,N,V_sdid) sdid;
@property (T@"NSString",R,N,V_lduid) lduid;
@property (T@"NSString",R,N,V_idMSTrustTimestamp) idMSTrustTimestamp;
```

## Class methods

```
+[TPStableTrustedDeviceID supportsSecureCoding];
```

## Instance methods

```
-[TPStableTrustedDeviceID encodeWithCoder:];
-[TPStableTrustedDeviceID hash];
-[TPStableTrustedDeviceID description];
-[TPStableTrustedDeviceID initWithCoder:];
-[TPStableTrustedDeviceID isEqual:];
-[TPStableTrustedDeviceID isEqualToStableTrustedDeviceID:];
-[TPStableTrustedDeviceID hasAllFields];
-[TPStableTrustedDeviceID idMSTrustTimestamp];
-[TPStableTrustedDeviceID initWithSDID:lduid:idMSTrustTimestamp:];
-[TPStableTrustedDeviceID lduid];
-[TPStableTrustedDeviceID sdid];
```
