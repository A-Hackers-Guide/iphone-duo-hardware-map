# `TUConversationInvitationPreference`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 10 instance methods, 10 class methods

## Instance variables

```
q _handleType;
q _notificationStyles;
```

## Properties

```
@property (Tq,R,N,V_handleType) handleType;
@property (Tq,R,N,V_notificationStyles) notificationStyles;
```

## Class methods

```
+[TUConversationInvitationPreference supportsSecureCoding];
+[TUConversationInvitationPreference letMeInResponseInvitationPreferences];
+[TUConversationInvitationPreference screenShareRequestInvitationPreferences];
+[TUConversationInvitationPreference invitationPreferencesForAllHandlesWithStyles:];
+[TUConversationInvitationPreference incomingCallInvitationPreferences];
+[TUConversationInvitationPreference nearbyInvitationPreferences];
+[TUConversationInvitationPreference standardInvitationPreferencesForLink];
+[TUConversationInvitationPreference incomingCallAndNotificationInvitationPreferences];
+[TUConversationInvitationPreference noNotificationInvitationPreferences];
+[TUConversationInvitationPreference validateNotificationStyles:];
```

## Instance methods

```
-[TUConversationInvitationPreference initWithHandleType:notificationStyles:];
-[TUConversationInvitationPreference encodeWithCoder:];
-[TUConversationInvitationPreference isEqualToInvitationPreference:];
-[TUConversationInvitationPreference hash];
-[TUConversationInvitationPreference description];
-[TUConversationInvitationPreference initWithCoder:];
-[TUConversationInvitationPreference copyWithZone:];
-[TUConversationInvitationPreference isEqual:];
-[TUConversationInvitationPreference notificationStyles];
-[TUConversationInvitationPreference handleType];
```
