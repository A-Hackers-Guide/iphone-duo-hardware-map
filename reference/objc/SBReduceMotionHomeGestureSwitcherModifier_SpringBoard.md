# `SBReduceMotionHomeGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- Protocols: `SBHomeGestureDockSwitcherModifierDelegate`, `SBHomeGestureFinalDestinationSwitcherModifierDelegate`
- 21 instance variables, 6 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"SBCoplanarSwitcherModifier" _coplanarLayoutModifier;
@"SBHomeGestureDockSwitcherModifier" _dockModifier;
@"SBHomeGestureFinalDestinationSwitcherModifier" _finalDestinationModifier;
@"SBDismissSiriSwitcherModifier" _dismissSiriModifier;
@"SBAppLayout" _selectedAppLayout;
q _startingEnvironmentMode;
B _continuingGesture;
B _lastGestureWasAnArcSwipe;
B _scrunchInitiated;
{CGPoint="x"d"y"d} _initialTouchLocation;
{CGPoint="x"d"y"d} _lastTouchLocation;
{CGPoint="x"d"y"d} _translation;
{CGPoint="x"d"y"d} _velocity;
{CGPoint="x"d"y"d} _translationAdjustmentForStartingFromHomeScreen;
B _gestureHasBegun;
B _gestureHasEnded;
Q _reduceMotionAxis;
B _endingGestureForAppSwitcher;
B _didWarmupReduceMotionHaptic;
B _shouldProvideBlur;
B _laysOutNeighboringCards;
```

## Properties

```
@property (TB,N,V_shouldProvideBlur) shouldProvideBlur;
@property (TB,N,V_laysOutNeighboringCards) laysOutNeighboringCards;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBReduceMotionHomeGestureSwitcherModifier handleGestureEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier scaleForIndex:];
-[SBReduceMotionHomeGestureSwitcherModifier _applyPrototypeSettings];
-[SBReduceMotionHomeGestureSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBReduceMotionHomeGestureSwitcherModifier isHomeScreenContentRequired];
-[SBReduceMotionHomeGestureSwitcherModifier didMoveToParentModifier:];
-[SBReduceMotionHomeGestureSwitcherModifier cornerRadiiForIndex:];
-[SBReduceMotionHomeGestureSwitcherModifier handleHomeGestureSettingsChangedEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier _updateTranslationAdjustmentForGestureFromHomeScreenIfNeededWithEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier homeScreenBackdropBlurType];
-[SBReduceMotionHomeGestureSwitcherModifier unconditionalDistanceThresholdForHome];
-[SBReduceMotionHomeGestureSwitcherModifier isSwitcherWindowVisible];
-[SBReduceMotionHomeGestureSwitcherModifier shouldRubberbandFullScreenHomeGrabberView];
-[SBReduceMotionHomeGestureSwitcherModifier appLayoutsToCacheSnapshots];
-[SBReduceMotionHomeGestureSwitcherModifier handleTransitionEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier _updateForGestureDidBeginWithEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBReduceMotionHomeGestureSwitcherModifier visibleAppLayouts];
-[SBReduceMotionHomeGestureSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBReduceMotionHomeGestureSwitcherModifier laysOutNeighboringCards];
-[SBReduceMotionHomeGestureSwitcherModifier wallpaperStyle];
-[SBReduceMotionHomeGestureSwitcherModifier frameForIndex:];
-[SBReduceMotionHomeGestureSwitcherModifier keyboardSuppressionMode];
-[SBReduceMotionHomeGestureSwitcherModifier _updateForGestureDidChangeWithEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier _responseForActivatingFinalDestination:];
-[SBReduceMotionHomeGestureSwitcherModifier appLayoutsToResignActive];
-[SBReduceMotionHomeGestureSwitcherModifier _newDockModifierRequiringVerticalSwipeToTrackDock:startingEnvironmentMode:];
-[SBReduceMotionHomeGestureSwitcherModifier setLaysOutNeighboringCards:];
-[SBReduceMotionHomeGestureSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBReduceMotionHomeGestureSwitcherModifier _updateForGestureDidEndWithEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier currentFinalDestination];
-[SBReduceMotionHomeGestureSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBReduceMotionHomeGestureSwitcherModifier _updateGestureTranslationAndVelocityWithEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier _updateReduceMotionAxisIfNecessaryWithEvent:];
-[SBReduceMotionHomeGestureSwitcherModifier initWithGestureID:selectedAppLayout:startingEnvironmentMode:scrunchInitiated:continuingGesture:lastGestureWasAnArcSwipe:];
-[SBReduceMotionHomeGestureSwitcherModifier setShouldProvideBlur:];
-[SBReduceMotionHomeGestureSwitcherModifier shouldProvideBlur];
```
