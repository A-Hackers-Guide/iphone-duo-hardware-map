# `_UISplitViewControllerAdaptiveTransitionLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISplitViewControllerAdaptiveLayout`
- 4 instance variables, 13 properties, 52 instance methods, 0 class methods

## Instance variables

```
previousLayout;
newLayout;
d progress;
d displayScale;
```

## Properties

```
@property (Td,N,Vprogress) progress;
@property (Td,N,VdisplayScale) displayScale;
@property (T{CGSize=dd},N,R) contentSize;
@property (T{CGSize=dd},N,R) minimumSize;
@property (T{CGSize=dd},N,R) preferredSize;
@property (Tq,N,R) primaryEdge;
@property (Tq,N,R) splitBehavior;
@property (Tq,N,R) planeCount;
@property (Tq,N,R) displayMode;
@property (TB,N,R) isCollapsed;
@property (Tq,N,R) presentedSplitViewControllerColumn;
@property (T@"<_UISplitViewControllerAdaptiveLayout>",N,R) interpolatedLayout;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveTransitionLayout columnModeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout preferredSplitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptiveTransitionLayout presentedSplitViewControllerColumn];
-[_UISplitViewControllerAdaptiveTransitionLayout prepareForDisplay];
-[_UISplitViewControllerAdaptiveTransitionLayout minimumSize];
-[_UISplitViewControllerAdaptiveTransitionLayout setProgress:];
-[_UISplitViewControllerAdaptiveTransitionLayout setDisplayScale:];
-[_UISplitViewControllerAdaptiveTransitionLayout init];
-[_UISplitViewControllerAdaptiveTransitionLayout splitViewControllerColumnDisplayedBeforeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout canShowSplitViewControllerColumn:withSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout displayScale];
-[_UISplitViewControllerAdaptiveTransitionLayout minimumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout splitViewControllerEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout userInterfaceLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout primaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout displayMode];
-[_UISplitViewControllerAdaptiveTransitionLayout enumerateDisplayOrder:];
-[_UISplitViewControllerAdaptiveTransitionLayout enumeratePlanes:withBlock:];
-[_UISplitViewControllerAdaptiveTransitionLayout contentSize];
-[_UISplitViewControllerAdaptiveTransitionLayout planeRubberBandInsetsForPlaneLevel:];
-[_UISplitViewControllerAdaptiveTransitionLayout secondaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout updatedPreferredColumns:toShowSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout progress];
-[_UISplitViewControllerAdaptiveTransitionLayout primaryEdge];
-[_UISplitViewControllerAdaptiveTransitionLayout planeTransformForPlaneLevel:];
-[_UISplitViewControllerAdaptiveTransitionLayout splitBehavior];
-[_UISplitViewControllerAdaptiveTransitionLayout canResizeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout isCollapsed];
-[_UISplitViewControllerAdaptiveTransitionLayout backgroundStyleForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout splitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptiveTransitionLayout separatorTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout enumerateDisplayInOrder:withBlock:];
-[_UISplitViewControllerAdaptiveTransitionLayout description];
-[_UISplitViewControllerAdaptiveTransitionLayout contentInsetsForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout separatorFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout planeFrameForPlaneLevel:];
-[_UISplitViewControllerAdaptiveTransitionLayout updatedPreferredColumns:toHideSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout columnTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout splitViewControllerColumnDisplayedAfterSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout planeCount];
-[_UISplitViewControllerAdaptiveTransitionLayout maskedCornersForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout columnVisibilityForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout primaryRectEdgeForPlaneLevel:];
-[_UISplitViewControllerAdaptiveTransitionLayout maximumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout dimmingLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout planeLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout rectEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout preferredSize];
-[_UISplitViewControllerAdaptiveTransitionLayout columnFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveTransitionLayout enumerateZOrder:planeLevel:withBlock:];
-[_UISplitViewControllerAdaptiveTransitionLayout initWithPreviousLayout:newLayout:];
-[_UISplitViewControllerAdaptiveTransitionLayout interpolatedLayout];
```
