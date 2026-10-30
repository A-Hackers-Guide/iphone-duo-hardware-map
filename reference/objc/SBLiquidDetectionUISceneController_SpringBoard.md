# `SBLiquidDetectionUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- Protocols: `SBFLiquidDetectionBlockProvider`
- 6 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<BSInvalidatable>" _suppressSystemGestures;
@"<BSInvalidatable>" _suppressSystemAperture;
@"<BSInvalidatable>" _disableIdleTimer;
B _presenting;
@"NSHashTable" _observers;
@"SBFDeviceLockOutController" _lockOutController;
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
+[SBLiquidDetectionUISceneController _setupInfo];
```

## Instance methods

```
-[SBLiquidDetectionUISceneController initWithSceneWorkspaceIdentifier:clientProcessIdentity:sceneVendingPolicy:traitsRole:jobLabel:level:];
-[SBLiquidDetectionUISceneController dealloc];
-[SBLiquidDetectionUISceneController scenePresenter:willDismissScene:];
-[SBLiquidDetectionUISceneController scenePresenter:didPresentScene:];
-[SBLiquidDetectionUISceneController _isDefaultPresenterDelegate];
-[SBLiquidDetectionUISceneController _newSceneControllerForWindowScene:sceneRequestOptions:traitsRole:level:];
-[SBLiquidDetectionUISceneController addLiquidDetectionObserver:];
-[SBLiquidDetectionUISceneController isLiquidDetectionBlocked];
-[SBLiquidDetectionUISceneController removeLiquidDetectionObserver:];
```
