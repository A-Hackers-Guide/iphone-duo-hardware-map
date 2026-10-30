# `TUCallFilterController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<TUCallFilterControllerActions>" _actionsDelegate;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"<TUCallFilterControllerActions>",R,W,N,V_actionsDelegate) actionsDelegate;
@property (TB,R,N) silenceUnknownCallersEnabled;
@property (TB,R,N) silenceUnknownFaceTimeCallersEnabled;
```

## Instance methods

```
-[TUCallFilterController actionsDelegate];
-[TUCallFilterController policyForAddresses:forBundleIdentifier:];
-[TUCallFilterController shouldRestrictAddresses:forBundleIdentifier:completion:];
-[TUCallFilterController queue];
-[TUCallFilterController containsRestrictedHandle:forBundleIdentifier:performSynchronously:];
-[TUCallFilterController shouldRestrictAddresses:forBundleIdentifier:performSynchronously:];
-[TUCallFilterController isUnknownAddress:normalizedAddress:forBundleIdentifier:];
-[TUCallFilterController willRestrictAddresses:forBundleIdentifier:];
-[TUCallFilterController callFilterStatusForDialRequest:];
-[TUCallFilterController addressesToCheckForRestrictionsInConversation:];
-[TUCallFilterController bundleIdentifierForCallProvider:];
-[TUCallFilterController callFilterStatusForHandle:bundleIdentifier:];
-[TUCallFilterController containsRestrictedHandle:forBundleIdentifier:];
-[TUCallFilterController initWithActionsDelegate:serialQueue:];
-[TUCallFilterController isRestrictedExclusivelyByScreenTimeForDialRequest:];
-[TUCallFilterController isUnknownHandle:];
-[TUCallFilterController restrictedContacts:callProvider:];
-[TUCallFilterController shouldRestrictAddresses:completion:];
-[TUCallFilterController shouldRestrictAddresses:forBundleIdentifier:];
-[TUCallFilterController shouldRestrictAddresses:performSynchronously:];
-[TUCallFilterController shouldRestrictConversation:performSynchronously:];
-[TUCallFilterController shouldRestrictDialRequest:];
-[TUCallFilterController shouldRestrictDialRequest:performSynchronously:];
-[TUCallFilterController shouldRestrictJoinConversationRequest:performSynchronously:];
-[TUCallFilterController silenceUnknownCallersEnabled];
-[TUCallFilterController silenceUnknownFaceTimeCallersEnabled];
```
