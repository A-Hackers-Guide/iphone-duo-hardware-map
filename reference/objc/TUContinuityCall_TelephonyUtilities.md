# `TUContinuityCall`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 11 properties, 15 instance methods, 1 class methods

## Instance variables

```
i _status;
@"NSUUID" _uuid;
@"NSUUID" _conversationUUID;
@"NSNumber" _isMuted;
@"NSNumber" _isCameraEnabled;
@"NSUUID" _callGroupUUID;
@"TUContinuityCallInfo" _callInfo;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (Ti,R,N,V_status) status;
@property (T@"NSUUID",R,N,V_conversationUUID) conversationUUID;
@property (T@"NSNumber",R,N,V_isMuted) isMuted;
@property (T@"NSNumber",R,N,V_isCameraEnabled) isCameraEnabled;
@property (T@"NSUUID",R,N,V_callGroupUUID) callGroupUUID;
@property (T@"TUContinuityCallInfo",R,N,V_callInfo) callInfo;
@property (T@"NSString",R,N) displayName;
@property (T@"NSString",R,N) callerIdSubstring;
@property (TB,R,N) isBranded;
@property (T@"NSArray",R,N) remoteMemberContactIdentifiers;
```

## Class methods

```
+[TUContinuityCall supportsSecureCoding];
```

## Instance methods

```
-[TUContinuityCall isMuted];
-[TUContinuityCall conversationUUID];
-[TUContinuityCall uuid];
-[TUContinuityCall displayName];
-[TUContinuityCall status];
-[TUContinuityCall encodeWithCoder:];
-[TUContinuityCall description];
-[TUContinuityCall initWithCoder:];
-[TUContinuityCall callGroupUUID];
-[TUContinuityCall isCameraEnabled];
-[TUContinuityCall callInfo];
-[TUContinuityCall callerIdSubstring];
-[TUContinuityCall initWithUUID:conversationUUID:callGroupUUID:status:isMuted:isCameraEnabled:callInfo:];
-[TUContinuityCall isBranded];
-[TUContinuityCall remoteMemberContactIdentifiers];
```
