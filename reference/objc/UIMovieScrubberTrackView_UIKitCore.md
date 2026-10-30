# `UIMovieScrubberTrackView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 21 instance variables, 2 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _summaryThumbnailViews;
@"NSArray" _summaryThumbnailTimestamps;
@"NSArray" _summaryThumbnailChildTimestamps;
@"NSDictionary" _thumbnailStartXValues;
@"NSDictionary" _childThumbnailViews;
@"NSMutableDictionary" _thumbnailViews;
@"NSArray" _timestamps;
@"UIMovieScrubberTrackOverlayView" _overlayView;
@"UIView" _maskContainerView;
{CGSize="width"d"height"d} _thumbnailSize;
f _zoomOriginXDelta;
f _zoomWidthDelta;
f _unclampedZoomWidthDelta;
f _zoomAnimationDuration;
d _duration;
d _value;
d _startValue;
d _endValue;
{?="delegateSizeOriginDelta"b1"delegateDidExpand"b1"delegateDidCollapse"b1"delegateWillRequestThumbs"b1"delegateDidRequestThumbs"b1"delegateZoomAnimationDuration"b1"delegateZoomAnimationDelay"b1"needsReload"b1"editing"b1"editingHandle"I"zoomIsDisabled"b1} _trackFlags;
@"<UIMovieScrubberTrackViewDataSource>" _dataSource;
@"<UIMovieScrubberTrackViewDelegate>" _delegate;
```

## Properties

```
@property (T@"<UIMovieScrubberTrackViewDataSource>",W,N,V_dataSource) dataSource;
@property (T@"<UIMovieScrubberTrackViewDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[UIMovieScrubberTrackView clear];
-[UIMovieScrubberTrackView layoutSubviews];
-[UIMovieScrubberTrackView setDataSource:];
-[UIMovieScrubberTrackView reloadData];
-[UIMovieScrubberTrackView setDelegate:];
-[UIMovieScrubberTrackView setValue:];
-[UIMovieScrubberTrackView setEditing:];
-[UIMovieScrubberTrackView dataSource];
-[UIMovieScrubberTrackView zoomAtPoint:];
-[UIMovieScrubberTrackView delegate];
-[UIMovieScrubberTrackView initWithFrame:];
-[UIMovieScrubberTrackView setThumbnailImage:forTimestamp:];
-[UIMovieScrubberTrackView _createImageViewForTimestamp:isSummaryThumbnail:];
-[UIMovieScrubberTrackView _reallyReloadData];
-[UIMovieScrubberTrackView _setOverlayViewIsZoomed:minValue:maxValue:];
-[UIMovieScrubberTrackView _unzoomAnimationDidFinish];
-[UIMovieScrubberTrackView _zoomAnimationDidFinish];
-[UIMovieScrubberTrackView animateFillFramesAway];
-[UIMovieScrubberTrackView setEndValue:];
-[UIMovieScrubberTrackView setStartValue:];
-[UIMovieScrubberTrackView setZoomAnimationDuration:];
-[UIMovieScrubberTrackView unzoom];
-[UIMovieScrubberTrackView zoomAnimationDuration];
```
