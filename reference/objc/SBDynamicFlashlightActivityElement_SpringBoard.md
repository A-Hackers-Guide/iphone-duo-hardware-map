# `SBDynamicFlashlightActivityElement`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSystemApertureContextProviding`, `SBSystemApertureLayoutCustomizing`, `SBSystemApertureSuppressible`, `SBUISystemApertureContentViewContaining`, `SBDynamicFlashlightActivityElementViewControllerDelegate`, `SBSystemApertureGestureCustomizing`, `SBFIdleTimerBehaviorProviding`, `CSExternalBehaviorProviding`, `PTSettingsKeyPathObserver`, `SBSystemApertureContextAccepting`, `SBSystemActionCoordinatedElementPreviewing`, `SAElement`, `SAActivityBehavior`, `SAUIElementViewProviding`, `SAUIContentTransitioning`, `SAUILayoutSpecifying`, `SBSystemActionElementPreviewing`
- 24 instance variables, 60 properties, 91 instance methods, 0 class methods

## Instance variables

```
@"SBSystemActionElementPreviewingCoordinator" _previewingCoordinator;
@"SBDynamicFlashlightActivityElementViewController" _elementViewController;
@"<SAAutomaticallyInvalidatable>" _alertingAssertion;
@"CSCoverSheetViewController" _coverSheetViewController;
@"SBDynamicFlashlightSettings" _flashlightSettings;
Q _obstructionEdge;
B _displayedWithLimitedSize;
B _previewing;
B _urgent;
B _expanding;
B _prominent;
@"<SAActivityHosting>" _activityHost;
@"UIView" _leadingView;
@"UIView" _trailingView;
q _layoutMode;
q _preferredLayoutMode;
@"<SAUILayoutHosting>" _layoutHost;
@"<SAElementHosting>" _elementHost;
@"<SBSystemAperturePlatformElementHosting>" _platformElementHost;
@"<SBSystemApertureGestureHandling>" _gestureHandler;
@"<SBDynamicFlashlightActivityElementDelegate>" _delegate;
@"<SBDynamicFlashlightState>" _flashlightState;
@"SBUISystemApertureCAPackageContentProvider" _leadingPackageViewProvider;
@"SBUISystemApertureTextContentProvider" _trailingTextProvider;
```

## Properties

```
@property (T@"SBUISystemApertureCAPackageContentProvider",R,N,V_leadingPackageViewProvider) leadingPackageViewProvider;
@property (T@"SBUISystemApertureTextContentProvider",R,N,V_trailingTextProvider) trailingTextProvider;
@property (T@"UIView",R,N) customView;
@property (T@"<SBDynamicFlashlightActivityElementDelegate>",W,N,V_delegate) delegate;
@property (T@"<SBDynamicFlashlightState>",&,N,V_flashlightState) flashlightState;
@property (TB,?,R,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
@property (TB,?,N,GisSuppressed) suppressed;
@property (T@"<SBSystemApertureGestureHandling>",W,N,V_gestureHandler) gestureHandler;
@property (Tq,R,N) idleTimerDuration;
@property (Tq,R,N) idleTimerMode;
@property (Tq,R,N) idleWarnMode;
@property (Td,?,R,N) customIdleExpirationTimeout;
@property (Td,?,R,N) customIdleWarningTimeout;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
@property (TB,?,R,N,GisAlerting) alerting;
@property (TB,?,N) elementProviderPrefersSuppression;
@property (TQ,?,N,V_obstructionEdge) obstructionEdge;
@property (TB,R,N,GisPreviewing) previewing;
@property (TB,R,N,GisUrgent) urgent;
@property (TB,R,N,GisExpanding) expanding;
@property (Tq,R,N,V_layoutMode) layoutMode;
@property (T@"<SBSystemAperturePlatformElementHosting>",?,W,N,V_platformElementHost) platformElementHost;
@property (T@"<SAElementHosting>",?,W,N,V_elementHost) elementHost;
@property (T@"NSString",R,C,N) clientIdentifier;
@property (T@"NSString",R,C,N) elementIdentifier;
@property (T@"<SAActivityHosting>",?,W,N,V_activityHost) activityHost;
@property (T@"UIView",R,N,V_leadingView) leadingView;
@property (T@"UIView",R,N,V_trailingView) trailingView;
@property (T@"UIView",R,N) minimalView;
@property (T@"UIView",?,R,N) detachedMinimalView;
@property (T@"<SAElement>",R,W,N) element;
@property (TQ,?,N) layoutAxis;
@property (Tq,R,N) minimumSupportedLayoutMode;
@property (Tq,R,N) maximumSupportedLayoutMode;
@property (Tq,R,N,V_preferredLayoutMode) preferredLayoutMode;
@property (T@"<SAUILayoutHosting>",?,W,N,V_layoutHost) layoutHost;
@property (TB,?,R,N,GisInteractiveDismissalEnabled) interactiveDismissalEnabled;
@property (TB,?,R,N,GisMinimalPresentationPossible) minimalPresentationPossible;
@property (TB,?,R,N,GisRequestingMenuPresentation) requestingMenuPresentation;
@property (TB,?,N,GisDisplayedWithLimitedSize,V_displayedWithLimitedSize) displayedWithLimitedSize;
@property (TB,N,GisProminent,V_prominent) prominent;
```

## Instance methods

```
-[SBDynamicFlashlightActivityElement pop];
-[SBDynamicFlashlightActivityElement setDisplayedWithLimitedSize:];
-[SBDynamicFlashlightActivityElement systemApertureLayoutCustomizingOptions];
-[SBDynamicFlashlightActivityElement layoutHost];
-[SBDynamicFlashlightActivityElement keyColor];
-[SBDynamicFlashlightActivityElement minimalView];
-[SBDynamicFlashlightActivityElement customView];
-[SBDynamicFlashlightActivityElement trailingView];
-[SBDynamicFlashlightActivityElement overridesConcentricPaddingForView:inLayoutMode:];
-[SBDynamicFlashlightActivityElement setLayoutMode:reason:];
-[SBDynamicFlashlightActivityElement setGestureHandler:];
-[SBDynamicFlashlightActivityElement concentricPaddingOverrideForView:inLayoutMode:];
-[SBDynamicFlashlightActivityElement layoutMode];
-[SBDynamicFlashlightActivityElement leadingView];
-[SBDynamicFlashlightActivityElement setLayoutHost:];
-[SBDynamicFlashlightActivityElement systemApertureCustomLayout];
-[SBDynamicFlashlightActivityElement isUrgent];
-[SBDynamicFlashlightActivityElement conformsToCSBehaviorProviding];
-[SBDynamicFlashlightActivityElement clientIdentifier];
-[SBDynamicFlashlightActivityElement isProvidedViewConcentric:inLayoutMode:];
-[SBDynamicFlashlightActivityElement element];
-[SBDynamicFlashlightActivityElement preferredSystemClipPadding];
-[SBDynamicFlashlightActivityElement preferredLayoutMode];
-[SBDynamicFlashlightActivityElement preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBDynamicFlashlightActivityElement obstructionEdge];
-[SBDynamicFlashlightActivityElement isDisplayedWithLimitedSize];
-[SBDynamicFlashlightActivityElement elementIdentifier];
-[SBDynamicFlashlightActivityElement viewProvider];
-[SBDynamicFlashlightActivityElement shouldSuppressElementWhileOnContinuityDisplay];
-[SBDynamicFlashlightActivityElement dealloc];
-[SBDynamicFlashlightActivityElement idleTimerDuration];
-[SBDynamicFlashlightActivityElement proximityDetectionMode];
-[SBDynamicFlashlightActivityElement setObstructionEdge:];
-[SBDynamicFlashlightActivityElement setPlatformElementHost:];
-[SBDynamicFlashlightActivityElement _canShowWhileLocked];
-[SBDynamicFlashlightActivityElement setDelegate:];
-[SBDynamicFlashlightActivityElement activityHost];
-[SBDynamicFlashlightActivityElement elementHost];
-[SBDynamicFlashlightActivityElement scrollingStrategy];
-[SBDynamicFlashlightActivityElement notificationBehavior];
-[SBDynamicFlashlightActivityElement isMinimalPresentationPossible];
-[SBDynamicFlashlightActivityElement delegate];
-[SBDynamicFlashlightActivityElement minimumSupportedLayoutMode];
-[SBDynamicFlashlightActivityElement conformsToCSExternalBehaviorProviding];
-[SBDynamicFlashlightActivityElement shouldSuppressElementWhileOnCoversheet];
-[SBDynamicFlashlightActivityElement gestureHandler];
-[SBDynamicFlashlightActivityElement idleTimerMode];
-[SBDynamicFlashlightActivityElement hasActivityBehavior];
-[SBDynamicFlashlightActivityElement coverSheetIdentifier];
-[SBDynamicFlashlightActivityElement layoutHostContainerViewDidLayoutSubviews:];
-[SBDynamicFlashlightActivityElement setUrgent:];
-[SBDynamicFlashlightActivityElement setProminent:];
-[SBDynamicFlashlightActivityElement contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBDynamicFlashlightActivityElement isProminent];
-[SBDynamicFlashlightActivityElement setActivityHost:];
-[SBDynamicFlashlightActivityElement isPreviewing];
-[SBDynamicFlashlightActivityElement idleWarnMode];
-[SBDynamicFlashlightActivityElement participantState];
-[SBDynamicFlashlightActivityElement settings:changedValueForKeyPath:];
-[SBDynamicFlashlightActivityElement setElementHost:];
-[SBDynamicFlashlightActivityElement maximumSupportedLayoutMode];
-[SBDynamicFlashlightActivityElement setPreviewing:];
-[SBDynamicFlashlightActivityElement elementOrientation];
-[SBDynamicFlashlightActivityElement platformElementHost];
-[SBDynamicFlashlightActivityElement restrictedCapabilities];
-[SBDynamicFlashlightActivityElement isExpanding];
-[SBDynamicFlashlightActivityElement setExpanding:];
-[SBDynamicFlashlightActivityElement preferredContentSizeDidInvalidateForContentViewProvider:];
-[SBDynamicFlashlightActivityElement trailingTextProvider];
-[SBDynamicFlashlightActivityElement flashlightState];
-[SBDynamicFlashlightActivityElement _alertingAssertionDidInvalidate:withReason:];
-[SBDynamicFlashlightActivityElement _frameForContentViewInContainerView:];
-[SBDynamicFlashlightActivityElement _layoutContentViewInContainerView:];
-[SBDynamicFlashlightActivityElement _leadingPackageStateForState:];
-[SBDynamicFlashlightActivityElement _setCustomViewExpanded:];
-[SBDynamicFlashlightActivityElement _setupContentViewInContainerView:];
-[SBDynamicFlashlightActivityElement _textColorForState:];
-[SBDynamicFlashlightActivityElement _trailingTextForState:];
-[SBDynamicFlashlightActivityElement dynamicFlashlightViewControllerCancelSystemApertureGestureHandlers];
-[SBDynamicFlashlightActivityElement dynamicFlashlightViewControllerDidChangeIntensity:width:animated:];
-[SBDynamicFlashlightActivityElement dynamicFlashlightViewControllerDidChangePreferredContentRect];
-[SBDynamicFlashlightActivityElement dynamicFlashlightViewControllerDidToggleFlashlight];
-[SBDynamicFlashlightActivityElement dynamicFlashlightViewControllerShouldDismiss];
-[SBDynamicFlashlightActivityElement dynamicFlashlightViewControllerUpdatePersistedIntensity:width:];
-[SBDynamicFlashlightActivityElement inhibitSystemLongPressGesture];
-[SBDynamicFlashlightActivityElement inhibitSystemPanGesture];
-[SBDynamicFlashlightActivityElement initWithState:coverSheetViewController:fixedWidth:];
-[SBDynamicFlashlightActivityElement leadingPackageViewProvider];
-[SBDynamicFlashlightActivityElement setFlashlightState:];
-[SBDynamicFlashlightActivityElement shouldRemainActiveWhileFlashlightIsOff];
-[SBDynamicFlashlightActivityElement takeAlertingAssertionWithReason:];
```
