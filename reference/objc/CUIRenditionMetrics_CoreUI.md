# `CUIRenditionMetrics`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 13 instance variables, 0 properties, 22 instance methods, 0 class methods

## Instance variables

```
{CGSize="width"d"height"d} _imageSize;
{CGSize="width"d"height"d} _defaultImageSize;
{CGSize="width"d"height"d} _edgeBottomLeftMargin;
{CGSize="width"d"height"d} _edgeTopRightMargin;
{CGSize="width"d"height"d} _contentBottomLeftMargin;
{CGSize="width"d"height"d} _contentTopRightMargin;
d _baseline;
{CGSize="width"d"height"d} _auxiliary1BottomLeftMargin;
{CGSize="width"d"height"d} _auxiliary1TopRightMargin;
{CGSize="width"d"height"d} _auxiliary2BottomLeftMargin;
{CGSize="width"d"height"d} _auxiliary2TopRightMargin;
d _scale;
{crmFlags="scalesVertically"b1"scalesHorizontally"b1"reserved"b14} _crmFlags;
```

## Instance methods

```
-[CUIRenditionMetrics imageSize];
-[CUIRenditionMetrics contentTopRightMargin];
-[CUIRenditionMetrics contentRect];
-[CUIRenditionMetrics hasOpaqueContentBounds];
-[CUIRenditionMetrics auxiliary2TopRightMargin];
-[CUIRenditionMetrics edgeRect];
-[CUIRenditionMetrics defaultImageSize];
-[CUIRenditionMetrics auxiliary2BottomLeftMargin];
-[CUIRenditionMetrics auxiliary1TopRightMargin];
-[CUIRenditionMetrics scale];
-[CUIRenditionMetrics insetContentRectWithMetrics:];
-[CUIRenditionMetrics auxiliary1BottomLeftMargin];
-[CUIRenditionMetrics baseline];
-[CUIRenditionMetrics edgeBottomLeftMargin];
-[CUIRenditionMetrics metricsByMirroringHorizontally];
-[CUIRenditionMetrics scalesVertically];
-[CUIRenditionMetrics scalesHorizontally];
-[CUIRenditionMetrics copyWithZone:];
-[CUIRenditionMetrics contentBottomLeftMargin];
-[CUIRenditionMetrics insetRectWithMetrics:];
-[CUIRenditionMetrics hasAlignmentEdgeMargins];
-[CUIRenditionMetrics edgeTopRightMargin];
```
