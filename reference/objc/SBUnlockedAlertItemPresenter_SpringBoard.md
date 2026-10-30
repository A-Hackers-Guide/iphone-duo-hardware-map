# `SBUnlockedAlertItemPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAlertItemPresenter`
- 1 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBAlertItemPresenterWindowSceneResolver" _windowSceneResolver;
```

## Properties

```
@property (T@"SBAlertItemPresenterWindowSceneResolver",&,N,V_windowSceneResolver) windowSceneResolver;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUnlockedAlertItemPresenter windowSceneDidDisconnect:];
-[SBUnlockedAlertItemPresenter canPresentMultipleAlertItemsSimultaneously];
-[SBUnlockedAlertItemPresenter dismissAlertItem:animated:completion:];
-[SBUnlockedAlertItemPresenter initWithSharedModalAlertItemPresenter:windowSceneManager:];
-[SBUnlockedAlertItemPresenter presentAlertItem:animated:completion:];
-[SBUnlockedAlertItemPresenter presentsAlertItemsModally];
-[SBUnlockedAlertItemPresenter setWindowSceneResolver:];
-[SBUnlockedAlertItemPresenter windowSceneDidConnect:withSharedModalAlertItemPresenter:];
-[SBUnlockedAlertItemPresenter windowSceneResolver];
```
