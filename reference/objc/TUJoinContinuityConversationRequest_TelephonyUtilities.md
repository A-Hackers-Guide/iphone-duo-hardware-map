# `TUJoinContinuityConversationRequest`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 10 instance methods, 4 class methods

## Instance variables

```
B _isAudioEnabled;
B _isVideoEnabled;
B _wantsStagingArea;
B _isOutgoing;
@"NSUUID" _uuid;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (TB,R,N,V_isAudioEnabled) isAudioEnabled;
@property (TB,R,N,V_isVideoEnabled) isVideoEnabled;
@property (TB,R,N,V_wantsStagingArea) wantsStagingArea;
@property (TB,R,N,V_isOutgoing) isOutgoing;
```

## Class methods

```
+[TUJoinContinuityConversationRequest supportsSecureCoding];
+[TUJoinContinuityConversationRequest requestForJoinWithUUID:isAudioEnabled:isVideoEnabled:];
+[TUJoinContinuityConversationRequest requestForJoinWithUUID:isAudioEnabled:isVideoEnabled:isOutgoing:];
+[TUJoinContinuityConversationRequest requestForStagingAreaWithUUID:];
```

## Instance methods

```
-[TUJoinContinuityConversationRequest isOutgoing];
-[TUJoinContinuityConversationRequest isVideoEnabled];
-[TUJoinContinuityConversationRequest isAudioEnabled];
-[TUJoinContinuityConversationRequest uuid];
-[TUJoinContinuityConversationRequest wantsStagingArea];
-[TUJoinContinuityConversationRequest encodeWithCoder:];
-[TUJoinContinuityConversationRequest description];
-[TUJoinContinuityConversationRequest initWithCoder:];
-[TUJoinContinuityConversationRequest initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:];
-[TUJoinContinuityConversationRequest initWithUUID:isAudioEnabled:isVideoEnabled:wantsStagingArea:isOutgoing:];
```
