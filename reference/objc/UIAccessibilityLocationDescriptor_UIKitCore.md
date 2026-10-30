# `UIAccessibilityLocationDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"NSAttributedString" _attributedName;
{CGPoint="x"d"y"d} _point;
```

## Properties

```
@property (T@"UIView",R,W,N,V_view) view;
@property (T{CGPoint=dd},R,N,V_point) point;
@property (T@"NSString",R,N) name;
@property (T@"NSAttributedString",R,N,V_attributedName) attributedName;
```

## Instance methods

```
-[UIAccessibilityLocationDescriptor attributedName];
-[UIAccessibilityLocationDescriptor view];
-[UIAccessibilityLocationDescriptor point];
-[UIAccessibilityLocationDescriptor hash];
-[UIAccessibilityLocationDescriptor isEqual:];
-[UIAccessibilityLocationDescriptor name];
-[UIAccessibilityLocationDescriptor initWithAttributedName:point:inView:];
-[UIAccessibilityLocationDescriptor initWithName:point:inView:];
-[UIAccessibilityLocationDescriptor initWithName:view:];
```
