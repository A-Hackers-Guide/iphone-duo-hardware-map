# `UIMovieScrubber`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIMovieScrubberTrackViewDataSource`, `UIMovieScrubberTrackViewDelegate`
- 30 instance variables, 24 properties, 97 instance methods, 2 class methods

## Instance variables

```
@"UIImageView" _thumbView;
@"UIMovieScrubberTrackView" _trackView;
@"UIMovieScrubberEditingView" _editingView;
@"UILabel" _elapsedLabel;
@"UILabel" _remainingLabel;
i _timeComponents;
@"UIImage" _fillImage;
@"UIImage" _innerShadowImage;
@"UIImage" _maskImage;
@"UIImage" _shadowImage;
@"<UIMovieScrubberDataSource>" _dataSource;
@"<UIMovieScrubberDelegate>" _delegate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _trackRect;
d _hitOffset;
d _zoomDelay;
B _showTimeViews;
B _editable;
d _value;
d _maximumValue;
d _minimumValue;
{CGPoint="x"d"y"d} _touchLocationWhenTrackPressBegan;
d _trimStartValue;
d _trimEndValue;
d _minTrimmedLength;
d _maxTrimmedLength;
d _zoomAnimationDuration;
d _zoomAnimationDelay;
{?="continuous"b1"animating"b1"creatingSnapshot"b1"needsReload"b1"layoutTimeViews"b1"computeTrackRect"b1"clampingTrimRange"I"zoomed"b1"zoomAnimating"b1"trackIsPressed"b1"trackAnimating"b1"thumbIsVisible"b1"handleIsPressed"b1"willBeginEditing"b1"editing"b1"editingHandle"I"rotationDisabled"I"isInNavigationBar"b1"delegateValueDidChange"b1"delegateStartValueDidChange"b1"delegateEndValueDidChange"b1"delegateWillBeginRequestingThumbnails"b1"delegateDidFinishRequestingThumbnails"b1"delegateWillBeginEditing"b1"delegateDidBeginEditing"b1"delegateDidCancelEditing"b1"delegateEditingAnimationFinished"b1"delegateWidthDeltaOriginXDelta"b1"delegateDidBeginAnimatingZoom"b1"delegateDidEndAnimatingZoom"b1"delegateWillZoom"b1"dataSourceRequestThumbnailImageIsSummmary"b1} _sliderFlags;
@"UIPanGestureRecognizer" _panGestureRecognizer;
d _edgeInset;
```

## Properties

```
@property (Td,N) value;
@property (Td,D,N) duration;
@property (Td,N,V_minTrimmedLength) minimumTrimLength;
@property (Td,N,V_maxTrimmedLength) maximumTrimLength;
@property (Td,N) trimStartValue;
@property (Td,N) trimEndValue;
@property (Td,R,N) zoomMinimumValue;
@property (Td,R,N) zoomMaximumValue;
@property (TB,R,N,GisZoomAnimating) zoomAnimating;
@property (TB,N) thumbIsVisible;
@property (TB,N,GisEditable) editable;
@property (TB,N,GisContinuous) continuous;
@property (T@"<UIMovieScrubberDataSource>",N) dataSource;
@property (T@"<UIMovieScrubberDelegate>",N) delegate;
@property (Td,N,V_zoomDelay) zoomDelay;
@property (TB,N,V_showTimeViews) showTimeViews;
@property (TB,R,N) isInsideNavigationBar;
@property (Td,N,V_edgeInset) edgeInset;
@property (T{UIEdgeInsets=dddd},R,N) alignmentMargins;
@property (TB,N,GisEditing) editing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIMovieScrubber _allowActionsToQueue];
+[UIMovieScrubber timeStringForSeconds:forceFullWidthComponents:isElapsed:];
```

## Instance methods

```
-[UIMovieScrubber isEditable];
-[UIMovieScrubber cancelTouchTracking];
-[UIMovieScrubber setValue:animated:];
-[UIMovieScrubber didMoveToWindow];
-[UIMovieScrubber intrinsicContentSize];
-[UIMovieScrubber init];
-[UIMovieScrubber setContinuous:];
-[UIMovieScrubber dealloc];
-[UIMovieScrubber isAnimatingValueChange];
-[UIMovieScrubber value];
-[UIMovieScrubber setEditing:animated:];
-[UIMovieScrubber layoutSubviews];
-[UIMovieScrubber setDataSource:];
-[UIMovieScrubber isContinuous];
-[UIMovieScrubber duration];
-[UIMovieScrubber reloadData];
-[UIMovieScrubber sizeThatFits:];
-[UIMovieScrubber setDelegate:];
-[UIMovieScrubber setValue:];
-[UIMovieScrubber setEditing:];
-[UIMovieScrubber dataSource];
-[UIMovieScrubber delegate];
-[UIMovieScrubber _sliderValueDidChange:];
-[UIMovieScrubber setFrame:];
-[UIMovieScrubber setEditable:];
-[UIMovieScrubber _controlTouchBegan:withEvent:];
-[UIMovieScrubber _handlePanGesture:];
-[UIMovieScrubber _controlTouchMoved:withEvent:];
-[UIMovieScrubber setDuration:];
-[UIMovieScrubber didMoveToSuperview];
-[UIMovieScrubber isEditing];
-[UIMovieScrubber initWithFrame:];
-[UIMovieScrubber _controlTouchEnded:withEvent:];
-[UIMovieScrubber isZoomAnimating];
-[UIMovieScrubber movieScrubberTrackViewDuration:];
-[UIMovieScrubber setThumbnailImage:forTimestamp:];
-[UIMovieScrubber _alwaysHandleScrollerMouseEvent];
-[UIMovieScrubber _animateAfterEdit:];
-[UIMovieScrubber _beginTrackPressWithLocatable:touchesBegan:];
-[UIMovieScrubber _cancelTrackPress:];
-[UIMovieScrubber _cancelTrackPressIfNeccessaryWithLocatable:];
-[UIMovieScrubber _computeTrackRectForBounds:];
-[UIMovieScrubber _editingHandleWithLocatable:];
-[UIMovieScrubber _editingRect];
-[UIMovieScrubber _editingRectForStartTime:endTime:];
-[UIMovieScrubber _initSubviews];
-[UIMovieScrubber _setValue:andSendAction:];
-[UIMovieScrubber _setZoomAnimating:];
-[UIMovieScrubber _sliderAnimationDidStop:];
-[UIMovieScrubber _sliderAnimationWillStart];
-[UIMovieScrubber _trackPressWasHeld];
-[UIMovieScrubber _trimAnimationDidStop:glassView:];
-[UIMovieScrubber _updateThumbLocation];
-[UIMovieScrubber _updateTimes];
-[UIMovieScrubber _valueForLocatable:];
-[UIMovieScrubber alignmentMargins];
-[UIMovieScrubber animateAfterEdit];
-[UIMovieScrubber animateCancelEdit];
-[UIMovieScrubber beginTrackingWithLocatable:];
-[UIMovieScrubber continueTrackingWithLocatable:];
-[UIMovieScrubber edgeInset];
-[UIMovieScrubber endTrackingWithLocatable:];
-[UIMovieScrubber forceUnzoom];
-[UIMovieScrubber forceZoom];
-[UIMovieScrubber isInsideNavigationBar];
-[UIMovieScrubber maximumTrimLength];
-[UIMovieScrubber minimumTrimLength];
-[UIMovieScrubber movieScrubberTrackView:clampedSizeWidthDelta:actualSizeWidthDelta:originXDelta:minimumVisibleValue:maximumVisibleValue:];
-[UIMovieScrubber movieScrubberTrackView:evenlySpacedTimestamps:startingAt:endingAt:];
-[UIMovieScrubber movieScrubberTrackView:requestThumbnailImageForTimestamp:isSummaryThumbnail:];
-[UIMovieScrubber movieScrubberTrackViewDidCollapse:];
-[UIMovieScrubber movieScrubberTrackViewDidExpand:];
-[UIMovieScrubber movieScrubberTrackViewDidFinishRequestingThumbnails:];
-[UIMovieScrubber movieScrubberTrackViewThumbnailAspectRatio:];
-[UIMovieScrubber movieScrubberTrackViewWillBeginRequestingThumbnails:];
-[UIMovieScrubber movieScrubberTrackViewZoomAnimationDelay:];
-[UIMovieScrubber movieScrubberTrackViewZoomAnimationDuration:];
-[UIMovieScrubber pointInsideThumb:withEvent:];
-[UIMovieScrubber setEdgeInset:];
-[UIMovieScrubber setMaximumTrimLength:];
-[UIMovieScrubber setMinimumTrimLength:];
-[UIMovieScrubber setRotationDisabled:];
-[UIMovieScrubber setShowTimeViews:];
-[UIMovieScrubber setThumbIsVisible:];
-[UIMovieScrubber setTrimEndValue:];
-[UIMovieScrubber setTrimStartValue:];
-[UIMovieScrubber setZoomAnimationDuration:];
-[UIMovieScrubber setZoomDelay:];
-[UIMovieScrubber showTimeViews];
-[UIMovieScrubber thumbIsVisible];
-[UIMovieScrubber thumbRectForValue:];
-[UIMovieScrubber trackRect];
-[UIMovieScrubber trimEndValue];
-[UIMovieScrubber trimStartValue];
-[UIMovieScrubber zoomDelay];
-[UIMovieScrubber zoomMaximumValue];
-[UIMovieScrubber zoomMinimumValue];
```
