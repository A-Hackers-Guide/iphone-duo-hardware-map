# `_UIDatePickerMode_DateAndTime`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDatePickerMode`
- 13 instance variables, 0 properties, 28 instance methods, 2 class methods

## Instance variables

```
B _weekdayLast;
d _wmdWeekMonthDayWidth;
d _wmdHourWidth;
d _wmdMinuteWidth;
d _wmdAMPMWidth;
d _wmdWeekdayWidth;
@"NSString" _weekdayFormat;
@"NSString" _monthDayFormat;
@"NSString" _hourFormat;
@"NSString" _minuteFormat;
@"NSString" _dayPeriodFormat;
@"NSDateFormatter" _relativeFormatter;
@"NSDateFormatter" _weekdayFormatter;
```

## Class methods

```
+[_UIDatePickerMode_DateAndTime datePickerMode];
+[_UIDatePickerMode_DateAndTime extractableCalendarUnits];
```

## Instance methods

```
-[_UIDatePickerMode_DateAndTime nextUnitLargerThanUnit:];
-[_UIDatePickerMode_DateAndTime elements];
-[_UIDatePickerMode_DateAndTime viewForRow:inComponent:reusingView:];
-[_UIDatePickerMode_DateAndTime dateFormatForCalendarUnit:];
-[_UIDatePickerMode_DateAndTime widthForCalendarUnit:font:maxWidth:];
-[_UIDatePickerMode_DateAndTime _shouldEnableWeekMonthDayForRow:];
-[_UIDatePickerMode_DateAndTime weekdayFormatter];
-[_UIDatePickerMode_DateAndTime componentWidthForDateTimeCalendarUnit:font:maxWidth:];
-[_UIDatePickerMode_DateAndTime _takeBaseDateComponentsFromDate:];
-[_UIDatePickerMode_DateAndTime _dateForWeekMonthDayRow:];
-[_UIDatePickerMode_DateAndTime rowForDate:dateComponents:component:currentRow:];
-[_UIDatePickerMode_DateAndTime loadDate:animated:];
-[_UIDatePickerMode_DateAndTime _shouldReset:];
-[_UIDatePickerMode_DateAndTime nextUnitSmallerThanUnit:];
-[_UIDatePickerMode_DateAndTime _resetBaseDateComponentsIfNecessaryFromDate:];
-[_UIDatePickerMode_DateAndTime baseDateComponents];
-[_UIDatePickerMode_DateAndTime localizedFormatString];
-[_UIDatePickerMode_DateAndTime relativeFormatter];
-[_UIDatePickerMode_DateAndTime _shouldEnableValueForRow:inComponent:calendarUnit:];
-[_UIDatePickerMode_DateAndTime numberOfRowsForCalendarUnit:];
-[_UIDatePickerMode_DateAndTime titleForRow:inComponent:];
-[_UIDatePickerMode_DateAndTime noteCalendarChanged];
-[_UIDatePickerMode_DateAndTime weekdayWidth];
-[_UIDatePickerMode_DateAndTime dateForRow:inCalendarUnit:];
-[_UIDatePickerMode_DateAndTime isWeekdayLast];
-[_UIDatePickerMode_DateAndTime updateEnabledStateOfViewForRow:inComponent:];
-[_UIDatePickerMode_DateAndTime resetComponentWidths];
-[_UIDatePickerMode_DateAndTime displayedCalendarUnits];
```
