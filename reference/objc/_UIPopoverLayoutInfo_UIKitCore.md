# `_UIPopoverLayoutInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 24 instance variables, 23 properties, 54 instance methods, 1 class methods

## Instance variables

```
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInset;
d _arrowHeight;
d _arrowOffset;
{CGSize="width"d"height"d} _preferredContentSize;
{CGSize="width"d"height"d} _anticipatedContentSize;
Q _preferredArrowDirections;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _containingFrame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _containingFrameInsets;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceViewRect;
B _canOverlapSourceViewRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
d _offset;
Q _arrowDirection;
B _preferLandscapeOrientations;
B _updatesEnabled;
@"NSMutableArray" _candidates;
B _preferSourceViewRectAlignment;
B _isRTL;
B _useContextMenuLayout;
B _shouldFillWindow;
@"NSArray" _divisionReservedRegions;
@"<_UIPopoverLayoutInfoDelegate>" _layoutInfoDelegate;
q _preferredHorizontalAlignment;
d _displayScale;
```

## Properties

```
@property (TB,N,G_updatesEnabled,S_setUpdatesEnabled:,V_updatesEnabled) updatesEnabled;
@property (T@"<_UIPopoverLayoutInfoDelegate>",W,N,V_layoutInfoDelegate) layoutInfoDelegate;
@property (T{UIEdgeInsets=dddd},N,V_contentInset) contentInset;
@property (Td,N,V_arrowHeight) arrowHeight;
@property (Td,N,V_arrowOffset) arrowOffset;
@property (T{CGSize=dd},N,V_preferredContentSize) preferredContentSize;
@property (T{CGSize=dd},N,V_anticipatedContentSize) anticipatedContentSize;
@property (TQ,N,V_preferredArrowDirections) preferredArrowDirections;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_containingFrame) containingFrame;
@property (T{UIEdgeInsets=dddd},N,V_containingFrameInsets) containingFrameInsets;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_sourceViewRect) sourceViewRect;
@property (TB,N,V_canOverlapSourceViewRect) canOverlapSourceViewRect;
@property (TB,N,V_preferSourceViewRectAlignment) preferSourceViewRectAlignment;
@property (TB,N,V_preferLandscapeOrientations) preferLandscapeOrientations;
@property (Tq,N,V_preferredHorizontalAlignment) preferredHorizontalAlignment;
@property (TB,N,V_isRTL) isRTL;
@property (TB,N,V_useContextMenuLayout) useContextMenuLayout;
@property (TB,N,V_shouldFillWindow) shouldFillWindow;
@property (Td,N,V_displayScale) displayScale;
@property (T@"NSArray",C,N,V_divisionReservedRegions) divisionReservedRegions;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (Td,R,N,V_offset) offset;
@property (TQ,R,N,V_arrowDirection) arrowDirection;
```

## Class methods

```
+[_UIPopoverLayoutInfo _observationKeys];
```

## Instance methods

```
-[_UIPopoverLayoutInfo candidates];
-[_UIPopoverLayoutInfo _updatesEnabled];
-[_UIPopoverLayoutInfo setPreferredContentSize:];
-[_UIPopoverLayoutInfo setLayoutInfoDelegate:];
-[_UIPopoverLayoutInfo observeValueForKeyPath:ofObject:change:context:];
-[_UIPopoverLayoutInfo useContextMenuLayout];
-[_UIPopoverLayoutInfo divisionReservedRegions];
-[_UIPopoverLayoutInfo setArrowHeight:];
-[_UIPopoverLayoutInfo _effectiveViewSourceRect];
-[_UIPopoverLayoutInfo anticipatedContentSize];
-[_UIPopoverLayoutInfo setDisplayScale:];
-[_UIPopoverLayoutInfo init];
-[_UIPopoverLayoutInfo setPreferLandscapeOrientations:];
-[_UIPopoverLayoutInfo displayScale];
-[_UIPopoverLayoutInfo _popoverViewSizeForContentSize:arrowDirection:];
-[_UIPopoverLayoutInfo dealloc];
-[_UIPopoverLayoutInfo setContentInset:];
-[_UIPopoverLayoutInfo preferSourceViewRectAlignment];
-[_UIPopoverLayoutInfo containingFrame];
-[_UIPopoverLayoutInfo _divisionAvoidingPresentationRect:forSourceViewRect:isDivided:];
-[_UIPopoverLayoutInfo setShouldFillWindow:];
-[_UIPopoverLayoutInfo sourceViewRect];
-[_UIPopoverLayoutInfo setCanOverlapSourceViewRect:];
-[_UIPopoverLayoutInfo setAnticipatedContentSize:];
-[_UIPopoverLayoutInfo preferredArrowDirections];
-[_UIPopoverLayoutInfo setSourceViewRect:];
-[_UIPopoverLayoutInfo setPreferSourceViewRectAlignment:];
-[_UIPopoverLayoutInfo preferLandscapeOrientations];
-[_UIPopoverLayoutInfo canOverlapSourceViewRect];
-[_UIPopoverLayoutInfo setContainingFrame:];
-[_UIPopoverLayoutInfo setContainingFrameInsets:];
-[_UIPopoverLayoutInfo updateProperties:];
-[_UIPopoverLayoutInfo layoutInfoDelegate];
-[_UIPopoverLayoutInfo description];
-[_UIPopoverLayoutInfo _setUpdatesEnabled:];
-[_UIPopoverLayoutInfo setPreferredHorizontalAlignment:];
-[_UIPopoverLayoutInfo setArrowOffset:];
-[_UIPopoverLayoutInfo arrowDirection];
-[_UIPopoverLayoutInfo arrowHeight];
-[_UIPopoverLayoutInfo preferredContentSize];
-[_UIPopoverLayoutInfo _updateOutputs];
-[_UIPopoverLayoutInfo setIsRTL:];
-[_UIPopoverLayoutInfo copyWithZone:];
-[_UIPopoverLayoutInfo preferredHorizontalAlignment];
-[_UIPopoverLayoutInfo setUseContextMenuLayout:];
-[_UIPopoverLayoutInfo isRTL];
-[_UIPopoverLayoutInfo shouldFillWindow];
-[_UIPopoverLayoutInfo containingFrameInsets];
-[_UIPopoverLayoutInfo offset];
-[_UIPopoverLayoutInfo contentInset];
-[_UIPopoverLayoutInfo arrowOffset];
-[_UIPopoverLayoutInfo setDivisionReservedRegions:];
-[_UIPopoverLayoutInfo frame];
-[_UIPopoverLayoutInfo setPreferredArrowDirections:];
```
