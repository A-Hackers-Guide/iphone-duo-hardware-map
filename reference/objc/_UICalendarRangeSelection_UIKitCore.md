# `_UICalendarRangeSelection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICalendarSelection`
- 4 instance variables, 2 properties, 18 instance methods, 0 class methods

## Instance variables

```
{?="canSelectDate"b1"didBeginSelection"b1"didEndSelection"b1"didSelectRange"b1} _delegateImplements;
@"NSDateComponents" _pendingStartDate;
@"_UICalendarDateRange" _dateRange;
@"<_UICalendarRangeSelectionDelegate>" _delegate;
```

## Properties

```
@property (T@"_UICalendarDateRange",C,N,V_dateRange) dateRange;
@property (T@"<_UICalendarRangeSelectionDelegate>",R,W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UICalendarRangeSelection initWithDelegate:];
-[_UICalendarRangeSelection init];
-[_UICalendarRangeSelection delegate];
-[_UICalendarRangeSelection dateRange];
-[_UICalendarRangeSelection _deselectDatesInRange:animated:];
-[_UICalendarRangeSelection _sanitizedDateRange:calendar:];
-[_UICalendarRangeSelection canSelectDate:];
-[_UICalendarRangeSelection didChangeAvailableDateRange:];
-[_UICalendarRangeSelection didChangeCalendar:];
-[_UICalendarRangeSelection didChangeVisibleMonth:];
-[_UICalendarRangeSelection didDeselectDate:];
-[_UICalendarRangeSelection didMoveToCalendarView];
-[_UICalendarRangeSelection didSelectDate:];
-[_UICalendarRangeSelection selectAllDatesAnimated:];
-[_UICalendarRangeSelection setDateRange:];
-[_UICalendarRangeSelection setDateRange:animated:];
-[_UICalendarRangeSelection shouldDeselectDate:];
-[_UICalendarRangeSelection willMoveToCalendarView:];
```
