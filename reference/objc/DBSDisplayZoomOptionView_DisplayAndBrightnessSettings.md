# `DBSDisplayZoomOptionView`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`
- 8 instance variables, 12 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _selected;
B _highlight;
Q _displayZoomOption;
@"<DBSDisplayZoomOptionViewDelegate>" _delegate;
@"UILabel" _optionNameLabel;
@"DBSCheckmarkView" __checkmarkView;
@"DBSDeviceDisplayZoomAnimationView" __packageView;
@"UIImpactFeedbackGenerator" __feedbackGenerator;
```

## Properties

```
@property (T@"UILabel",&,N,V_optionNameLabel) optionNameLabel;
@property (T@"DBSCheckmarkView",&,N,V__checkmarkView) _checkmarkView;
@property (T@"DBSDeviceDisplayZoomAnimationView",&,N,V__packageView) _packageView;
@property (T@"UIImpactFeedbackGenerator",&,N,V__feedbackGenerator) _feedbackGenerator;
@property (TB,N,Ghighlighted,V_highlight) highlight;
@property (TQ,R,N,V_displayZoomOption) displayZoomOption;
@property (T@"<DBSDisplayZoomOptionViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisSelected,V_selected) selected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DBSDisplayZoomOptionView startAnimation];
-[DBSDisplayZoomOptionView _checkmarkView];
-[DBSDisplayZoomOptionView setSelected:];
-[DBSDisplayZoomOptionView highlighted];
-[DBSDisplayZoomOptionView setDelegate:];
-[DBSDisplayZoomOptionView setHighlight:];
-[DBSDisplayZoomOptionView isSelected];
-[DBSDisplayZoomOptionView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[DBSDisplayZoomOptionView delegate];
-[DBSDisplayZoomOptionView _configureView];
-[DBSDisplayZoomOptionView _feedbackGenerator];
-[DBSDisplayZoomOptionView stopAnimation];
-[DBSDisplayZoomOptionView displayZoomOption];
-[DBSDisplayZoomOptionView optionNameLabel];
-[DBSDisplayZoomOptionView _packageView];
-[DBSDisplayZoomOptionView _userDidTapOnView:];
-[DBSDisplayZoomOptionView initWithFrame:displayZoomOption:];
-[DBSDisplayZoomOptionView setOptionNameLabel:];
-[DBSDisplayZoomOptionView set_checkmarkView:];
-[DBSDisplayZoomOptionView set_feedbackGenerator:];
-[DBSDisplayZoomOptionView set_packageView:];
```
