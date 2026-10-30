# `_UISplitViewControllerAdaptiveSingleColumnLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISplitViewControllerAdaptiveLayout`
- 3 instance variables, 10 properties, 52 instance methods, 0 class methods

## Instance variables

```
data;
dataSource;
delegate;
```

## Properties

```
@property (T{CGSize=dd},N,R) contentSize;
@property (T{CGSize=dd},N,R) minimumSize;
@property (T{CGSize=dd},N,R) preferredSize;
@property (Tq,N,R) primaryEdge;
@property (Tq,N,R) splitBehavior;
@property (Tq,N,R) planeCount;
@property (Tq,N,R) displayMode;
@property (TB,N,R) isCollapsed;
@property (Tq,N,R) presentedSplitViewControllerColumn;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveSingleColumnLayout columnModeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout preferredSplitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout presentedSplitViewControllerColumn];
-[_UISplitViewControllerAdaptiveSingleColumnLayout prepareForDisplay];
-[_UISplitViewControllerAdaptiveSingleColumnLayout minimumSize];
-[_UISplitViewControllerAdaptiveSingleColumnLayout init];
-[_UISplitViewControllerAdaptiveSingleColumnLayout splitViewControllerColumnDisplayedBeforeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout canShowSplitViewControllerColumn:withSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout minimumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout initWithDataSource:delegate:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout splitViewControllerEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout userInterfaceLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout primaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout preparePresentedColumn];
-[_UISplitViewControllerAdaptiveSingleColumnLayout displayMode];
-[_UISplitViewControllerAdaptiveSingleColumnLayout enumerateDisplayOrder:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout enumeratePlanes:withBlock:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout contentSize];
-[_UISplitViewControllerAdaptiveSingleColumnLayout planeRubberBandInsetsForPlaneLevel:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout secondaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout updatedPreferredColumns:toShowSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout prepareCollapsedColumns];
-[_UISplitViewControllerAdaptiveSingleColumnLayout primaryEdge];
-[_UISplitViewControllerAdaptiveSingleColumnLayout planeTransformForPlaneLevel:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout validateData];
-[_UISplitViewControllerAdaptiveSingleColumnLayout splitBehavior];
-[_UISplitViewControllerAdaptiveSingleColumnLayout canResizeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout isCollapsed];
-[_UISplitViewControllerAdaptiveSingleColumnLayout backgroundStyleForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout splitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout separatorTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout enumerateDisplayInOrder:withBlock:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout description];
-[_UISplitViewControllerAdaptiveSingleColumnLayout contentInsetsForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout separatorFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout planeFrameForPlaneLevel:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout canCollapseColumn:style:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout updatedPreferredColumns:toHideSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout columnTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout splitViewControllerColumnDisplayedAfterSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout planeCount];
-[_UISplitViewControllerAdaptiveSingleColumnLayout maskedCornersForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout columnVisibilityForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout primaryRectEdgeForPlaneLevel:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout maximumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout dimmingLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout prepareLayout];
-[_UISplitViewControllerAdaptiveSingleColumnLayout planeLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout rectEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout preferredSize];
-[_UISplitViewControllerAdaptiveSingleColumnLayout columnFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveSingleColumnLayout enumerateZOrder:planeLevel:withBlock:];
```
