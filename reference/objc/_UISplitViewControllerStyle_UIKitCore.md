# `_UISplitViewControllerStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualStyleProviding`
- 1 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"UISplitViewController" _splitViewController;
```

## Properties

```
@property (TB,R,N) allowsInteractivePresentationGestures;
@property (TB,R,N) dimsColumnsForOverlay;
@property (Tq,R,N) planeMaximumColumnCount;
@property (TB,R,N) showsSeparators;
@property (Td,R,N) separatorThickness;
@property (T@"UISplitViewController",R,W,N,V_splitViewController) splitViewController;
@property (T@"UIColor",R,N) primaryBackgroundColor;
@property (TB,R,N) alwaysHideSidebarToggleButton;
@property (Td,R,N) maximumRubberbandingDistance;
@property (TB,R,N) allowsColumnResize;
@property (TB,R,N) allowsSceneResize;
```

## Instance methods

```
-[_UISplitViewControllerStyle splitViewController];
-[_UISplitViewControllerStyle maximumRubberbandingDistance];
-[_UISplitViewControllerStyle separatorThickness];
-[_UISplitViewControllerStyle backgroundForBackgroundStyle:];
-[_UISplitViewControllerStyle preferredWidthForColumn:containerSize:];
-[_UISplitViewControllerStyle allowsInteractivePresentationGestures];
-[_UISplitViewControllerStyle maximumWidthForColumn:containerSize:];
-[_UISplitViewControllerStyle contentMarginStyleForColumn:];
-[_UISplitViewControllerStyle minimumWidthForColumn:containerSize:];
-[_UISplitViewControllerStyle planeMaximumColumnCount];
-[_UISplitViewControllerStyle frameInsetsForColumn:edge:];
-[_UISplitViewControllerStyle cornerRadiusForColumn:];
-[_UISplitViewControllerStyle initWithSplitViewController:];
-[_UISplitViewControllerStyle showsSeparators];
-[_UISplitViewControllerStyle primaryBackgroundColor];
-[_UISplitViewControllerStyle canDisplayAdjacentColumnBeneathColumn:];
-[_UISplitViewControllerStyle edgesExtendingIntoUnsafeAreaForColumn:];
-[_UISplitViewControllerStyle allowsColumnResize];
-[_UISplitViewControllerStyle allowsSceneResize];
-[_UISplitViewControllerStyle alwaysHideSidebarToggleButton];
-[_UISplitViewControllerStyle defaultMaximumWidthForColumn:withSize:splitBehavior:];
-[_UISplitViewControllerStyle dimsColumnsForOverlay];
-[_UISplitViewControllerStyle splitBehaviorForPreferredSplitBehavior:];
-[_UISplitViewControllerStyle splitBehaviorForSize:];
```
