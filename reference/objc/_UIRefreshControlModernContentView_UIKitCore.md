# `_UIRefreshControlModernContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRefreshControlContentView`
- 10 instance variables, 5 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _animationsAreValid;
@"UIView" _replicatorContainer;
@"_UIRefreshControlModernReplicatorView" _replicatorView;
@"_UIRefreshControlSeedView" _seed;
B _hasFinishedRevealing;
@"UILabel" _textLabel;
B _areAnimationsValid;
B _horizontallyCenteredFramesNeedUpdate;
d _currentPopStiffness;
d _impactIntensity;
```

## Properties

```
@property (TB,N,V_areAnimationsValid) areAnimationsValid;
@property (TB,N,V_horizontallyCenteredFramesNeedUpdate) horizontallyCenteredFramesNeedUpdate;
@property (T@"UILabel",R,N,V_textLabel) textLabel;
@property (Td,N,V_currentPopStiffness) currentPopStiffness;
@property (Td,N,V_impactIntensity) impactIntensity;
```

## Instance methods

```
-[_UIRefreshControlModernContentView setCurrentPopStiffness:];
-[_UIRefreshControlModernContentView _currentTimeOffset];
-[_UIRefreshControlModernContentView _tickDueToProgrammaticRefresh];
-[_UIRefreshControlModernContentView _effectiveTintColorWithAlpha:];
-[_UIRefreshControlModernContentView _percentageShowing];
-[_UIRefreshControlModernContentView _setSpunAppearance];
-[_UIRefreshControlModernContentView setHorizontallyCenteredFramesNeedUpdate:];
-[_UIRefreshControlModernContentView _setUnbloomedAppearance];
-[_UIRefreshControlModernContentView setAttributedTitle:];
-[_UIRefreshControlModernContentView textLabel];
-[_UIRefreshControlModernContentView _updateTimeOffsetOfRelevantLayers];
-[_UIRefreshControlModernContentView _unbloom];
-[_UIRefreshControlModernContentView _safeAreaInsetsDidChangeFromOldInsets:];
-[_UIRefreshControlModernContentView layoutSubviews];
-[_UIRefreshControlModernContentView _snappingMagic];
-[_UIRefreshControlModernContentView _resetToRevealingState];
-[_UIRefreshControlModernContentView style];
-[_UIRefreshControlModernContentView willTransitionFromState:toState:];
-[_UIRefreshControlModernContentView didTransitionFromState:toState:];
-[_UIRefreshControlModernContentView _effectiveTintColor];
-[_UIRefreshControlModernContentView currentPopStiffness];
-[_UIRefreshControlModernContentView _bloomedSeedTransform];
-[_UIRefreshControlModernContentView sizeThatFits:];
-[_UIRefreshControlModernContentView setTintColor:];
-[_UIRefreshControlModernContentView _heightAtWhichNoneOfTheInterfaceElementsAreVisibleEvenIfTheControlIsStillPartiallyOnScreen];
-[_UIRefreshControlModernContentView attributedTitle];
-[_UIRefreshControlModernContentView impactIntensity];
-[_UIRefreshControlModernContentView _spin];
-[_UIRefreshControlModernContentView areAnimationsValid];
-[_UIRefreshControlModernContentView _reveal];
-[_UIRefreshControlModernContentView _cleanUpAfterRevealing];
-[_UIRefreshControlModernContentView maximumSnappingHeight];
-[_UIRefreshControlModernContentView setRefreshControl:];
-[_UIRefreshControlModernContentView _maximumSnappingHeightScalingForScrollViewHeight];
-[_UIRefreshControlModernContentView _setBloomedAppearance];
-[_UIRefreshControlModernContentView setImpactIntensity:];
-[_UIRefreshControlModernContentView horizontallyCenteredFramesNeedUpdate];
-[_UIRefreshControlModernContentView setAreAnimationsValid:];
-[_UIRefreshControlModernContentView _unbloomedSeedTransform];
-[_UIRefreshControlModernContentView _removeAllAnimations];
-[_UIRefreshControlModernContentView initWithFrame:];
-[_UIRefreshControlModernContentView _bloom];
-[_UIRefreshControlModernContentView _goAway];
-[_UIRefreshControlModernContentView _tick];
```
