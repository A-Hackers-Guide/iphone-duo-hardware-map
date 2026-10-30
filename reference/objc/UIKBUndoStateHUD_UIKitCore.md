# `UIKBUndoStateHUD`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
q _controlType;
@"NSLayoutConstraint" _undoStateHUDWidthConstraint;
@"NSLayoutConstraint" _undoStateHUDHeightConstraint;
@"UIVisualEffectView" _shadowView;
@"UIView" _containerView;
@"UILabel" _labelView;
@"UIKBUndoStyling" _style;
```

## Properties

```
@property (T@"UIVisualEffectView",&,N,V_shadowView) shadowView;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UILabel",&,N,V_labelView) labelView;
@property (T@"UIKBUndoStyling",&,N,V_style) style;
@property (Tq,N,V_controlType) controlType;
@property (T@"NSLayoutConstraint",&,N,V_undoStateHUDWidthConstraint) undoStateHUDWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_undoStateHUDHeightConstraint) undoStateHUDHeightConstraint;
```

## Instance methods

```
-[UIKBUndoStateHUD setContainerView:];
-[UIKBUndoStateHUD setControlType:];
-[UIKBUndoStateHUD layoutSubviews];
-[UIKBUndoStateHUD style];
-[UIKBUndoStateHUD setStyle:];
-[UIKBUndoStateHUD containerView];
-[UIKBUndoStateHUD shadowView];
-[UIKBUndoStateHUD controlType];
-[UIKBUndoStateHUD setShadowView:];
-[UIKBUndoStateHUD labelView];
-[UIKBUndoStateHUD setUndoStateHUDWidthConstraint:];
-[UIKBUndoStateHUD initWithKeyboardAppearance:];
-[UIKBUndoStateHUD setLabelView:];
-[UIKBUndoStateHUD setUndoStateHUDHeightConstraint:];
-[UIKBUndoStateHUD undoStateHUDHeightConstraint];
-[UIKBUndoStateHUD undoStateHUDWidthConstraint];
-[UIKBUndoStateHUD updateUndoStateHUDControlType:available:];
```
