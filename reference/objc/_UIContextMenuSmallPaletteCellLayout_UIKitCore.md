# `_UIContextMenuSmallPaletteCellLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuCellLayout`
- 2 instance variables, 15 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"_UIContextMenuCellContentView" _contentView;
@"NSArray" _managedConstraints;
```

## Properties

```
@property (T@"_UIContextMenuCellContentView",W,N,V_contentView) contentView;
@property (T@"NSArray",&,N,V_managedConstraints) managedConstraints;
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
-[_UIContextMenuSmallPaletteCellLayout initWithContentView:];
-[_UIContextMenuSmallPaletteCellLayout setContentView:];
-[_UIContextMenuSmallPaletteCellLayout layoutSize];
-[_UIContextMenuSmallPaletteCellLayout setControlState:withAnimationCoordinator:];
-[_UIContextMenuSmallPaletteCellLayout useContentShapeForSelectionHighlight];
-[_UIContextMenuSmallPaletteCellLayout labelMaximumNumberOfLines];
-[_UIContextMenuSmallPaletteCellLayout contentShape];
-[_UIContextMenuSmallPaletteCellLayout preferredContentColorForCurrentState];
-[_UIContextMenuSmallPaletteCellLayout labelTextAlignment];
-[_UIContextMenuSmallPaletteCellLayout managedConstraints];
-[_UIContextMenuSmallPaletteCellLayout preferredBackgroundColorForCurrentState];
-[_UIContextMenuSmallPaletteCellLayout preferredIconFontUsingBoldFont:];
-[_UIContextMenuSmallPaletteCellLayout focusStyle];
-[_UIContextMenuSmallPaletteCellLayout removeConstraints];
-[_UIContextMenuSmallPaletteCellLayout contentView];
-[_UIContextMenuSmallPaletteCellLayout updateConstraints];
-[_UIContextMenuSmallPaletteCellLayout hoverStyle];
-[_UIContextMenuSmallPaletteCellLayout setManagedConstraints:];
-[_UIContextMenuSmallPaletteCellLayout installConstraints];
-[_UIContextMenuSmallPaletteCellLayout _rectForHighlightContentShape];
```
