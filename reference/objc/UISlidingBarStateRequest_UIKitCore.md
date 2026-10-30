# `UISlidingBarStateRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _userInitiated;
d _leadingWidth;
d _leadingOffscreenWidth;
d _trailingWidth;
d _trailingOffscreenWidth;
d _supplementaryWidth;
d _supplementaryOffscreenWidth;
d _rubberBandInset;
d _mainWidth;
```

## Properties

```
@property (TB,N,V_userInitiated) userInitiated;
@property (Td,N,V_leadingWidth) leadingWidth;
@property (Td,N,V_leadingOffscreenWidth) leadingOffscreenWidth;
@property (Td,N,V_trailingWidth) trailingWidth;
@property (Td,N,V_trailingOffscreenWidth) trailingOffscreenWidth;
@property (Td,N,V_supplementaryWidth) supplementaryWidth;
@property (Td,N,V_supplementaryOffscreenWidth) supplementaryOffscreenWidth;
@property (Td,N,V_rubberBandInset) rubberBandInset;
@property (Td,N,V_mainWidth) mainWidth;
```

## Instance methods

```
-[UISlidingBarStateRequest init];
-[UISlidingBarStateRequest userInitiated];
-[UISlidingBarStateRequest setUserInitiated:];
-[UISlidingBarStateRequest hash];
-[UISlidingBarStateRequest description];
-[UISlidingBarStateRequest copyWithZone:];
-[UISlidingBarStateRequest isEqual:];
-[UISlidingBarStateRequest setSupplementaryOffscreenWidth:];
-[UISlidingBarStateRequest _matchingState:];
-[UISlidingBarStateRequest rubberBandInset];
-[UISlidingBarStateRequest _closestEqualOrLargerState:];
-[UISlidingBarStateRequest _closestEqualOrLargerState:returningDistance:];
-[UISlidingBarStateRequest _closestState:];
-[UISlidingBarStateRequest _closestState:returningDistance:];
-[UISlidingBarStateRequest leadingOffscreenWidth];
-[UISlidingBarStateRequest leadingWidth];
-[UISlidingBarStateRequest mainWidth];
-[UISlidingBarStateRequest setLeadingOffscreenWidth:];
-[UISlidingBarStateRequest setLeadingWidth:];
-[UISlidingBarStateRequest setMainWidth:];
-[UISlidingBarStateRequest setRubberBandInset:];
-[UISlidingBarStateRequest setSupplementaryWidth:];
-[UISlidingBarStateRequest setTrailingOffscreenWidth:];
-[UISlidingBarStateRequest setTrailingWidth:];
-[UISlidingBarStateRequest supplementaryOffscreenWidth];
-[UISlidingBarStateRequest supplementaryWidth];
-[UISlidingBarStateRequest trailingOffscreenWidth];
-[UISlidingBarStateRequest trailingWidth];
```
