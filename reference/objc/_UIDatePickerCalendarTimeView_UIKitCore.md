# `_UIDatePickerCalendarTimeView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIDatePickerCompactTimeLabelDelegate`, `UIPopoverPresentationControllerDelegate`
- 15 instance variables, 14 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _showsTimeLabel;
B _followsSystemHourCycle;
@"NSString" _timeLocaleIdentifier;
@"NSArray" _clockLayoutConstraints;
@"_UIDatePickerOverlayPresentation" _presentation;
B _roundsToMinuteInterval;
B _shouldShowTimeLabel;
@"<_UIDatePickerCalendarTimeViewDelegate>" _delegate;
@"NSCalendar" _calendar;
@"NSLocale" _locale;
@"NSString" _customFontDesign;
q _minuteInterval;
@"_UIDatePickerCalendarTime" _selectedTime;
@"UILabel" _timeLabel;
@"_UIDatePickerCompactTimeLabel" _timeTextField;
```

## Properties

```
@property (T@"UILabel",R,N,V_timeLabel) timeLabel;
@property (T@"_UIDatePickerCompactTimeLabel",R,N,V_timeTextField) timeTextField;
@property (T@"<_UIDatePickerCalendarTimeViewDelegate>",W,N,V_delegate) delegate;
@property (T@"NSCalendar",R,N,V_calendar) calendar;
@property (T@"NSLocale",R,N,V_locale) locale;
@property (T@"NSString",C,N,V_customFontDesign) customFontDesign;
@property (Tq,N,V_minuteInterval) minuteInterval;
@property (TB,N,V_roundsToMinuteInterval) roundsToMinuteInterval;
@property (T@"_UIDatePickerCalendarTime",R,N,V_selectedTime) selectedTime;
@property (TB,N,V_shouldShowTimeLabel) shouldShowTimeLabel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDatePickerCalendarTimeView setSelectedDate:];
-[_UIDatePickerCalendarTimeView setMinuteInterval:];
-[_UIDatePickerCalendarTimeView willMoveToSuperview:];
-[_UIDatePickerCalendarTimeView _reload];
-[_UIDatePickerCalendarTimeView roundsToMinuteInterval];
-[_UIDatePickerCalendarTimeView calendar];
-[_UIDatePickerCalendarTimeView setDelegate:];
-[_UIDatePickerCalendarTimeView tintColorDidChange];
-[_UIDatePickerCalendarTimeView customFontDesign];
-[_UIDatePickerCalendarTimeView willMoveToWindow:];
-[_UIDatePickerCalendarTimeView locale];
-[_UIDatePickerCalendarTimeView minuteInterval];
-[_UIDatePickerCalendarTimeView delegate];
-[_UIDatePickerCalendarTimeView pointInside:withEvent:];
-[_UIDatePickerCalendarTimeView initWithFrame:];
-[_UIDatePickerCalendarTimeView setCustomFontDesign:];
-[_UIDatePickerCalendarTimeView primaryFirstResponder];
-[_UIDatePickerCalendarTimeView setRoundsToMinuteInterval:];
-[_UIDatePickerCalendarTimeView compactTimeLabel:didSelectTime:];
-[_UIDatePickerCalendarTimeView _reloadDateFormatters];
-[_UIDatePickerCalendarTimeView _setupViewHierarchy];
-[_UIDatePickerCalendarTimeView _updateClockLayout];
-[_UIDatePickerCalendarTimeView _updateFonts];
-[_UIDatePickerCalendarTimeView _updateTextFieldsFromSelectedDateComponents];
-[_UIDatePickerCalendarTimeView _updateTimeLabelTitleIfNeeded];
-[_UIDatePickerCalendarTimeView compactTimeLabel:shouldDismissForInteractionAtLocation:];
-[_UIDatePickerCalendarTimeView compactTimeLabelDidBeginEditing:];
-[_UIDatePickerCalendarTimeView compactTimeLabelDidEndEditing:];
-[_UIDatePickerCalendarTimeView compactTimeLabelWillBecomeFirstResponder:];
-[_UIDatePickerCalendarTimeView createDatePickerForCompactTimeLabel:];
-[_UIDatePickerCalendarTimeView reloadWithCalendar:locale:selectedDate:];
-[_UIDatePickerCalendarTimeView reloadWithCalendar:locale:selectedDate:followsSystemHourCycle:];
-[_UIDatePickerCalendarTimeView selectedTime];
-[_UIDatePickerCalendarTimeView setShouldShowTimeLabel:];
-[_UIDatePickerCalendarTimeView shouldShowTimeLabel];
-[_UIDatePickerCalendarTimeView timeLabel];
-[_UIDatePickerCalendarTimeView timeTextField];
```
