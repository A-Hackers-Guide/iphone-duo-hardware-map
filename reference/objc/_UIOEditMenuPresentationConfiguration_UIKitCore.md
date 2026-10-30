# `_UIOEditMenuPresentationConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 10 instance methods, 2 class methods

## Instance variables

```
B _enforcesMenuControllerLifecycle;
@"NSString" _identifier;
@"UIMenu" _menu;
q _preferredArrowDirection;
q _initialUserInterfaceStyle;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetRect;
```

## Properties

```
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"UIMenu",R,N,V_menu) menu;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_sourceRect) sourceRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_targetRect) targetRect;
@property (TB,R,N,V_enforcesMenuControllerLifecycle) enforcesMenuControllerLifecycle;
@property (Tq,R,N,V_preferredArrowDirection) preferredArrowDirection;
@property (Tq,R,N,V_initialUserInterfaceStyle) initialUserInterfaceStyle;
```

## Class methods

```
+[_UIOEditMenuPresentationConfiguration supportsSecureCoding];
+[_UIOEditMenuPresentationConfiguration configurationWithMenu:preferredArrowDirection:sourceRect:enforcesMenuControllerLifecycle:initialUserInterfaceStyle:];
```

## Instance methods

```
-[_UIOEditMenuPresentationConfiguration menu];
-[_UIOEditMenuPresentationConfiguration sourceRect];
-[_UIOEditMenuPresentationConfiguration identifier];
-[_UIOEditMenuPresentationConfiguration preferredArrowDirection];
-[_UIOEditMenuPresentationConfiguration targetRect];
-[_UIOEditMenuPresentationConfiguration encodeWithCoder:];
-[_UIOEditMenuPresentationConfiguration initWithCoder:];
-[_UIOEditMenuPresentationConfiguration enforcesMenuControllerLifecycle];
-[_UIOEditMenuPresentationConfiguration configurationWithTargetOrigin:];
-[_UIOEditMenuPresentationConfiguration initialUserInterfaceStyle];
```
