# `TUScreeningRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _UUID;
@"NSUUID" _callUUID;
```

## Properties

```
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (T@"NSUUID",&,N,V_callUUID) callUUID;
```

## Class methods

```
+[TUScreeningRequest supportsSecureCoding];
```

## Instance methods

```
-[TUScreeningRequest setUUID:];
-[TUScreeningRequest UUID];
-[TUScreeningRequest setCallUUID:];
-[TUScreeningRequest callUUID];
-[TUScreeningRequest encodeWithCoder:];
-[TUScreeningRequest description];
-[TUScreeningRequest initWithCoder:];
-[TUScreeningRequest copyWithZone:];
-[TUScreeningRequest initWithTUCallUpdate:];
```
