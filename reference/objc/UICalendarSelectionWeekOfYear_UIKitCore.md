# `UICalendarSelectionWeekOfYear`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICalendarSelection`
- 4 instance variables, 2 properties, 19 instance methods, 0 class methods

## Instance variables

```
{?="canSelect"b1"didSelect"b1} _delegateImplements;
@"NSArray" _dateComponentsForWeekOfYear;
@"NSDateComponents" _selectedWeekOfYear;
@"<UICalendarSelectionWeekOfYearDelegate>" _delegate;
```

## Properties

```
@property (T@"NSDateComponents",C,N,V_selectedWeekOfYear) selectedWeekOfYear;
@property (T@"<UICalendarSelectionWeekOfYearDelegate>",R,W,N,V_delegate) delegate;
```

## Instance methods

```
-[UICalendarSelectionWeekOfYear initWithDelegate:];
-[UICalendarSelectionWeekOfYear delegate];
-[UICalendarSelectionWeekOfYear setSelectedWeekOfYear:animated:];
-[UICalendarSelectionWeekOfYear _dateComponentsForWeekOfYear:];
-[UICalendarSelectionWeekOfYear _sendDelegateForSelectedDateChange];
-[UICalendarSelectionWeekOfYear _weekOfYearComponentsForDateComponents:];
-[UICalendarSelectionWeekOfYear canSelectDate:];
-[UICalendarSelectionWeekOfYear didChangeAvailableDateRange:];
-[UICalendarSelectionWeekOfYear didChangeCalendar:];
-[UICalendarSelectionWeekOfYear didDeselectDate:];
-[UICalendarSelectionWeekOfYear didMoveToCalendarView];
-[UICalendarSelectionWeekOfYear didSelectDate:];
-[UICalendarSelectionWeekOfYear renderOverhangDays];
-[UICalendarSelectionWeekOfYear roundedEdgeForDate:];
-[UICalendarSelectionWeekOfYear selectAllDatesAnimated:];
-[UICalendarSelectionWeekOfYear selectedWeekOfYear];
-[UICalendarSelectionWeekOfYear setSelectedWeekOfYear:];
-[UICalendarSelectionWeekOfYear shouldDeselectDate:];
-[UICalendarSelectionWeekOfYear willMoveToCalendarView:];
```
