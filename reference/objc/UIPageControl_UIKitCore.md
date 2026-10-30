# `UIPageControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 17 instance variables, 30 properties, 96 instance methods, 2 class methods

## Instance variables

```
@"_UIPageControlVisualProvider" _visualProvider;
{?="hideForSinglePage"b1"defersCurrentPageDisplay"b1"allowScrubbing"b1"allowTapping"b1"flickToEndGestureEnabled"b1"prefersTargetPageForDiscreteInteraction"b1} _pageControlFlags;
{?="verticalPadding"b1"horizontalPadding"b1"indicatorSpacing"b1"backgroundView"b1} _custom;
d _horizontalPadding;
d _verticalPadding;
d _indicatorSpacing;
d _minimumPressDurationForContinuousInteraction;
Q _preferredNumberOfVisibleIndicators;
q _numberOfPages;
q _currentPage;
@"UIPageControlProgress" _progress;
@"UIColor" _pageIndicatorTintColor;
@"UIColor" _currentPageIndicatorTintColor;
q _backgroundStyle;
q _direction;
q _previousPage;
@"UIVisualEffect" __platterEffect;
```

## Properties

```
@property (Td,N,S_setCustomHorizontalPadding:) _customHorizontalPadding;
@property (Td,N,S_setCustomVerticalPadding:) _customVerticalPadding;
@property (Td,N,S_setCustomIndicatorSpacing:) _customIndicatorSpacing;
@property (Td,N,S_setOverrideMinimumPressDurationForContinuousInteraction:) _overrideMinimumPressDurationForContinuousInteraction;
@property (TQ,N,G_preferredNumberOfVisibleIndicators,S_setPreferredNumberOfVisibleIndicators:) preferredNumberOfVisibleIndicators;
@property (TB,N,S_setAllowsDiscreteInteraction:) _allowsDiscreteInteraction;
@property (Td,N,S_setIndicatorOpacity:) _indicatorOpacity;
@property (T@"UIView",&,N,S_setPlatterBackgroundView:) _platterBackgroundView;
@property (TB,N,S_setPrefersTargetPageForDiscreteInteraction:) _prefersTargetPageForDiscreteInteraction;
@property (T{CGAffineTransform=dddddd},N,S_setActiveTransformForTouchedPage:) _activeTransformForTouchedPage;
@property (T{CGAffineTransform=dddddd},N,S_setTargetTransformForTouchedPage:) _targetTransformForTouchedPage;
@property (T{CAColorMatrix=ffffffffffffffffffff},N,S_setPageIndicatorVibrantColorMatrix:) _pageIndicatorVibrantColorMatrix;
@property (T{CAColorMatrix=ffffffffffffffffffff},N,S_setActivePageIndicatorVibrantColorMatrix:) _activePageIndicatorVibrantColorMatrix;
@property (Tq,N,V_previousPage) previousPage;
@property (TB,N,S_setFlickToEndGestureEnabled:) _flickToEndGestureEnabled;
@property (T@"UIVisualEffect",&,N,S_setPlatterEffect:,V__platterEffect) _platterEffect;
@property (T@"UIPageControlProgress",&,N,S_setPageProgress:) _pageProgress;
@property (Tq,N,V_numberOfPages) numberOfPages;
@property (Tq,N,V_currentPage) currentPage;
@property (TB,N) hidesForSinglePage;
@property (T@"UIPageControlProgress",&,N,V_progress) progress;
@property (T@"UIColor",&,N,V_pageIndicatorTintColor) pageIndicatorTintColor;
@property (T@"UIColor",&,N,V_currentPageIndicatorTintColor) currentPageIndicatorTintColor;
@property (Tq,N,V_backgroundStyle) backgroundStyle;
@property (Tq,N,V_direction) direction;
@property (Tq,R,N) interactionState;
@property (TB,N) allowsContinuousInteraction;
@property (T@"UIImage",&,N) preferredIndicatorImage;
@property (T@"UIImage",&,N) preferredCurrentPageIndicatorImage;
@property (TB,N) defersCurrentPageDisplay;
```

## Class methods

```
+[UIPageControl doesOverrideMethod:inBaseClass:];
+[UIPageControl _visualProviderForPageControl:];
```

## Instance methods

```
-[UIPageControl _controlEventsForActionTriggered];
-[UIPageControl didMoveToWindow];
-[UIPageControl intrinsicContentSize];
-[UIPageControl setProgress:];
-[UIPageControl setPreferredIndicatorImage:];
-[UIPageControl endTrackingWithTouch:withEvent:];
-[UIPageControl setCurrentPage:];
-[UIPageControl dealloc];
-[UIPageControl setDirection:];
-[UIPageControl layoutSubviews];
-[UIPageControl sizeForNumberOfPages:];
-[UIPageControl preferredIndicatorImage];
-[UIPageControl canBecomeFocused];
-[UIPageControl setSemanticContentAttribute:];
-[UIPageControl progress];
-[UIPageControl direction];
-[UIPageControl backgroundStyle];
-[UIPageControl sizeThatFits:];
-[UIPageControl _contentHuggingDefault_isUsuallyFixedHeight];
-[UIPageControl gestureRecognizerShouldBegin:];
-[UIPageControl currentPage];
-[UIPageControl encodeWithCoder:];
-[UIPageControl isElementAccessibilityExposedToInterfaceBuilder];
-[UIPageControl numberOfPages];
-[UIPageControl initWithCoder:];
-[UIPageControl _populateArchivedSubviews:];
-[UIPageControl interactionState];
-[UIPageControl _isVertical];
-[UIPageControl initWithFrame:];
-[UIPageControl setBackgroundStyle:];
-[UIPageControl _contentHuggingDefault_isUsuallyFixedWidth];
-[UIPageControl indicatorImageForPage:];
-[UIPageControl setAllowsContinuousInteraction:];
-[UIPageControl _activePageIndicatorVibrantColorMatrix];
-[UIPageControl _activeTransformForTouchedPage];
-[UIPageControl _allowsDiscreteInteraction];
-[UIPageControl _customHorizontalPadding];
-[UIPageControl _customIndicatorSpacing];
-[UIPageControl _customVerticalPadding];
-[UIPageControl _displayedPage];
-[UIPageControl _emitValueChanged];
-[UIPageControl _flickToEndGestureEnabled];
-[UIPageControl _implementsCustomCurrentPageImagesOverride];
-[UIPageControl _implementsCustomPageImagesOverride];
-[UIPageControl _indicatorFrameForPage:];
-[UIPageControl _indicatorOpacity];
-[UIPageControl _invalidateIndicators];
-[UIPageControl _overrideMinimumPressDurationForContinuousInteraction];
-[UIPageControl _pageIndicatorVibrantColorMatrix];
-[UIPageControl _pageProgress];
-[UIPageControl _platterBackgroundView];
-[UIPageControl _platterEffect];
-[UIPageControl _prefersTargetPageForDiscreteInteraction];
-[UIPageControl _setActivePageIndicatorVibrantColorMatrix:];
-[UIPageControl _setActiveTransformForTouchedPage:];
-[UIPageControl _setAllowsDiscreteInteraction:];
-[UIPageControl _setCurrentPage:];
-[UIPageControl _setCustomHorizontalPadding:];
-[UIPageControl _setCustomIndicatorSpacing:];
-[UIPageControl _setCustomVerticalPadding:];
-[UIPageControl _setFlickToEndGestureEnabled:];
-[UIPageControl _setIndicatorOpacity:];
-[UIPageControl _setOverrideMinimumPressDurationForContinuousInteraction:];
-[UIPageControl _setPage:interactionState:];
-[UIPageControl _setPageIndicatorVibrantColorMatrix:];
-[UIPageControl _setPageProgress:];
-[UIPageControl _setPlatterBackgroundView:];
-[UIPageControl _setPlatterEffect:];
-[UIPageControl _setPreferredNumberOfVisibleIndicators:];
-[UIPageControl _setPrefersTargetPageForDiscreteInteraction:];
-[UIPageControl _setTargetTransformForTouchedPage:];
-[UIPageControl _setVertical:];
-[UIPageControl _targetTransformForTouchedPage];
-[UIPageControl _traitCollectionDidChangeOnSubtreeInternal:];
-[UIPageControl _updateCurrentPage:updateDisplayImmediately:];
-[UIPageControl _updateCurrentPageDisplayWithForceUpdate:];
-[UIPageControl _updateCurrentPageProgress];
-[UIPageControl allowsContinuousInteraction];
-[UIPageControl currentPageIndicatorImageForPage:];
-[UIPageControl currentPageIndicatorTintColor];
-[UIPageControl defersCurrentPageDisplay];
-[UIPageControl hidesForSinglePage];
-[UIPageControl pageIndicatorTintColor];
-[UIPageControl preferredCurrentPageIndicatorImage];
-[UIPageControl previousPage];
-[UIPageControl setCurrentPageIndicatorImage:forPage:];
-[UIPageControl setCurrentPageIndicatorTintColor:];
-[UIPageControl setDefersCurrentPageDisplay:];
-[UIPageControl setHidesForSinglePage:];
-[UIPageControl setIndicatorImage:forPage:];
-[UIPageControl setNumberOfPages:];
-[UIPageControl setPageIndicatorTintColor:];
-[UIPageControl setPreferredCurrentPageIndicatorImage:];
-[UIPageControl setPreviousPage:];
-[UIPageControl shouldTrack];
-[UIPageControl updateCurrentPageDisplay];
```
