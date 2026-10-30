# `_UISliderFluidConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISliderConfiguration`
- 10 instance variables, 16 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _disableAllSliderVisuals;
B _disableSliderRubberbandTransform;
@"<_UISliderFluidInteractionDelegate>" _delegate;
d _expansionFactor;
d _horizontalExpansionFactor;
d _stretchLimit;
@"UIView" _minimumValueView;
@"UIView" _maximumValueView;
@"UIVisualEffect" _minimumTrackEffect;
@"UIVisualEffect" _maximumTrackEffect;
```

## Properties

```
@property (T@"<_UISliderFluidInteractionDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_expansionFactor) expansionFactor;
@property (Td,N,V_horizontalExpansionFactor) horizontalExpansionFactor;
@property (Td,N,V_stretchLimit) stretchLimit;
@property (T@"UIView",&,N,V_minimumValueView) minimumValueView;
@property (T@"UIView",&,N,V_maximumValueView) maximumValueView;
@property (T@"UIVisualEffect",&,N,V_minimumTrackEffect) minimumTrackEffect;
@property (T@"UIVisualEffect",&,N,V_maximumTrackEffect) maximumTrackEffect;
@property (TB,N,V_disableAllSliderVisuals) disableAllSliderVisuals;
@property (TB,N,V_disableSliderRubberbandTransform) disableSliderRubberbandTransform;
@property (T@"UIBlurEffect",&,N,S_setMinimumTrackBlurEffect:) minimumTrackBlurEffect;
@property (T@"UIBlurEffect",&,N,S_setMaximumTrackBlurEffect:) maximumTrackBlurEffect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISliderFluidConfiguration stretchLimit];
-[_UISliderFluidConfiguration minimumTrackBlurEffect];
-[_UISliderFluidConfiguration setMaximumTrackEffect:];
-[_UISliderFluidConfiguration setExpansionFactor:];
-[_UISliderFluidConfiguration _setMaximumTrackBlurEffect:];
-[_UISliderFluidConfiguration setMinimumValueView:];
-[_UISliderFluidConfiguration init];
-[_UISliderFluidConfiguration disableSliderRubberbandTransform];
-[_UISliderFluidConfiguration setDisableSliderRubberbandTransform:];
-[_UISliderFluidConfiguration setStretchLimit:];
-[_UISliderFluidConfiguration _setMinimumTrackBlurEffect:];
-[_UISliderFluidConfiguration minimumTrackEffect];
-[_UISliderFluidConfiguration minimumValueView];
-[_UISliderFluidConfiguration setDelegate:];
-[_UISliderFluidConfiguration disableAllSliderVisuals];
-[_UISliderFluidConfiguration maximumTrackBlurEffect];
-[_UISliderFluidConfiguration setHorizontalExpansionFactor:];
-[_UISliderFluidConfiguration delegate];
-[_UISliderFluidConfiguration setMaximumValueView:];
-[_UISliderFluidConfiguration copyWithZone:];
-[_UISliderFluidConfiguration setDisableAllSliderVisuals:];
-[_UISliderFluidConfiguration isEqual:];
-[_UISliderFluidConfiguration expansionFactor];
-[_UISliderFluidConfiguration maximumTrackEffect];
-[_UISliderFluidConfiguration setMinimumTrackEffect:];
-[_UISliderFluidConfiguration horizontalExpansionFactor];
-[_UISliderFluidConfiguration maximumValueView];
```
