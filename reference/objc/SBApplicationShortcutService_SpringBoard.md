# `SBApplicationShortcutService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationServerShortcutDelegate`
- 7 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBApplicationPlaceholderController" _applicationPlaceholderController;
@"SBIconController" _iconController;
@"SBRecentAppLayouts" _recentAppLayouts;
@"SBWindowSceneManager" _windowSceneManager;
@"FBServiceClientAuthenticator" _serviceClientFullAccessEntitlementAuthenticator;
@"FBServiceClientAuthenticator" _serviceClientCustomImageEntitlementAuthenticator;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationShortcutService _deviceSupportsMultiwindow];
-[SBApplicationShortcutService _authenticateClient:forBundleIdentifier:withCompletionHandler:];
-[SBApplicationShortcutService _checkEntitlementsForClient:withCompletionHandler:];
-[SBApplicationShortcutService _sanitizeApplicationShortcutItems:withEntitlements:];
-[SBApplicationShortcutService applicationServer:client:fetchApplicationShortcutItemsOfTypes:forBundleIdentifier:withCompletion:];
-[SBApplicationShortcutService applicationServer:client:setDynamicApplicationShortcutItems:forBundleIdentifier:];
-[SBApplicationShortcutService initWithApplicationController:applicationPlaceholderController:iconController:recentAppLayouts:windowSceneManager:];
```
