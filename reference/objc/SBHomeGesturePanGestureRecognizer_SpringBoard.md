# `SBHomeGesturePanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBScreenEdgePanGestureRecognizer`
- Protocols: `PTSettingsKeyObserver`, `SBGestureRecognizerPanGestureProviding`, `SBGestureRecognizerTouchHistoryProviding`
- 10 instance variables, 14 properties, 45 instance methods, 1 class methods

## Instance variables

```
B _needsUpdateExclusionTrapezoids;
B _preventHorizontalSwipesOutsideTrapezoid;
B _installedAsSystemGesture;
@"<SBHomeGesturePanGestureRecognizerContextDelegate>" _contextDelegate;
@"<SBHomeGesturePanGestureRecognizerHysteresisDelegate>" _hysteresisDelegate;
@"SBHomeGestureSettings" _homeGestureSettings;
@"<SBFluidSwitcherGestureExclusionShape>" _portraitExclusionTrapezoid;
@"<SBFluidSwitcherGestureExclusionShape>" _landscapeExclusionTrapezoid;
@"SBTouchHistory" _touchHistory;
d _hysteresisWhenTouchesBegan;
```

## Properties

```
@property (T@"SBHomeGestureSettings",&,N,V_homeGestureSettings) homeGestureSettings;
@property (T@"<SBFluidSwitcherGestureExclusionShape>",&,N,V_portraitExclusionTrapezoid) portraitExclusionTrapezoid;
@property (T@"<SBFluidSwitcherGestureExclusionShape>",&,N,V_landscapeExclusionTrapezoid) landscapeExclusionTrapezoid;
@property (T@"SBTouchHistory",&,N,V_touchHistory) touchHistory;
@property (Td,N,V_hysteresisWhenTouchesBegan) hysteresisWhenTouchesBegan;
@property (T@"<SBHomeGesturePanGestureRecognizerContextDelegate>",W,N,V_contextDelegate) contextDelegate;
@property (T@"<SBHomeGesturePanGestureRecognizerHysteresisDelegate>",W,N,V_hysteresisDelegate) hysteresisDelegate;
@property (TB,N,V_preventHorizontalSwipesOutsideTrapezoid) preventHorizontalSwipesOutsideTrapezoid;
@property (TB,N,V_installedAsSystemGesture) installedAsSystemGesture;
@property (T@"UIView",R,W,N) viewForTouchHistory;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBHomeGesturePanGestureRecognizer homeGesturePanGestureRecognizerWithTarget:action:];
```

## Instance methods

```
-[SBHomeGesturePanGestureRecognizer _SBLogTouchesWithMethodName:withMethodName:];
-[SBHomeGesturePanGestureRecognizer initWithTarget:action:type:options:];
-[SBHomeGesturePanGestureRecognizer setTouchHistory:];
-[SBHomeGesturePanGestureRecognizer _touchInterfaceOrientation];
-[SBHomeGesturePanGestureRecognizer averageTouchPathAngleOverTimeDuration:];
-[SBHomeGesturePanGestureRecognizer _shouldBegin];
-[SBHomeGesturePanGestureRecognizer touchesEnded:withEvent:];
-[SBHomeGesturePanGestureRecognizer conformsToSBGestureRecognizerTouchHistoryProviding];
-[SBHomeGesturePanGestureRecognizer viewForTouchHistory];
-[SBHomeGesturePanGestureRecognizer peakSpeed];
-[SBHomeGesturePanGestureRecognizer touchHistory];
-[SBHomeGesturePanGestureRecognizer sb_commonInitHomeGesturePanGestureRecognizer];
-[SBHomeGesturePanGestureRecognizer _currentKeyboardExclusionCompositeShape];
-[SBHomeGesturePanGestureRecognizer timeWithinRadius:];
-[SBHomeGesturePanGestureRecognizer _isOutsideOfExclusionTrapezoid];
-[SBHomeGesturePanGestureRecognizer _shouldUseLandscapeExclusionTrapezoid];
-[SBHomeGesturePanGestureRecognizer homeGestureSettings];
-[SBHomeGesturePanGestureRecognizer _updateHomeGestureParameters];
-[SBHomeGesturePanGestureRecognizer setContextDelegate:];
-[SBHomeGesturePanGestureRecognizer setInstalledAsSystemGesture:];
-[SBHomeGesturePanGestureRecognizer reset];
-[SBHomeGesturePanGestureRecognizer _setNeedsUpdateExclusionTrapezoids];
-[SBHomeGesturePanGestureRecognizer setPortraitExclusionTrapezoid:];
-[SBHomeGesturePanGestureRecognizer touchesBegan:withEvent:];
-[SBHomeGesturePanGestureRecognizer hysteresisWhenTouchesBegan];
-[SBHomeGesturePanGestureRecognizer touchesMoved:withEvent:];
-[SBHomeGesturePanGestureRecognizer settings:changedValueForKey:];
-[SBHomeGesturePanGestureRecognizer hysteresisDelegate];
-[SBHomeGesturePanGestureRecognizer setPreventHorizontalSwipesOutsideTrapezoid:];
-[SBHomeGesturePanGestureRecognizer _shouldUsePortraitExclusionTrapezoid];
-[SBHomeGesturePanGestureRecognizer setHomeGestureSettings:];
-[SBHomeGesturePanGestureRecognizer setDelegate:];
-[SBHomeGesturePanGestureRecognizer contextDelegate];
-[SBHomeGesturePanGestureRecognizer preventHorizontalSwipesOutsideTrapezoid];
-[SBHomeGesturePanGestureRecognizer _updateExclusionTrapezoidsIfNeeded];
-[SBHomeGesturePanGestureRecognizer landscapeExclusionTrapezoid];
-[SBHomeGesturePanGestureRecognizer setHysteresisWhenTouchesBegan:];
-[SBHomeGesturePanGestureRecognizer _currentExclusionShapeForEdge:];
-[SBHomeGesturePanGestureRecognizer averageTouchVelocityOverTimeDuration:];
-[SBHomeGesturePanGestureRecognizer _shouldBlockHomeGestureForKeyboardInputMode:];
-[SBHomeGesturePanGestureRecognizer setLandscapeExclusionTrapezoid:];
-[SBHomeGesturePanGestureRecognizer setHysteresisDelegate:];
-[SBHomeGesturePanGestureRecognizer _surfaceType];
-[SBHomeGesturePanGestureRecognizer installedAsSystemGesture];
-[SBHomeGesturePanGestureRecognizer portraitExclusionTrapezoid];
```
