# `SBPIPStashView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PTSettingsKeyObserver`
- 12 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
d _startBlurThreshold;
d _completeBlurThreshold;
@"SBPIPStashVisualSettings" _settings;
@"SBPIPBackdropView" _backdropView;
@"UIView" _lightTintView;
@"UIView" _darkTintView;
@"UIImageView" _leftChevron;
@"UIImageView" _rightChevron;
B _chevronsHidden;
B _isChevronShownLeft;
d _blurProgress;
d _stashedTabWidth;
```

## Properties

```
@property (Td,N,V_blurProgress) blurProgress;
@property (Td,N,V_stashedTabWidth) stashedTabWidth;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPStashView initWithFrame:settings:];
-[SBPIPStashView dealloc];
-[SBPIPStashView layoutSubviews];
-[SBPIPStashView settings:changedValueForKey:];
-[SBPIPStashView blurProgress];
-[SBPIPStashView _setContinuousCornerRadius:];
-[SBPIPStashView traitCollectionDidChange:];
-[SBPIPStashView initWithFrame:];
-[SBPIPStashView stashedTabWidth];
-[SBPIPStashView layoutStashChevrons];
-[SBPIPStashView resetChevronState];
-[SBPIPStashView setBlurProgress:];
-[SBPIPStashView setChevronHidden:left:];
-[SBPIPStashView setStashedTabWidth:];
-[SBPIPStashView _updateSettingsDerivedValues];
```
