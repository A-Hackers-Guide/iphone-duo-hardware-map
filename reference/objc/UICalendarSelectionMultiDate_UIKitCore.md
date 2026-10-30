# `UICalendarSelectionMultiDate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICalendarSelection`
- 3 instance variables, 2 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _selectedDates;
{?="canSelect"b1"canDeselect"b1"didSelect"b1"didDeselect"b1} _delegateImplements;
@"<UICalendarSelectionMultiDateDelegate>" _delegate;
```

## Properties

```
@property (T@"NSArray",C,N) selectedDates;
@property (T@"<UICalendarSelectionMultiDateDelegate>",R,W,N,V_delegate) delegate;
```

## Instance methods

```
-[UICalendarSelectionMultiDate initWithDelegate:];
-[UICalendarSelectionMultiDate init];
-[UICalendarSelectionMultiDate delegate];
-[UICalendarSelectionMultiDate highlightsToday];
-[UICalendarSelectionMultiDate _removeSelectedDatesSatisfyingPredicate:];
-[UICalendarSelectionMultiDate _sanitizeDateComponents:calendar:];
-[UICalendarSelectionMultiDate _selectedDatesSatisfyingPredicate:];
-[UICalendarSelectionMultiDate canSelectDate:];
-[UICalendarSelectionMultiDate didChangeAvailableDateRange:];
-[UICalendarSelectionMultiDate didChangeCalendar:];
-[UICalendarSelectionMultiDate didChangeVisibleMonth:];
-[UICalendarSelectionMultiDate didDeselectDate:];
-[UICalendarSelectionMultiDate didMoveToCalendarView];
-[UICalendarSelectionMultiDate didSelectDate:];
-[UICalendarSelectionMultiDate selectAllDatesAnimated:];
-[UICalendarSelectionMultiDate selectedDates];
-[UICalendarSelectionMultiDate setSelectedDates:];
-[UICalendarSelectionMultiDate setSelectedDates:animated:];
-[UICalendarSelectionMultiDate shouldDeselectDate:];
-[UICalendarSelectionMultiDate willMoveToCalendarView:];
```
