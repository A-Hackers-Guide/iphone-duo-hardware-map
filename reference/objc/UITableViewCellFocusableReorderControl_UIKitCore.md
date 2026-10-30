# `UITableViewCellFocusableReorderControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITableViewCellReorderControl`
- Protocols: `_UIFloatingContentViewDelegate`
- 5 instance variables, 4 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"_UIFloatingContentView" _floatingContentView;
@"UIPanGestureRecognizer" _panRecognizer;
@"UITapGestureRecognizer" _upArrowButtonRecognizer;
@"UITapGestureRecognizer" _downArrowButtonRecognizer;
B _cellHasReorderingAppearance;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITableViewCellFocusableReorderControl didUpdateFocusInContext:withAnimationCoordinator:];
-[UITableViewCellFocusableReorderControl pressesCancelled:withEvent:];
-[UITableViewCellFocusableReorderControl pressesEnded:withEvent:];
-[UITableViewCellFocusableReorderControl endTrackingWithTouch:withEvent:];
-[UITableViewCellFocusableReorderControl continueTrackingWithTouch:withEvent:];
-[UITableViewCellFocusableReorderControl layoutSubviews];
-[UITableViewCellFocusableReorderControl beginTrackingWithTouch:withEvent:];
-[UITableViewCellFocusableReorderControl pressesBegan:withEvent:];
-[UITableViewCellFocusableReorderControl traitCollectionDidChange:];
-[UITableViewCellFocusableReorderControl floatingContentView:isTransitioningFromState:toState:];
-[UITableViewCellFocusableReorderControl shouldUpdateFocusInContext:];
-[UITableViewCellFocusableReorderControl floatingContentView:didFinishTransitioningToState:];
-[UITableViewCellFocusableReorderControl _panRecognizer:];
-[UITableViewCellFocusableReorderControl _upArrowButton:];
-[UITableViewCellFocusableReorderControl _arrowButton:];
-[UITableViewCellFocusableReorderControl _beginIndirectTracking];
-[UITableViewCellFocusableReorderControl _downArrowButton:];
-[UITableViewCellFocusableReorderControl _endIndirectTracking];
-[UITableViewCellFocusableReorderControl _shouldHandlePressEvent:];
-[UITableViewCellFocusableReorderControl _updateFloatingViewForCurrentTraits];
-[UITableViewCellFocusableReorderControl _updateFocusedFloatingContentView:];
-[UITableViewCellFocusableReorderControl initWithTableViewCell:];
-[UITableViewCellFocusableReorderControl wantsMaskingWhileAnimatingDisabled];
```
