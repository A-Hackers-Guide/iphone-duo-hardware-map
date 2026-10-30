# `SBScreenBrightnessDebugHUDView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBScreenBrightnessObserving`, `BSInvalidatable`
- 6 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBScreenBrightnessParticipant" _participant;
@"SBWindowScene" _windowScene;
@"UILabel" _rawValueLabel;
@"UILabel" _sanitizedValueLabel;
@"UILabel" _windowSceneValueLabel;
@"UIStackView" _stackView;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBScreenBrightnessDebugHUDView _invalidateLayout];
-[SBScreenBrightnessDebugHUDView dealloc];
-[SBScreenBrightnessDebugHUDView invalidate];
-[SBScreenBrightnessDebugHUDView sizeThatFits:];
-[SBScreenBrightnessDebugHUDView initWithCoordinator:];
-[SBScreenBrightnessDebugHUDView _clearNumberLabel:];
-[SBScreenBrightnessDebugHUDView _numberLabel];
-[SBScreenBrightnessDebugHUDView _titleLabelWithString:];
-[SBScreenBrightnessDebugHUDView _updateNumberLabel:withDoubleValue:];
-[SBScreenBrightnessDebugHUDView _windowSceneBrightnessDidUpdate:];
-[SBScreenBrightnessDebugHUDView brightnessDidChange:];
-[SBScreenBrightnessDebugHUDView sanitizedBrightnessDidChange:];
-[SBScreenBrightnessDebugHUDView updateWindowScene:];
```
