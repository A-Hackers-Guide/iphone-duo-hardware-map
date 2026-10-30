# `_UISplitViewControllerAdaptiveLayoutDataSource` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",R,N) containerDivisionReservedRegions;
@property (T{UIEdgeInsets=dddd},R,N) containerInsets;
@property (T{CGSize=dd},R,N) containerSize;
@property (TB,R,N) hasAppeared;
@property (TB,R,N) hasDisplayModeButton;
@property (TB,R,N) isRTL;
@property (T@"NSArray",R,N) planes;
@property (T@"_UISplitViewControllerAdaptiveLayoutPreferences",R,N) preferences;
@property (T{_UISplitViewControllerAdaptiveLayoutPreferredColumns=qqqqqqQQ},R,N) preferredColumns;
@property (Tq,R,N) primaryEdge;
@property (Tq,R,N) style;
@property (T@"UITraitCollection",R,N) traitCollection;
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveLayoutDataSource containerSize];
-[_UISplitViewControllerAdaptiveLayoutDataSource planes];
-[_UISplitViewControllerAdaptiveLayoutDataSource traitCollection];
-[_UISplitViewControllerAdaptiveLayoutDataSource preferences];
-[_UISplitViewControllerAdaptiveLayoutDataSource hasAppeared];
-[_UISplitViewControllerAdaptiveLayoutDataSource style];
-[_UISplitViewControllerAdaptiveLayoutDataSource primaryEdge];
-[_UISplitViewControllerAdaptiveLayoutDataSource columnForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayoutDataSource preferredColumns];
-[_UISplitViewControllerAdaptiveLayoutDataSource additionalContainerContentInsetsForSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveLayoutDataSource hasDisplayModeButton];
-[_UISplitViewControllerAdaptiveLayoutDataSource containerDivisionReservedRegions];
-[_UISplitViewControllerAdaptiveLayoutDataSource isRTL];
-[_UISplitViewControllerAdaptiveLayoutDataSource containerInsets];
```
