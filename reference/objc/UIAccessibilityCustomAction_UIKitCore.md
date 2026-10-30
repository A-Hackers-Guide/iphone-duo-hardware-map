# `UIAccessibilityCustomAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 7 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"UIImage" _image;
@"NSAttributedString" _attributedName;
@ _target;
: _selector;
@? _actionHandler;
@"NSString" _category;
```

## Properties

```
@property (T@"NSString",C,N) name;
@property (T@"UIImage",&,N,V_image) image;
@property (T@"NSAttributedString",C,N,V_attributedName) attributedName;
@property (T@,W,N,V_target) target;
@property (T:,N,V_selector) selector;
@property (T@?,C,N,V_actionHandler) actionHandler;
@property (T@"NSString",C,N,V_category) category;
```

## Instance methods

```
-[UIAccessibilityCustomAction selector];
-[UIAccessibilityCustomAction setCategory:];
-[UIAccessibilityCustomAction init];
-[UIAccessibilityCustomAction category];
-[UIAccessibilityCustomAction attributedName];
-[UIAccessibilityCustomAction setActionHandler:];
-[UIAccessibilityCustomAction setSelector:];
-[UIAccessibilityCustomAction actionHandler];
-[UIAccessibilityCustomAction setTarget:];
-[UIAccessibilityCustomAction setName:];
-[UIAccessibilityCustomAction image];
-[UIAccessibilityCustomAction target];
-[UIAccessibilityCustomAction name];
-[UIAccessibilityCustomAction setImage:];
-[UIAccessibilityCustomAction initWithAttributedName:actionHandler:];
-[UIAccessibilityCustomAction initWithAttributedName:image:actionHandler:];
-[UIAccessibilityCustomAction initWithAttributedName:image:target:selector:];
-[UIAccessibilityCustomAction initWithAttributedName:target:selector:];
-[UIAccessibilityCustomAction initWithName:actionHandler:];
-[UIAccessibilityCustomAction initWithName:image:actionHandler:];
-[UIAccessibilityCustomAction initWithName:image:target:selector:];
-[UIAccessibilityCustomAction initWithName:target:selector:];
-[UIAccessibilityCustomAction setAttributedName:];
```
