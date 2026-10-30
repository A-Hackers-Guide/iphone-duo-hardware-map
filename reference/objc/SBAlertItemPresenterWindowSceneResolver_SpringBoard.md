# `SBAlertItemPresenterWindowSceneResolver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _modalAlertPresenters;
@"SBWindowSceneManager" _windowSceneManager;
```

## Properties

```
@property (T@"NSMapTable",R,&,N,V_modalAlertPresenters) modalAlertPresenters;
@property (T@"SBWindowSceneManager",R,&,N,V_windowSceneManager) windowSceneManager;
```

## Instance methods

```
-[SBAlertItemPresenterWindowSceneResolver windowSceneDidDisconnect:];
-[SBAlertItemPresenterWindowSceneResolver windowSceneManager];
-[SBAlertItemPresenterWindowSceneResolver initWithSharedModalAlertItemPresenter:windowSceneManager:];
-[SBAlertItemPresenterWindowSceneResolver modalAlertPresenters];
-[SBAlertItemPresenterWindowSceneResolver resolvedSharedModalAlertItemPresenterForAlertItem:];
-[SBAlertItemPresenterWindowSceneResolver windowSceneDidConnect:withSharedModalAlertItemPresenter:];
```
