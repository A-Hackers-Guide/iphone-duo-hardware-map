# `TUCallRecordingRequest`

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
@property (T@"NSUUID",&,N,V_callUUID) callUUID;
@property (T@"NSUUID",&,N,V_UUID) UUID;
```

## Class methods

```
+[TUCallRecordingRequest supportsSecureCoding];
```

## Instance methods

```
-[TUCallRecordingRequest setUUID:];
-[TUCallRecordingRequest UUID];
-[TUCallRecordingRequest setCallUUID:];
-[TUCallRecordingRequest callUUID];
-[TUCallRecordingRequest encodeWithCoder:];
-[TUCallRecordingRequest description];
-[TUCallRecordingRequest initWithCoder:];
-[TUCallRecordingRequest copyWithZone:];
-[TUCallRecordingRequest initWithCall:];
```
