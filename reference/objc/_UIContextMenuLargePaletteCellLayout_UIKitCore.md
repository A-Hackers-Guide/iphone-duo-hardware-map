# `_UIContextMenuLargePaletteCellLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIContextMenuCellLayout`
- 2 instance variables, 15 properties, 19 instance methods, 0 class methods

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
-[_UIContextMenuLargePaletteCellLayout initWithContentView:];
-[_UIContextMenuLargePaletteCellLayout setContentView:];
-[_UIContextMenuLargePaletteCellLayout layoutSize];
-[_UIContextMenuLargePaletteCellLayout setControlState:withAnimationCoordinator:];
-[_UIContextMenuLargePaletteCellLayout useContentShapeForSelectionHighlight];
-[_UIContextMenuLargePaletteCellLayout labelMaximumNumberOfLines];
-[_UIContextMenuLargePaletteCellLayout contentShape];
-[_UIContextMenuLargePaletteCellLayout preferredContentColorForCurrentState];
-[_UIContextMenuLargePaletteCellLayout labelTextAlignment];
-[_UIContextMenuLargePaletteCellLayout managedConstraints];
-[_UIContextMenuLargePaletteCellLayout preferredBackgroundColorForCurrentState];
-[_UIContextMenuLargePaletteCellLayout preferredIconFontUsingBoldFont:];
-[_UIContextMenuLargePaletteCellLayout focusStyle];
-[_UIContextMenuLargePaletteCellLayout removeConstraints];
-[_UIContextMenuLargePaletteCellLayout contentView];
-[_UIContextMenuLargePaletteCellLayout updateConstraints];
-[_UIContextMenuLargePaletteCellLayout hoverStyle];
-[_UIContextMenuLargePaletteCellLayout setManagedConstraints:];
-[_UIContextMenuLargePaletteCellLayout installConstraints];
```
