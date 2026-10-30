# `_UIInteractivePageControlVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIPageControlVisualProvider`
- Protocols: `_UIPageIndicatorFeedDelegate`, `_UIPageIndicatorStoreDelegate`, `UIGestureRecognizerDelegate`, `_UIControlEventsGestureRecognizerDelegate`
- 29 instance variables, 24 properties, 87 instance methods, 0 class methods

## Instance variables

```
{?="scrubbing"b1"platterExpanded"b1"didScrubPastInitialThreshold"b1} _state;
q _indicatorStartIndex;
q _numberOfVisibleIndicators;
q _targetPage;
q _currentTick;
q _tickThreshold;
d _panDistance;
d _indicatorPaddingOffset;
d _continuousStartIndex;
B _hasGlassBackground;
@"UIView" _backgroundView;
@"_UIPageControlContentView" _contentView;
@"_UIPageControlIndicatorContentView" _indicatorContentView;
@"CADisplayLink" _displayLink;
@"UITapGestureRecognizer" _tapGestureRecognizer;
@"UILongPressGestureRecognizer" _scrubbingGestureRecognizer;
d _preciseTouchedPage;
@"UIDelayedAction" _successiveTapAction;
q _previousMoveDirection;
@"_UIPageIndicatorFeed" _indicatorFeed;
@"_UIPageIndicatorStore" _indicatorStore;
@"_UIPageControlInteractor" _interactor;
@"UIViewFloatAnimatableProperty" _continuousDisplayedPage;
@"UIViewFloatAnimatableProperty" _scrubProgress;
@"CAMediaTimingFunction" _indicatorTransformCurve;
q _resolvedDirection;
@"UISelectionFeedbackGenerator" _selectionFeedbackGenerator;
@"UIImpactFeedbackGenerator" _joggingFeedbackGenerator;
{CGPoint="x"d"y"d} _previousTouchLocation;
```

## Properties

```
@property (T@"_UIPageControlContentView",&,N,V_contentView) contentView;
@property (T@"_UIPageControlIndicatorContentView",&,N,V_indicatorContentView) indicatorContentView;
@property (TB,N,GisPlatterExpanded) platterExpanded;
@property (TB,N,GisScrubbing) scrubbing;
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T@"UITapGestureRecognizer",&,N,V_tapGestureRecognizer) tapGestureRecognizer;
@property (T@"UILongPressGestureRecognizer",&,N,V_scrubbingGestureRecognizer) scrubbingGestureRecognizer;
@property (Td,N,V_preciseTouchedPage) preciseTouchedPage;
@property (T@"UIDelayedAction",&,N,V_successiveTapAction) successiveTapAction;
@property (Tq,N,V_previousMoveDirection) previousMoveDirection;
@property (T{CGPoint=dd},N,V_previousTouchLocation) previousTouchLocation;
@property (T@"_UIPageIndicatorFeed",&,N,V_indicatorFeed) indicatorFeed;
@property (T@"_UIPageIndicatorStore",&,N,V_indicatorStore) indicatorStore;
@property (T@"_UIPageControlInteractor",&,N,V_interactor) interactor;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_continuousDisplayedPage) continuousDisplayedPage;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_scrubProgress) scrubProgress;
@property (T@"CAMediaTimingFunction",&,N,V_indicatorTransformCurve) indicatorTransformCurve;
@property (Tq,R,N,V_resolvedDirection) resolvedDirection;
@property (T@"UISelectionFeedbackGenerator",&,N,V_selectionFeedbackGenerator) selectionFeedbackGenerator;
@property (T@"UIImpactFeedbackGenerator",&,N,V_joggingFeedbackGenerator) joggingFeedbackGenerator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIInteractivePageControlVisualProvider displayLink];
-[_UIInteractivePageControlVisualProvider tapGestureRecognizer];
-[_UIInteractivePageControlVisualProvider invalidateIndicators];
-[_UIInteractivePageControlVisualProvider didTapPageControl:];
-[_UIInteractivePageControlVisualProvider scrubProgress];
-[_UIInteractivePageControlVisualProvider previousMoveDirection];
-[_UIInteractivePageControlVisualProvider interactor];
-[_UIInteractivePageControlVisualProvider setContentView:];
-[_UIInteractivePageControlVisualProvider didUpdateNumberOfPages];
-[_UIInteractivePageControlVisualProvider intrinsicContentSize];
-[_UIInteractivePageControlVisualProvider indicatorTransformCurve];
-[_UIInteractivePageControlVisualProvider isPlatterExpanded];
-[_UIInteractivePageControlVisualProvider updateDisplayedPageToCurrentPage];
-[_UIInteractivePageControlVisualProvider shouldDisableTouchTracking];
-[_UIInteractivePageControlVisualProvider setPreferredIndicatorImage:];
-[_UIInteractivePageControlVisualProvider setCustomActiveIndicatorImage:forPage:];
-[_UIInteractivePageControlVisualProvider setScrubbing:];
-[_UIInteractivePageControlVisualProvider previousTouchLocation];
-[_UIInteractivePageControlVisualProvider traitCollectionDidChangeOnSubtree:];
-[_UIInteractivePageControlVisualProvider resolvedDirection];
-[_UIInteractivePageControlVisualProvider setIndicatorTransformCurve:];
-[_UIInteractivePageControlVisualProvider successiveTapAction];
-[_UIInteractivePageControlVisualProvider isScrubbing];
-[_UIInteractivePageControlVisualProvider layoutSubviews];
-[_UIInteractivePageControlVisualProvider selectionFeedbackGenerator];
-[_UIInteractivePageControlVisualProvider sizeForNumberOfPages:];
-[_UIInteractivePageControlVisualProvider scrubbingGestureRecognizer];
-[_UIInteractivePageControlVisualProvider configureIndicator:atPage:];
-[_UIInteractivePageControlVisualProvider configureIndicatorImagesForIndicator:atPage:];
-[_UIInteractivePageControlVisualProvider setInteractor:];
-[_UIInteractivePageControlVisualProvider setPreviousTouchLocation:];
-[_UIInteractivePageControlVisualProvider setScrubProgress:];
-[_UIInteractivePageControlVisualProvider customIndicatorImageForPage:];
-[_UIInteractivePageControlVisualProvider preferredIndicatorImage];
-[_UIInteractivePageControlVisualProvider setCustomIndicatorImage:forPage:];
-[_UIInteractivePageControlVisualProvider setPreviousMoveDirection:];
-[_UIInteractivePageControlVisualProvider setPreferredActiveIndicatorImage:];
-[_UIInteractivePageControlVisualProvider indicatorContentView];
-[_UIInteractivePageControlVisualProvider setDisplayLink:];
-[_UIInteractivePageControlVisualProvider setJoggingFeedbackGenerator:];
-[_UIInteractivePageControlVisualProvider sizeThatFits:];
-[_UIInteractivePageControlVisualProvider setActivePageIndicatorVibrantColorMatrix:];
-[_UIInteractivePageControlVisualProvider indicatorStore];
-[_UIInteractivePageControlVisualProvider gestureRecognizerShouldBegin:];
-[_UIInteractivePageControlVisualProvider setIndicatorOpacity:];
-[_UIInteractivePageControlVisualProvider setIndicatorContentView:];
-[_UIInteractivePageControlVisualProvider preferredActiveIndicatorImage];
-[_UIInteractivePageControlVisualProvider didUpdateBackgroundEffect];
-[_UIInteractivePageControlVisualProvider prepare];
-[_UIInteractivePageControlVisualProvider setIndicatorFeed:];
-[_UIInteractivePageControlVisualProvider didUpdatePageIndicatorTintColor];
-[_UIInteractivePageControlVisualProvider didUpdateCurrentPageIndicatorTintColor];
-[_UIInteractivePageControlVisualProvider gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIInteractivePageControlVisualProvider contentView];
-[_UIInteractivePageControlVisualProvider pruneArchivedSubviews:];
-[_UIInteractivePageControlVisualProvider backgroundView];
-[_UIInteractivePageControlVisualProvider setSuccessiveTapAction:];
-[_UIInteractivePageControlVisualProvider didUpdateBackgroundStyle];
-[_UIInteractivePageControlVisualProvider indicatorFeed];
-[_UIInteractivePageControlVisualProvider indicatorSizeForImage:];
-[_UIInteractivePageControlVisualProvider indicatorOpacity];
-[_UIInteractivePageControlVisualProvider preciseTouchedPage];
-[_UIInteractivePageControlVisualProvider joggingFeedbackGenerator];
-[_UIInteractivePageControlVisualProvider didUpdateInteractionTypeAvailability];
-[_UIInteractivePageControlVisualProvider continuousDisplayedPage];
-[_UIInteractivePageControlVisualProvider setScrubbingGestureRecognizer:];
-[_UIInteractivePageControlVisualProvider setTapGestureRecognizer:];
-[_UIInteractivePageControlVisualProvider didUpdateLayoutDirection];
-[_UIInteractivePageControlVisualProvider didUpdatePageProgress];
-[_UIInteractivePageControlVisualProvider setPreciseTouchedPage:];
-[_UIInteractivePageControlVisualProvider setIndicatorStore:];
-[_UIInteractivePageControlVisualProvider didUpdateCustomLayoutValues];
-[_UIInteractivePageControlVisualProvider setContinuousDisplayedPage:];
-[_UIInteractivePageControlVisualProvider resetSuccessiveTapInfo];
-[_UIInteractivePageControlVisualProvider setPlatterExpanded:];
-[_UIInteractivePageControlVisualProvider maxVisibleIndicators];
-[_UIInteractivePageControlVisualProvider setSelectionFeedbackGenerator:];
-[_UIInteractivePageControlVisualProvider displayLinkTicked:];
-[_UIInteractivePageControlVisualProvider controlEventsGestureRecognizer:recognizedControlEvent:withEvent:];
-[_UIInteractivePageControlVisualProvider setBackgroundView:];
-[_UIInteractivePageControlVisualProvider supportsContinuousInteraction];
-[_UIInteractivePageControlVisualProvider setPage:interactionState:];
-[_UIInteractivePageControlVisualProvider didUpdateCurrentPageProgress];
-[_UIInteractivePageControlVisualProvider indicatorFrameForPage:];
-[_UIInteractivePageControlVisualProvider customActiveIndicatorImageForPage:];
-[_UIInteractivePageControlVisualProvider didScrubPageControl:];
-[_UIInteractivePageControlVisualProvider setPageIndicatorVibrantColorMatrix:];
```
