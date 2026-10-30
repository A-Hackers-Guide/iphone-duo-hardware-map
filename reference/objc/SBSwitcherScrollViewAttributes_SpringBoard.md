# `SBSwitcherScrollViewAttributes`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _scrollViewPagingEnabled;
B _interpolatesDuringSwipeToKill;
d _decelerationRate;
{CGSize="width"d"height"d} _contentSize;
{CGSize="width"d"height"d} _interpageSpacingForPaging;
{CGPoint="x"d"y"d} _pagingOrigin;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T{CGSize=dd},N,V_contentSize) contentSize;
@property (Td,N,V_decelerationRate) decelerationRate;
@property (TB,N,V_scrollViewPagingEnabled) scrollViewPagingEnabled;
@property (T{CGSize=dd},N,V_interpageSpacingForPaging) interpageSpacingForPaging;
@property (T{CGPoint=dd},N,V_pagingOrigin) pagingOrigin;
@property (TB,N,V_interpolatesDuringSwipeToKill) interpolatesDuringSwipeToKill;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
```

## Instance methods

```
-[SBSwitcherScrollViewAttributes mutableCopyWithZone:];
-[SBSwitcherScrollViewAttributes contentSize];
-[SBSwitcherScrollViewAttributes setContentSize:];
-[SBSwitcherScrollViewAttributes setFrame:];
-[SBSwitcherScrollViewAttributes copyWithZone:];
-[SBSwitcherScrollViewAttributes frame];
-[SBSwitcherScrollViewAttributes decelerationRate];
-[SBSwitcherScrollViewAttributes setDecelerationRate:];
-[SBSwitcherScrollViewAttributes pagingOrigin];
-[SBSwitcherScrollViewAttributes _copyWithClass:];
-[SBSwitcherScrollViewAttributes setPagingOrigin:];
-[SBSwitcherScrollViewAttributes interpageSpacingForPaging];
-[SBSwitcherScrollViewAttributes interpolatesDuringSwipeToKill];
-[SBSwitcherScrollViewAttributes scrollViewPagingEnabled];
-[SBSwitcherScrollViewAttributes setInterpageSpacingForPaging:];
-[SBSwitcherScrollViewAttributes setInterpolatesDuringSwipeToKill:];
-[SBSwitcherScrollViewAttributes setScrollViewPagingEnabled:];
```
