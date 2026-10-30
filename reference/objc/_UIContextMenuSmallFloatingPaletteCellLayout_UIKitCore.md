# `_UIContextMenuSmallFloatingPaletteCellLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuCellLayout`
- 4 instance variables, 17 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"_UIContextMenuCellContentView" _contentView;
@"NSArray" _managedConstraints;
@"_UIFloatingContentView" _floatingContentView;
Q _controlState;
```

## Properties

```
@property (T@"_UIContextMenuCellContentView",W,N,V_contentView) contentView;
@property (T@"NSArray",&,N,V_managedConstraints) managedConstraints;
@property (T@"_UIFloatingContentView",&,N,V_floatingContentView) floatingContentView;
@property (TQ,N,V_controlState) controlState;
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
-[_UIContextMenuSmallFloatingPaletteCellLayout initWithContentView:];
-[_UIContextMenuSmallFloatingPaletteCellLayout setContentView:];
-[_UIContextMenuSmallFloatingPaletteCellLayout layoutSize];
-[_UIContextMenuSmallFloatingPaletteCellLayout setControlState:withAnimationCoordinator:];
-[_UIContextMenuSmallFloatingPaletteCellLayout useContentShapeForSelectionHighlight];
-[_UIContextMenuSmallFloatingPaletteCellLayout labelMaximumNumberOfLines];
-[_UIContextMenuSmallFloatingPaletteCellLayout contentShape];
-[_UIContextMenuSmallFloatingPaletteCellLayout preferredContentColorForCurrentState];
-[_UIContextMenuSmallFloatingPaletteCellLayout labelTextAlignment];
-[_UIContextMenuSmallFloatingPaletteCellLayout managedConstraints];
-[_UIContextMenuSmallFloatingPaletteCellLayout preferredBackgroundColorForCurrentState];
-[_UIContextMenuSmallFloatingPaletteCellLayout preferredIconFontUsingBoldFont:];
-[_UIContextMenuSmallFloatingPaletteCellLayout focusStyle];
-[_UIContextMenuSmallFloatingPaletteCellLayout floatingContentView];
-[_UIContextMenuSmallFloatingPaletteCellLayout removeConstraints];
-[_UIContextMenuSmallFloatingPaletteCellLayout contentView];
-[_UIContextMenuSmallFloatingPaletteCellLayout updateConstraints];
-[_UIContextMenuSmallFloatingPaletteCellLayout hoverStyle];
-[_UIContextMenuSmallFloatingPaletteCellLayout setManagedConstraints:];
-[_UIContextMenuSmallFloatingPaletteCellLayout installConstraints];
-[_UIContextMenuSmallFloatingPaletteCellLayout _configureSharedFloatingContentViewStyle];
-[_UIContextMenuSmallFloatingPaletteCellLayout allowsHighlightingOnHover];
-[_UIContextMenuSmallFloatingPaletteCellLayout controlState];
-[_UIContextMenuSmallFloatingPaletteCellLayout setControlState:];
-[_UIContextMenuSmallFloatingPaletteCellLayout setFloatingContentView:];
```
