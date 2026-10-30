# `SBHomeGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- Protocols: `SBHomeGestureDockSwitcherModifierDelegate`, `SBHomeGestureFinalDestinationSwitcherModifierDelegate`
- 54 instance variables, 6 properties, 99 instance methods, 0 class methods

## Instance variables

```
B _inMultitasking;
@"UIViewFloatAnimatableProperty" _inMultitaskingChangedProperty;
{CGPoint="x"d"y"d} _touchOffset;
d _lastFrameOffsetX;
d _lastTranslationXForRubberbanding;
d _translationXLostToRubberbanding;
B _hasTriggeredCardFlyIn;
d _translationYWhenTriggeredCardFlyIn;
B _hasBecomeCoplanarSinceGestureFromSwitcherBegan;
{CGPoint="x"d"y"d} _gestureLiftOffVelocity;
{CGPoint="x"d"y"d} _gestureLiftOffTranslation;
{CGPoint="x"d"y"d} _translationAdjustmentForStartingFromSwitcher;
{CGPoint="x"d"y"d} _translationAdjustmentForStartingFromHomeScreen;
d _progressToInSwitcherCardScale;
d _progressToMaxTranslation;
{CGPoint="x"d"y"d} _translation;
{CGPoint="x"d"y"d} _velocity;
d _stackedProgress;
{CGPoint="x"d"y"d} _initialCentroid;
{CGPoint="x"d"y"d} _centroid;
{CGPoint="x"d"y"d} _centroidAdjustment;
d _absoluteScale;
{CGPoint="x"d"y"d} _translationWithoutScale;
@"CADisplayLink" _displayLink;
d _lastTouchTimestamp;
q _gestureHoldTimer;
{CGPoint="x"d"y"d} _initialTouchLocation;
{CGPoint="x"d"y"d} _lastTouchLocation;
B _everTranslatedUpwards;
B _cancelledGestureForEmptySwitcher;
d _toHomeScreenAlpha;
d _toHomeScreenBlurProgress;
d _toHomeScreenDimmingAlpha;
d _homeGestureXOffsetFactor;
B _didWarmupFlyInHaptic;
B _didPlayFlyInHaptic;
B _gestureHasBegun;
B _gestureHasEnded;
@"SBSwitcherModifier" _multitaskingModifier;
@"SBCoplanarSwitcherModifier" _coplanarLayoutModifier;
@"SBHomeGestureDockSwitcherModifier" _dockModifier;
@"SBHomeGestureFinalDestinationSwitcherModifier" _finalDestinationModifier;
@"SBDismissSiriSwitcherModifier" _dismissSiriModifier;
@"SBAppLayout" _selectedAppLayout;
q _startingEnvironmentMode;
B _scrunchInitiated;
B _continuingGesture;
B _lastGestureWasAnArcSwipe;
B _shouldResignActive;
d _homeGestureMinimumCardScale;
d _homeGestureMinimumCardScaleRubberBandingRange;
B _isPendingViewsForAcceleratedHomeGesture;
B _laysOutNeighboringCards;
B _providesHomeScreenDimmingAlpha;
```

## Properties

```
@property (TB,N,V_laysOutNeighboringCards) laysOutNeighboringCards;
@property (TB,N,V_providesHomeScreenDimmingAlpha) providesHomeScreenDimmingAlpha;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHomeGestureSwitcherModifier handleGestureEvent:];
-[SBHomeGestureSwitcherModifier scaleForIndex:];
-[SBHomeGestureSwitcherModifier _displayLinkFired:];
-[SBHomeGestureSwitcherModifier titleOpacityForIndex:];
-[SBHomeGestureSwitcherModifier homeScreenScale];
-[SBHomeGestureSwitcherModifier isContainerStatusBarVisible];
-[SBHomeGestureSwitcherModifier homeScreenBackdropBlurProgress];
-[SBHomeGestureSwitcherModifier homeScreenDimmingAlpha];
-[SBHomeGestureSwitcherModifier _applyPrototypeSettings];
-[SBHomeGestureSwitcherModifier _updateInMultitaskingIfNeededWithEvent:];
-[SBHomeGestureSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBHomeGestureSwitcherModifier homeScreenAlpha];
-[SBHomeGestureSwitcherModifier isHomeScreenContentRequired];
-[SBHomeGestureSwitcherModifier didMoveToParentModifier:];
-[SBHomeGestureSwitcherModifier cornerRadiiForIndex:];
-[SBHomeGestureSwitcherModifier _inSwitcherCenterYOffsetWhenPresented];
-[SBHomeGestureSwitcherModifier handleHomeGestureSettingsChangedEvent:];
-[SBHomeGestureSwitcherModifier _updateTranslationAdjustmentForGestureFromHomeScreenIfNeededWithEvent:];
-[SBHomeGestureSwitcherModifier _distanceYToMaxTranslation];
-[SBHomeGestureSwitcherModifier animationAttributesForLayoutElement:];
-[SBHomeGestureSwitcherModifier _rubberbandedTranslationForAdjacentCards];
-[SBHomeGestureSwitcherModifier homeScreenBackdropBlurType];
-[SBHomeGestureSwitcherModifier _switcherCardScale];
-[SBHomeGestureSwitcherModifier _isTranslationPastDistanceThresholdToUnconditionallyGoHome:];
-[SBHomeGestureSwitcherModifier liftOffTranslationForGestureEnd];
-[SBHomeGestureSwitcherModifier _responseForStudyLogDidBeginGesture];
-[SBHomeGestureSwitcherModifier unconditionalDistanceThresholdForHome];
-[SBHomeGestureSwitcherModifier _responseForUpdatingIconViewVisibility:];
-[SBHomeGestureSwitcherModifier debugDescription];
-[SBHomeGestureSwitcherModifier isSwitcherWindowVisible];
-[SBHomeGestureSwitcherModifier titleAndIconOpacityForIndex:];
-[SBHomeGestureSwitcherModifier appLayoutsToCacheSnapshots];
-[SBHomeGestureSwitcherModifier dimmingAlphaForLayoutRole:inAppLayout:];
-[SBHomeGestureSwitcherModifier handleTransitionEvent:];
-[SBHomeGestureSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBHomeGestureSwitcherModifier _updateForGestureDidBeginWithEvent:];
-[SBHomeGestureSwitcherModifier _responseForSBEventGestureBeganWithTimeDelta:];
-[SBHomeGestureSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBHomeGestureSwitcherModifier visibleAppLayouts];
-[SBHomeGestureSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBHomeGestureSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBHomeGestureSwitcherModifier laysOutNeighboringCards];
-[SBHomeGestureSwitcherModifier handleSwitcherSettingsChangedEvent:];
-[SBHomeGestureSwitcherModifier shadowOpacityForLayoutRole:atIndex:];
-[SBHomeGestureSwitcherModifier headerStyleForIndex:];
-[SBHomeGestureSwitcherModifier wallpaperStyle];
-[SBHomeGestureSwitcherModifier _responseForUpdatingLayoutForGestureBegan];
-[SBHomeGestureSwitcherModifier frameForIndex:];
-[SBHomeGestureSwitcherModifier dealloc];
-[SBHomeGestureSwitcherModifier selectedAppLayout];
-[SBHomeGestureSwitcherModifier wallpaperScale];
-[SBHomeGestureSwitcherModifier _hasTraveledSufficientDistanceForHomeOrAppSwitcher];
-[SBHomeGestureSwitcherModifier wallpaperOverlayAlphaForIndex:];
-[SBHomeGestureSwitcherModifier initWithGestureID:selectedAppLayout:startingEnvironmentMode:multitaskingModifier:scrunchInitiated:continuingGesture:lastGestureWasAnArcSwipe:];
-[SBHomeGestureSwitcherModifier _selectedAppLayoutIndex];
-[SBHomeGestureSwitcherModifier _scaleForAdjacentCards];
-[SBHomeGestureSwitcherModifier _responseForCancelingSystemGesturesIfNeededWithFinalDestination:];
-[SBHomeGestureSwitcherModifier _beginAnimatingMultitaskingPropertyWithMode:settings:];
-[SBHomeGestureSwitcherModifier _unadjustedGestureTranslation];
-[SBHomeGestureSwitcherModifier _responseForSBEventGestureEndWithEvent:finalDestination:];
-[SBHomeGestureSwitcherModifier _scaleForOffscreenAdjacentCardsForFlyIn];
-[SBHomeGestureSwitcherModifier isPendingViewsForAcceleratedHomeGesture];
-[SBHomeGestureSwitcherModifier handleRemovalEvent:];
-[SBHomeGestureSwitcherModifier providesHomeScreenDimmingAlpha];
-[SBHomeGestureSwitcherModifier _updateForGestureDidChangeWithEvent:];
-[SBHomeGestureSwitcherModifier _responseForActivatingFinalDestination:];
-[SBHomeGestureSwitcherModifier _inMultitaskingForLocation:translation:];
-[SBHomeGestureSwitcherModifier isShowingOrAnimatingCardsForFlyIn];
-[SBHomeGestureSwitcherModifier _responseForStudyLogDidEndGestureWithEvent:finalDestination:destinationReason:];
-[SBHomeGestureSwitcherModifier _scaleForTranslation:];
-[SBHomeGestureSwitcherModifier isHitTestBlockingViewVisible];
-[SBHomeGestureSwitcherModifier _updateShouldResignActiveWithEvent:];
-[SBHomeGestureSwitcherModifier _frameOffsetForTranslation:];
-[SBHomeGestureSwitcherModifier appLayoutsToResignActive];
-[SBHomeGestureSwitcherModifier _updateGestureTranslationVelocityAndProgressWithEvent:];
-[SBHomeGestureSwitcherModifier _newDockModifierRequiringVerticalSwipeToTrackDock:startingEnvironmentMode:];
-[SBHomeGestureSwitcherModifier _layoutSettingsForAppLayout:layoutSettings:];
-[SBHomeGestureSwitcherModifier _hasPausedEnoughForFlyIn];
-[SBHomeGestureSwitcherModifier _coplanarSpacing];
-[SBHomeGestureSwitcherModifier _updateStackedProgress];
-[SBHomeGestureSwitcherModifier _shouldResignActiveBasedOnCardScale];
-[SBHomeGestureSwitcherModifier _centerYOffsetDuringGesture];
-[SBHomeGestureSwitcherModifier _shouldPositionAdjacentCardsOffscreenForFlyIn];
-[SBHomeGestureSwitcherModifier setLaysOutNeighboringCards:];
-[SBHomeGestureSwitcherModifier lighteningAlphaForIndex:];
-[SBHomeGestureSwitcherModifier _preventPositioningCardsOffscreenForFlatBottomEdgeSwipe];
-[SBHomeGestureSwitcherModifier preferredStatusBarAxis];
-[SBHomeGestureSwitcherModifier _updateFrameOffsetForXRubberbandingForTranslation:];
-[SBHomeGestureSwitcherModifier setProvidesHomeScreenDimmingAlpha:];
-[SBHomeGestureSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBHomeGestureSwitcherModifier _cornerRadiusSettings];
-[SBHomeGestureSwitcherModifier liftOffVelocityForGestureEnd];
-[SBHomeGestureSwitcherModifier _isSelectedAppLayoutAtIndex:];
-[SBHomeGestureSwitcherModifier _updateForGestureDidEndWithEvent:];
-[SBHomeGestureSwitcherModifier _distanceYToInSwitcherCardScale];
-[SBHomeGestureSwitcherModifier _responseForActivatingReachabilityIfNeededWithFinalDestination:];
-[SBHomeGestureSwitcherModifier _gestureProgressToMaxTranslationForTranslation:];
-[SBHomeGestureSwitcherModifier currentFinalDestination];
-[SBHomeGestureSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
```
