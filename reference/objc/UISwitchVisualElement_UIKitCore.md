# `UISwitchVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 21 instance methods, 3 class methods

## Instance variables

```
B _enabled;
@"NSString" _title;
@"<UISwitchControl>" _switchControl;
@"UIImpactFeedbackGenerator" _impactFeedbackGenerator;
d _enabledAlpha;
```

## Properties

```
@property (Td,N,V_enabledAlpha) enabledAlpha;
@property (TB,N,V_enabled) enabled;
@property (T@"NSString",C,V_title) title;
@property (T@"<UISwitchControl>",W,N,V_switchControl) switchControl;
@property (T@"UIImpactFeedbackGenerator",&,N,V_impactFeedbackGenerator) impactFeedbackGenerator;
```

## Class methods

```
+[UISwitchVisualElement preferredContentSize];
+[UISwitchVisualElement preferredAlignmentRectInsets];
+[UISwitchVisualElement isFixedSize];
```

## Instance methods

```
-[UISwitchVisualElement setOnTintColor:];
-[UISwitchVisualElement _intrinsicContentSizeInvalidatedForChildView:];
-[UISwitchVisualElement setOnImage:];
-[UISwitchVisualElement enabled];
-[UISwitchVisualElement setOn:animated:];
-[UISwitchVisualElement tintColorDidChange];
-[UISwitchVisualElement setTintColor:];
-[UISwitchVisualElement title];
-[UISwitchVisualElement setEnabled:];
-[UISwitchVisualElement setShowsOnOffLabel:];
-[UISwitchVisualElement setOffImage:];
-[UISwitchVisualElement setTitle:];
-[UISwitchVisualElement preferredContentSize];
-[UISwitchVisualElement setThumbTintColor:];
-[UISwitchVisualElement setSwitchControl:];
-[UISwitchVisualElement initWithFrame:];
-[UISwitchVisualElement enabledAlpha];
-[UISwitchVisualElement impactFeedbackGenerator];
-[UISwitchVisualElement setEnabledAlpha:];
-[UISwitchVisualElement setImpactFeedbackGenerator:];
-[UISwitchVisualElement switchControl];
```
