# `DBSExternalDisplayMultitaskingOptionView`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _selected;
@"<DBSExternalDisplayMultitaskingOptionViewDelegate>" _delegate;
Q _multitaskingOption;
@"UIImpactFeedbackGenerator" __feedbackGenerator;
@"DBSCheckmarkView" __checkmarkView;
```

## Properties

```
@property (T@"UIImpactFeedbackGenerator",&,N,V__feedbackGenerator) _feedbackGenerator;
@property (T@"DBSCheckmarkView",&,N,V__checkmarkView) _checkmarkView;
@property (T@"<DBSExternalDisplayMultitaskingOptionViewDelegate>",W,N,V_delegate) delegate;
@property (TQ,R,N,V_multitaskingOption) multitaskingOption;
@property (TB,N,GisSelected,V_selected) selected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DBSExternalDisplayMultitaskingOptionView _checkmarkView];
-[DBSExternalDisplayMultitaskingOptionView setSelected:];
-[DBSExternalDisplayMultitaskingOptionView setDelegate:];
-[DBSExternalDisplayMultitaskingOptionView isSelected];
-[DBSExternalDisplayMultitaskingOptionView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[DBSExternalDisplayMultitaskingOptionView delegate];
-[DBSExternalDisplayMultitaskingOptionView _configureView];
-[DBSExternalDisplayMultitaskingOptionView _feedbackGenerator];
-[DBSExternalDisplayMultitaskingOptionView multitaskingOption];
-[DBSExternalDisplayMultitaskingOptionView _imageHeight:];
-[DBSExternalDisplayMultitaskingOptionView _userDidTapOnView:];
-[DBSExternalDisplayMultitaskingOptionView initWithFrame:multitaskingOption:];
-[DBSExternalDisplayMultitaskingOptionView set_checkmarkView:];
-[DBSExternalDisplayMultitaskingOptionView set_feedbackGenerator:];
```
