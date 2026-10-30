# `SBDashBoardSetupView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAAnimationDelegate`, `SBWallpaperUnlockProgressObserver`
- 40 instance variables, 12 properties, 72 instance methods, 0 class methods

## Instance variables

```
@"UILabel" _titleLabel;
@"UIStackView" _activationLockStackView;
@"UIImageView" _activationLockImage;
@"UILabel" _activationLockWarningLabel;
@"UILabel" _activationLockDetailLabel;
@"UILabel" _storeRestrictedTitleLabel;
@"UILabel" _storeRestrictedBodyLabel;
@"UILabel" _storeRestrictedLinkLabel;
@"UIView" _storeRestrictedContainer;
@"UILabel" _securityResearchDeviceTitleLabel;
@"UIView" _securityResearchDeviceContainer;
@"UIImageView" _securityResearchHeaderIcon;
@"UILabel" _securityResearchSubtitleLabel;
@"SBFTouchPassThroughView" _homeAffordanceContainer;
@"CSHomeAffordanceView" _homeAffordanceView;
@"UIView" _homeAffordanceCallToActionContainer;
@"SBUILegibilityLabel" _homeAffordanceCallToActionLabel;
@"SBUICallToActionLabel" _homeButtonCallToActionLabel;
@"NSObject<OS_dispatch_source>" _homeButtonCallToActionTimer;
@"NSArray" _activationInfoViewConstraints;
@"NSString" _currentLanguage;
@"SBCursiveTextView" _cursiveTextView;
@"SASBookendViewProvider" _glassCursiveTextViewProvider;
B _isCursiveTitleAnimationDesired;
@"SASCaptureSessionTextureDataSource" _glassTextureDataSource;
@"SBWallpaperController" _observedWallpaperController;
d _startTime;
d _customDelayDuration;
@"CADisplayLink" _displayLink;
B _isStoreRestricted;
B _isSecurityResearchDevice;
B _suppressingElements;
@"NSLayoutConstraint" _titleYOffsetConstraint;
B _activationLocked;
@"UIView" _activationInfoView;
@"UIView" _regulatoryInfoView;
@"_UILegibilitySettings" _legibilitySettings;
@"UIButton" _infoButton;
@"UIView" _childIconView;
@"<SBSolariumCursiveTextAnimationDelegate>" _glassCursiveTextAnimationDelegate;
```

## Properties

```
@property (T@"<SBSolariumCursiveTextAnimationDelegate>",W,N,V_glassCursiveTextAnimationDelegate) glassCursiveTextAnimationDelegate;
@property (T@"CSHomeAffordanceView",&,N,V_homeAffordanceView) homeAffordanceView;
@property (T@"UIView",&,N,V_activationInfoView) activationInfoView;
@property (T@"UIView",&,N,V_regulatoryInfoView) regulatoryInfoView;
@property (T@"_UILegibilitySettings",&,N,V_legibilitySettings) legibilitySettings;
@property (T@"UIButton",R,N,V_infoButton) infoButton;
@property (TB,N,GisActivationLocked,V_activationLocked) activationLocked;
@property (T@"UIView",&,N,V_childIconView) childIconView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardSetupView _updateLegibilitySettings];
-[SBDashBoardSetupView setOrientation:];
-[SBDashBoardSetupView didMoveToWindow];
-[SBDashBoardSetupView animationDidStop:finished:];
-[SBDashBoardSetupView dealloc];
-[SBDashBoardSetupView homeAffordanceView];
-[SBDashBoardSetupView layoutSubviews];
-[SBDashBoardSetupView _layoutHomeAffordance];
-[SBDashBoardSetupView _removeResetAnimationForKeyPath:onLayer:];
-[SBDashBoardSetupView isActivationLocked];
-[SBDashBoardSetupView _createDisplayLink];
-[SBDashBoardSetupView legibilitySettings];
-[SBDashBoardSetupView setHomeAffordanceView:];
-[SBDashBoardSetupView setLegibilitySettings:];
-[SBDashBoardSetupView _onDisplayLink:];
-[SBDashBoardSetupView _titleView];
-[SBDashBoardSetupView infoButton];
-[SBDashBoardSetupView _setupConstraints];
-[SBDashBoardSetupView _addTitleLabel];
-[SBDashBoardSetupView _removeDisplayLink];
-[SBDashBoardSetupView setCoverSheetContext:];
-[SBDashBoardSetupView _addActivationLockLabels];
-[SBDashBoardSetupView setActivationLockWarningString:detailString:forLanguage:];
-[SBDashBoardSetupView setTitleString:forLanguage:];
-[SBDashBoardSetupView _actsLikeStoreRestricted];
-[SBDashBoardSetupView _addHomeAffordanceCallToAction];
-[SBDashBoardSetupView _addHomeAffordanceForCoverSheetContext:];
-[SBDashBoardSetupView _addHomeButtonCallToAction];
-[SBDashBoardSetupView _addInfoButton];
-[SBDashBoardSetupView _addResetAnimationForKeyPath:onLayer:dispatchGroup:];
-[SBDashBoardSetupView _addSecurityResearchLabels];
-[SBDashBoardSetupView _addStoreRestrictedLabels];
-[SBDashBoardSetupView _adjustTitleVisibilityForInfoViews];
-[SBDashBoardSetupView _animateCursiveForTimePassed];
-[SBDashBoardSetupView _animateHomeAffordanceCallToActionToActive:withDispatchGroup:];
-[SBDashBoardSetupView _animateHomeAffordanceToActive:withDispatchGroup:];
-[SBDashBoardSetupView _animateHomeButtonCallToActionToActive:withDispatchGroup:];
-[SBDashBoardSetupView _animateView:toActive:withDispatchGroup:];
-[SBDashBoardSetupView _canStartGlassCursiveTitleAnimation];
-[SBDashBoardSetupView _glassCaptureOrientation];
-[SBDashBoardSetupView _hasNonCursiveSuppressingUI];
-[SBDashBoardSetupView _hasSuppressingUI];
-[SBDashBoardSetupView _isShowingModalTakeoverUI];
-[SBDashBoardSetupView _layoutActivationInfoView];
-[SBDashBoardSetupView _layoutHomeAffordanceCallToAction];
-[SBDashBoardSetupView _layoutHomeButtonCallToAction];
-[SBDashBoardSetupView _layoutRegulatoryInfo];
-[SBDashBoardSetupView _removeNormalAnimationForKeyPath:onLayer:];
-[SBDashBoardSetupView _retargetGlassTextureToCurrentSceneIfNeeded];
-[SBDashBoardSetupView _setupActivationInfoConstraintsIfNeeded];
-[SBDashBoardSetupView _startupDidFinish:];
-[SBDashBoardSetupView _updateBaselineAndChildIconConstraints];
-[SBDashBoardSetupView _updateHelloVisibility];
-[SBDashBoardSetupView _wallpaperCaptureMatchesGlassFrame:];
-[SBDashBoardSetupView activationInfoView];
-[SBDashBoardSetupView animateComponents:toActive:withCompletion:];
-[SBDashBoardSetupView childIconView];
-[SBDashBoardSetupView glassCursiveTextAnimationDelegate];
-[SBDashBoardSetupView initWithFrame:usingHomeAffordance:coverSheetContext:isStoreRestricted:isSecurityResearchDevice:];
-[SBDashBoardSetupView prepareSolariumCursiveTextViewWithDelegate:completion:];
-[SBDashBoardSetupView regulatoryInfoView];
-[SBDashBoardSetupView setActivationInfoView:];
-[SBDashBoardSetupView setActivationLocked:];
-[SBDashBoardSetupView setCallToActionString:forLanguage:];
-[SBDashBoardSetupView setChildIconView:];
-[SBDashBoardSetupView setChildIconVisible:animated:withDelay:];
-[SBDashBoardSetupView setGlassCursiveTextAnimationDelegate:];
-[SBDashBoardSetupView setInfoButtonVisible:animated:withDelay:];
-[SBDashBoardSetupView setRegulatoryInfoView:];
-[SBDashBoardSetupView setStoreRestrictedStrings:bodyString:linkString:forLanguage:];
-[SBDashBoardSetupView setSuppressingAllElements:];
-[SBDashBoardSetupView wallpaperUnlockProgressDidUpdate:];
```
