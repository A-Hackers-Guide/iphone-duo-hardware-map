# `SBHomeGestureFinalDestinationSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 28 instance variables, 3 properties, 20 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _initialTranslationAdjustment;
d _minYDistanceForHomeOrSwitcher;
{CGPoint="x"d"y"d} _translation;
{CGPoint="x"d"y"d} _velocity;
d _lastTouchTimestamp;
d _lastAverageVelocityYForAcceleration;
{CGPoint="x"d"y"d} _initialTouchLocation;
{CGPoint="x"d"y"d} _lastTouchLocation;
{CGPoint="x"d"y"d} _directionSwitchLocation;
B _movingTowardsNextLayoutState;
d _adaptiveMinimumYVelocityForHome;
d _adaptivePauseVelocityThresholdForAppSwitcher;
d _adaptiveVelocitySlopeThresholdForArc;
d _lastFinalDestination;
q _edgeRegionSampleCounter;
B _updateEdgeRegionSampleCounter;
B _gestureHasBegun;
B _gestureHasEnded;
Q _numberOfTouchSamples;
@"SBHomeGestureDockSwitcherModifier" _dockModifier;
q _startingEnvironmentMode;
B _scrunchInitiated;
B _continuingGesture;
q _touchType;
B _isMouseEvent;
@"<SBHomeGestureFinalDestinationSwitcherModifierDelegate>" _finalDestinationDelegate;
B _hasSeenAccelerationDipForAppSwitcher;
@"NSString" _finalDestinationReason;
```

## Properties

```
@property (Tq,R,N) currentFinalDestination;
@property (T@"NSString",R,N,V_finalDestinationReason) finalDestinationReason;
@property (TB,R,N,V_hasSeenAccelerationDipForAppSwitcher) hasSeenAccelerationDipForAppSwitcher;
```

## Instance methods

```
-[SBHomeGestureFinalDestinationSwitcherModifier handleGestureEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier _applyPrototypeSettings];
-[SBHomeGestureFinalDestinationSwitcherModifier didMoveToParentModifier:];
-[SBHomeGestureFinalDestinationSwitcherModifier handleHomeGestureSettingsChangedEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier _unconditionalDistanceThresholdForHome];
-[SBHomeGestureFinalDestinationSwitcherModifier _isTranslationPastDistanceThresholdToUnconditionallyGoHome:];
-[SBHomeGestureFinalDestinationSwitcherModifier debugDescription];
-[SBHomeGestureFinalDestinationSwitcherModifier _updateForGestureDidBeginWithEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier handleSwitcherSettingsChangedEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier finalDestinationReason];
-[SBHomeGestureFinalDestinationSwitcherModifier _updateAdaptiveThresholdsForCurrentFinalDestination:velocityAverage:];
-[SBHomeGestureFinalDestinationSwitcherModifier _adjustedFinalDestinationAccountingForEdgeDataDistortion:location:];
-[SBHomeGestureFinalDestinationSwitcherModifier _updateForGestureDidChangeWithEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier initWithDelegate:initialTranslationAdjustment:minYDistanceForHomeOrSwitcher:startingEnvironmentMode:continuingGesture:dockModifier:];
-[SBHomeGestureFinalDestinationSwitcherModifier _updateGestureTranslationVelocityAndProgressWithEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier studyLogData];
-[SBHomeGestureFinalDestinationSwitcherModifier hasSeenAccelerationDipForAppSwitcher];
-[SBHomeGestureFinalDestinationSwitcherModifier _updateForGestureDidEndWithEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier _hasTraveledSufficientDistanceForHomeOrAppSwitcherForMouseEvent:];
-[SBHomeGestureFinalDestinationSwitcherModifier currentFinalDestination];
```
