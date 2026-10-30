# `SBControlCenterCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBControlCenterCoordinating`, `SBControlCenterPresenting`, `CCSControlCenterOperationServiceContextProviding`
- 9 instance variables, 15 properties, 41 instance methods, 2 class methods

## Instance variables

```
@"SBControlCenterDefaults" _controlCenterDefaults;
@"CCUIMainViewControllerFactory" _viewControllerFactory;
@"SBSensorActivityDataProvider" _sensorActivityDataProvider;
@"CCUISystemControlsCoordinator" _systemControlsCoordinator;
@"NSHashTable" _observers;
@"NSMapTable" _controllersByWindowSceneIdentifier;
@"SBControlCenterController" _embeddedDisplayControlCenterController;
@"SBControlCenterController" _swapTargetControlCenterController;
@"SBControlCenterController" _swapSourceControlCenterController;
```

## Properties

```
@property (T@"CCUIMainViewControllerFactory",R,N) viewControllerFactory;
@property (T@"SBSensorActivityDataProvider",R,N) sensorActivityDataProvider;
@property (T@"CCUISystemControlsCoordinator",&,N,V_systemControlsCoordinator) systemControlsCoordinator;
@property (T@"NSHashTable",&,N,V_observers) observers;
@property (T@"NSMapTable",&,N,V_controllersByWindowSceneIdentifier) controllersByWindowSceneIdentifier;
@property (T@"SBControlCenterController",&,N,V_embeddedDisplayControlCenterController) embeddedDisplayControlCenterController;
@property (T@"SBControlCenterController",W,N,V_swapTargetControlCenterController) swapTargetControlCenterController;
@property (T@"SBControlCenterController",W,N,V_swapSourceControlCenterController) swapSourceControlCenterController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisPresented) presented;
@property (TB,R,N,GisPresentedOrDismissing) presentedOrDismissing;
@property (TB,R,N,GisVisible) visible;
```

## Class methods

```
+[SBControlCenterCoordinator sharedInstance];
+[SBControlCenterCoordinator sharedInstanceIfExists];
```

## Instance methods

```
-[SBControlCenterCoordinator dismissAnimated:];
-[SBControlCenterCoordinator sensorActivityDataProvider];
-[SBControlCenterCoordinator isPresented];
-[SBControlCenterCoordinator removeObserver:];
-[SBControlCenterCoordinator presentAnimated:completion:];
-[SBControlCenterCoordinator handleMenuButtonTap];
-[SBControlCenterCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBControlCenterCoordinator dealloc];
-[SBControlCenterCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBControlCenterCoordinator dismissAnimated:completion:];
-[SBControlCenterCoordinator isVisible];
-[SBControlCenterCoordinator addObserver:];
-[SBControlCenterCoordinator isPresentedOrDismissing];
-[SBControlCenterCoordinator canBePresented];
-[SBControlCenterCoordinator presentAnimated:];
-[SBControlCenterCoordinator setObservers:];
-[SBControlCenterCoordinator observers];
-[SBControlCenterCoordinator handleIndirectStatusBarAction];
-[SBControlCenterCoordinator viewControllerFactory];
-[SBControlCenterCoordinator beginObservingSystemState];
-[SBControlCenterCoordinator mostPresentableControlCenterWindowScene];
-[SBControlCenterCoordinator _mostPresentableControlCenterController];
-[SBControlCenterCoordinator controllersByWindowSceneIdentifier];
-[SBControlCenterCoordinator dismissControlCenterEverywhereAnimated:];
-[SBControlCenterCoordinator embeddedDisplayControlCenterController];
-[SBControlCenterCoordinator initWithSensorActivityDataProvider:];
-[SBControlCenterCoordinator notifyObserversThatControlCenterController:didDismissOnWindowScene:];
-[SBControlCenterCoordinator notifyObserversThatControlCenterController:didPresentOnWindowScene:];
-[SBControlCenterCoordinator notifyObserversThatControlCenterController:willDismissOnWindowScene:];
-[SBControlCenterCoordinator notifyObserversThatControlCenterController:willPresentOnWindowScene:];
-[SBControlCenterCoordinator presentedControlCenterController];
-[SBControlCenterCoordinator registerControlCenterController:forWindowScene:];
-[SBControlCenterCoordinator setControllersByWindowSceneIdentifier:];
-[SBControlCenterCoordinator setEmbeddedDisplayControlCenterController:];
-[SBControlCenterCoordinator setSwapSourceControlCenterController:];
-[SBControlCenterCoordinator setSwapTargetControlCenterController:];
-[SBControlCenterCoordinator setSystemControlsCoordinator:];
-[SBControlCenterCoordinator swapSourceControlCenterController];
-[SBControlCenterCoordinator swapTargetControlCenterController];
-[SBControlCenterCoordinator systemControlsCoordinator];
-[SBControlCenterCoordinator visibleControlCenterController];
```
