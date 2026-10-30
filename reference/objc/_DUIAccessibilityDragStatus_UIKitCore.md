# `_DUIAccessibilityDragStatus`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _forbidden;
q _itemCount;
Q _potentialOperation;
```

## Properties

```
@property (Tq,N,V_itemCount) itemCount;
@property (TQ,N,V_potentialOperation) potentialOperation;
@property (TB,N,V_forbidden) forbidden;
```

## Class methods

```
+[_DUIAccessibilityDragStatus supportsSecureCoding];
```

## Instance methods

```
-[_DUIAccessibilityDragStatus itemCount];
-[_DUIAccessibilityDragStatus setItemCount:];
-[_DUIAccessibilityDragStatus encodeWithCoder:];
-[_DUIAccessibilityDragStatus description];
-[_DUIAccessibilityDragStatus initWithCoder:];
-[_DUIAccessibilityDragStatus forbidden];
-[_DUIAccessibilityDragStatus potentialOperation];
-[_DUIAccessibilityDragStatus setForbidden:];
-[_DUIAccessibilityDragStatus setPotentialOperation:];
```
