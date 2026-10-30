# `TUCallRecordingSessionBase`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 6 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _redisclosing;
@"NSUUID" _UUID;
@"NSString" _callUUID;
@"NSDate" _recordingStartedDate;
@"NSDate" _recordingEndedDate;
@"NSUUID" _requestUUID;
```

## Properties

```
@property (T@"NSUUID",&,N,V_UUID) UUID;
@property (T@"NSUUID",&,N,V_requestUUID) requestUUID;
@property (T@"NSString",&,N,V_callUUID) callUUID;
@property (T@"NSDate",&,N,V_recordingStartedDate) recordingStartedDate;
@property (T@"NSDate",&,N,V_recordingEndedDate) recordingEndedDate;
@property (TB,N,GisRedisclosing,V_redisclosing) redisclosing;
```

## Class methods

```
+[TUCallRecordingSessionBase supportsSecureCoding];
```

## Instance methods

```
-[TUCallRecordingSessionBase requestUUID];
-[TUCallRecordingSessionBase setRequestUUID:];
-[TUCallRecordingSessionBase setUUID:];
-[TUCallRecordingSessionBase UUID];
-[TUCallRecordingSessionBase setCallUUID:];
-[TUCallRecordingSessionBase callUUID];
-[TUCallRecordingSessionBase encodeWithCoder:];
-[TUCallRecordingSessionBase description];
-[TUCallRecordingSessionBase initWithCoder:];
-[TUCallRecordingSessionBase copyWithZone:];
-[TUCallRecordingSessionBase isEqual:];
-[TUCallRecordingSessionBase initWithUUID:callUUID:requestUUID:recordingStartedDate:recordingEndedDate:isRedisclosing:];
-[TUCallRecordingSessionBase isEqualToRecordingSessionBase:];
-[TUCallRecordingSessionBase isRedisclosing];
-[TUCallRecordingSessionBase recordingEndedDate];
-[TUCallRecordingSessionBase recordingStartedDate];
-[TUCallRecordingSessionBase setRecordingEndedDate:];
-[TUCallRecordingSessionBase setRecordingStartedDate:];
-[TUCallRecordingSessionBase setRedisclosing:];
```
