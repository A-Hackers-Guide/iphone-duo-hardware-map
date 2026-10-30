# `UIInputSwitcherSegmentControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 5 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _usesDarkTheme;
q _selectedSegmentIndex;
@"NSArray" _segmentTitles;
@"NSArray" _segmentImages;
@"UIStackView" _stackView;
```

## Properties

```
@property (T@"UIStackView",&,N,V_stackView) stackView;
@property (TB,N,V_usesDarkTheme) usesDarkTheme;
@property (Tq,N,V_selectedSegmentIndex) selectedSegmentIndex;
@property (TQ,R,N) numberOfSegments;
@property (T@"NSArray",C,N,V_segmentTitles) segmentTitles;
@property (T@"NSArray",&,N,V_segmentImages) segmentImages;
```

## Instance methods

```
-[UIInputSwitcherSegmentControl layoutSubviews];
-[UIInputSwitcherSegmentControl touchesBegan:withEvent:];
-[UIInputSwitcherSegmentControl touchesMoved:withEvent:];
-[UIInputSwitcherSegmentControl stackView];
-[UIInputSwitcherSegmentControl setStackView:];
-[UIInputSwitcherSegmentControl initWithFrame:];
-[UIInputSwitcherSegmentControl _populateSegmentViewsWithCount:];
-[UIInputSwitcherSegmentControl _removeAllSegmentViews];
-[UIInputSwitcherSegmentControl numberOfSegments];
-[UIInputSwitcherSegmentControl segmentImages];
-[UIInputSwitcherSegmentControl segmentTitles];
-[UIInputSwitcherSegmentControl selectedSegmentIndex];
-[UIInputSwitcherSegmentControl setSegmentImages:];
-[UIInputSwitcherSegmentControl setSegmentTitles:];
-[UIInputSwitcherSegmentControl setSelectedSegmentIndex:];
-[UIInputSwitcherSegmentControl setUsesDarkTheme:];
-[UIInputSwitcherSegmentControl shouldTrack];
-[UIInputSwitcherSegmentControl updateSelectionWithPoint:];
-[UIInputSwitcherSegmentControl usesDarkTheme];
```
