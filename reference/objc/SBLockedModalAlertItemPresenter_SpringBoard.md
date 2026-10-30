# `SBLockedModalAlertItemPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlertItemPresenter`, `SBFLockScreenActionProvider`
- 2 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBAlertItemPresenterWindowSceneResolver" _windowSceneResolver;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
```

## Properties

```
@property (T@"SBAlertItemPresenterWindowSceneResolver",&,N,V_windowSceneResolver) windowSceneResolver;
@property (T@"SBLockScreenCoordinator",&,N,V_lockScreenCoordinator) lockScreenCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLockedModalAlertItemPresenter windowSceneDidDisconnect:];
-[SBLockedModalAlertItemPresenter lockScreenCoordinator];
-[SBLockedModalAlertItemPresenter setLockScreenCoordinator:];
-[SBLockedModalAlertItemPresenter lockScreenActionContext];
-[SBLockedModalAlertItemPresenter canPresentMultipleAlertItemsSimultaneously];
-[SBLockedModalAlertItemPresenter dismissAlertItem:animated:completion:];
-[SBLockedModalAlertItemPresenter initWithSharedModalAlertItemPresenter:windowSceneManager:lockScreenCoordinator:];
-[SBLockedModalAlertItemPresenter presentAlertItem:animated:completion:];
-[SBLockedModalAlertItemPresenter presentsAlertItemsModally];
-[SBLockedModalAlertItemPresenter setWindowSceneResolver:];
-[SBLockedModalAlertItemPresenter windowSceneDidConnect:withSharedModalAlertItemPresenter:];
-[SBLockedModalAlertItemPresenter windowSceneResolver];
```
