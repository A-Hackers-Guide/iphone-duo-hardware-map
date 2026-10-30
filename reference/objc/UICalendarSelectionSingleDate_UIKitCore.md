# `UICalendarSelectionSingleDate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICalendarSelection`
- 4 instance variables, 3 properties, 18 instance methods, 0 class methods

## Instance variables

```
{?="canSelect"b1"didSelect"b1} _delegateImplements;
B __selectionFollowsMonthSelection;
@"<UICalendarSelectionSingleDateDelegate>" _delegate;
@"NSDateComponents" _selectedDate;
```

## Properties

```
@property (TB,N,V__selectionFollowsMonthSelection) _selectionFollowsMonthSelection;
@property (T@"<UICalendarSelectionSingleDateDelegate>",R,W,N,V_delegate) delegate;
@property (T@"NSDateComponents",C,N,V_selectedDate) selectedDate;
```

## Instance methods

```
-[UICalendarSelectionSingleDate selectedDate];
-[UICalendarSelectionSingleDate initWithDelegate:];
-[UICalendarSelectionSingleDate setSelectedDate:];
-[UICalendarSelectionSingleDate delegate];
-[UICalendarSelectionSingleDate _selectionFollowsMonthSelection];
-[UICalendarSelectionSingleDate _sendDelegateForSelectedDateChange];
-[UICalendarSelectionSingleDate canSelectDate:];
-[UICalendarSelectionSingleDate didChangeAvailableDateRange:];
-[UICalendarSelectionSingleDate didChangeCalendar:];
-[UICalendarSelectionSingleDate didChangeVisibleMonth:];
-[UICalendarSelectionSingleDate didDeselectDate:];
-[UICalendarSelectionSingleDate didMoveToCalendarView];
-[UICalendarSelectionSingleDate didSelectDate:];
-[UICalendarSelectionSingleDate selectAllDatesAnimated:];
-[UICalendarSelectionSingleDate setSelectedDate:animated:];
-[UICalendarSelectionSingleDate set_selectionFollowsMonthSelection:];
-[UICalendarSelectionSingleDate shouldDeselectDate:];
-[UICalendarSelectionSingleDate willMoveToCalendarView:];
```
