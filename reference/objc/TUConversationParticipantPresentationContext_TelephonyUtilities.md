# `TUConversationParticipantPresentationContext`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _isInCanvas;
Q _participantIdentifier;
Q _videoQuality;
@"NSNumber" _visibility;
@"NSNumber" _prominence;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _spatialPosition;
```

## Properties

```
@property (TQ,R,N,V_participantIdentifier) participantIdentifier;
@property (TQ,R,N,V_videoQuality) videoQuality;
@property (T@"NSNumber",R,N,V_visibility) visibility;
@property (T@"NSNumber",R,N,V_prominence) prominence;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_spatialPosition) spatialPosition;
@property (TB,R,N,V_isInCanvas) isInCanvas;
```

## Class methods

```
+[TUConversationParticipantPresentationContext supportsSecureCoding];
```

## Instance methods

```
-[TUConversationParticipantPresentationContext isInCanvas];
-[TUConversationParticipantPresentationContext prominence];
-[TUConversationParticipantPresentationContext videoQuality];
-[TUConversationParticipantPresentationContext visibility];
-[TUConversationParticipantPresentationContext spatialPosition];
-[TUConversationParticipantPresentationContext participantIdentifier];
-[TUConversationParticipantPresentationContext initWithParticipantIdentifier:videoQuality:visibility:prominence:spatialPosition:isInCanvas:];
-[TUConversationParticipantPresentationContext encodeWithCoder:];
-[TUConversationParticipantPresentationContext description];
-[TUConversationParticipantPresentationContext initWithCoder:];
```
