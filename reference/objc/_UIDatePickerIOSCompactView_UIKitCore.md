# `_UIDatePickerIOSCompactView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UIDatePickerCompactTimeLabelDelegate`, `_UIDatePickerCompactDateLabelDelegate`, `_UIDatePickerOverlayPresentationDelegate`, `UIGestureRecognizerDelegate`, `_UIDatePickerViewComponent`
- 15 instance variables, 14 properties, 58 instance methods, 0 class methods

## Instance variables

```
{?="isEnabled"b1"implementsCustomDidSelectComponent"b1} _flags;
@"NSDateFormatter" _dateFormatterMedium;
@"NSDateFormatter" _dateFormatterShort;
@"UILayoutGuide" _timeViewLayoutGuide;
@"UILayoutGuide" _contentLayoutGuide;
@"NSDateFormatter" _layoutFormatter;
B _dateOnLeadingSide;
@"NSArray" _dateTimeConstraints;
@"_UIDatePickerOverlayPresentation" _presentation;
q _activeComponent;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UIDatePicker" _datePicker;
@"_UIDatePickerDataModel" _data;
@"_UIDatePickerCompactDateLabel" _dateView;
@"_UIDatePickerCompactTimeLabel" _timeView;
```

## Properties

```
@property (T@"_UIDatePickerCompactDateLabel",R,N,V_dateView) dateView;
@property (T@"_UIDatePickerCompactTimeLabel",R,N,V_timeView) timeView;
@property (TB,R,N) alignConstraintsToLayoutGuide;
@property (T@"NSDictionary",&,N) overrideAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIDatePicker",W,N,V_datePicker) datePicker;
@property (T@"_UIDatePickerDataModel",&,N,V_data) data;
@property (Tq,R,N) datePickerStyle;
@property (T{UIEdgeInsets=dddd},R,N) appliedInsetsToEdgeOfContent;
@property (Td,?,N) timeInterval;
@property (Td,?,R,N) contentWidth;
```

## Instance methods

```
-[_UIDatePickerIOSCompactView dateView];
-[_UIDatePickerIOSCompactView appliedInsetsToEdgeOfContent];
-[_UIDatePickerIOSCompactView didChangeLocale];
-[_UIDatePickerIOSCompactView timeView];
-[_UIDatePickerIOSCompactView didChangeDateFrom:animated:];
-[_UIDatePickerIOSCompactView willMoveToSuperview:];
-[_UIDatePickerIOSCompactView _setEnabled:];
-[_UIDatePickerIOSCompactView setDatePicker:];
-[_UIDatePickerIOSCompactView datePickerStyle];
-[_UIDatePickerIOSCompactView data];
-[_UIDatePickerIOSCompactView didChangeMinimumDate];
-[_UIDatePickerIOSCompactView didChangeMinuteInterval];
-[_UIDatePickerIOSCompactView didChangeRoundsToMinuteInterval];
-[_UIDatePickerIOSCompactView didChangeTimeZone];
-[_UIDatePickerIOSCompactView tintColorDidChange];
-[_UIDatePickerIOSCompactView gestureRecognizerShouldBegin:];
-[_UIDatePickerIOSCompactView willMoveToWindow:];
-[_UIDatePickerIOSCompactView didChangeCalendar];
-[_UIDatePickerIOSCompactView setData:];
-[_UIDatePickerIOSCompactView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIDatePickerIOSCompactView hasDefaultSize];
-[_UIDatePickerIOSCompactView displaySelectedDateAnimated:];
-[_UIDatePickerIOSCompactView updateConstraints];
-[_UIDatePickerIOSCompactView didChangeToday];
-[_UIDatePickerIOSCompactView _updateUI];
-[_UIDatePickerIOSCompactView didChangeMaximumDate];
-[_UIDatePickerIOSCompactView setContentHorizontalAlignment:];
-[_UIDatePickerIOSCompactView initWithFrame:];
-[_UIDatePickerIOSCompactView datePicker];
-[_UIDatePickerIOSCompactView didChangeMode];
-[_UIDatePickerIOSCompactView _contentHuggingDefault_isUsuallyFixedWidth];
-[_UIDatePickerIOSCompactView didReset];
-[_UIDatePickerIOSCompactView compactTimeLabel:didSelectTime:];
-[_UIDatePickerIOSCompactView _resignActiveComponentAnimated:];
-[_UIDatePickerIOSCompactView _contentSizeCategoryDidChange:previousTraits:];
-[_UIDatePickerIOSCompactView _datePickerPresentation:didChangeActiveMode:];
-[_UIDatePickerIOSCompactView _didReceivePanGestureRecognizer:];
-[_UIDatePickerIOSCompactView _reloadTimeViewTimeFormat];
-[_UIDatePickerIOSCompactView _sizeThatFits:];
-[_UIDatePickerIOSCompactView _updateDateBeforeTimeValue];
-[_UIDatePickerIOSCompactView _updateDateViewTextAlignment];
-[_UIDatePickerIOSCompactView _updateEnabledStyling];
-[_UIDatePickerIOSCompactView alignConstraintsToLayoutGuide];
-[_UIDatePickerIOSCompactView compactDateLabelDidBeginEditing:];
-[_UIDatePickerIOSCompactView compactDateLabelDidEndEditing:];
-[_UIDatePickerIOSCompactView compactTimeLabel:shouldDismissForInteractionAtLocation:];
-[_UIDatePickerIOSCompactView compactTimeLabelDidBeginEditing:];
-[_UIDatePickerIOSCompactView compactTimeLabelDidEndEditing:];
-[_UIDatePickerIOSCompactView compactTimeLabelWillBecomeFirstResponder:];
-[_UIDatePickerIOSCompactView createDatePickerForCompactDateLabel:];
-[_UIDatePickerIOSCompactView createDatePickerForCompactTimeLabel:];
-[_UIDatePickerIOSCompactView defaultSize];
-[_UIDatePickerIOSCompactView didChangeCompactStyleDelegate];
-[_UIDatePickerIOSCompactView overrideAttributes];
-[_UIDatePickerIOSCompactView setActiveComponent:];
-[_UIDatePickerIOSCompactView setOverrideAttributes:];
-[_UIDatePickerIOSCompactView updateTimeZoneDisplay];
-[_UIDatePickerIOSCompactView usesAutoLayout];
```
