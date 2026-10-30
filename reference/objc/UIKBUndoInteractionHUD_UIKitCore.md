# `UIKBUndoInteractionHUD`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 13 instance variables, 13 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"<UIInteractiveUndoHUDActionDelegate>" _actionDelegate;
q _mode;
@"UIKBUndoControl" _leftButtonView;
@"UIKBUndoControl" _rightButtonView;
@"UIKBUndoControl" _aCutButtonView;
@"UIKBUndoControl" _aCopyButtonView;
@"UIKBUndoControl" _aPasteButtonView;
@"UIVisualEffectView" _backgroundEffectView;
@"UIVisualEffectView" _shadowView;
@"UIView" _containerView;
@"UIKBUndoStyling" _style;
@"UILabel" _instructionalLabel;
@"NSDate" _appearanceDate;
```

## Properties

```
@property (T@"UIVisualEffectView",&,N,V_backgroundEffectView) backgroundEffectView;
@property (T@"UIVisualEffectView",&,N,V_shadowView) shadowView;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"UIKBUndoStyling",&,N,V_style) style;
@property (T@"UIKBUndoControl",&,N,V_leftButtonView) leftButtonView;
@property (T@"UIKBUndoControl",&,N,V_rightButtonView) rightButtonView;
@property (T@"UIKBUndoControl",&,N,V_aCutButtonView) aCutButtonView;
@property (T@"UIKBUndoControl",&,N,V_aCopyButtonView) aCopyButtonView;
@property (T@"UIKBUndoControl",&,N,V_aPasteButtonView) aPasteButtonView;
@property (T@"UILabel",&,N,V_instructionalLabel) instructionalLabel;
@property (T@"NSDate",&,N,V_appearanceDate) appearanceDate;
@property (Tq,N,V_mode) mode;
@property (T@"<UIInteractiveUndoHUDActionDelegate>",W,N,V_actionDelegate) actionDelegate;
```

## Instance methods

```
-[UIKBUndoInteractionHUD setContainerView:];
-[UIKBUndoInteractionHUD setBackgroundEffectView:];
-[UIKBUndoInteractionHUD layoutSubviews];
-[UIKBUndoInteractionHUD style];
-[UIKBUndoInteractionHUD setMode:];
-[UIKBUndoInteractionHUD setStyle:];
-[UIKBUndoInteractionHUD setActionDelegate:];
-[UIKBUndoInteractionHUD containerView];
-[UIKBUndoInteractionHUD willMoveToWindow:];
-[UIKBUndoInteractionHUD shadowView];
-[UIKBUndoInteractionHUD mode];
-[UIKBUndoInteractionHUD actionDelegate];
-[UIKBUndoInteractionHUD backgroundEffectView];
-[UIKBUndoInteractionHUD setShadowView:];
-[UIKBUndoInteractionHUD pointInside:withEvent:];
-[UIKBUndoInteractionHUD aCopyButtonView];
-[UIKBUndoInteractionHUD controlForType:];
-[UIKBUndoInteractionHUD controlActionUpInside:forEvent:];
-[UIKBUndoInteractionHUD rightButtonView];
-[UIKBUndoInteractionHUD aCutButtonView];
-[UIKBUndoInteractionHUD aPasteButtonView];
-[UIKBUndoInteractionHUD appearanceDate];
-[UIKBUndoInteractionHUD availableOfControl:];
-[UIKBUndoInteractionHUD controlActionDown:];
-[UIKBUndoInteractionHUD controlActionUpOutside:];
-[UIKBUndoInteractionHUD createSeparatorView];
-[UIKBUndoInteractionHUD initWithKeyboardAppearance:isRTL:mode:sceneBounds:];
-[UIKBUndoInteractionHUD instructionalLabel];
-[UIKBUndoInteractionHUD leftButtonView];
-[UIKBUndoInteractionHUD performDelegateRedoAndUpdateHUDIfNeeded];
-[UIKBUndoInteractionHUD performDelegateUndoAndUpdateHUDIfNeeded];
-[UIKBUndoInteractionHUD setACopyButtonView:];
-[UIKBUndoInteractionHUD setACutButtonView:];
-[UIKBUndoInteractionHUD setAPasteButtonView:];
-[UIKBUndoInteractionHUD setAppearanceDate:];
-[UIKBUndoInteractionHUD setInstructionalLabel:];
-[UIKBUndoInteractionHUD setLeftButtonView:];
-[UIKBUndoInteractionHUD setRightButtonView:];
-[UIKBUndoInteractionHUD updateControlWithDirection:travelProgress:isRTL:];
-[UIKBUndoInteractionHUD updateHUDControlState];
```
