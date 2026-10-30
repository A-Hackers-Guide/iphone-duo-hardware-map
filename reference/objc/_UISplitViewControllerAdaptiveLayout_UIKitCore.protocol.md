# `_UISplitViewControllerAdaptiveLayout` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 45 instance methods, 0 class methods

## Properties

```
@property (T{CGSize=dd},R,N) contentSize;
@property (T{CGSize=dd},R,N) minimumSize;
@property (T{CGSize=dd},R,N) preferredSize;
@property (Tq,R,N) primaryEdge;
@property (Tq,R,N) splitBehavior;
@property (Tq,R,N) planeCount;
@property (Tq,R,N) displayMode;
@property (TB,R,N) isCollapsed;
@property (Tq,R,N) presentedSplitViewControllerColumn;
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveLayout columnModeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout preferredSplitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptiveLayout presentedSplitViewControllerColumn];
-[_UISplitViewControllerAdaptiveLayout prepareForDisplay];
-[_UISplitViewControllerAdaptiveLayout minimumSize];
-[_UISplitViewControllerAdaptiveLayout splitViewControllerColumnDisplayedBeforeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout canShowSplitViewControllerColumn:withSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout minimumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout initWithDataSource:delegate:];
-[_UISplitViewControllerAdaptiveLayout splitViewControllerEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout userInterfaceLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout primaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout displayMode];
-[_UISplitViewControllerAdaptiveLayout enumerateDisplayOrder:];
-[_UISplitViewControllerAdaptiveLayout enumeratePlanes:withBlock:];
-[_UISplitViewControllerAdaptiveLayout contentSize];
-[_UISplitViewControllerAdaptiveLayout planeRubberBandInsetsForPlaneLevel:];
-[_UISplitViewControllerAdaptiveLayout secondaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout updatedPreferredColumns:toShowSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout primaryEdge];
-[_UISplitViewControllerAdaptiveLayout planeTransformForPlaneLevel:];
-[_UISplitViewControllerAdaptiveLayout splitBehavior];
-[_UISplitViewControllerAdaptiveLayout canResizeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout isCollapsed];
-[_UISplitViewControllerAdaptiveLayout backgroundStyleForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout splitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptiveLayout separatorTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout enumerateDisplayInOrder:withBlock:];
-[_UISplitViewControllerAdaptiveLayout contentInsetsForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout separatorFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout planeFrameForPlaneLevel:];
-[_UISplitViewControllerAdaptiveLayout updatedPreferredColumns:toHideSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout columnTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout splitViewControllerColumnDisplayedAfterSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout planeCount];
-[_UISplitViewControllerAdaptiveLayout maskedCornersForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout columnVisibilityForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout primaryRectEdgeForPlaneLevel:];
-[_UISplitViewControllerAdaptiveLayout maximumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout dimmingLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout planeLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout rectEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout preferredSize];
-[_UISplitViewControllerAdaptiveLayout columnFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayout enumerateZOrder:planeLevel:withBlock:];
```
