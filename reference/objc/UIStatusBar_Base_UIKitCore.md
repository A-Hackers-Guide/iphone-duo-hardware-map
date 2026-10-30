# `UIStatusBar_Base`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIScrollsToTopInitiatorView`
- Protocols: `UIStatusBarServerClient`, `UIStatusBarStateObserver`
- 27 instance variables, 33 properties, 138 instance methods, 11 class methods

## Instance variables

```
B _persistentAnimationsEnabled;
B _foreground;
B _hidden;
B _registered;
B _serverUpdatesDisabled;
B _suppressesHiddenSideEffects;
B _homeItemsDisabled;
B _disablesRasterization;
@"<UIStatusBarStyleDelegate>" _styleDelegate;
@"<UIStatusBarCarPlayDockDataProviding>" _dockDataProvider;
Q _styleOverrides;
@"UIStatusBarWindow" _statusBarWindow;
q _orientation;
@"UIStatusBarServer" _statusBarServer;
@"<UIStatusBarStateProvider>" _inProcessStateProvider;
^{?=[46B]b1b1b1b1b1b1b1b1b2b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Ib1b1b1b1b1b1b1b1{?=[46B][64c][64c][256c]iiii[100c][100c][100c][100c][2[100c]][1024c]IIb1b1iib1IIiI[150c]iib1b1b1[256c]b1b1b1b2b2b1Ib1b1b1[256c][256c][100c]b1b1b1b1b1db1b1b1[100c][100c][256c][256c][100c][100c]b2b2I[100c]}} _localDataOverrides;
q _requestedStyle;
@"<UIViewControllerTransitionCoordinator>" __transitionCoordinator;
@"UIColor" _foregroundColor;
q _legibilityStyle;
@"UIStatusBarStyleRequest" _styleRequest;
Q _activeStyleOverride;
q _mode;
@"NSArray" _enabledPartIdentifiers;
@"NSArray" _disabledPartIdentifiers;
@"<UIStatusBarManager>" _manager;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _avoidanceFrame;
```

## Properties

```
@property (T@"UIStatusBarServer",&,N,V_statusBarServer) statusBarServer;
@property (TB,N,V_foreground) foreground;
@property (TB,N,V_hidden) hidden;
@property (TB,N,V_registered) registered;
@property (T@"<UIStatusBarStateProvider>",&,N,V_inProcessStateProvider) inProcessStateProvider;
@property (T^{?=[46B]b1b1b1b1b1b1b1b1b2b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1Ib1b1b1b1b1b1b1b1{?=[46B][64c][64c][256c]iiii[100c][100c][100c][100c][2[100c]][1024c]IIb1b1iib1IIiI[150c]iib1b1b1[256c]b1b1b1b2b2b1Ib1b1b1[256c][256c][100c]b1b1b1b1b1db1b1b1[100c][100c][256c][256c][100c][100c]b2b2I[100c]}},R,N,V_localDataOverrides) localDataOverrides;
@property (TB,N,V_serverUpdatesDisabled) serverUpdatesDisabled;
@property (Tq,N,G_requestStyle,S_setRequestedStyle:,V_requestedStyle) requestedStyle;
@property (T@"<UIViewControllerTransitionCoordinator>",W,N,V__transitionCoordinator) _transitionCoordinator;
@property (TB,N,V_suppressesHiddenSideEffects) suppressesHiddenSideEffects;
@property (TB,N,V_homeItemsDisabled) homeItemsDisabled;
@property (TB,N,S_setDisablesRasterization:,V_disablesRasterization) disablesRasterization;
@property (T@"UIColor",&,N,V_foregroundColor) foregroundColor;
@property (Tq,N,V_legibilityStyle) legibilityStyle;
@property (T@"UIStatusBarStyleRequest",C,N,V_styleRequest) styleRequest;
@property (TQ,N,V_activeStyleOverride) activeStyleOverride;
@property (Tq,N,V_mode) mode;
@property (T@"NSArray",C,N,V_enabledPartIdentifiers) enabledPartIdentifiers;
@property (T@"NSArray",C,N,V_disabledPartIdentifiers) disabledPartIdentifiers;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_avoidanceFrame) avoidanceFrame;
@property (T@"<UIStatusBarManager>",W,N,V_manager) manager;
@property (T@"UIView",W,N) sensorActivityIndicator;
@property (T@"UIFont",R,N) clockFont;
@property (T@"<UIStatusBarStyleDelegate>",W,N,V_styleDelegate) styleDelegate;
@property (T@"<UIStatusBarCarPlayDockDataProviding>",W,N,V_dockDataProvider) dockDataProvider;
@property (T@"UIStatusBarWindow",R,W,N,V_statusBarWindow) statusBarWindow;
@property (TB,N,V_persistentAnimationsEnabled) persistentAnimationsEnabled;
@property (TQ,R,N,V_styleOverrides) styleOverrides;
@property (Tq,N,V_orientation) orientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIStatusBar_Base _implementationClass];
+[UIStatusBar_Base _defaultStyleForRequestedStyle:styleOverrides:activeStyleOverride:];
+[UIStatusBar_Base _heightForStyle:orientation:forStatusBarFrame:inWindow:isAzulBLinked:];
+[UIStatusBar_Base _defaultStyleForRequestedStyle:styleOverrides:];
+[UIStatusBar_Base _frameInSceneReferenceSpaceForStyle:orientation:inSceneWithReferenceSize:];
+[UIStatusBar_Base _heightForStyle:orientation:forStatusBarFrame:inWindow:];
+[UIStatusBar_Base _setImplementationClass:];
+[UIStatusBar_Base _viewControllerAdjustmentForOrientation:inWindow:];
+[UIStatusBar_Base heightForStyle:orientation:];
+[UIStatusBar_Base heightForStyle:orientation:inWindow:];
+[UIStatusBar_Base heightForStyle:orientation:inWindow:isAzulBLinked:];
```

## Instance methods

```
-[UIStatusBar_Base alphaForPartWithIdentifier:];
-[UIStatusBar_Base forceUpdate:];
-[UIStatusBar_Base frameForPartWithIdentifier:];
-[UIStatusBar_Base setOffset:forPartWithIdentifier:];
-[UIStatusBar_Base setForegroundColor:];
-[UIStatusBar_Base setHidden:animationParameters:];
-[UIStatusBar_Base setOrientation:];
-[UIStatusBar_Base setEnabledPartIdentifiers:];
-[UIStatusBar_Base jiggleLockIcon];
-[UIStatusBar_Base currentStyle];
-[UIStatusBar_Base disabledPartIdentifiers];
-[UIStatusBar_Base setForegroundColor:animationParameters:];
-[UIStatusBar_Base setRegistered:];
-[UIStatusBar_Base _willEnterForeground:];
-[UIStatusBar_Base requestStyle:];
-[UIStatusBar_Base setForeground:];
-[UIStatusBar_Base foreground];
-[UIStatusBar_Base currentHeight];
-[UIStatusBar_Base intrinsicContentSize];
-[UIStatusBar_Base setHidden:];
-[UIStatusBar_Base defaultHeight];
-[UIStatusBar_Base setManager:];
-[UIStatusBar_Base actionForPartWithIdentifier:];
-[UIStatusBar_Base orientation];
-[UIStatusBar_Base setAction:forPartWithIdentifier:];
-[UIStatusBar_Base _getStyle:andActiveOverride:forRequestedStyle:];
-[UIStatusBar_Base dealloc];
-[UIStatusBar_Base statusBarServer:didReceiveGlowAnimationState:forStyle:];
-[UIStatusBar_Base setLegibilityStyle:];
-[UIStatusBar_Base manager];
-[UIStatusBar_Base setSensorActivityIndicator:];
-[UIStatusBar_Base _requestStyle:partStyles:animationParameters:forced:];
-[UIStatusBar_Base forceUpdateData:];
-[UIStatusBar_Base setAlpha:forPartWithIdentifier:];
-[UIStatusBar_Base setMode:];
-[UIStatusBar_Base activeTintColor];
-[UIStatusBar_Base setForegroundAlpha:animationParameters:];
-[UIStatusBar_Base isHidden];
-[UIStatusBar_Base setAlpha:];
-[UIStatusBar_Base setTintColor:];
-[UIStatusBar_Base offsetForPartWithIdentifier:];
-[UIStatusBar_Base setAvoidanceFrame:animationSettings:options:];
-[UIStatusBar_Base avoidanceFrame];
-[UIStatusBar_Base _transitionCoordinator];
-[UIStatusBar_Base legibilityStyle];
-[UIStatusBar_Base mode];
-[UIStatusBar_Base isTranslucent];
-[UIStatusBar_Base registered];
-[UIStatusBar_Base statusBarServer:didReceiveDoubleHeightStatusString:forStyle:];
-[UIStatusBar_Base sensorActivityIndicator];
-[UIStatusBar_Base _didEnterBackground:];
-[UIStatusBar_Base setDisabledPartIdentifiers:];
-[UIStatusBar_Base statusBarServer:didReceiveStatusBarData:withActions:];
-[UIStatusBar_Base clockFont];
-[UIStatusBar_Base foregroundColor];
-[UIStatusBar_Base statusBarWindow];
-[UIStatusBar_Base didMoveToSuperview];
-[UIStatusBar_Base statusBarServer:didReceiveStyleOverrides:];
-[UIStatusBar_Base initWithFrame:];
-[UIStatusBar_Base setStyleRequest:animationParameters:];
-[UIStatusBar_Base setLegibilityStyle:animationParameters:];
-[UIStatusBar_Base setAvoidanceFrame:];
-[UIStatusBar_Base statusBarStateProvider:didPostStatusBarData:withActions:];
-[UIStatusBar_Base enabledPartIdentifiers];
-[UIStatusBar_Base _initWithFrame:showForegroundView:wantsServer:inProcessStateProvider:];
-[UIStatusBar_Base defaultDoubleHeight];
-[UIStatusBar_Base hidden];
-[UIStatusBar_Base _setHidden:animationParameters:];
-[UIStatusBar_Base setEnabledCenterItems:duration:];
-[UIStatusBar_Base setSuppressesHiddenSideEffects:];
-[UIStatusBar_Base setPersistentAnimationsEnabled:];
-[UIStatusBar_Base statusBarServer];
-[UIStatusBar_Base _canShowInOrientation:];
-[UIStatusBar_Base _clearOverrideHeight];
-[UIStatusBar_Base _evaluateServerRegistration];
-[UIStatusBar_Base _hiddenAlphaForHideAnimationParameters:];
-[UIStatusBar_Base _hiddenTransformForHideAnimationParameters:];
-[UIStatusBar_Base _isTransparent];
-[UIStatusBar_Base _noteStyleOverridesChangedLocally];
-[UIStatusBar_Base _performAnimations:withParameters:completion:];
-[UIStatusBar_Base _performBlockWhileIgnoringForegroundViewChanges:];
-[UIStatusBar_Base _rectIntersectsTimeItem:];
-[UIStatusBar_Base _requestStyle];
-[UIStatusBar_Base _setDisablesRasterization:];
-[UIStatusBar_Base _setOverrideHeight:];
-[UIStatusBar_Base _setRequestedStyle:];
-[UIStatusBar_Base _shouldSeekHigherPriorityTouchTarget];
-[UIStatusBar_Base _statusBarDidAnimateRotation];
-[UIStatusBar_Base _statusBarWillAnimateRotation];
-[UIStatusBar_Base _styleOverridesDidChange:];
-[UIStatusBar_Base _usesModernBar];
-[UIStatusBar_Base activeStyleOverride];
-[UIStatusBar_Base animateUnlock];
-[UIStatusBar_Base currentFrame];
-[UIStatusBar_Base disablesRasterization];
-[UIStatusBar_Base dockDataProvider];
-[UIStatusBar_Base forceUpdateDoubleHeightStatus];
-[UIStatusBar_Base forceUpdateStyleOverrides:];
-[UIStatusBar_Base forceUpdateToData:animated:];
-[UIStatusBar_Base forgetEitherSideHistory];
-[UIStatusBar_Base frameForOrientation:];
-[UIStatusBar_Base heightForOrientation:];
-[UIStatusBar_Base heightForOrientation:isAzulBLinked:];
-[UIStatusBar_Base homeItemsDisabled];
-[UIStatusBar_Base inProcessStateProvider];
-[UIStatusBar_Base initWithFrame:showForegroundView:];
-[UIStatusBar_Base initWithFrame:showForegroundView:inProcessStateProvider:];
-[UIStatusBar_Base isDoubleHeight];
-[UIStatusBar_Base localDataOverrides];
-[UIStatusBar_Base persistentAnimationsEnabled];
-[UIStatusBar_Base requestStyle:animated:];
-[UIStatusBar_Base requestStyle:animated:forced:];
-[UIStatusBar_Base requestStyle:animation:startTime:duration:curve:];
-[UIStatusBar_Base requestStyle:animationParameters:];
-[UIStatusBar_Base requestStyle:animationParameters:forced:];
-[UIStatusBar_Base requestStyle:partStyles:animationParameters:forced:];
-[UIStatusBar_Base serverUpdatesDisabled];
-[UIStatusBar_Base setActiveStyleOverride:];
-[UIStatusBar_Base setAvoidanceFrame:animationSettings:];
-[UIStatusBar_Base setAvoidanceFrame:animationSettings:isInteractive:];
-[UIStatusBar_Base setDockDataProvider:];
-[UIStatusBar_Base setHidden:animated:];
-[UIStatusBar_Base setHomeItemsDisabled:];
-[UIStatusBar_Base setInProcessStateProvider:];
-[UIStatusBar_Base setLocalDataOverrides:];
-[UIStatusBar_Base setServerUpdatesDisabled:];
-[UIStatusBar_Base setShowsOnlyCenterItems:];
-[UIStatusBar_Base setStatusBarServer:];
-[UIStatusBar_Base setStyleDelegate:];
-[UIStatusBar_Base setStyleRequest:];
-[UIStatusBar_Base setTintColor:withDuration:];
-[UIStatusBar_Base set_transitionCoordinator:];
-[UIStatusBar_Base showsContentsOnScreen];
-[UIStatusBar_Base styleDelegate];
-[UIStatusBar_Base styleForRequestedStyle:];
-[UIStatusBar_Base styleOverrides];
-[UIStatusBar_Base styleRequest];
-[UIStatusBar_Base suppressesHiddenSideEffects];
```
