# `CAMSmartStylePreviewGridView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAMSmartStylePreviewViewDelegate`
- 11 instance variables, 19 properties, 38 instance methods, 1 class methods

## Instance variables

```
@"<CAMSmartStylePreviewGridViewDelegate>" _delegate;
Q _layout;
d _itemSpacing;
d _itemCornerRadius;
d _nonExpandedItemAlpha;
Q _expandedItemIndex;
@"CEKSmartStyle" _style;
@"CEKTextureStyle" _textureStyle;
@"NSString" _logIdentifier;
@"NSArray" __previewViews;
q __expansionAnimationCount;
```

## Properties

```
@property (T@"NSArray",R,N,V__previewViews) _previewViews;
@property (TB,R,N) _allowsExpandOnTap;
@property (Tq,N,S_setExpansionAnimationCount:,V__expansionAnimationCount) _expansionAnimationCount;
@property (T@"<CAMSmartStylePreviewGridViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R,N,V_layout) layout;
@property (TQ,R,N) gridItemCount;
@property (Td,N,V_itemSpacing) itemSpacing;
@property (Td,N,V_itemCornerRadius) itemCornerRadius;
@property (Td,N,V_nonExpandedItemAlpha) nonExpandedItemAlpha;
@property (TQ,N,V_expandedItemIndex) expandedItemIndex;
@property (TB,R,N) didFinishRendering;
@property (T@"CEKSmartStyle",&,N,V_style) style;
@property (T@"CEKTextureStyle",&,N,V_textureStyle) textureStyle;
@property (TB,R,N,GisAnimatingGrid) animatingGrid;
@property (T@"NSString",C,N,V_logIdentifier) logIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMSmartStylePreviewGridView gridItemCountForLayout:];
```

## Instance methods

```
-[CAMSmartStylePreviewGridView speedUpFadeInAnimations];
-[CAMSmartStylePreviewGridView nonExpandedItemAlpha];
-[CAMSmartStylePreviewGridView setNonExpandedItemAlpha:];
-[CAMSmartStylePreviewGridView itemCornerRadius];
-[CAMSmartStylePreviewGridView setPreviewZoomScale:animated:];
-[CAMSmartStylePreviewGridView setExpandedItemIndex:];
-[CAMSmartStylePreviewGridView _subviewFrame2x2ForIndex:];
-[CAMSmartStylePreviewGridView textureStyle];
-[CAMSmartStylePreviewGridView gridItemCount];
-[CAMSmartStylePreviewGridView updateGridIndex:withResourceLoadResult:];
-[CAMSmartStylePreviewGridView layoutSubviews];
-[CAMSmartStylePreviewGridView setLogIdentifier:];
-[CAMSmartStylePreviewGridView _subviewGeometryForIndex:];
-[CAMSmartStylePreviewGridView style];
-[CAMSmartStylePreviewGridView setTextureStyle:];
-[CAMSmartStylePreviewGridView _subviewFrameForIndex:];
-[CAMSmartStylePreviewGridView setStyle:];
-[CAMSmartStylePreviewGridView handleTap:];
-[CAMSmartStylePreviewGridView logIdentifier];
-[CAMSmartStylePreviewGridView _setExpansionAnimationCount:];
-[CAMSmartStylePreviewGridView _subviewFrame1Big5SmallForIndex:];
-[CAMSmartStylePreviewGridView initWithLayout:];
-[CAMSmartStylePreviewGridView _expansionAnimationCount];
-[CAMSmartStylePreviewGridView setDelegate:];
-[CAMSmartStylePreviewGridView setItemCornerRadius:];
-[CAMSmartStylePreviewGridView isAnimatingGrid];
-[CAMSmartStylePreviewGridView _allowsExpandOnTap];
-[CAMSmartStylePreviewGridView smartStylePreviewViewDidFinishRendering:];
-[CAMSmartStylePreviewGridView itemSpacing];
-[CAMSmartStylePreviewGridView setExpandedItemIndex:animated:];
-[CAMSmartStylePreviewGridView delegate];
-[CAMSmartStylePreviewGridView didFinishRendering];
-[CAMSmartStylePreviewGridView setItemSpacing:];
-[CAMSmartStylePreviewGridView _updateStyleOnPreviewViews];
-[CAMSmartStylePreviewGridView layout];
-[CAMSmartStylePreviewGridView setSmartStyle:textureStyle:];
-[CAMSmartStylePreviewGridView expandedItemIndex];
-[CAMSmartStylePreviewGridView _previewViews];
```
