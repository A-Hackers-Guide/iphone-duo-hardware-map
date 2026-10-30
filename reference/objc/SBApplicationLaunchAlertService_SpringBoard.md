# `SBApplicationLaunchAlertService`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBSceneManagerObserver`, `FBSceneObserver`, `BSInvalidatable`
- 7 instance variables, 4 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSSet" _launchAlertEvaluators;
@"SBApplicationController" _applicationController;
@"SBAlertItemsController" _alertItemsController;
@"SBSceneManager" _sceneManager;
@"NSMutableSet" _foregroundingScenes;
@"NSMutableDictionary" _mapBundleIDToLaunchAlertInfo;
B _invalidated;
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
-[SBApplicationLaunchAlertService sceneManager:didAddExternalForegroundApplicationSceneHandle:];
-[SBApplicationLaunchAlertService succinctDescriptionBuilder];
-[SBApplicationLaunchAlertService sceneManager:didRemoveExternalForegroundApplicationSceneHandle:];
-[SBApplicationLaunchAlertService init];
-[SBApplicationLaunchAlertService _sceneDidResignForeground:];
-[SBApplicationLaunchAlertService showLaunchAlertOfType:forApplication:];
-[SBApplicationLaunchAlertService dealloc];
-[SBApplicationLaunchAlertService sceneContentStateDidChange:];
-[SBApplicationLaunchAlertService descriptionWithMultilinePrefix:];
-[SBApplicationLaunchAlertService succinctDescription];
-[SBApplicationLaunchAlertService _sceneWillBecomeForeground:];
-[SBApplicationLaunchAlertService invalidate];
-[SBApplicationLaunchAlertService _reallyShowLaunchAlertOfType:withLaunchAlertInfo:application:];
-[SBApplicationLaunchAlertService _tryShowLaunchAlertsForLaunchAlertInfo:];
-[SBApplicationLaunchAlertService initWithSceneManager:launchAlertEvaluators:applicationController:alertItemsController:];
-[SBApplicationLaunchAlertService description];
-[SBApplicationLaunchAlertService _sceneDidBecomeForeground:];
-[SBApplicationLaunchAlertService _invalidateAndDismissLaunchAlertsForLaunchAlertInfo:];
-[SBApplicationLaunchAlertService descriptionBuilderWithMultilinePrefix:];
```
