# `UITextItemMenuConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 2 class methods

## Instance variables

```
q __preferredExpression;
Q __preferredElementDisplayMode;
@"UIMenu" _menu;
@"UITextItemMenuPreview" _preview;
```

## Properties

```
@property (Tq,N,V__preferredExpression) _preferredExpression;
@property (TQ,N,V__preferredElementDisplayMode) _preferredElementDisplayMode;
@property (T@"UIMenu",R,N,V_menu) menu;
@property (T@"UITextItemMenuPreview",R,N,V_preview) preview;
```

## Class methods

```
+[UITextItemMenuConfiguration configurationWithMenu:];
+[UITextItemMenuConfiguration configurationWithPreview:menu:];
```

## Instance methods

```
-[UITextItemMenuConfiguration menu];
-[UITextItemMenuConfiguration preview];
-[UITextItemMenuConfiguration _preferredElementDisplayMode];
-[UITextItemMenuConfiguration set_preferredElementDisplayMode:];
-[UITextItemMenuConfiguration _initWithPreview:menu:];
-[UITextItemMenuConfiguration _preferredExpression];
-[UITextItemMenuConfiguration set_preferredExpression:];
```
