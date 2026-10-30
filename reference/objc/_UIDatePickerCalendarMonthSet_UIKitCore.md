# `_UIDatePickerCalendarMonthSet`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSCalendar" _calendar;
Q _rangeLength;
@"_UIDatePickerCalendarMonth" _referenceMonth;
@"NSMutableIndexSet" _loadedMonthOffsets;
@"NSMutableOrderedSet" _loadedMonths;
```

## Instance methods

```
-[_UIDatePickerCalendarMonthSet _monthAtOffset:];
-[_UIDatePickerCalendarMonthSet _clearLoadedData];
-[_UIDatePickerCalendarMonthSet _ensureReferenceMonthWithFallbackMonth:];
-[_UIDatePickerCalendarMonthSet _loadOffsetRange:];
-[_UIDatePickerCalendarMonthSet _offsetRangeForMonth:];
-[_UIDatePickerCalendarMonthSet _shiftReferenceMonthToFitOffsetMonthsIfNecessary:];
-[_UIDatePickerCalendarMonthSet indexOfMonth:];
-[_UIDatePickerCalendarMonthSet initWithCalendar:rangeLength:];
-[_UIDatePickerCalendarMonthSet insertMonthsAroundMonth:loadedIndexRange:];
-[_UIDatePickerCalendarMonthSet loadedMonths];
-[_UIDatePickerCalendarMonthSet monthAtIndex:];
-[_UIDatePickerCalendarMonthSet reloadWithMonthsAroundMonth:];
```
