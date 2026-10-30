# `_UIDatePickerWheelsTimeLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDatePickerCalendarTimeLabel`
- Protocols: `_UIControlEventsGestureRecognizerDelegate`
- 13 instance variables, 8 properties, 30 instance methods, 1 class methods

## Instance variables

```
@"UILabel" _measurementLabel;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hoursReferenceFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _minutesReferenceFrame;
q _highlightedScope;
B _highlightedForTouch;
@"UIView" _touchHighlightedView;
B _wheelsActive;
@"_UIControlEventsGestureRecognizer" _controlEventsGestureRecognizer;
@"<_UIDatePickerWheelsTimeLabelDelegate>" _wheelsDelegate;
@"UIView" _contentView;
@"UILabel" _hourLabel;
@"UILabel" _minuteLabel;
@"UILabel" _timeSeparatorLabel;
```

## Properties

```
@property (T@"UIView",R,N,V_contentView) contentView;
@property (T@"UILabel",R,N,V_hourLabel) hourLabel;
@property (T@"UILabel",R,N,V_minuteLabel) minuteLabel;
@property (T@"UILabel",R,N,V_timeSeparatorLabel) timeSeparatorLabel;
@property (T@"_UIControlEventsGestureRecognizer",R,N,V_controlEventsGestureRecognizer) controlEventsGestureRecognizer;
@property (T@"<_UIDatePickerWheelsTimeLabelDelegate>",W,N,V_wheelsDelegate) wheelsDelegate;
@property (TB,N,V_wheelsActive) wheelsActive;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) combinedTextRectFromLabels;
```

## Class methods

```
+[_UIDatePickerWheelsTimeLabel supportsScribbleInteraction];
```

## Instance methods

```
-[_UIDatePickerWheelsTimeLabel hourRect];
-[_UIDatePickerWheelsTimeLabel wheelsActive];
-[_UIDatePickerWheelsTimeLabel _viewForHighlightedTouchAtPoint:];
-[_UIDatePickerWheelsTimeLabel setWheelsActive:];
-[_UIDatePickerWheelsTimeLabel timeSeparatorLabel];
-[_UIDatePickerWheelsTimeLabel stateMachineUpdateFromState:toState:];
-[_UIDatePickerWheelsTimeLabel controlEventsGestureRecognizer];
-[_UIDatePickerWheelsTimeLabel updateMinutesFromDatePicker:wheelsChanged:];
-[_UIDatePickerWheelsTimeLabel setHighlightedForTouch:];
-[_UIDatePickerWheelsTimeLabel initWithTimeFormat:minuteInterval:];
-[_UIDatePickerWheelsTimeLabel endEditingWheels];
-[_UIDatePickerWheelsTimeLabel displaysTimeOfDayLabel];
-[_UIDatePickerWheelsTimeLabel decrementBehaviour];
-[_UIDatePickerWheelsTimeLabel _treatMinutesAsHoursForState:];
-[_UIDatePickerWheelsTimeLabel contentView];
-[_UIDatePickerWheelsTimeLabel setWheelsDelegate:];
-[_UIDatePickerWheelsTimeLabel configureLabelsForHour:minute:];
-[_UIDatePickerWheelsTimeLabel wheelsDelegate];
-[_UIDatePickerWheelsTimeLabel minuteRect];
-[_UIDatePickerWheelsTimeLabel hourLabel];
-[_UIDatePickerWheelsTimeLabel beginEditingWheels];
-[_UIDatePickerWheelsTimeLabel willBeginWritingInScribbleInteraction];
-[_UIDatePickerWheelsTimeLabel font];
-[_UIDatePickerWheelsTimeLabel pushCurrentStateIntoUI];
-[_UIDatePickerWheelsTimeLabel minuteLabel];
-[_UIDatePickerWheelsTimeLabel setContentHidden:];
-[_UIDatePickerWheelsTimeLabel combinedTextRectFromLabels];
-[_UIDatePickerWheelsTimeLabel controlEventsGestureRecognizer:recognizedControlEvent:withEvent:];
-[_UIDatePickerWheelsTimeLabel updateHoursFromDatePicker:wheelsChanged:];
-[_UIDatePickerWheelsTimeLabel setFont:];
```
