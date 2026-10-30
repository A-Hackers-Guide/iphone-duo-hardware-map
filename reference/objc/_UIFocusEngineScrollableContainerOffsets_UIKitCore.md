# `_UIFocusEngineScrollableContainerOffsets`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _adjustsTargetsOnContentOffsetChanges;
@"_UIFocusEnvironmentScrollableContainerTuple" _environmentScrollableContainer;
@"<UIScrollViewDelegate>" _scrollDelegate;
d _convergenceRate;
@? _completion;
{CGPoint="x"d"y"d} _startContentOffset;
{CGPoint="x"d"y"d} _lastContentOffset;
{CGPoint="x"d"y"d} _lastRoundedOffset;
{CGPoint="x"d"y"d} _targetContentOffset;
{CGPoint="x"d"y"d} _lastVelocity;
```

## Properties

```
@property (TB,N,V_adjustsTargetsOnContentOffsetChanges) adjustsTargetsOnContentOffsetChanges;
@property (T@"_UIFocusEnvironmentScrollableContainerTuple",&,N,V_environmentScrollableContainer) environmentScrollableContainer;
@property (T@"<UIScrollViewDelegate>",&,N,V_scrollDelegate) scrollDelegate;
@property (T{CGPoint=dd},N,V_startContentOffset) startContentOffset;
@property (T{CGPoint=dd},N,V_lastContentOffset) lastContentOffset;
@property (T{CGPoint=dd},N,V_lastRoundedOffset) lastRoundedOffset;
@property (T{CGPoint=dd},N,V_targetContentOffset) targetContentOffset;
@property (Td,N,V_convergenceRate) convergenceRate;
@property (T{CGPoint=dd},N,V_lastVelocity) lastVelocity;
@property (T@?,C,N,V_completion) completion;
```

## Instance methods

```
-[_UIFocusEngineScrollableContainerOffsets setCompletion:];
-[_UIFocusEngineScrollableContainerOffsets completion];
-[_UIFocusEngineScrollableContainerOffsets setTargetContentOffset:];
-[_UIFocusEngineScrollableContainerOffsets targetContentOffset];
-[_UIFocusEngineScrollableContainerOffsets convergenceRate];
-[_UIFocusEngineScrollableContainerOffsets adjustsTargetsOnContentOffsetChanges];
-[_UIFocusEngineScrollableContainerOffsets environmentScrollableContainer];
-[_UIFocusEngineScrollableContainerOffsets lastContentOffset];
-[_UIFocusEngineScrollableContainerOffsets lastRoundedOffset];
-[_UIFocusEngineScrollableContainerOffsets lastVelocity];
-[_UIFocusEngineScrollableContainerOffsets scrollDelegate];
-[_UIFocusEngineScrollableContainerOffsets setAdjustsTargetsOnContentOffsetChanges:];
-[_UIFocusEngineScrollableContainerOffsets setConvergenceRate:];
-[_UIFocusEngineScrollableContainerOffsets setEnvironmentScrollableContainer:];
-[_UIFocusEngineScrollableContainerOffsets setLastContentOffset:];
-[_UIFocusEngineScrollableContainerOffsets setLastRoundedOffset:];
-[_UIFocusEngineScrollableContainerOffsets setLastVelocity:];
-[_UIFocusEngineScrollableContainerOffsets setScrollDelegate:];
-[_UIFocusEngineScrollableContainerOffsets setStartContentOffset:];
-[_UIFocusEngineScrollableContainerOffsets startContentOffset];
```
