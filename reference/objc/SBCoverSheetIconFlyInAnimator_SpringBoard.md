# `SBCoverSheetIconFlyInAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBCenterIconZoomAnimator`
- Protocols: `PTSettingsKeyObserver`
- 29 instance variables, 8 properties, 39 instance methods, 0 class methods

## Instance variables

```
d _baselineDistance;
d _effectMultiplier;
d _distanceExponent;
d _flyZResponse;
d _flyZCurveFactor;
d _iconAlphaResponse;
d _verticalDockCenterPointOffsetX;
d _verticalDockCenterPointOffsetY;
d _dockFlyZResponseMultiplier;
d _iconFlyZMaxDistance;
d _iconFlyZMaxDistanceForPhone;
d _iconFlyZMaxDistanceForPad;
d _iconFlyZDistanceExponent;
d _velocity;
Q _animationType;
B _hasBeenPrepared;
B _isReversing;
@"NSMapTable" _iconPositions;
@"NSMapTable" _disableGlassGroupingAssertionsForIconViews;
{CGPoint="x"d"y"d} _spotlightSearchButtonRestingPosition;
@"UIView" _spotlightSearchButtonView;
@"NSMapTable" _iconZoomViewRestingPositions;
@"UIView" _floatingDockView;
@"NSHashTable" _glassGroupParentViewsAwaitingRestore;
@"SBCoverSheetIconFlyInAlphaFadeAssertion" _alphaFadeAssertion;
@"UIViewFloatAnimatableProperty" _spreadMultiplierAnimatableProperty;
@"CAMediaTimingFunction" _timingFunction;
@"UIPageControl" _pageControl;
@"SBFloatingDockBehaviorAssertion" _floatingDockBehaviorHidingAssertion;
```

## Properties

```
@property (T@"UIViewFloatAnimatableProperty",&,N,V_spreadMultiplierAnimatableProperty) spreadMultiplierAnimatableProperty;
@property (T@"CAMediaTimingFunction",&,N,V_timingFunction) timingFunction;
@property (T@"UIPageControl",&,N,V_pageControl) pageControl;
@property (T@"SBFloatingDockBehaviorAssertion",&,N,V_floatingDockBehaviorHidingAssertion) floatingDockBehaviorHidingAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCoverSheetIconFlyInAnimator _enumerateAdditionalIconZoomViewsWithHandler:];
-[SBCoverSheetIconFlyInAnimator setTimingFunction:];
-[SBCoverSheetIconFlyInAnimator _positionForSpreadMultiplier:point:center:];
-[SBCoverSheetIconFlyInAnimator _prepareAnimation];
-[SBCoverSheetIconFlyInAnimator _updateDockForFraction:];
-[SBCoverSheetIconFlyInAnimator _blurRadiusForSpreadValue:];
-[SBCoverSheetIconFlyInAnimator _setCameraAnchorPointForContainer:];
-[SBCoverSheetIconFlyInAnimator _setZPositionForView:center:andFraction:];
-[SBCoverSheetIconFlyInAnimator _setAnimationFraction:withCenter:];
-[SBCoverSheetIconFlyInAnimator dealloc];
-[SBCoverSheetIconFlyInAnimator timingFunction];
-[SBCoverSheetIconFlyInAnimator _iconViewAlphaForSpreadValue:];
-[SBCoverSheetIconFlyInAnimator animateZPositionsToFraction:completionGroup:completion:];
-[SBCoverSheetIconFlyInAnimator setFloatingDockBehaviorHidingAssertion:];
-[SBCoverSheetIconFlyInAnimator settings:changedValueForKey:];
-[SBCoverSheetIconFlyInAnimator _effectiveCenterPoint];
-[SBCoverSheetIconFlyInAnimator setFractionForAlphaFadeOfViews:];
-[SBCoverSheetIconFlyInAnimator _cleanupAnimation];
-[SBCoverSheetIconFlyInAnimator setPageControl:];
-[SBCoverSheetIconFlyInAnimator _referenceBounds];
-[SBCoverSheetIconFlyInAnimator pageControl];
-[SBCoverSheetIconFlyInAnimator spreadMultiplierAnimatableProperty];
-[SBCoverSheetIconFlyInAnimator _velocityForSpreadMultiplier:spreadMultiplierVelocity:point:center:];
-[SBCoverSheetIconFlyInAnimator _prepareToAnimateZPositions];
-[SBCoverSheetIconFlyInAnimator _effectiveCenterPointForVerticalDockOverwriteWithLibraryPodFolderController:];
-[SBCoverSheetIconFlyInAnimator setSpreadMultiplierAnimatableProperty:];
-[SBCoverSheetIconFlyInAnimator _restoreIconGlassGroupingBehaviors];
-[SBCoverSheetIconFlyInAnimator _updateWithSettings:];
-[SBCoverSheetIconFlyInAnimator _createAnimatablePropertiesWithView:];
-[SBCoverSheetIconFlyInAnimator _perspectiveTransform];
-[SBCoverSheetIconFlyInAnimator _updateSpreadMultiplierForPresentation:];
-[SBCoverSheetIconFlyInAnimator _responseForPoint:center:];
-[SBCoverSheetIconFlyInAnimator _setZoomViewAnchorPoint];
-[SBCoverSheetIconFlyInAnimator floatingDockBehaviorHidingAssertion];
-[SBCoverSheetIconFlyInAnimator _effectiveCenterPointForVerticalDockOverwriteWithRootFolderController:];
-[SBCoverSheetIconFlyInAnimator initWithFolderController:];
-[SBCoverSheetIconFlyInAnimator prepareWithVelocity:forFlyIn:];
-[SBCoverSheetIconFlyInAnimator setIconSpreadFraction:];
-[SBCoverSheetIconFlyInAnimator _flyOutGlassGroupParentViews];
```
