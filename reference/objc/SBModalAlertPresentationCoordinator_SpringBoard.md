# `SBModalAlertPresentationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 8 instance variables, 9 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"<SBModalAlertPresentationCoordinatorDelegate>" _delegate;
@"UIApplicationSceneDeactivationManager" _sceneDeactivationManager;
@"NSMutableSet" _activeModalAlertPresenters;
@"SBModalAlertPresenter" _springBoardModalAlertPresenter;
@"UIApplicationSceneDeactivationAssertion" _systemModalAlertsActiveSceneDeactivationAssertion;
@"NSMutableSet" _hideApplicationModalAlertAssertions;
@"<BSInvalidatable>" _hideApplicationModalAlertsAssertionWhileSBModalAlertsActive;
@"<BSInvalidatable>" _sysdiagnoseStateHandler;
```

## Properties

```
@property (T@"SBModalAlertPresenter",&,N,G_getSpringBoardPresenter,S_setSpringBoardPresenter:,V_springBoardModalAlertPresenter) springBoardPresenter;
@property (T@"<SBModalAlertPresentationCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (TB,R,D,N,GisShowingModalAlert) showingModalAlert;
@property (TB,R,D,N,GisShowingSystemModalAlert) showingSystemModalAlert;
@property (TB,R,D,N,GcanShowApplicationModalAlerts) canShowApplicationModalAlerts;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBModalAlertPresentationCoordinator isShowingModalAlert];
-[SBModalAlertPresentationCoordinator succinctDescriptionBuilder];
-[SBModalAlertPresentationCoordinator descriptionWithMultilinePrefix:];
-[SBModalAlertPresentationCoordinator succinctDescription];
-[SBModalAlertPresentationCoordinator setDelegate:];
-[SBModalAlertPresentationCoordinator delegate];
-[SBModalAlertPresentationCoordinator description];
-[SBModalAlertPresentationCoordinator descriptionBuilderWithMultilinePrefix:];
-[SBModalAlertPresentationCoordinator _addModalAlertPresenterIfNecessary:];
-[SBModalAlertPresentationCoordinator _adjustApplicationSceneSettingsForModalAlertsAndFence:];
-[SBModalAlertPresentationCoordinator _fencingTransitionContext:];
-[SBModalAlertPresentationCoordinator _getSpringBoardPresenter];
-[SBModalAlertPresentationCoordinator _noteSpringBoardModalAlertStateChanged:];
-[SBModalAlertPresentationCoordinator _removeModalAlertPresenter:];
-[SBModalAlertPresentationCoordinator _setSpringBoardPresenter:];
-[SBModalAlertPresentationCoordinator canShowApplicationModalAlerts];
-[SBModalAlertPresentationCoordinator hideApplicationModalAlertsForReason:];
-[SBModalAlertPresentationCoordinator initWithSceneDeactivationManager:];
-[SBModalAlertPresentationCoordinator isShowingSystemModalAlert];
```
