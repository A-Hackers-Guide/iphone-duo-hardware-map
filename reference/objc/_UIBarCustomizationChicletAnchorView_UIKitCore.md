# `_UIBarCustomizationChicletAnchorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 6 instance variables, 6 properties, 18 instance methods, 6 class methods

## Instance variables

```
B _jiggling;
B _debugUIEnabled;
q _state;
d _contentPadding;
@"_UIBarCustomizationChiclet" _chiclet;
@"UIView" _positionAdaptorView;
```

## Properties

```
@property (T@"UIView",&,N,V_positionAdaptorView) positionAdaptorView;
@property (TB,N,V_debugUIEnabled) debugUIEnabled;
@property (Tq,N,V_state) state;
@property (Td,N,V_contentPadding) contentPadding;
@property (TB,N,V_jiggling) jiggling;
@property (T@"_UIBarCustomizationChiclet",&,N,V_chiclet) chiclet;
```

## Class methods

```
+[_UIBarCustomizationChicletAnchorView _jitterRotationAnimationWithAmount:];
+[_UIBarCustomizationChicletAnchorView _jitterRotationAnimationWithStrength:];
+[_UIBarCustomizationChicletAnchorView _jitterXTranslationAnimationWithAmount:];
+[_UIBarCustomizationChicletAnchorView _jitterXTranslationAnimationWithStrength:];
+[_UIBarCustomizationChicletAnchorView _jitterYTranslationAnimationWithAmount:];
+[_UIBarCustomizationChicletAnchorView _jitterYTranslationAnimationWithStrength:];
```

## Instance methods

```
-[_UIBarCustomizationChicletAnchorView setState:];
-[_UIBarCustomizationChicletAnchorView isUserInteractionEnabled];
-[_UIBarCustomizationChicletAnchorView init];
-[_UIBarCustomizationChicletAnchorView layoutSubviews];
-[_UIBarCustomizationChicletAnchorView hitTest:withEvent:];
-[_UIBarCustomizationChicletAnchorView sizeThatFits:];
-[_UIBarCustomizationChicletAnchorView description];
-[_UIBarCustomizationChicletAnchorView setContentPadding:];
-[_UIBarCustomizationChicletAnchorView contentPadding];
-[_UIBarCustomizationChicletAnchorView state];
-[_UIBarCustomizationChicletAnchorView chiclet];
-[_UIBarCustomizationChicletAnchorView debugUIEnabled];
-[_UIBarCustomizationChicletAnchorView jiggling];
-[_UIBarCustomizationChicletAnchorView positionAdaptorView];
-[_UIBarCustomizationChicletAnchorView setChiclet:];
-[_UIBarCustomizationChicletAnchorView setDebugUIEnabled:];
-[_UIBarCustomizationChicletAnchorView setJiggling:];
-[_UIBarCustomizationChicletAnchorView setPositionAdaptorView:];
```
