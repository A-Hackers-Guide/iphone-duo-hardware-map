# `SBAppSwitcherSystemService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemServiceServerAppSwitcherDelegate`, `SBWindowSceneAttachmentObserving`
- 5 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"FBServiceClientAuthenticator" _requestAppearanceForHiddenAppAuthenticator;
@"SBApplicationController" _applicationController;
@"SBMainSwitcherControllerCoordinator" _switcherControllerCoordinator;
@"NSHashTable" _commandTabControllers;
@"NSMutableSet" _allowedHiddenBundleIdentifiers;
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
-[SBAppSwitcherSystemService windowSceneDidDisconnect:];
-[SBAppSwitcherSystemService windowSceneDidConnect:];
-[SBAppSwitcherSystemService _addAllowedHiddenBundleIdentifier:];
-[SBAppSwitcherSystemService _registerCommandTabController:];
-[SBAppSwitcherSystemService _removeAllowedHiddenBundleIdentifier:];
-[SBAppSwitcherSystemService _requestAppearanceForHiddenAppWithBundleIdentifier:assertionPort:forClient:withCompletion:];
-[SBAppSwitcherSystemService _unregisterCommandTabController:];
-[SBAppSwitcherSystemService initWithApplicationController:switcherControllerCoordinator:];
-[SBAppSwitcherSystemService systemServiceServer:requestAppearanceForHiddenAppWithBundleIdentifier:assertionPort:forClient:withCompletion:];
-[SBAppSwitcherSystemService systemServiceServer:requestUpdateWindowingMode:forClient:completion:];
-[SBAppSwitcherSystemService systemServiceServer:resetLayoutAttributesForClient:completion:];
```
