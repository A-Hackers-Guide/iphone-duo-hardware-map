# `_UICalendarHeaderView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`
- 8 instance variables, 7 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSDateFormatter" _longFormatter;
@"NSDateFormatter" _shortFormatter;
@"_UICalendarHeaderTitleButton" _monthYearButton;
@"UIButton" _previousMonthButton;
@"UIButton" _nextMonthButton;
B _expanded;
@"<_UICalendarHeaderViewDelegate>" _delegate;
@"_UICalendarDataModel" _dataModel;
```

## Properties

```
@property (T@"<_UICalendarHeaderViewDelegate>",W,N,V_delegate) delegate;
@property (T@"_UICalendarDataModel",&,N,V_dataModel) dataModel;
@property (TB,R,N,GisExpanded,V_expanded) expanded;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICalendarHeaderView didMoveToWindow];
-[_UICalendarHeaderView setExpanded:];
-[_UICalendarHeaderView _updateFont];
-[_UICalendarHeaderView pointerInteraction:styleForRegion:];
-[_UICalendarHeaderView isExpanded];
-[_UICalendarHeaderView _intrinsicSizeWithinSize:];
-[_UICalendarHeaderView layoutSubviews];
-[_UICalendarHeaderView sizeThatFits:];
-[_UICalendarHeaderView setDelegate:];
-[_UICalendarHeaderView tintColorDidChange];
-[_UICalendarHeaderView delegate];
-[_UICalendarHeaderView dataModel];
-[_UICalendarHeaderView setExpanded:animated:];
-[_UICalendarHeaderView didUpdateLocale];
-[_UICalendarHeaderView _adjustMonth:];
-[_UICalendarHeaderView _setupDateFormatter];
-[_UICalendarHeaderView _setupViewHierarchy];
-[_UICalendarHeaderView _updateMonthButtonEnablement];
-[_UICalendarHeaderView _updateMonthButtonVisibility];
-[_UICalendarHeaderView _updateMonthYearLabel];
-[_UICalendarHeaderView didUpdateCalendar];
-[_UICalendarHeaderView didUpdateDateRange];
-[_UICalendarHeaderView didUpdateFontDesign];
-[_UICalendarHeaderView didUpdateTimeZone];
-[_UICalendarHeaderView didUpdateVisibleMonth];
-[_UICalendarHeaderView initWithDataModel:delegate:];
-[_UICalendarHeaderView setDataModel:];
```
