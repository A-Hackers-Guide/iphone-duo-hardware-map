# `UIKeyboardDockItemButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- 6 instance variables, 6 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"CAShapeLayer" _shapeLayer;
@"CAShapeLayer" _debugHitLayer;
@"_UISlotView" _secureDictationSlotView;
q _currentLayoutType;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _tapActionRegion;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_tapActionRegion) tapActionRegion;
@property (T@"NSString",&,N,V_identifier) identifier;
@property (T@"CAShapeLayer",&,N,V_shapeLayer) shapeLayer;
@property (T@"CAShapeLayer",&,N,V_debugHitLayer) debugHitLayer;
@property (T@"_UISlotView",&,N,V_secureDictationSlotView) secureDictationSlotView;
@property (Tq,N,V_currentLayoutType) currentLayoutType;
```

## Instance methods

```
-[UIKeyboardDockItemButton shapeLayer];
-[UIKeyboardDockItemButton buttonFont];
-[UIKeyboardDockItemButton identifier];
-[UIKeyboardDockItemButton setShapeLayer:];
-[UIKeyboardDockItemButton setTapActionRegion:];
-[UIKeyboardDockItemButton tapActionRegion];
-[UIKeyboardDockItemButton drawRect:];
-[UIKeyboardDockItemButton imageRectForContentRect:];
-[UIKeyboardDockItemButton setCurrentLayoutType:];
-[UIKeyboardDockItemButton setSecureDictationSlotView:];
-[UIKeyboardDockItemButton layoutSubviews];
-[UIKeyboardDockItemButton _setupDictationSlotView];
-[UIKeyboardDockItemButton pointInsideTapActionRegion:];
-[UIKeyboardDockItemButton rectWithSize:forContentRect:withAlignmentRectInsets:];
-[UIKeyboardDockItemButton setIdentifier:];
-[UIKeyboardDockItemButton setTintColor:];
-[UIKeyboardDockItemButton debugHitLayer];
-[UIKeyboardDockItemButton prepareForReuse];
-[UIKeyboardDockItemButton currentLayoutType];
-[UIKeyboardDockItemButton addAnimatitionIfNeeded];
-[UIKeyboardDockItemButton updateFillColor];
-[UIKeyboardDockItemButton setupDictationAnimationButtonIfNeeded];
-[UIKeyboardDockItemButton setDebugHitLayer:];
-[UIKeyboardDockItemButton titleRectForContentRect:];
-[UIKeyboardDockItemButton didMoveToSuperview];
-[UIKeyboardDockItemButton secureDictationSlotView];
```
