# `SBModalAlertPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `FBSceneObserver`
- 6 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"SBModalAlertPresentationCoordinator" _modalAlertPresentationCoordinator;
@"FBScene" _scene;
Q _visibleModalAlertCount;
B _invalidated;
B _isSystemPresenter;
@"NSHashTable" _visibleAlertAssertions;
```

## Properties

```
@property (T@"FBScene",&,N,S_setScene:,V_scene) scene;
@property (T@"SBModalAlertPresentationCoordinator",&,N,V_modalAlertPresentationCoordinator) modalAlertPresentationCoordinator;
@property (TB,R,D,N,GisShowingModalAlert) showingModalAlert;
@property (TB,R,D,N,GisForeground) foreground;
@property (TQ,N,V_visibleModalAlertCount) visibleModalAlertCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBModalAlertPresenter setModalAlertPresentationCoordinator:];
-[SBModalAlertPresenter visibleModalAlertCount];
-[SBModalAlertPresenter isShowingModalAlert];
-[SBModalAlertPresenter succinctDescriptionBuilder];
-[SBModalAlertPresenter acquireVisibleModalAlertAssertionWithDescription:];
-[SBModalAlertPresenter scene:didUpdateSettings:];
-[SBModalAlertPresenter dealloc];
-[SBModalAlertPresenter _addOrRemoveModalAlertPresenterIfNecessary];
-[SBModalAlertPresenter _initWithModalAlertPresentationCoordinator:scene:];
-[SBModalAlertPresenter descriptionWithMultilinePrefix:];
-[SBModalAlertPresenter isForeground];
-[SBModalAlertPresenter initWithScene:];
-[SBModalAlertPresenter succinctDescription];
-[SBModalAlertPresenter invalidate];
-[SBModalAlertPresenter scene];
-[SBModalAlertPresenter incrementVisibleModalAlertCount];
-[SBModalAlertPresenter description];
-[SBModalAlertPresenter initForSystemApplication];
-[SBModalAlertPresenter _setScene:];
-[SBModalAlertPresenter decrementVisibleModalAlertCount];
-[SBModalAlertPresenter modalAlertPresentationCoordinator];
-[SBModalAlertPresenter _addOrRemoveModalAlertPresenterIfNecessaryWithForegroundState:fromOrToTerminalState:];
-[SBModalAlertPresenter descriptionBuilderWithMultilinePrefix:];
-[SBModalAlertPresenter setVisibleModalAlertCount:];
```
