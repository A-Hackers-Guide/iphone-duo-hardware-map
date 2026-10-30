# `SBHomeGestureDockSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 17 instance variables, 1 properties, 24 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _lastTouchLocation;
{CGPoint="x"d"y"d} _unadjustedGestureTranslation;
{CGPoint="x"d"y"d} _velocity;
{CGPoint="x"d"y"d} _translationAdjustmentForFloatingDock;
B _currentlyTrackingDock;
B _wasTrackingDockWhenGestureBegan;
B _hadOpenDockFolderWhenGestureBegan;
B _hadOpenHomeScreenFolderWhenGestureBegan;
B _hadOpenForegroundLibraryWhenGestureBegan;
B _verticallyRubberbandedOutOfDock;
B _wantsDockAssertion;
B _highEnoughToShowDock;
B _gestureHasBegun;
B _gestureHasEnded;
@"<SBHomeGestureDockSwitcherModifierDelegate>" _delegate;
q _startingEnvironmentMode;
B _requireVerticalSwipeToTrackDock;
```

## Properties

```
@property (TB,R,N,GisCurrentlyTrackingDock,V_currentlyTrackingDock) currentlyTrackingDock;
```

## Instance methods

```
-[SBHomeGestureDockSwitcherModifier handleGestureEvent:];
-[SBHomeGestureDockSwitcherModifier _applyPrototypeSettings];
-[SBHomeGestureDockSwitcherModifier dockWindowLevelPriority];
-[SBHomeGestureDockSwitcherModifier dockWindowLevel];
-[SBHomeGestureDockSwitcherModifier didMoveToParentModifier:];
-[SBHomeGestureDockSwitcherModifier handleHomeGestureSettingsChangedEvent:];
-[SBHomeGestureDockSwitcherModifier dockProgress];
-[SBHomeGestureDockSwitcherModifier debugDescription];
-[SBHomeGestureDockSwitcherModifier wantsDockWindowLevelAssertion];
-[SBHomeGestureDockSwitcherModifier _updateForGestureDidBeginWithEvent:];
-[SBHomeGestureDockSwitcherModifier wantsDockBehaviorAssertion];
-[SBHomeGestureDockSwitcherModifier dockUpdateMode];
-[SBHomeGestureDockSwitcherModifier _hasTraveledSufficientDistanceForHomeOrAppSwitcher];
-[SBHomeGestureDockSwitcherModifier _updateForGestureDidChangeWithEvent:];
-[SBHomeGestureDockSwitcherModifier studyLogData];
-[SBHomeGestureDockSwitcherModifier _updateForGestureDidEndWithEvent:];
-[SBHomeGestureDockSwitcherModifier _shouldPresentDockForFinalDestination:];
-[SBHomeGestureDockSwitcherModifier _rubberbandedOutOfDockHorizontally];
-[SBHomeGestureDockSwitcherModifier _updateGestureTranslationAndVelocityWithEvent:];
-[SBHomeGestureDockSwitcherModifier adjustedFinalDestinationForDestination:withTranslation:velocity:];
-[SBHomeGestureDockSwitcherModifier adjustedTranslationForTranslation:];
-[SBHomeGestureDockSwitcherModifier initWithDelegate:startingEnvironmentMode:requireVerticalSwipeToTrackDock:];
-[SBHomeGestureDockSwitcherModifier isCurrentlyTrackingDock];
-[SBHomeGestureDockSwitcherModifier translationForAdjustedTranslation:];
```
