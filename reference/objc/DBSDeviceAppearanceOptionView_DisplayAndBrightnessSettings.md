# `DBSDeviceAppearanceOptionView`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`
- 9 instance variables, 13 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _highlight;
@"<DBSDeviceAppearanceOptionViewDelegate>" _delegate;
Q _appearanceOption;
@"UIStackView" __stackView;
@"UIImageView" __previewImageView;
@"UILabel" __timeLabel;
@"UILabel" __label;
@"DBSCheckmarkView" __checkmarkView;
@"UIImpactFeedbackGenerator" __feedbackGenerator;
```

## Properties

```
@property (T@"UIStackView",&,N,V__stackView) _stackView;
@property (T@"UIImageView",&,N,V__previewImageView) _previewImageView;
@property (T@"UILabel",&,N,V__timeLabel) _timeLabel;
@property (T@"UILabel",&,N,V__label) _label;
@property (T@"DBSCheckmarkView",&,N,V__checkmarkView) _checkmarkView;
@property (T@"UIImpactFeedbackGenerator",&,N,V__feedbackGenerator) _feedbackGenerator;
@property (TB,N,Ghighlighted,V_highlight) highlight;
@property (T@"<DBSDeviceAppearanceOptionViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R,N,V_appearanceOption) appearanceOption;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DBSDeviceAppearanceOptionView _label];
-[DBSDeviceAppearanceOptionView _checkmarkView];
-[DBSDeviceAppearanceOptionView _timeLabel];
-[DBSDeviceAppearanceOptionView highlighted];
-[DBSDeviceAppearanceOptionView setDelegate:];
-[DBSDeviceAppearanceOptionView setHighlight:];
-[DBSDeviceAppearanceOptionView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[DBSDeviceAppearanceOptionView delegate];
-[DBSDeviceAppearanceOptionView _stackView];
-[DBSDeviceAppearanceOptionView traitCollectionDidChange:];
-[DBSDeviceAppearanceOptionView _configureView];
-[DBSDeviceAppearanceOptionView _feedbackGenerator];
-[DBSDeviceAppearanceOptionView initWithFrame:appearanceOption:];
-[DBSDeviceAppearanceOptionView _previewImageView];
-[DBSDeviceAppearanceOptionView _updateViewForCurrentInterfaceStyle:];
-[DBSDeviceAppearanceOptionView _userDidTapOnView:];
-[DBSDeviceAppearanceOptionView appearanceOption];
-[DBSDeviceAppearanceOptionView set_checkmarkView:];
-[DBSDeviceAppearanceOptionView set_feedbackGenerator:];
-[DBSDeviceAppearanceOptionView set_label:];
-[DBSDeviceAppearanceOptionView set_previewImageView:];
-[DBSDeviceAppearanceOptionView set_stackView:];
-[DBSDeviceAppearanceOptionView set_timeLabel:];
```
