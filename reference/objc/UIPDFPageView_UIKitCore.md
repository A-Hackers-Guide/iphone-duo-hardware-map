# `UIPDFPageView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 41 instance variables, 22 properties, 88 instance methods, 0 class methods

## Instance variables

```
@"UIPDFDocument" _document;
Q _pageIndex;
@"UIPDFViewTouchHandler" _touchHandler;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _pageToViewTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _viewToPageTransform;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cropBox;
d _margin;
B _allowSelection;
@"UIPDFSelectionController" _selectionController;
@"<NSObject><UIPDFPageViewDelegate>" _delegate;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} zoomRect;
B _useBackingLayer;
@"CALayer" _backingLayer;
@"UIImage" _backgroundImage;
B _backgroundIsScheduled;
Q _backgroundScheduleCount;
B _backgroundIsFullResolution;
B _boundsChanged;
B _useTiledContent;
B _enableLightMemoryFootprint;
@"CALayer" _contentLayer;
@"CALayer" _effectsLayer;
@"UIPDFPageContentDelegate" _contentDelegate;
@"UIPDFAnnotationController" _annotationController;
B _scalePageOnDraw;
^{CGColor=} _highLightColor;
B _animateSetFrame;
@"UIActivityIndicatorView" _activityIndicator;
B _showActivityIndicator;
@"UIColor" _backingLayerColor;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableArray" _highlights;
d _cachedScale;
B _allowHighlighting;
@"UIPDFSearchHighlightsController" _searchHighlightController;
@"NSMutableArray" _searchHiglightLayers;
@"UIPDFPage" _page;
B showAnnotations;
B _allowTwoFingerSelection;
B _showTextAnnotations;
B _showLinkAnnotationUnderline;
```

## Properties

```
@property (T@"UIPDFDocument",R,&,D) document;
@property (TQ,R,D) pageIndex;
@property (T@"UIPDFPage",D) page;
@property (T@"<NSObject><UIPDFPageViewDelegate>",N,V_delegate) delegate;
@property (Td,N,V_margin) margin;
@property (T@"CALayer",R,N,V_contentLayer) contentLayer;
@property (T@"CALayer",R,N,V_effectsLayer) effectsLayer;
@property (TB,N,V_allowSelection) allowSelection;
@property (TB,N,V_useBackingLayer) useBackingLayer;
@property (T@"UIPDFSelectionController",V_selectionController) selectionController;
@property (T^{CGColor=},R) highLightColor;
@property (TB,D,N) allowMenu;
@property (TB,N,V_animateSetFrame) animateSetFrame;
@property (T@"UIImage",&,D) backgroundImage;
@property (T@"UIColor",&,N,V_backingLayerColor) backingLayerColor;
@property (TB,N,V_showActivityIndicator) showActivityIndicator;
@property (TB,N,VshowAnnotations) showAnnotations;
@property (TB,D,N) allowHighlighting;
@property (TB,N,V_showTextAnnotations) showTextAnnotations;
@property (T@"UIPDFAnnotationController",R,N,V_annotationController) annotationController;
@property (TB,N,V_showLinkAnnotationUnderline) showLinkAnnotationUnderline;
@property (TB,N,V_allowTwoFingerSelection) allowTwoFingerSelection;
```

## Instance methods

```
-[UIPDFPageView margin];
-[UIPDFPageView clearSelection];
-[UIPDFPageView setMargin:];
-[UIPDFPageView setNeedsDisplay];
-[UIPDFPageView setSelectionController:];
-[UIPDFPageView willMoveToSuperview:];
-[UIPDFPageView document];
-[UIPDFPageView setBackgroundImage:];
-[UIPDFPageView backgroundImage];
-[UIPDFPageView init];
-[UIPDFPageView dealloc];
-[UIPDFPageView addLayers:];
-[UIPDFPageView layoutSubviews];
-[UIPDFPageView setPage:];
-[UIPDFPageView sizeThatFits:];
-[UIPDFPageView setDelegate:];
-[UIPDFPageView selectionController];
-[UIPDFPageView pageIndex];
-[UIPDFPageView page];
-[UIPDFPageView delegate];
-[UIPDFPageView setFrame:];
-[UIPDFPageView contentLayer];
-[UIPDFPageView annotationController];
-[UIPDFPageView initWithPage:];
-[UIPDFPageView suspendInstantTouchHighlighting];
-[UIPDFPageView animateSetFrame];
-[UIPDFPageView setShowLinkAnnotationUnderline:];
-[UIPDFPageView showAnnotations];
-[UIPDFPageView useBackingLayer];
-[UIPDFPageView _annotForPoint:rect:];
-[UIPDFPageView addPage:];
-[UIPDFPageView addWidgetToSelection];
-[UIPDFPageView allowHighlighting];
-[UIPDFPageView allowMenu];
-[UIPDFPageView allowSelection];
-[UIPDFPageView allowTwoFingerSelection];
-[UIPDFPageView backingLayerColor];
-[UIPDFPageView clearSearchHighlights];
-[UIPDFPageView convertPointFromPDFPageSpace:];
-[UIPDFPageView convertPointToPDFPageSpace:];
-[UIPDFPageView convertRectFromPDFPageSpace:];
-[UIPDFPageView convertRectToPDFPageSpace:];
-[UIPDFPageView createBackingLayer];
-[UIPDFPageView didReceiveMemoryWarning:];
-[UIPDFPageView didScroll:];
-[UIPDFPageView displayContent];
-[UIPDFPageView doubleTapAt:];
-[UIPDFPageView drawAnnotations:];
-[UIPDFPageView effectsLayer];
-[UIPDFPageView enableLightMemoryFootprint];
-[UIPDFPageView fitRect:];
-[UIPDFPageView fitWidth:atVertical:];
-[UIPDFPageView hasSearchHighlights];
-[UIPDFPageView hideSelection];
-[UIPDFPageView highLightColor];
-[UIPDFPageView highlightSearchSelection:animated:];
-[UIPDFPageView ignoreTouches:];
-[UIPDFPageView initWithPage:tiledContent:];
-[UIPDFPageView initWithPageLimitedMemory:];
-[UIPDFPageView layoutTextEffects];
-[UIPDFPageView receiveBackgroundImage:info:];
-[UIPDFPageView rectangleOfInterestAt:kind:];
-[UIPDFPageView removeBackingLayer];
-[UIPDFPageView scheduleBackgroundImage];
-[UIPDFPageView searchHighlightSelectionAt:];
-[UIPDFPageView setAllowHighlighting:];
-[UIPDFPageView setAllowMenu:];
-[UIPDFPageView setAllowSelection:];
-[UIPDFPageView setAllowTwoFingerSelection:];
-[UIPDFPageView setAnimateSetFrame:];
-[UIPDFPageView setBackingLayerColor:];
-[UIPDFPageView setDrawingSurfaceLayer:];
-[UIPDFPageView setSelectionNeedsDisplay];
-[UIPDFPageView setShowActivityIndicator:];
-[UIPDFPageView setShowAnnotations:];
-[UIPDFPageView setShowTextAnnotations:];
-[UIPDFPageView setTransforms];
-[UIPDFPageView setUseBackingLayer:];
-[UIPDFPageView showActivityIndicator];
-[UIPDFPageView showContent];
-[UIPDFPageView showLinkAnnotationUnderline];
-[UIPDFPageView showSelection];
-[UIPDFPageView showTextAnnotations];
-[UIPDFPageView singleTapAt:];
-[UIPDFPageView stopActivityIndicator];
-[UIPDFPageView twoFingerDoubleTapAt:];
-[UIPDFPageView viewDidZoom:];
-[UIPDFPageView willDoSomethingWithTap:];
```
