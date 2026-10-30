# `_UIContextMenuCellLayout` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 15 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) layoutSize;
@property (Tq,R,N) labelTextAlignment;
@property (TQ,R,N) labelMaximumNumberOfLines;
@property (T@"UIColor",R,N) preferredContentColorForCurrentState;
@property (T@"UIColor",R,N) preferredBackgroundColorForCurrentState;
@property (T@"UIHoverStyle",R,N) hoverStyle;
@property (T@"UIShape",R,N) contentShape;
@property (TB,R,N) useContentShapeForSelectionHighlight;
@property (Tq,R,N) focusStyle;
```

## Instance methods

```
-[_UIContextMenuCellLayout initWithContentView:];
-[_UIContextMenuCellLayout layoutSize];
-[_UIContextMenuCellLayout setControlState:withAnimationCoordinator:];
-[_UIContextMenuCellLayout useContentShapeForSelectionHighlight];
-[_UIContextMenuCellLayout labelMaximumNumberOfLines];
-[_UIContextMenuCellLayout contentShape];
-[_UIContextMenuCellLayout preferredContentColorForCurrentState];
-[_UIContextMenuCellLayout labelTextAlignment];
-[_UIContextMenuCellLayout preferredBackgroundColorForCurrentState];
-[_UIContextMenuCellLayout preferredIconFontUsingBoldFont:];
-[_UIContextMenuCellLayout focusStyle];
-[_UIContextMenuCellLayout removeConstraints];
-[_UIContextMenuCellLayout updateConstraints];
-[_UIContextMenuCellLayout hoverStyle];
-[_UIContextMenuCellLayout installConstraints];
```
