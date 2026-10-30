# `_UIImageContentLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 17 instance methods, 1 class methods

## Instance variables

```
{?="contentsIsCGImage"b1} _flags;
@? _contentInfoGenerator;
{?="rendition"@"_UIImageContentRendition""contents"@"drawScale"d} _contentInfo;
d _contentsVectorScale;
B _symbolLayerNeedsHorizontalFlip;
d _contentsScaleFactor;
d _baselineOffsetFromTop;
d _baselineOffsetFromBottom;
{CGSize="width"d"height"d} _contentsSize;
{CGSize="width"d"height"d} _renderSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _alignmentRectInsets;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _contentsTransform;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _symbolLayerPositionTransform;
```

## Properties

```
@property (T{CGAffineTransform=dddddd},R,N,V_contentsTransform) contentsTransform;
@property (T{CGAffineTransform=dddddd},R,N,V_symbolLayerPositionTransform) symbolLayerPositionTransform;
@property (TB,R,N,V_symbolLayerNeedsHorizontalFlip) symbolLayerNeedsHorizontalFlip;
@property (Td,R,N,V_contentsScaleFactor) contentsScaleFactor;
@property (T{CGSize=dd},R,N,V_contentsSize) contentsSize;
@property (T@,R,N) contents;
@property (T{UIEdgeInsets=dddd},R,N,V_contentInsets) contentInsets;
@property (T{UIEdgeInsets=dddd},R,N,V_alignmentRectInsets) alignmentRectInsets;
@property (T@"UIColor",R,N) contentsMultiplyColor;
@property (T@"NSArray",R,N) contentEffects;
@property (TI,R,N) contentDrawMode;
@property (T@"_UIImageContentRBSymbolConfiguration",R,N) rbSymbolConfiguration;
@property (Td,R,N,V_baselineOffsetFromBottom) baselineOffsetFromBottom;
@property (T{CGSize=dd},R,N,V_renderSize) renderSize;
```

## Class methods

```
+[_UIImageContentLayout layoutForSource:inTarget:withSize:];
```

## Instance methods

```
-[_UIImageContentLayout renderSize];
-[_UIImageContentLayout contentsTransform];
-[_UIImageContentLayout contents];
-[_UIImageContentLayout alignmentRectInsets];
-[_UIImageContentLayout contentsSize];
-[_UIImageContentLayout symbolLayerNeedsHorizontalFlip];
-[_UIImageContentLayout contentEffects];
-[_UIImageContentLayout contentsMultiplyColor];
-[_UIImageContentLayout drawInContext:withSize:];
-[_UIImageContentLayout contentsScaleFactor];
-[_UIImageContentLayout contentInsets];
-[_UIImageContentLayout description];
-[_UIImageContentLayout hasContents];
-[_UIImageContentLayout rbSymbolConfiguration];
-[_UIImageContentLayout contentDrawMode];
-[_UIImageContentLayout symbolLayerPositionTransform];
-[_UIImageContentLayout baselineOffsetFromBottom];
```
