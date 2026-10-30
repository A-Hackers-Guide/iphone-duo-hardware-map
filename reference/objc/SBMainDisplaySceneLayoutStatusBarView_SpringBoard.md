# `SBMainDisplaySceneLayoutStatusBarView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyObserver`, `UIStatusBarStyleDelegate_SpringBoardOnly`, `SBDeviceApplicationSceneStatusBarStateObserver`
- 22 instance variables, 9 properties, 72 instance methods, 0 class methods

## Instance variables

```
@"BSUIOrientationTransformWrapperView" _statusBarContainerView;
@"UIView" _statusBarWrapperView;
@"UIStatusBar" _statusBar;
@"SBStatusBarReusePool" _statusBarReusePool;
@"_UIStatusBar" _statusBarUnderlyingViewAccessor;
@"NSMutableSet" _statusBarRequiringReasons;
@"NSMutableDictionary" _partIdentifiersDefaultStyles;
@"NSMutableDictionary" _partIdentifiersCustomStyles;
@"NSMutableDictionary" _hitTestLayers;
@"NSString" _statusBarBreadcrumbSceneIdentifier;
B _statusBarLaidOutForClassic;
B _lastHiddenValueForAnimation;
@"UITapGestureRecognizer" _statusBarSingleTapGestureRecognizer;
@"UITapGestureRecognizer" _showDebugGestureRecognizer;
@"SBMedusaSettings" _medusaSettings;
B _debugBackgroundColorEnabled;
B _debugOffsetEnabled;
Q _debugOffsetIndex;
@"UIColor" _debugBackgroundColor;
{?="styleDelegateWants_statusBar_styleForRequestedStyle_overrides"b1"styleDelegateWants_statusBar_willAnimateFromHeight_toHeight_duration_animation"b1"styleDelegateWants_statusBar_didAnimateFromHeight_toHeight_animation"b1"styleDelegateWants_statusBarSystemNavigationAction"b1"styleDelegateWants_statusBar_didTriggerButtonType_withAction"b1"styleDelegateWants_statusBar_didTriggerButtonType_withAction_context"b1"styleDelegateWants_statusBar_effectiveStyleOverridesForRequestedStyle_overrides"b1"styleDelegateWants_overriddenRequestedStyleFromStyle"b1"dataSourceWants_statusBarPartsForSceneWithIdentifier"b1"dataSourceWants_currentlyValidStatusBarPartIdentifiers"b1"dataSourceWants_statusBarDescriberAtPoint_inView_pointInSceneLayoutSpace"b1"dataSourceWants_frameForSceneIdentifier_inView"b1"dataSourceWants_statusBarAvoidanceFrame"b1} _conformanceFlags;
@"<SBMainDisplaySceneLayoutStatusBarViewDataSource>" _dataSource;
@"<UIStatusBarStyleDelegate_SpringBoardOnly>" _realStyleDelegate;
```

## Properties

```
@property (T@"<UIStatusBarStyleDelegate_SpringBoardOnly>",W,N,V_realStyleDelegate) realStyleDelegate;
@property (TB,R,N,GisRequiringStatusBar) requiringStatusBar;
@property (TB,R,N,GisStatusBarEffectivelyHidden) statusBarEffectivelyHidden;
@property (T@"<SBMainDisplaySceneLayoutStatusBarViewDataSource>",W,N,V_dataSource) dataSource;
@property (Tq,N) containerOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeBackgroundActivitiesToSuppressTo:];
-[SBMainDisplaySceneLayoutStatusBarView endRequiringStatusBarForReason:];
-[SBMainDisplaySceneLayoutStatusBarView _setDebugOffsetIndex:];
-[SBMainDisplaySceneLayoutStatusBarView containerOrientation];
-[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeStatusBarAlphaTo:];
-[SBMainDisplaySceneLayoutStatusBarView _statusBarShowDebug:];
-[SBMainDisplaySceneLayoutStatusBarView statusBarSystemNavigationAction:];
-[SBMainDisplaySceneLayoutStatusBarView _setDebugBackgroundColor:];
-[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeStatusBarStyleTo:];
-[SBMainDisplaySceneLayoutStatusBarView _enumerateValidStatusBarPartIdentifiersForSceneWithIdentifier:withBlock:];
-[SBMainDisplaySceneLayoutStatusBarView _applyBackgroundActivitiesToSuppress:toSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView beginRequiringStatusBarForReason:];
-[SBMainDisplaySceneLayoutStatusBarView _statusBarDescriberForPrimaryApplicationIfAny];
-[SBMainDisplaySceneLayoutStatusBarView setContainerOrientation:];
-[SBMainDisplaySceneLayoutStatusBarView _updateDebugBackgroundColor];
-[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeStatusBarStyleTo:forPartWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView _validStatusBarPartIdentifiersForSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView dealloc];
-[SBMainDisplaySceneLayoutStatusBarView _defaultStatusBarStyleRequest];
-[SBMainDisplaySceneLayoutStatusBarView setDataSource:];
-[SBMainDisplaySceneLayoutStatusBarView statusBar:willAnimateFromHeight:toHeight:duration:animation:];
-[SBMainDisplaySceneLayoutStatusBarView _addStatusBarIfNeeded];
-[SBMainDisplaySceneLayoutStatusBarView updateBreadcrumbActionIfNecessary];
-[SBMainDisplaySceneLayoutStatusBarView _applyStatusBarStyle:toPartIdentifier:ofSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView settings:changedValueForKey:];
-[SBMainDisplaySceneLayoutStatusBarView _statusBarFrameForOrientation:];
-[SBMainDisplaySceneLayoutStatusBarView statusBar:styleForRequestedStyle:overrides:];
-[SBMainDisplaySceneLayoutStatusBarView _statusBarSingleTapped:];
-[SBMainDisplaySceneLayoutStatusBarView setRealStyleDelegate:];
-[SBMainDisplaySceneLayoutStatusBarView _applyStatusBarAlpha:toSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView statusBar:didTriggerButtonType:withAction:];
-[SBMainDisplaySceneLayoutStatusBarView _statusBarAvoidanceFrame];
-[SBMainDisplaySceneLayoutStatusBarView _updateHitTestLayers];
-[SBMainDisplaySceneLayoutStatusBarView _applyStatusBarAvoidanceFrame:toSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView layoutStatusBarForSpringBoardRotationToOrientation:];
-[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeStatusBarAvoidanceFrameTo:];
-[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeStatusBarOrientationTo:];
-[SBMainDisplaySceneLayoutStatusBarView dataSource];
-[SBMainDisplaySceneLayoutStatusBarView _allowChangingIndividualStatusBarParts];
-[SBMainDisplaySceneLayoutStatusBarView isStatusBarEffectivelyHidden];
-[SBMainDisplaySceneLayoutStatusBarView _currentlyValidStatusBarPartIdentifiers];
-[SBMainDisplaySceneLayoutStatusBarView _anyAppViewControllerOwningInterfaceOrientation];
-[SBMainDisplaySceneLayoutStatusBarView realStyleDelegate];
-[SBMainDisplaySceneLayoutStatusBarView _effectiveStatusBarStyleOverridesToSuppress];
-[SBMainDisplaySceneLayoutStatusBarView _applyStatusBarStyle:toSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView _sceneHandleForClassicApplicationIfAny];
-[SBMainDisplaySceneLayoutStatusBarView applyStatusBarStylesForDescriber:];
-[SBMainDisplaySceneLayoutStatusBarView createStatusBarWithFrame:interfaceOrientation:reason:];
-[SBMainDisplaySceneLayoutStatusBarView _setupDebugging];
-[SBMainDisplaySceneLayoutStatusBarView _effectiveStyleForPartIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView _updateDebugOffset];
-[SBMainDisplaySceneLayoutStatusBarView _statusBarTapped:type:];
-[SBMainDisplaySceneLayoutStatusBarView _animateHidden:withAnimation:transitionHandler:applyHandler:];
-[SBMainDisplaySceneLayoutStatusBarView _applyStatusBarHidden:withAnimation:toSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView statusBar:didTriggerButtonType:withAction:context:];
-[SBMainDisplaySceneLayoutStatusBarView _reusePool];
-[SBMainDisplaySceneLayoutStatusBarView _tearDownStatusBar];
-[SBMainDisplaySceneLayoutStatusBarView isRequiringStatusBar];
-[SBMainDisplaySceneLayoutStatusBarView didInvalidateStatusBarDescriptionForSceneWithIdentifier:];
-[SBMainDisplaySceneLayoutStatusBarView statusBar:didAnimateFromHeight:toHeight:animation:];
-[SBMainDisplaySceneLayoutStatusBarView sceneWithIdentifier:didChangeStatusBarHiddenTo:withAnimation:];
-[SBMainDisplaySceneLayoutStatusBarView overriddenRequestedStyleFromStyle:];
-[SBMainDisplaySceneLayoutStatusBarView initWithFrame:];
-[SBMainDisplaySceneLayoutStatusBarView _statusBarNeedsSpecialLayoutForClassic];
-[SBMainDisplaySceneLayoutStatusBarView _effectiveBackgroundActivityIdentifiersToSuppress];
-[SBMainDisplaySceneLayoutStatusBarView _hiddenTransformForAnimation:];
-[SBMainDisplaySceneLayoutStatusBarView statusBar:effectiveStyleOverridesForRequestedStyle:overrides:];
-[SBMainDisplaySceneLayoutStatusBarView allValidStatusBarPartIdentifiers];
-[SBMainDisplaySceneLayoutStatusBarView statusBarStyleRequestForStatusBarPart:];
-[SBMainDisplaySceneLayoutStatusBarView _hiddenAlphaForAnimation:];
-[SBMainDisplaySceneLayoutStatusBarView updateStatusBarOrientationForLegacyApp];
-[SBMainDisplaySceneLayoutStatusBarView _layoutStatusBarForOrientation:];
```
