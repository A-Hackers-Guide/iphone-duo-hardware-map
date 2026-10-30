# `TUConversationHandoffContext`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _prefersToPlayDuringWombat;
B _setUplinkMuted;
@"NSSet" _invitationPreferences;
@"TUConversationPresentationContext" _presentationContext;
```

## Properties

```
@property (TB,N,V_prefersToPlayDuringWombat) prefersToPlayDuringWombat;
@property (T@"NSSet",C,N,V_invitationPreferences) invitationPreferences;
@property (T@"TUConversationPresentationContext",C,N,V_presentationContext) presentationContext;
@property (TB,N,V_setUplinkMuted) setUplinkMuted;
```

## Class methods

```
+[TUConversationHandoffContext supportsSecureCoding];
```

## Instance methods

```
-[TUConversationHandoffContext init];
-[TUConversationHandoffContext presentationContext];
-[TUConversationHandoffContext setPresentationContext:];
-[TUConversationHandoffContext setPrefersToPlayDuringWombat:];
-[TUConversationHandoffContext encodeWithCoder:];
-[TUConversationHandoffContext hash];
-[TUConversationHandoffContext description];
-[TUConversationHandoffContext initWithCoder:];
-[TUConversationHandoffContext copyWithZone:];
-[TUConversationHandoffContext prefersToPlayDuringWombat];
-[TUConversationHandoffContext isEqual:];
-[TUConversationHandoffContext invitationPreferences];
-[TUConversationHandoffContext isEqualToHandoffContext:];
-[TUConversationHandoffContext setInvitationPreferences:];
-[TUConversationHandoffContext setSetUplinkMuted:];
-[TUConversationHandoffContext setUplinkMuted];
```
