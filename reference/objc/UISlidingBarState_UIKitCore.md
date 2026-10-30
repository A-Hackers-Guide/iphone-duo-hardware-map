# `UISlidingBarState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 20 instance variables, 27 properties, 61 instance methods, 0 class methods

## Instance variables

```
B __treatLeadingHiddenAsOverlaps;
B __treatTrailingHiddenAsOverlaps;
B __treatSupplementaryHiddenAsOverlaps;
d _leadingWidth;
d _leadingOffscreenWidth;
d _trailingWidth;
d _trailingOffscreenWidth;
d _supplementaryWidth;
d _supplementaryOffscreenWidth;
d _mainWidth;
@"UISlidingBarConfiguration" _configuration;
d _leadingDragOffset;
d _trailingDragOffset;
d _supplementaryDragOffset;
d __leadingOverlayWidth;
d __trailingOverlayWidth;
d __supplementaryOverlayWidth;
d __rubberBandInset;
d __keyboardAdjustment;
q __collapsedState;
```

## Properties

```
@property (Td,N,V_leadingWidth) leadingWidth;
@property (Td,N,V_trailingWidth) trailingWidth;
@property (Td,N,V_supplementaryWidth) supplementaryWidth;
@property (Td,N,V_leadingOffscreenWidth) leadingOffscreenWidth;
@property (Td,N,V_trailingOffscreenWidth) trailingOffscreenWidth;
@property (Td,N,V_supplementaryOffscreenWidth) supplementaryOffscreenWidth;
@property (Td,N,V_leadingDragOffset) leadingDragOffset;
@property (Td,N,V_trailingDragOffset) trailingDragOffset;
@property (Td,N,V_supplementaryDragOffset) supplementaryDragOffset;
@property (Td,N,V_mainWidth) mainWidth;
@property (T@"UISlidingBarConfiguration",&,N,V_configuration) configuration;
@property (Td,N,S_setLeadingOverlayWidth:,V__leadingOverlayWidth) _leadingOverlayWidth;
@property (TB,N,S_setTreatLeadingHiddenAsOverlaps:,V__treatLeadingHiddenAsOverlaps) _treatLeadingHiddenAsOverlaps;
@property (Td,N,S_setTrailingOverlayWidth:,V__trailingOverlayWidth) _trailingOverlayWidth;
@property (TB,N,S_setTreatTrailingHiddenAsOverlaps:,V__treatTrailingHiddenAsOverlaps) _treatTrailingHiddenAsOverlaps;
@property (Td,N,S_setSupplementaryOverlayWidth:,V__supplementaryOverlayWidth) _supplementaryOverlayWidth;
@property (TB,N,S_setTreatSupplementaryHiddenAsOverlaps:,V__treatSupplementaryHiddenAsOverlaps) _treatSupplementaryHiddenAsOverlaps;
@property (Td,N,V__rubberBandInset) _rubberBandInset;
@property (Td,N,V__keyboardAdjustment) _keyboardAdjustment;
@property (Tq,N,S_setCollapsedState:,V__collapsedState) _collapsedState;
@property (TB,R,N) leadingOverlapsMain;
@property (TB,R,N) trailingOverlapsMain;
@property (TB,R,N) supplementaryOverlapsMain;
@property (TB,R,N,GisCollapsed) collapsed;
@property (TB,R,N) isLeadingVisible;
@property (TB,R,N) isTrailingVisible;
@property (TB,R,N) isSupplementaryVisible;
```

## Instance methods

```
-[UISlidingBarState setConfiguration:];
-[UISlidingBarState _configuration];
-[UISlidingBarState configuration];
-[UISlidingBarState isCollapsed];
-[UISlidingBarState hash];
-[UISlidingBarState description];
-[UISlidingBarState copyWithZone:];
-[UISlidingBarState isEqual:];
-[UISlidingBarState _setCollapsedState:];
-[UISlidingBarState setSupplementaryOffscreenWidth:];
-[UISlidingBarState _collapsedState];
-[UISlidingBarState matchesRequest:];
-[UISlidingBarState _absoluteDistanceFromRequest:];
-[UISlidingBarState _distanceFromRequest:];
-[UISlidingBarState _interactiveStateRequest];
-[UISlidingBarState _keyboardAdjustment];
-[UISlidingBarState _leadingEntirelyOverlapsMain];
-[UISlidingBarState _leadingOverlayWidth];
-[UISlidingBarState _rubberBandInset];
-[UISlidingBarState _setLeadingOverlayWidth:];
-[UISlidingBarState _setSupplementaryOverlayWidth:];
-[UISlidingBarState _setTrailingOverlayWidth:];
-[UISlidingBarState _setTreatLeadingHiddenAsOverlaps:];
-[UISlidingBarState _setTreatSupplementaryHiddenAsOverlaps:];
-[UISlidingBarState _setTreatTrailingHiddenAsOverlaps:];
-[UISlidingBarState _shouldUseSlidingBars];
-[UISlidingBarState _supplementaryEntirelyOverlapsMain];
-[UISlidingBarState _supplementaryOverlayWidth];
-[UISlidingBarState _trailingEntirelyOverlapsMain];
-[UISlidingBarState _trailingOverlayWidth];
-[UISlidingBarState _treatLeadingHiddenAsOverlaps];
-[UISlidingBarState _treatSupplementaryHiddenAsOverlaps];
-[UISlidingBarState _treatTrailingHiddenAsOverlaps];
-[UISlidingBarState isLeadingVisible];
-[UISlidingBarState isSupplementaryVisible];
-[UISlidingBarState isTrailingVisible];
-[UISlidingBarState leadingDragOffset];
-[UISlidingBarState leadingOffscreenWidth];
-[UISlidingBarState leadingOverlapsMain];
-[UISlidingBarState leadingWidth];
-[UISlidingBarState mainWidth];
-[UISlidingBarState setLeadingDragOffset:];
-[UISlidingBarState setLeadingOffscreenWidth:];
-[UISlidingBarState setLeadingWidth:];
-[UISlidingBarState setMainWidth:];
-[UISlidingBarState setSupplementaryDragOffset:];
-[UISlidingBarState setSupplementaryWidth:];
-[UISlidingBarState setTrailingDragOffset:];
-[UISlidingBarState setTrailingOffscreenWidth:];
-[UISlidingBarState setTrailingWidth:];
-[UISlidingBarState set_keyboardAdjustment:];
-[UISlidingBarState set_rubberBandInset:];
-[UISlidingBarState stateRequest];
-[UISlidingBarState supplementaryDragOffset];
-[UISlidingBarState supplementaryOffscreenWidth];
-[UISlidingBarState supplementaryOverlapsMain];
-[UISlidingBarState supplementaryWidth];
-[UISlidingBarState trailingDragOffset];
-[UISlidingBarState trailingOffscreenWidth];
-[UISlidingBarState trailingOverlapsMain];
-[UISlidingBarState trailingWidth];
```
