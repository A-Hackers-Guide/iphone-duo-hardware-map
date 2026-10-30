# `UISSceneHostingExternalSettingsModifierClient`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"BSServiceConnectionEndpoint" _endpoint;
@"NSObject<OS_dispatch_queue>" _queue;
B _queue_invalidated;
@"BSServiceConnection" _queue_connection;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISSceneHostingExternalSettingsModifierClient defaultShellEndpoint];
```

## Instance methods

```
-[UISSceneHostingExternalSettingsModifierClient init];
-[UISSceneHostingExternalSettingsModifierClient dealloc];
-[UISSceneHostingExternalSettingsModifierClient invalidate];
-[UISSceneHostingExternalSettingsModifierClient initWithServerEndpoint:];
-[UISSceneHostingExternalSettingsModifierClient requestSettingsModifiersForProcessIdentity:withCompletion:];
```
