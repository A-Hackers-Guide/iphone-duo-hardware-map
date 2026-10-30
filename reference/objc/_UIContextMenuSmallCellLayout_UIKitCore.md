# `_UIContextMenuSmallCellLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuCellLayout`
- 4 instance variables, 17 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"_UIContextMenuCellContentView" _contentView;
@"NSArray" _managedConstraints;
@"NSLayoutConstraint" _firstBaselineConstraint;
@"NSLayoutConstraint" _minHeightConstraint;
```

## Properties

```
@property (T@"_UIContextMenuCellContentView",W,N,V_contentView) contentView;
@property (T@"NSArray",&,N,V_managedConstraints) managedConstraints;
@property (T@"NSLayoutConstraint",&,N,V_firstBaselineConstraint) firstBaselineConstraint;
@property (T@"NSLayoutConstraint",&,N,V_minHeightConstraint) minHeightConstraint;
@property (Tq,R,N) layoutSize;
@property (Tq,R,N) labelTextAlignment;
@property (TQ,R,N) labelMaximumNumberOfLines;
@property (T@"UIColor",R,N) preferredContentColorForCurrentState;
@property (T@"UIColor",R,N) preferredBackgroundColorForCurrentState;
@property (T@"UIHoverStyle",R,N) hoverStyle;
@property (T@"UIShape",R,N) contentShape;
@property (TB,R,N) useContentShapeForSelectionHighlight;
@property (Tq,R,N) focusStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuSmallCellLayout initWithContentView:];
-[_UIContextMenuSmallCellLayout setContentView:];
-[_UIContextMenuSmallCellLayout layoutSize];
-[_UIContextMenuSmallCellLayout setControlState:withAnimationCoordinator:];
-[_UIContextMenuSmallCellLayout useContentShapeForSelectionHighlight];
-[_UIContextMenuSmallCellLayout labelMaximumNumberOfLines];
-[_UIContextMenuSmallCellLayout contentShape];
-[_UIContextMenuSmallCellLayout preferredContentColorForCurrentState];
-[_UIContextMenuSmallCellLayout labelTextAlignment];
-[_UIContextMenuSmallCellLayout managedConstraints];
-[_UIContextMenuSmallCellLayout preferredBackgroundColorForCurrentState];
-[_UIContextMenuSmallCellLayout preferredIconFontUsingBoldFont:];
-[_UIContextMenuSmallCellLayout focusStyle];
-[_UIContextMenuSmallCellLayout removeConstraints];
-[_UIContextMenuSmallCellLayout contentView];
-[_UIContextMenuSmallCellLayout updateConstraints];
-[_UIContextMenuSmallCellLayout hoverStyle];
-[_UIContextMenuSmallCellLayout setManagedConstraints:];
-[_UIContextMenuSmallCellLayout installConstraints];
-[_UIContextMenuSmallCellLayout firstBaselineConstraint];
-[_UIContextMenuSmallCellLayout minHeightConstraint];
-[_UIContextMenuSmallCellLayout setFirstBaselineConstraint:];
-[_UIContextMenuSmallCellLayout setMinHeightConstraint:];
```
