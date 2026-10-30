# `_UITextFloatingCursorSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIInvalidatable`
- 4 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isValid;
@"<UITextCursorAssertion>" _ghostCursorAssertion;
@"UITextSelectionDisplayInteraction" _manager;
@"UIStandardTextCursorView" _floatingCursorView;
```

## Properties

```
@property (T@"UITextSelectionDisplayInteraction",R,W,N,V_manager) manager;
@property (T@"UIStandardTextCursorView",R,N,V_floatingCursorView) floatingCursorView;
@property (T@"UIView",R,N,G_selectionContainerView) selectionContainerView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextFloatingCursorSession _invalidate];
-[_UITextFloatingCursorSession dealloc];
-[_UITextFloatingCursorSession manager];
-[_UITextFloatingCursorSession _invalidateAnimated:];
-[_UITextFloatingCursorSession _selectionContainerView];
-[_UITextFloatingCursorSession _springAnimation];
-[_UITextFloatingCursorSession _updateCursorFadedHiddenForFloatingCursorAtPoint:];
-[_UITextFloatingCursorSession floatingCursorPositionForPoint:lineSnapping:];
-[_UITextFloatingCursorSession floatingCursorView];
-[_UITextFloatingCursorSession initWithCursorView:selectionManager:];
-[_UITextFloatingCursorSession updateWithPoint:inContainer:animated:];
```
