# `UIDatePicker`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIPickerViewScrollTesting`, `NSCoding`
- 11 instance variables, 31 properties, 107 instance methods, 3 class methods

## Instance variables

```
{?="selectionBarIgnoresInset"I} _datePickerViewFlags;
@"UIView<_UIDatePickerViewComponent>" _pickerView;
@"_UIDatePickerDataModel" _data;
B _useCurrentDateDuringDecoding;
B _ignoresEmitValueChanged;
@"_UIDatePickerStyle" _style;
B __useCurrentDateDuringDecoding;
B __displaysTimeZone;
@"<_UIDatePickerCompactStyleDelegate>" __compactStyleDelegate;
q _preferredDatePickerStyle;
@"_UIDatePickerOverlayPresentation" __overlayPresentation;
```

## Properties

```
@property (T@"_UIDatePickerStyle",R,N,V_style) _style;
@property (T@"_UIDatePickerOverlayPresentation",W,N,V__overlayPresentation) _overlayPresentation;
@property (Td,D,N) timeInterval;
@property (TB,N,S_setUseCurrentDateDuringDecoding:,V__useCurrentDateDuringDecoding) _useCurrentDateDuringDecoding;
@property (TB,N,S_setDisplaysTimeZone:,V__displaysTimeZone) _displaysTimeZone;
@property (T@"<_UIDatePickerCompactStyleDelegate>",W,N,S_setCompactStyleDelegate:,V__compactStyleDelegate) _compactStyleDelegate;
@property (T@"NSDictionary",&,N,S_setOverrideCompactTextAttributes:) _overrideCompactTextAttributes;
@property (TB,D,N,G_allowsZeroCountDownDuration,S_setAllowsZeroCountDownDuration:) allowsZeroCountDownDuration;
@property (TB,D,N,G_allowsZeroTimeInterval,S_setAllowsZeroTimeInterval:) allowsZeroTimeInterval;
@property (T@"NSDate",R,D,N,G_dateUnderSelectionBar) dateUnderSelectionBar;
@property (T@"UIColor",&,N,G_highlightColor,S_setHighlightColor:) highlightColor;
@property (T@"UIColor",&,N,G_textColor,S_setTextColor:) textColor;
@property (T@"UIColor",&,N,G_textShadowColor,S_setTextShadowColor:) textShadowColor;
@property (T@"UIColor",&,N,G_magnifierLineColor,S_setMagnifierLineColor:) magnifierLineColor;
@property (Td,R,D,N,G_contentWidth) contentWidth;
@property (TB,R,D,N,G_isTimeIntervalMode) isTimeIntervalMode;
@property (T{UIEdgeInsets=dddd},R,N) _appliedInsetsToEdgeOfContent;
@property (TB,N,S_setSelectionBarIgnoresInset:) _selectionBarIgnoresInset;
@property (T@"NSString",&,N,G_customFontDesign,S_setCustomFontDesign:) customFontDesign;
@property (Tq,D,N) datePickerMode;
@property (T@"NSLocale",&,D,N) locale;
@property (T@"NSCalendar",C,D,N) calendar;
@property (T@"NSTimeZone",&,D,N) timeZone;
@property (T@"NSDate",&,D,N) date;
@property (T@"NSDate",&,D,N) minimumDate;
@property (T@"NSDate",&,D,N) maximumDate;
@property (Td,D,N) countDownDuration;
@property (Tq,D,N) minuteInterval;
@property (Tq,N,V_preferredDatePickerStyle) preferredDatePickerStyle;
@property (Tq,R,N) datePickerStyle;
@property (TB,N) roundsToMinuteInterval;
```

## Class methods

```
+[UIDatePicker _prepareStyleStorageIfNecessary];
+[UIDatePicker _styleForIdiom:];
+[UIDatePicker _registerStyle:forIdiom:];
```

## Instance methods

```
-[UIDatePicker _controlEventsForActionTriggered];
-[UIDatePicker _commonInit];
-[UIDatePicker second];
-[UIDatePicker setTimeZone:];
-[UIDatePicker setCalendar:];
-[UIDatePicker _setTextColor:];
-[UIDatePicker timeInterval];
-[UIDatePicker _systemDefaultFocusGroupIdentifier];
-[UIDatePicker minute];
-[UIDatePicker setMinuteInterval:];
-[UIDatePicker _labelTextForCalendarUnit:];
-[UIDatePicker _textColor];
-[UIDatePicker invalidateIntrinsicContentSize];
-[UIDatePicker setDate:];
-[UIDatePicker _intrinsicSizeWithinSize:];
-[UIDatePicker _setAllowsZeroCountDownDuration:];
-[UIDatePicker datePickerStyle];
-[UIDatePicker setLocale:];
-[UIDatePicker becomeFirstResponder];
-[UIDatePicker dateComponents];
-[UIDatePicker layoutMarginsDidChange];
-[UIDatePicker hitTest:withEvent:];
-[UIDatePicker roundsToMinuteInterval];
-[UIDatePicker _selectedTextForCalendarUnit:];
-[UIDatePicker resignFirstResponder];
-[UIDatePicker calendar];
-[UIDatePicker setBounds:];
-[UIDatePicker setHighlightsToday:];
-[UIDatePicker date];
-[UIDatePicker setBackgroundColor:];
-[UIDatePicker _contentWidth];
-[UIDatePicker timeZone];
-[UIDatePicker sizeThatFits:];
-[UIDatePicker _contentHuggingDefault_isUsuallyFixedHeight];
-[UIDatePicker setDelegate:];
-[UIDatePicker locale];
-[UIDatePicker minimumDate];
-[UIDatePicker minuteInterval];
-[UIDatePicker _highlightColor];
-[UIDatePicker setEnabled:];
-[UIDatePicker _setAllowsZeroTimeInterval:];
-[UIDatePicker _isTimeIntervalMode];
-[UIDatePicker encodeWithCoder:];
-[UIDatePicker setDatePickerMode:];
-[UIDatePicker setFrame:];
-[UIDatePicker _allowsZeroTimeInterval];
-[UIDatePicker _allowsZeroCountDownDuration];
-[UIDatePicker _style];
-[UIDatePicker initWithCoder:];
-[UIDatePicker traitCollectionDidChange:];
-[UIDatePicker setTimeInterval:];
-[UIDatePicker _populateArchivedSubviews:];
-[UIDatePicker setMaximumDate:];
-[UIDatePicker setMinimumDate:];
-[UIDatePicker hour];
-[UIDatePicker setContentHorizontalAlignment:];
-[UIDatePicker initWithFrame:];
-[UIDatePicker datePickerMode];
-[UIDatePicker setRoundsToMinuteInterval:];
-[UIDatePicker maximumDate];
-[UIDatePicker _contentHuggingDefault_isUsuallyFixedWidth];
-[UIDatePicker _emitEndEditing];
-[UIDatePicker _appliedInsetsToEdgeOfContent];
-[UIDatePicker _compactStyleDelegate];
-[UIDatePicker _compactStyleSetActiveComponent:];
-[UIDatePicker _customFontDesign];
-[UIDatePicker _datePickerReset:];
-[UIDatePicker _dateUnderSelectionBar];
-[UIDatePicker _displaysTimeZone];
-[UIDatePicker _emitBeginEditing];
-[UIDatePicker _emitValueChanged];
-[UIDatePicker _installPickerView:updatingSize:];
-[UIDatePicker _lastSelectedDateComponents];
-[UIDatePicker _magnifierLineColor];
-[UIDatePicker _overlayPresentation];
-[UIDatePicker _overrideCompactTextAttributes];
-[UIDatePicker _performScrollTest:withIterations:rowsToScroll:inComponent:];
-[UIDatePicker _registerObservers];
-[UIDatePicker _selectionBarIgnoresInset];
-[UIDatePicker _setCompactStyleDelegate:];
-[UIDatePicker _setCustomFontDesign:];
-[UIDatePicker _setDisplaysTimeZone:];
-[UIDatePicker _setHighlightColor:];
-[UIDatePicker _setHighlightsToday:];
-[UIDatePicker _setMagnifierLineColor:];
-[UIDatePicker _setOverrideCompactTextAttributes:];
-[UIDatePicker _setSelectionBarIgnoresInset:];
-[UIDatePicker _setTextShadowColor:];
-[UIDatePicker _setUpInitialValues];
-[UIDatePicker _setUseCurrentDateDuringDecoding:];
-[UIDatePicker _setUsesBlackChrome:];
-[UIDatePicker _textShadowColor];
-[UIDatePicker _todayChanged:];
-[UIDatePicker _updatePickerDateFromOldDate:animated:];
-[UIDatePicker _updatePickerViewIfNecessary];
-[UIDatePicker _useCurrentDateDuringDecoding];
-[UIDatePicker _workaround66574039_updateLayoutMargins];
-[UIDatePicker awakeFromNib];
-[UIDatePicker countDownDuration];
-[UIDatePicker preferredDatePickerStyle];
-[UIDatePicker setCountDownDuration:];
-[UIDatePicker setDate:animate:];
-[UIDatePicker setDate:animated:];
-[UIDatePicker setDateComponents:];
-[UIDatePicker setPreferredDatePickerStyle:];
-[UIDatePicker setStaggerTimeIntervals:];
-[UIDatePicker set_overlayPresentation:];
```
