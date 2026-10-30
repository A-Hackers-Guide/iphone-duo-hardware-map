# `SlidingPaneViewState`

- Image: [`/System/Library/PrivateFrameworks/FMCoreUI.framework/FMCoreUI`](../userland/System__Library__PrivateFrameworks__FMCoreUI.framework__FMCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _shouldNotifyOfPaneSizeChanges;
@"UIViewController" _paneViewController;
@"ISPaneFrameView" _paneView;
@"UIVisualEffectView" _visualEffectView;
@"NSLayoutConstraint" _paneVerticalPositionConstraint;
@"NSLayoutConstraint" _paneHorizontalPositionConstraint;
Q _edge;
```

## Properties

```
@property (T@"UIViewController",&,N,V_paneViewController) paneViewController;
@property (T@"ISPaneFrameView",&,N,V_paneView) paneView;
@property (T@"UIVisualEffectView",&,N,V_visualEffectView) visualEffectView;
@property (T@"NSLayoutConstraint",&,N,V_paneVerticalPositionConstraint) paneVerticalPositionConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paneHorizontalPositionConstraint) paneHorizontalPositionConstraint;
@property (TB,N,V_shouldNotifyOfPaneSizeChanges) shouldNotifyOfPaneSizeChanges;
@property (TQ,N,V_edge) edge;
```

## Instance methods

```
-[SlidingPaneViewState setEdge:];
-[SlidingPaneViewState visualEffectView];
-[SlidingPaneViewState edge];
-[SlidingPaneViewState dealloc];
-[SlidingPaneViewState setVisualEffectView:];
-[SlidingPaneViewState paneViewController];
-[SlidingPaneViewState initWithViewController:edge:];
-[SlidingPaneViewState paneHorizontalPositionConstraint];
-[SlidingPaneViewState paneVerticalPositionConstraint];
-[SlidingPaneViewState paneView];
-[SlidingPaneViewState setPaneHorizontalPositionConstraint:];
-[SlidingPaneViewState setPaneVerticalPositionConstraint:];
-[SlidingPaneViewState setPaneView:];
-[SlidingPaneViewState setPaneViewController:];
-[SlidingPaneViewState setShouldNotifyOfPaneSizeChanges:];
-[SlidingPaneViewState shouldNotifyOfPaneSizeChanges];
```
