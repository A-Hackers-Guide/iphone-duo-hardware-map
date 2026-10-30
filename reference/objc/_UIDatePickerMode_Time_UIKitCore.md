# `_UIDatePickerMode_Time`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDatePickerMode`
- 6 instance variables, 0 properties, 13 instance methods, 2 class methods

## Instance variables

```
d _timeHourWidth;
d _timeMinuteWidth;
d _timeAMPMWidth;
@"NSString" _hourFormat;
@"NSString" _minuteFormat;
@"NSString" _dayPeriodFormat;
```

## Class methods

```
+[_UIDatePickerMode_Time datePickerMode];
+[_UIDatePickerMode_Time extractableCalendarUnits];
```

## Instance methods

```
-[_UIDatePickerMode_Time nextUnitLargerThanUnit:];
-[_UIDatePickerMode_Time dateFormatForCalendarUnit:];
-[_UIDatePickerMode_Time widthForCalendarUnit:font:maxWidth:];
-[_UIDatePickerMode_Time _shouldReset:];
-[_UIDatePickerMode_Time nextUnitSmallerThanUnit:];
-[_UIDatePickerMode_Time localizedFormatString];
-[_UIDatePickerMode_Time rowHeight];
-[_UIDatePickerMode_Time _shouldEnableValueForRow:inComponent:calendarUnit:];
-[_UIDatePickerMode_Time numberOfRowsForCalendarUnit:];
-[_UIDatePickerMode_Time noteCalendarChanged];
-[_UIDatePickerMode_Time font];
-[_UIDatePickerMode_Time resetComponentWidths];
-[_UIDatePickerMode_Time displayedCalendarUnits];
```
