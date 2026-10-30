# `SBLockElementViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivityProvidedContentElement`
- Protocols: `SBUIBiometricResourceObserver`, `SBSystemApertureSuppressible`, `SAElementViewProviding`, `SBSystemApertureLayoutCustomizing`, `SBSystemApertureElementAssertionObserving`, `SBSystemApertureContextAccepting`, `SBSystemApertureContextProviding`, `SAUIContentTransitioning`
- 25 instance variables, 25 properties, 76 instance methods, 2 class methods

## Instance variables

```
@"SBUIBiometricResource" _sharedResource;
B _allowsBioUnlock;
B _isAuthenticated;
B _hasActiveUnlockAttempt;
B _isEmpty;
B _isElementRegistered;
B _isInBloomMode;
B _isAcquiring;
B _matchFailed;
B _earlyMatchingFeedback;
Q _unlockMode;
q _priorLayoutMode;
q _biometrics;
@"SBUIProudLockIconView" _leadingLock;
@"SBLockElementTrailingContentView" _trailingContentView;
@? _pendingShakeBlock;
B _displayedWithLimitedSize;
@"<SAElementHosting>" _elementHost;
q _layoutMode;
@"<SAUILayoutHosting>" _layoutHost;
Q _obstructionEdge;
@"SBWindowScene" _windowScene;
@"SBUISystemApertureContentProvider" _contentProvider;
@"SBUISystemApertureCustomContentProvider" _lockProvider;
@"SBUISystemApertureCustomContentProvider" _trailingPackageProvider;
```

## Properties

```
@property (T@"SBUISystemApertureContentProvider",&,N,V_contentProvider) contentProvider;
@property (T@"SBUISystemApertureCustomContentProvider",&,N,V_lockProvider) lockProvider;
@property (T@"SBUISystemApertureCustomContentProvider",&,N,V_trailingPackageProvider) trailingPackageProvider;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,N,SsetEmpty:,V_isEmpty) isEmpty;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,?,N,GisSuppressed) suppressed;
@property (T@"<SAElement>",R,W,N) element;
@property (Tq,?,R,N) systemApertureCustomLayout;
@property (Tq,?,R,N) customLayoutRequestingSpecialFlowerBoundsResizingAnimation;
@property (Tq,?,R,N) systemApertureLayoutCustomizingOptions;
@property (TB,?,N,GisAffiliatedWithSessionMonitor) affiliatedWithSessionMonitor;
@property (TB,?,R,N,GisAlerting) alerting;
@property (TB,?,N) elementProviderPrefersSuppression;
@property (TQ,?,N,V_obstructionEdge) obstructionEdge;
@property (T@"UIColor",?,R,N) keyColor;
@property (T@"FBScene",?,R,N) scene;
@property (TB,?,R,N) preventsSwipeToHide;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredAvoidanceRect;
@property (Td,?,R,N) preferredAvoidanceCornerRadius;
@property (TB,?,R,N) inhibitsIndicatorMitosis;
@property (Td,?,R,N) preferredSystemClipPadding;
```

## Class methods

```
+[SBLockElementViewProvider _indicatorAllowsSecureRendering];
+[SBLockElementViewProvider deviceSupportsElement];
```

## Instance methods

```
-[SBLockElementViewProvider setDisplayedWithLimitedSize:];
-[SBLockElementViewProvider layoutHost];
-[SBLockElementViewProvider setAuthenticated:];
-[SBLockElementViewProvider setLayoutMode:reason:];
-[SBLockElementViewProvider layoutMode];
-[SBLockElementViewProvider setLayoutHost:];
-[SBLockElementViewProvider systemApertureCustomLayout];
-[SBLockElementViewProvider clientIdentifier];
-[SBLockElementViewProvider isProvidedViewConcentric:inLayoutMode:];
-[SBLockElementViewProvider systemApertureElementAssertionInvalidated];
-[SBLockElementViewProvider element];
-[SBLockElementViewProvider preferredLayoutMode];
-[SBLockElementViewProvider preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:];
-[SBLockElementViewProvider obstructionEdge];
-[SBLockElementViewProvider isDisplayedWithLimitedSize];
-[SBLockElementViewProvider elementIdentifier];
-[SBLockElementViewProvider _effectiveDeviceClass];
-[SBLockElementViewProvider systemApertureElementAssertionAcquired];
-[SBLockElementViewProvider viewProvider];
-[SBLockElementViewProvider shouldSuppressElementWhileOnContinuityDisplay];
-[SBLockElementViewProvider setObstructionEdge:];
-[SBLockElementViewProvider handleElementViewEvent:];
-[SBLockElementViewProvider setContentProvider:];
-[SBLockElementViewProvider sizeThatFitsSize:forProvidedView:inLayoutMode:];
-[SBLockElementViewProvider initWithWindowScene:];
-[SBLockElementViewProvider _canShowWhileLocked];
-[SBLockElementViewProvider elementHost];
-[SBLockElementViewProvider isEmpty];
-[SBLockElementViewProvider isMinimalPresentationPossible];
-[SBLockElementViewProvider contentProvider];
-[SBLockElementViewProvider shouldSuppressElementWhileOverLiquidDetectionCriticalUI];
-[SBLockElementViewProvider minimumSupportedLayoutMode];
-[SBLockElementViewProvider handleBiometricEvent:];
-[SBLockElementViewProvider shouldSuppressElementWhileOnCoversheet];
-[SBLockElementViewProvider hasActivityBehavior];
-[SBLockElementViewProvider layoutHostContainerViewDidLayoutSubviews:];
-[SBLockElementViewProvider setEmpty:];
-[SBLockElementViewProvider destinationWindowScene];
-[SBLockElementViewProvider windowScene];
-[SBLockElementViewProvider contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:];
-[SBLockElementViewProvider setElementHost:];
-[SBLockElementViewProvider maximumSupportedLayoutMode];
-[SBLockElementViewProvider elementOrientation];
-[SBLockElementViewProvider biometricResource:observeEvent:];
-[SBLockElementViewProvider biometricResource:matchingEnabledDidChange:];
-[SBLockElementViewProvider shake];
-[SBLockElementViewProvider lockProvider];
-[SBLockElementViewProvider _treatAsAmbient];
-[SBLockElementViewProvider _updateLeadingPackageVisibility];
-[SBLockElementViewProvider _setUnlockMode:];
-[SBLockElementViewProvider _activelyWantsMatching];
-[SBLockElementViewProvider _allowsBiometricUnlock];
-[SBLockElementViewProvider _cancelPendingShake];
-[SBLockElementViewProvider _elementSizeLeading:forLayoutMode:];
-[SBLockElementViewProvider _isSensorVariantCenterPill];
-[SBLockElementViewProvider _isShowingInLandscape];
-[SBLockElementViewProvider _isV68Cover];
-[SBLockElementViewProvider _isV68Inner];
-[SBLockElementViewProvider _scheduleShake];
-[SBLockElementViewProvider _setAcquiring:];
-[SBLockElementViewProvider _toggleUnlockMode];
-[SBLockElementViewProvider _treatsAsAmbientSearching];
-[SBLockElementViewProvider _unlockMode];
-[SBLockElementViewProvider _updateAllowsBioUnlock];
-[SBLockElementViewProvider _updateTrailingGlyph];
-[SBLockElementViewProvider _updateTrailingPackageVisibility];
-[SBLockElementViewProvider _updateUnlockModeForState];
-[SBLockElementViewProvider leadingLock];
-[SBLockElementViewProvider preventsSwipeToHide];
-[SBLockElementViewProvider setBloomed:];
-[SBLockElementViewProvider setEarlyMatchingFeedback:];
-[SBLockElementViewProvider setLockProvider:];
-[SBLockElementViewProvider setTrailingPackageProvider:];
-[SBLockElementViewProvider shouldIgnoreSystemChromeSuppression];
-[SBLockElementViewProvider trailingContentView];
-[SBLockElementViewProvider trailingPackageProvider];
```
