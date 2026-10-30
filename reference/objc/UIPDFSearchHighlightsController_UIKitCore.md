# `UIPDFSearchHighlightsController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CALayerDelegate`
- 8 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _searchHighlightLayers;
@"UIPDFPageView" _pageView;
^{CGColor=} _highlightColor;
^{CGColor=} _borderColor;
^{CGColor=} _shadowColor;
B _pageRendered;
@"NSMutableArray" _rectangles;
@"UIPDFSelection" _selection;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPDFSearchHighlightsController layoutSublayersOfLayer:];
-[UIPDFSearchHighlightsController setNeedsDisplay];
-[UIPDFSearchHighlightsController dealloc];
-[UIPDFSearchHighlightsController drawLayer:inContext:];
-[UIPDFSearchHighlightsController hitTest:];
-[UIPDFSearchHighlightsController _addAnimation2:];
-[UIPDFSearchHighlightsController _addAnimation:];
-[UIPDFSearchHighlightsController addLayer:path:shadowPath:animated:];
-[UIPDFSearchHighlightsController addSearchHighlightForRotatedSelection:animated:];
-[UIPDFSearchHighlightsController addSearchHighlightForSelection:animated:];
-[UIPDFSearchHighlightsController clearSearchHighlights];
-[UIPDFSearchHighlightsController hasSearchHighlights];
-[UIPDFSearchHighlightsController indexOfColumnBreakStartingAt:];
-[UIPDFSearchHighlightsController initWithPageView:];
-[UIPDFSearchHighlightsController makeType1Path:shadowPath:];
-[UIPDFSearchHighlightsController makeType1Shadow:rect:inset:];
-[UIPDFSearchHighlightsController makeType2Path:to:shadowPath:];
-[UIPDFSearchHighlightsController makeType2Shadow:rect:];
-[UIPDFSearchHighlightsController makeType3Path:from:to:shadowPath:];
-[UIPDFSearchHighlightsController makeType4Path:from:to:shadowPath:];
-[UIPDFSearchHighlightsController pageDidRender:];
-[UIPDFSearchHighlightsController unionFrom:to:];
```
