# `_UIDatePickerDateRange`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="ignoresRange"b1} _flags;
@"NSDate" _startDate;
@"NSDate" _endDate;
```

## Properties

```
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (T@"NSDate",R,N,V_endDate) endDate;
```

## Instance methods

```
-[_UIDatePickerDateRange startDate];
-[_UIDatePickerDateRange init];
-[_UIDatePickerDateRange endDate];
-[_UIDatePickerDateRange initWithStartDate:endDate:];
-[_UIDatePickerDateRange containsDate:];
-[_UIDatePickerDateRange _containsDate:withAccuracy:inCalendar:];
-[_UIDatePickerDateRange containsDay:];
-[_UIDatePickerDateRange containsMonth:];
-[_UIDatePickerDateRange copyWithEndDate:];
-[_UIDatePickerDateRange copyWithStartDate:];
-[_UIDatePickerDateRange dateInRangeForDate:];
```
