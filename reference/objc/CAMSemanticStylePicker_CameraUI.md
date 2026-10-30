# `CAMSemanticStylePicker`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIScrollViewDelegate`
- 17 instance variables, 26 properties, 61 instance methods, 0 class methods

## Instance variables

```
B _hidesSelfWhenNotExpanded;
B __selectedTileExpanded;
B __needsUpdateContentOffset;
Q _selectedStyleIndex;
Q _numberOfStyles;
q _material;
d _spacerWidth;
@"UIColor" _materialColor;
@"<CAMSemanticStylePickerDelegate>" _delegate;
d _contentBottomMargin;
@"UIPageControl" _pageControl;
q _pageControlMaxNumberOfDots;
@"UIScrollView" __scrollView;
@"NSMutableArray" __tileViews;
@"NSMutableArray" __spacerViews;
Q __expansionAnimationCounter;
@"CAMFeedbackController" __feedbackController;
```

## Properties

```
@property (T@"UIScrollView",R,N,V__scrollView) _scrollView;
@property (T@"NSMutableArray",R,N,V__tileViews) _tileViews;
@property (T@"NSMutableArray",R,N,V__spacerViews) _spacerViews;
@property (TB,N,S_setSelectedTileExpanded:,V__selectedTileExpanded) _selectedTileExpanded;
@property (TQ,N,S_setExpandedAnimationCounter:,V__expansionAnimationCounter) _expansionAnimationCounter;
@property (TB,N,S_setNeedsUpdateContentOffset:,V__needsUpdateContentOffset) _needsUpdateContentOffset;
@property (TB,R,N,G_isScrollActive) _scrollActive;
@property (T@"CAMFeedbackController",R,N,V__feedbackController) _feedbackController;
@property (TB,N) scrollEnabled;
@property (TB,N) scrollViewUserInteractionEnabled;
@property (TQ,N,V_selectedStyleIndex) selectedStyleIndex;
@property (TQ,N,V_numberOfStyles) numberOfStyles;
@property (Td,R,N) fractionalPageIndex;
@property (TB,N) expanded;
@property (TB,N,V_hidesSelfWhenNotExpanded) hidesSelfWhenNotExpanded;
@property (Tq,N,V_material) material;
@property (Td,N,V_spacerWidth) spacerWidth;
@property (T@"UIColor",N,V_materialColor) materialColor;
@property (T@"<CAMSemanticStylePickerDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_contentBottomMargin) contentBottomMargin;
@property (T@"UIPageControl",R,N,V_pageControl) pageControl;
@property (Tq,N,V_pageControlMaxNumberOfDots) pageControlMaxNumberOfDots;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSemanticStylePicker _feedbackController];
-[CAMSemanticStylePicker _scrollView];
-[CAMSemanticStylePicker setMaterial:withDuration:];
-[CAMSemanticStylePicker setExpanded:];
-[CAMSemanticStylePicker setMaterialColor:];
-[CAMSemanticStylePicker materialColor];
-[CAMSemanticStylePicker layoutSubviews];
-[CAMSemanticStylePicker hitTest:withEvent:];
-[CAMSemanticStylePicker setBounds:];
-[CAMSemanticStylePicker pageControl];
-[CAMSemanticStylePicker setDelegate:];
-[CAMSemanticStylePicker setScrollEnabled:];
-[CAMSemanticStylePicker setContentBottomMargin:];
-[CAMSemanticStylePicker delegate];
-[CAMSemanticStylePicker setFrame:];
-[CAMSemanticStylePicker _updateMaterialOpacityWithDuration:];
-[CAMSemanticStylePicker scrollEnabled];
-[CAMSemanticStylePicker contentBottomMargin];
-[CAMSemanticStylePicker setMaterial:];
-[CAMSemanticStylePicker material];
-[CAMSemanticStylePicker pointInside:withEvent:];
-[CAMSemanticStylePicker initWithFrame:];
-[CAMSemanticStylePicker setExpanded:animated:];
-[CAMSemanticStylePicker scrollViewDidScroll:];
-[CAMSemanticStylePicker expanded];
-[CAMSemanticStylePicker _setSelectedStyleIndex:shouldDelegate:shouldUpdateLayout:animated:];
-[CAMSemanticStylePicker _updateScrollViewContentOffset];
-[CAMSemanticStylePicker numberOfStyles];
-[CAMSemanticStylePicker _tileViews];
-[CAMSemanticStylePicker _handlePageControlValueChanged:];
-[CAMSemanticStylePicker _isScrollActive];
-[CAMSemanticStylePicker _performHaptics];
-[CAMSemanticStylePicker presentatationStyleRectAtIndex:];
-[CAMSemanticStylePicker setSelectedStyleIndex:animated:];
-[CAMSemanticStylePicker _prepareHaptics];
-[CAMSemanticStylePicker setSpacerWidth:];
-[CAMSemanticStylePicker _contentOffsetForIndex:];
-[CAMSemanticStylePicker _expansionAnimationCounter];
-[CAMSemanticStylePicker _fractionalIndexForContentOffset];
-[CAMSemanticStylePicker _fractionalIndexForContentOffset:];
-[CAMSemanticStylePicker _handlePageControlTouchDown:];
-[CAMSemanticStylePicker _needsUpdateContentOffset];
-[CAMSemanticStylePicker _selectedTileExpanded];
-[CAMSemanticStylePicker _setExpandedAnimationCounter:];
-[CAMSemanticStylePicker _setNeedsUpdateContentOffset:];
-[CAMSemanticStylePicker _setSelectedTileExpanded:];
-[CAMSemanticStylePicker _spacerViews];
-[CAMSemanticStylePicker _tileFrames];
-[CAMSemanticStylePicker _updateTileAlphas];
-[CAMSemanticStylePicker fractionalPageIndex];
-[CAMSemanticStylePicker hidesSelfWhenNotExpanded];
-[CAMSemanticStylePicker modelStyleRectAtIndex:];
-[CAMSemanticStylePicker pageControlMaxNumberOfDots];
-[CAMSemanticStylePicker scrollViewUserInteractionEnabled];
-[CAMSemanticStylePicker selectedStyleIndex];
-[CAMSemanticStylePicker setHidesSelfWhenNotExpanded:];
-[CAMSemanticStylePicker setNumberOfStyles:];
-[CAMSemanticStylePicker setPageControlMaxNumberOfDots:];
-[CAMSemanticStylePicker setScrollViewUserInteractionEnabled:];
-[CAMSemanticStylePicker setSelectedStyleIndex:];
-[CAMSemanticStylePicker spacerWidth];
```
