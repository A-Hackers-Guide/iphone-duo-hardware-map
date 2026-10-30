# `TUSmartHoldingSessionRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _uuid;
@"NSUUID" _callUUID;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (T@"NSUUID",R,N,V_callUUID) callUUID;
```

## Class methods

```
+[TUSmartHoldingSessionRequest supportsSecureCoding];
```

## Instance methods

```
-[TUSmartHoldingSessionRequest uuid];
-[TUSmartHoldingSessionRequest callUUID];
-[TUSmartHoldingSessionRequest encodeWithCoder:];
-[TUSmartHoldingSessionRequest initWithCoder:];
-[TUSmartHoldingSessionRequest copyWithZone:];
-[TUSmartHoldingSessionRequest initWithCallUUID:];
```
