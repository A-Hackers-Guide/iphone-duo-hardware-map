# `_UIDatePickerCalendarView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICalendarSelectionSingleDateDelegate`, `_UIDatePickerCalendarTimeViewDelegate`, `_UIDatePickerViewComponent`
- 10 instance variables, 10 properties, 63 instance methods, 0 class methods

## Instance variables

```
{?="needsUpdateDate"b1"animateUpdateDate"b1"isEnabled"b1} _flags;
@"_UIDatePickerStyle" _visualStyle;
@"UICalendarView" _calendarView;
@"UICalendarSelectionSingleDate" _selection;
@"_UIDatePickerCalendarTimeView" _timeView;
@"UIView" _calendarTimeSeparatorView;
{CGSize="width"d"height"d} _lastSize;
Q _stateUpdatesInFlight;
@"UIDatePicker" _datePicker;
@"_UIDatePickerDataModel" _data;
```

## Properties

```
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
-[_UIDatePickerCalendarView appliedInsetsToEdgeOfContent];
-[_UIDatePickerCalendarView didChangeLocale];
-[_UIDatePickerCalendarView didChangeDateFrom:animated:];
-[_UIDatePickerCalendarView _setEnabled:];
-[_UIDatePickerCalendarView setDatePicker:];
-[_UIDatePickerCalendarView _intrinsicSizeWithinSize:];
-[_UIDatePickerCalendarView _reload];
-[_UIDatePickerCalendarView datePickerStyle];
-[_UIDatePickerCalendarView data];
-[_UIDatePickerCalendarView didChangeMinimumDate];
-[_UIDatePickerCalendarView didChangeMinuteInterval];
-[_UIDatePickerCalendarView layoutSubviews];
-[_UIDatePickerCalendarView layoutMarginsDidChange];
-[_UIDatePickerCalendarView setBounds:];
-[_UIDatePickerCalendarView didChangeRoundsToMinuteInterval];
-[_UIDatePickerCalendarView didChangeTimeZone];
-[_UIDatePickerCalendarView sizeThatFits:];
-[_UIDatePickerCalendarView didChangeCalendar];
-[_UIDatePickerCalendarView setData:];
-[_UIDatePickerCalendarView setFrame:];
-[_UIDatePickerCalendarView hasDefaultSize];
-[_UIDatePickerCalendarView displaySelectedDateAnimated:];
-[_UIDatePickerCalendarView didChangeToday];
-[_UIDatePickerCalendarView didChangeMaximumDate];
-[_UIDatePickerCalendarView initWithFrame:];
-[_UIDatePickerCalendarView primaryFirstResponder];
-[_UIDatePickerCalendarView datePicker];
-[_UIDatePickerCalendarView didChangeMode];
-[_UIDatePickerCalendarView didReset];
-[_UIDatePickerCalendarView _reloadTimeView];
-[_UIDatePickerCalendarView _axesForDerivingIntrinsicContentSizeFromLayoutSize];
-[_UIDatePickerCalendarView _reloadCalendarView];
-[_UIDatePickerCalendarView _reloadDateRange];
-[_UIDatePickerCalendarView _setNeedsUpdateDateAnimated:];
-[_UIDatePickerCalendarView _shouldDisplayCalendarTimeSeparator];
-[_UIDatePickerCalendarView _shouldDisplayCalendarView];
-[_UIDatePickerCalendarView _shouldDisplayTimeView];
-[_UIDatePickerCalendarView _shouldUpdateDataForComponents:date:];
-[_UIDatePickerCalendarView _shouldUpdateTimeViewForSelectedTime:];
-[_UIDatePickerCalendarView _sizeThatFits:];
-[_UIDatePickerCalendarView _updateContentSizeLimitations];
-[_UIDatePickerCalendarView _updateCustomFonts];
-[_UIDatePickerCalendarView _updateDataForComponents:];
-[_UIDatePickerCalendarView _updateDate];
-[_UIDatePickerCalendarView _updateDateIfNeeded];
-[_UIDatePickerCalendarView _updateEnabledStyling];
-[_UIDatePickerCalendarView _updateLayoutMargins];
-[_UIDatePickerCalendarView _updateModuleVisibility];
-[_UIDatePickerCalendarView _updateSelectedDay:animated:notify:];
-[_UIDatePickerCalendarView _updateSelectedDay:time:animated:notify:];
-[_UIDatePickerCalendarView _updateSelectedTime:notify:];
-[_UIDatePickerCalendarView _updateTimeViewForSelectedDate:animated:];
-[_UIDatePickerCalendarView _workaround66574039_datePickerDidUpdateLayoutMargins];
-[_UIDatePickerCalendarView createDatePickerForTimeView:];
-[_UIDatePickerCalendarView dateSelection:canSelectDate:];
-[_UIDatePickerCalendarView dateSelection:didSelectDate:];
-[_UIDatePickerCalendarView defaultSize];
-[_UIDatePickerCalendarView didChangeCustomFontDesign];
-[_UIDatePickerCalendarView timeView:didSelectTime:];
-[_UIDatePickerCalendarView timeViewDidBeginEditing:];
-[_UIDatePickerCalendarView timeViewDidEndEditing:];
-[_UIDatePickerCalendarView timeViewWillBecomeFirstResponder:];
-[_UIDatePickerCalendarView usesAutoLayout];
```
