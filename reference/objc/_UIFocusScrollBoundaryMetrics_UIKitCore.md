# `_UIFocusScrollBoundaryMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _shouldSearchX;
B _shouldSearchY;
B _isMinX;
B _isMaxX;
B _isMinY;
B _isMaxY;
@"<UIFocusItem>" _focusItem;
@"<UIFocusEnvironment>" _owningEnvironment;
@"<UIFocusItemScrollableContainer>" _scrollableContainer;
{CGPoint="x"d"y"d} _localFocusedCenter;
{CGPoint="x"d"y"d} _minContentOffset;
{CGPoint="x"d"y"d} _maxContentOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _localFocusedRect;
```

## Properties

```
@property (T@"<UIFocusItem>",R,N,V_focusItem) focusItem;
@property (T@"<UIFocusEnvironment>",R,N,V_owningEnvironment) owningEnvironment;
@property (T@"<UIFocusItemScrollableContainer>",R,N,V_scrollableContainer) scrollableContainer;
@property (TB,R,N,V_shouldSearchX) shouldSearchX;
@property (TB,R,N,V_shouldSearchY) shouldSearchY;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_localFocusedRect) localFocusedRect;
@property (T{CGPoint=dd},R,N,V_localFocusedCenter) localFocusedCenter;
@property (T{CGPoint=dd},R,N,V_minContentOffset) minContentOffset;
@property (T{CGPoint=dd},R,N,V_maxContentOffset) maxContentOffset;
@property (TB,N,V_isMinX) isMinX;
@property (TB,N,V_isMaxX) isMaxX;
@property (TB,N,V_isMinY) isMinY;
@property (TB,N,V_isMaxY) isMaxY;
```

## Instance methods

```
-[_UIFocusScrollBoundaryMetrics checkOtherRect:];
-[_UIFocusScrollBoundaryMetrics _checkScrollableBounds];
-[_UIFocusScrollBoundaryMetrics checkOtherFocusItem:];
-[_UIFocusScrollBoundaryMetrics consumeOtherMetrics:];
-[_UIFocusScrollBoundaryMetrics focusItem];
-[_UIFocusScrollBoundaryMetrics hasDisprovedAllRelevantAssumptions];
-[_UIFocusScrollBoundaryMetrics initWithFocusItem:owningEnvironment:scrollableContainer:];
-[_UIFocusScrollBoundaryMetrics initWithFocusItem:scrollView:];
-[_UIFocusScrollBoundaryMetrics isMaxX];
-[_UIFocusScrollBoundaryMetrics isMaxY];
-[_UIFocusScrollBoundaryMetrics isMinX];
-[_UIFocusScrollBoundaryMetrics isMinY];
-[_UIFocusScrollBoundaryMetrics localFocusedCenter];
-[_UIFocusScrollBoundaryMetrics localFocusedRect];
-[_UIFocusScrollBoundaryMetrics maxContentOffset];
-[_UIFocusScrollBoundaryMetrics minContentOffset];
-[_UIFocusScrollBoundaryMetrics owningEnvironment];
-[_UIFocusScrollBoundaryMetrics scrollableContainer];
-[_UIFocusScrollBoundaryMetrics setIsMaxX:];
-[_UIFocusScrollBoundaryMetrics setIsMaxY:];
-[_UIFocusScrollBoundaryMetrics setIsMinX:];
-[_UIFocusScrollBoundaryMetrics setIsMinY:];
-[_UIFocusScrollBoundaryMetrics shouldSearchX];
-[_UIFocusScrollBoundaryMetrics shouldSearchY];
```
