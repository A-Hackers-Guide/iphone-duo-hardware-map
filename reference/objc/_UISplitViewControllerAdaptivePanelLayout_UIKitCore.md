# `_UISplitViewControllerAdaptivePanelLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISplitViewControllerAdaptiveLayout`
- 4 instance variables, 10 properties, 48 instance methods, 0 class methods

## Instance variables

```
data;
solution;
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
-[_UISplitViewControllerAdaptivePanelLayout columnModeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout preferredSplitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptivePanelLayout presentedSplitViewControllerColumn];
-[_UISplitViewControllerAdaptivePanelLayout prepareForDisplay];
-[_UISplitViewControllerAdaptivePanelLayout minimumSize];
-[_UISplitViewControllerAdaptivePanelLayout init];
-[_UISplitViewControllerAdaptivePanelLayout splitViewControllerColumnDisplayedBeforeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout canShowSplitViewControllerColumn:withSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout minimumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout initWithDataSource:delegate:];
-[_UISplitViewControllerAdaptivePanelLayout splitViewControllerEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout userInterfaceLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout primaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout displayMode];
-[_UISplitViewControllerAdaptivePanelLayout enumerateDisplayOrder:];
-[_UISplitViewControllerAdaptivePanelLayout enumeratePlanes:withBlock:];
-[_UISplitViewControllerAdaptivePanelLayout contentSize];
-[_UISplitViewControllerAdaptivePanelLayout planeRubberBandInsetsForPlaneLevel:];
-[_UISplitViewControllerAdaptivePanelLayout secondaryEdgeButtonForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout updatedPreferredColumns:toShowSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout primaryEdge];
-[_UISplitViewControllerAdaptivePanelLayout planeTransformForPlaneLevel:];
-[_UISplitViewControllerAdaptivePanelLayout splitBehavior];
-[_UISplitViewControllerAdaptivePanelLayout canResizeSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout isCollapsed];
-[_UISplitViewControllerAdaptivePanelLayout backgroundStyleForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout splitViewControllerColumnAtEdge:];
-[_UISplitViewControllerAdaptivePanelLayout separatorTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout enumerateDisplayInOrder:withBlock:];
-[_UISplitViewControllerAdaptivePanelLayout description];
-[_UISplitViewControllerAdaptivePanelLayout contentInsetsForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout separatorFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout planeFrameForPlaneLevel:];
-[_UISplitViewControllerAdaptivePanelLayout updatedPreferredColumns:toHideSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout columnTransformForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout splitViewControllerColumnDisplayedAfterSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout planeCount];
-[_UISplitViewControllerAdaptivePanelLayout maskedCornersForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout columnVisibilityForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout primaryRectEdgeForPlaneLevel:];
-[_UISplitViewControllerAdaptivePanelLayout maximumWidthForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout dimmingLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout prepareLayout];
-[_UISplitViewControllerAdaptivePanelLayout planeLevelForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout rectEdgeForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout preferredSize];
-[_UISplitViewControllerAdaptivePanelLayout columnFrameForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptivePanelLayout enumerateZOrder:planeLevel:withBlock:];
```
