# `UISSceneHostingExternalSettingsModifierService`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISSceneHostingExternalSettingsModifierXPCServerInterface`, `BSServiceConnectionListenerDelegate`, `BSInvalidatable`
- 6 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BSServiceQueue" _calloutQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
@"BSServiceConnectionListener" _lock_listener;
@"<UISSceneHostingExternalSettingsModifierServiceDelegate>" _lock_delegate;
{?="delegateSupportsSettingsModifiersForClientProcessIdentityHostedByAuditToken"b1} _lock_delegateFlags;
```

## Properties

```
@property (T@"<UISSceneHostingExternalSettingsModifierServiceDelegate>",W,N) delegate;
@property (T@"BSServiceConnectionEndpoint",R,N) endpoint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISSceneHostingExternalSettingsModifierService listener:didReceiveConnection:withContext:];
-[UISSceneHostingExternalSettingsModifierService init];
-[UISSceneHostingExternalSettingsModifierService dealloc];
-[UISSceneHostingExternalSettingsModifierService endpoint];
-[UISSceneHostingExternalSettingsModifierService invalidate];
-[UISSceneHostingExternalSettingsModifierService setDelegate:];
-[UISSceneHostingExternalSettingsModifierService delegate];
-[UISSceneHostingExternalSettingsModifierService requestSettingsModifiersForProcessIdentity:withCompletion:];
-[UISSceneHostingExternalSettingsModifierService initWithCalloutQueue:];
```
