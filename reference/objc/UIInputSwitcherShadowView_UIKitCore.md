# `UIInputSwitcherShadowView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
i m_mode;
d m_pointerOffset;
@"NSArray" m_gradientColors;
@"UIKeyboardMenuView" _menu;
@"_UIBackdropView" _blurView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyRect;
```

## Properties

```
@property (Ti,N,Vm_mode) mode;
@property (T@"UIKeyboardMenuView",N,V_menu) menu;
@property (T@"_UIBackdropView",&,N,V_blurView) blurView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_keyRect) keyRect;
@property (Td,N,Vm_pointerOffset) pointerOffset;
@property (T@"NSArray",&,N,Vm_gradientColors) gradientColors;
```

## Instance methods

```
-[UIInputSwitcherShadowView menu];
-[UIInputSwitcherShadowView blurView];
-[UIInputSwitcherShadowView setBlurView:];
-[UIInputSwitcherShadowView keyRect];
-[UIInputSwitcherShadowView setPointerOffset:];
-[UIInputSwitcherShadowView drawRect:];
-[UIInputSwitcherShadowView layoutSubviews];
-[UIInputSwitcherShadowView setMode:];
-[UIInputSwitcherShadowView setKeyRect:];
-[UIInputSwitcherShadowView mode];
-[UIInputSwitcherShadowView setFrame:];
-[UIInputSwitcherShadowView initWithFrame:];
-[UIInputSwitcherShadowView pointerOffset];
-[UIInputSwitcherShadowView setMenu:];
-[UIInputSwitcherShadowView gradientColors];
-[UIInputSwitcherShadowView setGradientColors:];
```
