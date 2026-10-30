# `TUContinuitySessionInfo`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 8 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _isDedicatedSession;
@"TUNearbyDeviceHandle" _device;
@"NSArray" _calls;
@"NSArray" _activeConversations;
@"NSArray" _recentCalls;
@"NSDictionary" _recentCallsContacts;
@"NSArray" _conversationLinks;
@"NSArray" _favorites;
```

## Properties

```
@property (T@"TUNearbyDeviceHandle",R,N,V_device) device;
@property (T@"NSArray",R,N,V_calls) calls;
@property (T@"NSArray",R,N,V_activeConversations) activeConversations;
@property (T@"NSArray",R,N,V_recentCalls) recentCalls;
@property (T@"NSDictionary",R,N,V_recentCallsContacts) recentCallsContacts;
@property (T@"NSArray",R,N,V_conversationLinks) conversationLinks;
@property (TB,R,N,V_isDedicatedSession) isDedicatedSession;
@property (T@"NSArray",R,N,V_favorites) favorites;
```

## Class methods

```
+[TUContinuitySessionInfo supportsSecureCoding];
```

## Instance methods

```
-[TUContinuitySessionInfo calls];
-[TUContinuitySessionInfo activeConversations];
-[TUContinuitySessionInfo device];
-[TUContinuitySessionInfo recentCalls];
-[TUContinuitySessionInfo encodeWithCoder:];
-[TUContinuitySessionInfo description];
-[TUContinuitySessionInfo initWithCoder:];
-[TUContinuitySessionInfo copyWithZone:];
-[TUContinuitySessionInfo conversationLinks];
-[TUContinuitySessionInfo favorites];
-[TUContinuitySessionInfo initWithDevice:calls:activeConversations:favorites:];
-[TUContinuitySessionInfo initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:conversationLinks:];
-[TUContinuitySessionInfo initWithDevice:calls:activeConversations:recentCalls:recentCallsContacts:isDedicatedSession:favorites:conversationLinks:recentCallsInfos:callBlockedStates:];
-[TUContinuitySessionInfo isDedicatedSession];
-[TUContinuitySessionInfo recentCallsContacts];
```
