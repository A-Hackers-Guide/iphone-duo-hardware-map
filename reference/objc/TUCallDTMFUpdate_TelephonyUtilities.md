# `TUCallDTMFUpdate`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _digits;
@"NSUUID" _UUID;
```

## Properties

```
@property (T@"NSString",C,N,V_digits) digits;
@property (T@"NSUUID",&,N,V_UUID) UUID;
```

## Class methods

```
+[TUCallDTMFUpdate supportsSecureCoding];
```

## Instance methods

```
-[TUCallDTMFUpdate setUUID:];
-[TUCallDTMFUpdate UUID];
-[TUCallDTMFUpdate encodeWithCoder:];
-[TUCallDTMFUpdate description];
-[TUCallDTMFUpdate initWithCoder:];
-[TUCallDTMFUpdate copyWithZone:];
-[TUCallDTMFUpdate digits];
-[TUCallDTMFUpdate initWithDigits:];
-[TUCallDTMFUpdate setDigits:];
```
