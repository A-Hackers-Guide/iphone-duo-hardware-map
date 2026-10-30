# `_UIInputViewSetPlacementDragToDismiss`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIInputViewSetPlacementOnScreen`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 11 instance methods, 2 class methods

## Instance variables

```
B _dismissKeyboardOnly;
d _offset;
```

## Properties

```
@property (Td,N,V_offset) offset;
@property (TB,N,V_dismissKeyboardOnly) dismissKeyboardOnly;
```

## Class methods

```
+[_UIInputViewSetPlacementDragToDismiss supportsSecureCoding];
+[_UIInputViewSetPlacementDragToDismiss placementWithOffset:dismissKeyboardOnly:];
```

## Instance methods

```
-[_UIInputViewSetPlacementDragToDismiss dismissKeyboardOnly];
-[_UIInputViewSetPlacementDragToDismiss isInteractive];
-[_UIInputViewSetPlacementDragToDismiss applicatorClassForKeyboard:];
-[_UIInputViewSetPlacementDragToDismiss verticalConstraintForInputViewSet:hostView:containerView:];
-[_UIInputViewSetPlacementDragToDismiss setDismissKeyboardOnly:];
-[_UIInputViewSetPlacementDragToDismiss encodeWithCoder:];
-[_UIInputViewSetPlacementDragToDismiss showsInputOrAssistantViewsForTracking];
-[_UIInputViewSetPlacementDragToDismiss initWithCoder:];
-[_UIInputViewSetPlacementDragToDismiss setOffset:];
-[_UIInputViewSetPlacementDragToDismiss isEqual:];
-[_UIInputViewSetPlacementDragToDismiss offset];
```
