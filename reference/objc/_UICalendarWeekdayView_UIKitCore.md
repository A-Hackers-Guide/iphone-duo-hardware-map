# `_UICalendarWeekdayView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
{?="rebuildLabels"B} _flags;
@"NSArray" _labels;
@"_UICalendarDataModel" _dataModel;
@"_UIDatePickerLinkedLabel" _sizingLabel;
d _preferredLabelWidth;
```

## Properties

```
@property (T@"_UICalendarDataModel",R,N,V_dataModel) dataModel;
@property (T@"_UIDatePickerLinkedLabel",R,N,V_sizingLabel) sizingLabel;
@property (Td,N,V_preferredLabelWidth) preferredLabelWidth;
```

## Instance methods

```
-[_UICalendarWeekdayView _updateFont];
-[_UICalendarWeekdayView _intrinsicSizeWithinSize:];
-[_UICalendarWeekdayView layoutSubviews];
-[_UICalendarWeekdayView sizeThatFits:];
-[_UICalendarWeekdayView dataModel];
-[_UICalendarWeekdayView didUpdateLocale];
-[_UICalendarWeekdayView _rebuildLabels];
-[_UICalendarWeekdayView _setNeedsRebuildLabels];
-[_UICalendarWeekdayView didUpdateCalendar];
-[_UICalendarWeekdayView didUpdateFontDesign];
-[_UICalendarWeekdayView initWithDataModel:];
-[_UICalendarWeekdayView preferredLabelWidth];
-[_UICalendarWeekdayView setPreferredLabelWidth:];
-[_UICalendarWeekdayView sizingLabel];
```
