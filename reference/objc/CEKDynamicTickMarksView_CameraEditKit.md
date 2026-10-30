# `CEKDynamicTickMarksView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_TtP13CameraEditKit19TickMarksDataSource_`, `_TtP13CameraEditKit17TickMarksDelegate_`, `CEKTickMarksContainer`, `CEKImageTickMarksConfiguration`, `CEKCellTickMarksConfiguration`
- 20 instance variables, 28 properties, 65 instance methods, 0 class methods

## Instance variables

```
B _enabled;
B _highlightSelectedIndex;
B __needsTickMarkRefresh;
B __waveAnimationDelayActive;
@"<CEKTickMarksImageDataProvider>" _imageDataProvider;
@"<CEKTickMarksCellDataProvider>" _cellDataProvider;
@"_TtC13CameraEditKit14TickMarksModel" _tickMarksModel;
@"<CEKSliderTickMarksDelegate>" _delegate;
Q _selectedTickMarkIndex;
@"NSIndexSet" _magneticTickMarkIndexes;
@"UIColor" _selectedTickColor;
@"NSArray" _tickColorGradient;
@"NSMutableSet" __tickMarksReusePool;
@"NSMutableDictionary" __tickMarksByIndex;
@"_TtC13CameraEditKit24TickMarksVisibilityModel" __tickMarksVisibilityModel;
@"NSIndexSet" __installedTickMarkIndexes;
@"NSIndexSet" __selectedIndexes;
@"NSMutableIndexSet" __waveIndexes;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleBounds;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _contentTransform;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V__tickMarksReusePool) _tickMarksReusePool;
@property (T@"NSMutableDictionary",R,N,V__tickMarksByIndex) _tickMarksByIndex;
@property (T@"_TtC13CameraEditKit24TickMarksVisibilityModel",R,N,V__tickMarksVisibilityModel) _tickMarksVisibilityModel;
@property (T@"NSIndexSet",&,N,S_setInstalledTickMarkIndexes:,V__installedTickMarkIndexes) _installedTickMarkIndexes;
@property (TB,R,N,G_isUsingImages) _usingImages;
@property (TB,R,N,G_isUsingCells) _usingCells;
@property (T@"NSIndexSet",&,N,S_setSelectedIndexes:,V__selectedIndexes) _selectedIndexes;
@property (TB,R,N,V__needsTickMarkRefresh) _needsTickMarkRefresh;
@property (T@"NSMutableIndexSet",&,N,S_setWaveIndexes:,V__waveIndexes) _waveIndexes;
@property (TB,N,S_setWaveAnimationDelayActive:,V__waveAnimationDelayActive) _waveAnimationDelayActive;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_visibleBounds) visibleBounds;
@property (TQ,N,V_selectedTickMarkIndex) selectedTickMarkIndex;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"NSIndexSet",&,N,V_magneticTickMarkIndexes) magneticTickMarkIndexes;
@property (TB,N,V_highlightSelectedIndex) highlightSelectedIndex;
@property (T@"UIColor",&,N,V_selectedTickColor) selectedTickColor;
@property (T@"NSArray",C,N,V_tickColorGradient) tickColorGradient;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{UIEdgeInsets=dddd},R,D,N) alignmentRectInsets;
@property (T@"<CEKSliderTickMarksDelegate>",W,N,V_delegate) delegate;
@property (T@"_TtC13CameraEditKit14TickMarksModel",R,N,V_tickMarksModel) tickMarksModel;
@property (T@"<CEKTickMarksImageDataProvider>",W,N,V_imageDataProvider) imageDataProvider;
@property (T{CGAffineTransform=dddddd},N,V_contentTransform) contentTransform;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<CEKTickMarksCellDataProvider>",W,N,V_cellDataProvider) cellDataProvider;
```

## Instance methods

```
-[CEKDynamicTickMarksView _frameForTickMarkAtIndex:selected:];
-[CEKDynamicTickMarksView highlightSelectedIndex];
-[CEKDynamicTickMarksView _colorForTickMarkAtIndex:selected:isTickEnabled:];
-[CEKDynamicTickMarksView _tickMarksReusePool];
-[CEKDynamicTickMarksView _dequeueAndInstallTickMarkForIndex:];
-[CEKDynamicTickMarksView _waveAnimationDelayActive];
-[CEKDynamicTickMarksView _layoutDynamicCellTickMark:atIndex:];
-[CEKDynamicTickMarksView _isUsingCells];
-[CEKDynamicTickMarksView _lengthForMagneticTickMark];
-[CEKDynamicTickMarksView tickMarksModelDidChangeAppearanceWithModel:];
-[CEKDynamicTickMarksView _needsTickMarkRefresh];
-[CEKDynamicTickMarksView _setInstalledTickMarkIndexes:];
-[CEKDynamicTickMarksView _waveIndexes];
-[CEKDynamicTickMarksView _removeAndEnqueueTickMarkAtIndex:];
-[CEKDynamicTickMarksView tickMarksModelDidChangeWidthForTickMarkCountWithModel:];
-[CEKDynamicTickMarksView performWaveAnimation];
-[CEKDynamicTickMarksView setContentTransform:];
-[CEKDynamicTickMarksView selectedTickMarkIndex];
-[CEKDynamicTickMarksView layoutSubviews];
-[CEKDynamicTickMarksView _installedTickMarkIndexes];
-[CEKDynamicTickMarksView _configureTickMark:forIndex:];
-[CEKDynamicTickMarksView _tickMarksVisibilityModel];
-[CEKDynamicTickMarksView contentTransform];
-[CEKDynamicTickMarksView _configureHighlightForTickMark:atIndex:];
-[CEKDynamicTickMarksView setContentTransform:animated:];
-[CEKDynamicTickMarksView _selectedIndexes];
-[CEKDynamicTickMarksView isEnabled];
-[CEKDynamicTickMarksView _lengthForStandardTickMark];
-[CEKDynamicTickMarksView _recycleTickMarks];
-[CEKDynamicTickMarksView selectedTickColor];
-[CEKDynamicTickMarksView setDelegate:];
-[CEKDynamicTickMarksView visibleBounds];
-[CEKDynamicTickMarksView setImageDataProvider:];
-[CEKDynamicTickMarksView setTickColorGradient:];
-[CEKDynamicTickMarksView setMagneticTickMarkIndexes:];
-[CEKDynamicTickMarksView setSelectedTickMarkIndex:];
-[CEKDynamicTickMarksView setEnabled:];
-[CEKDynamicTickMarksView setSelectedTickColor:];
-[CEKDynamicTickMarksView _isUsingImages];
-[CEKDynamicTickMarksView cellDataProvider];
-[CEKDynamicTickMarksView setSelectedTickMarkIndex:animated:];
-[CEKDynamicTickMarksView delegate];
-[CEKDynamicTickMarksView _setWaveIndexes:];
-[CEKDynamicTickMarksView setHighlightSelectedIndex:];
-[CEKDynamicTickMarksView _destroyAllTickMarks];
-[CEKDynamicTickMarksView setHighlightSelectedIndex:animated:];
-[CEKDynamicTickMarksView magneticTickMarkIndexes];
-[CEKDynamicTickMarksView setVisibleBounds:];
-[CEKDynamicTickMarksView tickColorGradient];
-[CEKDynamicTickMarksView _lengthForSelectedTickMark];
-[CEKDynamicTickMarksView _refreshTickMarksHighlight];
-[CEKDynamicTickMarksView _refreshTickMarks];
-[CEKDynamicTickMarksView _bounds:containsTickMarkAtIndex:];
-[CEKDynamicTickMarksView imageDataProvider];
-[CEKDynamicTickMarksView _setWaveAnimationDelayActive:];
-[CEKDynamicTickMarksView setCellDataProvider:];
-[CEKDynamicTickMarksView _configureTickMark:forIndex:selected:];
-[CEKDynamicTickMarksView _setNeedsRefreshTickMarks];
-[CEKDynamicTickMarksView _indexesIntersectingVisibleBounds];
-[CEKDynamicTickMarksView reloadContent];
-[CEKDynamicTickMarksView frameForTickMarkAtIndex:];
-[CEKDynamicTickMarksView initWithFrame:];
-[CEKDynamicTickMarksView _tickMarksByIndex];
-[CEKDynamicTickMarksView _setSelectedIndexes:];
-[CEKDynamicTickMarksView tickMarksModel];
```
