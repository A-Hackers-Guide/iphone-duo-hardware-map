# `SBHUDCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHUDControlling`, `SBWindowSceneAttachmentObserving`
- 1 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _controllersByWindowSceneIdentifier;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_controllersByWindowSceneIdentifier) controllersByWindowSceneIdentifier;
@property (TB,R,N) anyHUDsVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHUDCoordinator init];
-[SBHUDCoordinator windowSceneDidDisconnect:];
-[SBHUDCoordinator windowSceneDidConnect:];
-[SBHUDCoordinator HUDSessionForViewController:identifier:];
-[SBHUDCoordinator _mostActiveHUDController];
-[SBHUDCoordinator acquireHUDHiddenAssertionForIdentifier:withReason:];
-[SBHUDCoordinator anyHUDsVisible];
-[SBHUDCoordinator controllersByWindowSceneIdentifier];
-[SBHUDCoordinator dismissHUDs:];
-[SBHUDCoordinator knownHUDControllerForIdentifier:];
-[SBHUDCoordinator presentedHUDControllerForIdentifier:];
-[SBHUDCoordinator setControllersByWindowSceneIdentifier:];
```
