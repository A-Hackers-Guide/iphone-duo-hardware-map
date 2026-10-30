# `_UIDatePickerMode_Date`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDatePickerMode`
- 6 instance variables, 0 properties, 13 instance methods, 2 class methods

## Instance variables

```
d _dateYearWidth;
d _dateMonthWidth;
d _dateDayWidth;
@"NSString" _yearFormat;
@"NSString" _monthFormat;
@"NSString" _dayFormat;
```

## Class methods

```
+[_UIDatePickerMode_Date datePickerMode];
+[_UIDatePickerMode_Date extractableCalendarUnits];
```

## Instance methods

```
-[_UIDatePickerMode_Date nextUnitLargerThanUnit:];
-[_UIDatePickerMode_Date dateFormatForCalendarUnit:];
-[_UIDatePickerMode_Date widthForCalendarUnit:font:maxWidth:];
-[_UIDatePickerMode_Date rowForDate:dateComponents:component:currentRow:];
-[_UIDatePickerMode_Date _shouldReset:];
-[_UIDatePickerMode_Date nextUnitSmallerThanUnit:];
-[_UIDatePickerMode_Date localizedFormatString];
-[_UIDatePickerMode_Date _shouldEnableValueForRow:inComponent:calendarUnit:];
-[_UIDatePickerMode_Date numberOfRowsForCalendarUnit:];
-[_UIDatePickerMode_Date noteCalendarChanged];
-[_UIDatePickerMode_Date resetComponentWidths];
-[_UIDatePickerMode_Date displayedCalendarUnits];
-[_UIDatePickerMode_Date _dateForYearRow:];
```
