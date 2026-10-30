# `UIMenuController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIEditMenuInteractionDelegate`
- 6 instance variables, 8 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"UIEditMenuInteraction" _currentMenuInteraction;
@"NSArray" _extraMenuItems;
@"UIView" _targetView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetRect;
B _menuNeedsUpdate;
q _arrowDirection;
```

## Properties

```
@property (TB,N,GisMenuVisible) menuVisible;
@property (Tq,N,V_arrowDirection) arrowDirection;
@property (T@"NSArray",C,D,N) menuItems;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) menuFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIMenuController sharedMenuController];
```

## Instance methods

```
-[UIMenuController setArrowDirection:];
-[UIMenuController editMenuInteraction:willPresentMenuForConfiguration:animator:];
-[UIMenuController update];
-[UIMenuController init];
-[UIMenuController dealloc];
-[UIMenuController editMenuInteraction:targetRectForConfiguration:];
-[UIMenuController editMenuInteraction:willDismissMenuForConfiguration:animator:];
-[UIMenuController arrowDirection];
-[UIMenuController editMenuInteraction:menuForConfiguration:suggestedActions:];
-[UIMenuController _resolvedEditMenuArrowDirection];
-[UIMenuController setMenuVisible:];
-[UIMenuController _setTargetRect:inView:animated:];
-[UIMenuController _applicationDidAddDeactivationReason:];
-[UIMenuController _dismissEditMenu];
-[UIMenuController _editMenuInteraction:firstResponderTargetForConfiguration:];
-[UIMenuController _prepareEditMenuInteractionIfNeeded];
-[UIMenuController _presentEditMenu];
-[UIMenuController _shouldPassthroughInView];
-[UIMenuController _targetRect];
-[UIMenuController _targetView];
-[UIMenuController hideMenu];
-[UIMenuController hideMenuFromView:];
-[UIMenuController isMenuVisible];
-[UIMenuController menuFrame];
-[UIMenuController menuItems];
-[UIMenuController setMenuItems:];
-[UIMenuController setMenuVisible:animated:];
-[UIMenuController setTargetRect:inView:];
-[UIMenuController showMenuFromView:rect:];
```
