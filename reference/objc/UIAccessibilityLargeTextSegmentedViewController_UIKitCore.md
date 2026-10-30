# `UIAccessibilityLargeTextSegmentedViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 5 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UISegmentedControl" _segmentedControl;
@"NSMutableArray" _segmentButtons;
@"UISegment" _originalSelectedSegment;
@"NSArray" _segments;
@"UIScrollView" _mainScrollView;
```

## Properties

```
@property (T@"UISegment",&,N,V_originalSelectedSegment) originalSelectedSegment;
@property (T@"NSArray",&,N,V_segments) segments;
@property (T@"UIScrollView",&,N,V_mainScrollView) mainScrollView;
@property (T@"UISegmentedControl",&,N,V_segmentedControl) segmentedControl;
@property (T@"NSMutableArray",&,N,V_segmentButtons) segmentButtons;
```

## Instance methods

```
-[UIAccessibilityLargeTextSegmentedViewController segments];
-[UIAccessibilityLargeTextSegmentedViewController viewDidLayoutSubviews];
-[UIAccessibilityLargeTextSegmentedViewController _canShowWhileLocked];
-[UIAccessibilityLargeTextSegmentedViewController setSegments:];
-[UIAccessibilityLargeTextSegmentedViewController _configureSegmentViews];
-[UIAccessibilityLargeTextSegmentedViewController _orientationChanged:];
-[UIAccessibilityLargeTextSegmentedViewController buttonPress:];
-[UIAccessibilityLargeTextSegmentedViewController buttonTouchDown:];
-[UIAccessibilityLargeTextSegmentedViewController buttonTouchUp:];
-[UIAccessibilityLargeTextSegmentedViewController initWithSegmentedControl:segments:delegate:];
-[UIAccessibilityLargeTextSegmentedViewController mainScrollView];
-[UIAccessibilityLargeTextSegmentedViewController originalSelectedSegment];
-[UIAccessibilityLargeTextSegmentedViewController segmentButtons];
-[UIAccessibilityLargeTextSegmentedViewController segmentFromSegment:];
-[UIAccessibilityLargeTextSegmentedViewController segmentedControl];
-[UIAccessibilityLargeTextSegmentedViewController setMainScrollView:];
-[UIAccessibilityLargeTextSegmentedViewController setOriginalSelectedSegment:];
-[UIAccessibilityLargeTextSegmentedViewController setSegmentButtons:];
-[UIAccessibilityLargeTextSegmentedViewController setSegmentedControl:];
```
