# `_UIDatePickerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPickerView`
- Protocols: `_UIDatePickerCalendarTimeLabelDelegate`, `_UIDatePickerWheelsTimeLabelDelegate`, `UIGestureRecognizerDelegateInternal`, `UIPopoverPresentationControllerDelegate`, `_UIPassthroughScrollInteractionDelegate`, `_UIControlEventsGestureRecognizerDelegate`, `UIPickerViewDelegate`, `UIPickerViewDataSource`, `_UIDatePickerWheelsViewComponent`
- 13 instance variables, 25 properties, 130 instance methods, 0 class methods

## Instance variables

```
q _loadingDate;
B _allowsZeroTimeInterval;
@"_UIDatePickerMode" _mode;
@"UILabel" _hourLabel;
@"UILabel" _minuteLabel;
i _expectedDayPeriod;
{?="staggerTimeIntervals"b1"loadingDateOrTime"b1"highlightsToday"b1"updatingWithKeyInput"b1"isPendingManualKeyboardPresentation"b1"isPresentingManualKeyboard"b1"selectionBarTableHidden"b1"receivedTextInputUpdate"b1"isPresentingOrDismissingKeyboard"b1"ignoringSelectionUpdates"b1"dayPeriodUpdatedComponents"b1} _datePickerFlags;
@"_UIPassthroughScrollInteraction" _passthroughInteraction;
@"UIDatePicker" _datePicker;
@"_UIDatePickerDataModel" _data;
@"_UIDatePickerNumericKeyboardViewController" _numericKeyboardViewController;
@"_UIDatePickerWheelsTimeLabel" _timeInputLabel;
@"_UIControlEventsGestureRecognizer" _controlEventsGestureRecognizer;
```

## Properties

```
@property (T@"_UIDatePickerNumericKeyboardViewController",R,N,V_numericKeyboardViewController) numericKeyboardViewController;
@property (T@"_UIDatePickerWheelsTimeLabel",R,N,V_timeInputLabel) timeInputLabel;
@property (T@"_UIControlEventsGestureRecognizer",R,N,V_controlEventsGestureRecognizer) controlEventsGestureRecognizer;
@property (TB,N) passthroughInteractionEnabled;
@property (TB,D,N) highlightsToday;
@property (T@"NSCalendar",R,D,N) calendar;
@property (T@"NSLocale",R,D,N) locale;
@property (T@"UIFont",R,D,N,G_hrMinFont) hrMinFont;
@property (T@"_UIDatePickerDataModel",&,N,V_data) data;
@property (Td,N) timeInterval;
@property (TB,N,G_allowsZeroCountDownDuration,S_setAllowsZeroCountDownDuration:) allowsZeroCountDownDuration;
@property (TB,N,G_allowsZeroTimeInterval,S_setAllowsZeroTimeInterval:) allowsZeroTimeInterval;
@property (Td,R,D,N) contentWidth;
@property (TB,R,D,N,G_isTimeIntervalMode) isTimeIntervalMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIColor",&,N,G_highlightColor,S_setHighlightColor:) highlightColor;
@property (T@"UIColor",&,N,G_textColor,S_setTextColor:) textColor;
@property (T@"UIColor",&,N,G_textShadowColor,S_setTextShadowColor:) textShadowColor;
@property (T@"UIColor",&,N,G_magnifierLineColor,S_setMagnifierLineColor:) magnifierLineColor;
@property (T@"UIDatePicker",W,N,V_datePicker) datePicker;
@property (Tq,R,N) datePickerStyle;
@property (T{UIEdgeInsets=dddd},R,N) appliedInsetsToEdgeOfContent;
```

## Instance methods

```
-[_UIDatePickerView _setMode:];
-[_UIDatePickerView pickerView:rowHeightForComponent:];
-[_UIDatePickerView _gestureRecognizerFailed:];
-[_UIDatePickerView keyboardTypeForTimeLabel:];
-[_UIDatePickerView _updateDateOrTime];
-[_UIDatePickerView _setTextColor:];
-[_UIDatePickerView appliedInsetsToEdgeOfContent];
-[_UIDatePickerView didChangeLocale];
-[_UIDatePickerView gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UIDatePickerView timeInterval];
-[_UIDatePickerView _updateDateForNewDateRange];
-[_UIDatePickerView _updateLabelColors];
-[_UIDatePickerView presentationControllerWillDismiss:];
-[_UIDatePickerView didChangeDateFrom:animated:];
-[_UIDatePickerView _fadeLabelForCalendarUnit:toText:animated:];
-[_UIDatePickerView _labelTextForCalendarUnit:];
-[_UIDatePickerView presentationControllerDidDismiss:];
-[_UIDatePickerView _selectRow:inComponent:animated:notify:];
-[_UIDatePickerView willMoveToSuperview:];
-[_UIDatePickerView gestureRecognizer:shouldReceiveTouch:];
-[_UIDatePickerView timeLabelDidBecomeFirstResponder:];
-[_UIDatePickerView timeLabelDidEndEditing:];
-[_UIDatePickerView _minutesStringForHour:minutes:];
-[_UIDatePickerView _permittedArrowDirectionForKeyboardPopover];
-[_UIDatePickerView setDatePicker:];
-[_UIDatePickerView _makeNewCalendarUnitLabel];
-[_UIDatePickerView staggerTimeIntervals];
-[_UIDatePickerView pickerView:widthForComponent:];
-[_UIDatePickerView _setAllowsZeroCountDownDuration:];
-[_UIDatePickerView numberOfComponentsInPickerView:];
-[_UIDatePickerView timeLabelDidResignFirstResponder:];
-[_UIDatePickerView _dismissManualKeyboard];
-[_UIDatePickerView datePickerStyle];
-[_UIDatePickerView _enableCustomKeyboardIfNecessary];
-[_UIDatePickerView data];
-[_UIDatePickerView dealloc];
-[_UIDatePickerView didChangeMinimumDate];
-[_UIDatePickerView didChangeMinuteInterval];
-[_UIDatePickerView _updateWheelsForUpdatedTextInputWithForcedUpdate:];
-[_UIDatePickerView _shouldInstallTimeInputLabelForDatePickerMode:];
-[_UIDatePickerView layoutSubviews];
-[_UIDatePickerView _currentTimeInputLabelFrame];
-[_UIDatePickerView _uninstallTimeInputLabelIfNeeded];
-[_UIDatePickerView _existingLabelForCalendarUnit:];
-[_UIDatePickerView _selectedTextForCalendarUnit:];
-[_UIDatePickerView timeInputLabel];
-[_UIDatePickerView _loadDateAnimated:];
-[_UIDatePickerView _viewForSelectedRowInComponent:];
-[_UIDatePickerView setHighlightsToday:];
-[_UIDatePickerView shadowColor];
-[_UIDatePickerView passthroughScrollInteractionDidRecognize:atLocation:];
-[_UIDatePickerView didChangeRoundsToMinuteInterval];
-[_UIDatePickerView _positionLabel:forCalendarUnit:relativeTo:order:];
-[_UIDatePickerView didChangeTimeZone];
-[_UIDatePickerView pickerView:didSelectRow:inComponent:];
-[_UIDatePickerView _contentHuggingDefault_isUsuallyFixedHeight];
-[_UIDatePickerView passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UIDatePickerView _hrMinFont];
-[_UIDatePickerView pickerView:numberOfRowsInComponent:];
-[_UIDatePickerView popoverPresentationController:willRepositionPopoverToRect:inView:];
-[_UIDatePickerView _selectionBarRowInComponent:];
-[_UIDatePickerView controlEventsGestureRecognizer];
-[_UIDatePickerView willMoveToWindow:];
-[_UIDatePickerView pickerView:viewForRow:forComponent:reusingView:];
-[_UIDatePickerView setPassthroughInteractionEnabled:];
-[_UIDatePickerView didChangeCalendar];
-[_UIDatePickerView _currentTimeFormat];
-[_UIDatePickerView _resetSelectionOfTables];
-[_UIDatePickerView numericKeyboardViewController];
-[_UIDatePickerView timeLabel:didReceiveText:];
-[_UIDatePickerView _installTimeInputLabelIfNeeded];
-[_UIDatePickerView _updateLocaleTimeZoneOrCalendar];
-[_UIDatePickerView setData:];
-[_UIDatePickerView _updateTextColorForCalendarUnitLabel:];
-[_UIDatePickerView _setAllowsZeroTimeInterval:];
-[_UIDatePickerView wheelsTimeLabelShouldReceiveInteraction:];
-[_UIDatePickerView _isTimeIntervalMode];
-[_UIDatePickerView scrollViewWillBeginDragging:];
-[_UIDatePickerView gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIDatePickerView _labelForCalendarUnit:createIfNecessary:];
-[_UIDatePickerView timeLabelDidBeginEditing:];
-[_UIDatePickerView _componentsSelectedAfterEnforcingValidityOfComponents:withLastManipulatedComponent:];
-[_UIDatePickerView timeLabelShouldSuppressSoftwareKeyboard:];
-[_UIDatePickerView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIDatePickerView timeLabelWillBecomeFirstResponder:];
-[_UIDatePickerView timeLabelCanBecomeFirstResponder:];
-[_UIDatePickerView _performWhileIgnoringSelectionUpdates:];
-[_UIDatePickerView _updateEnabledCellsIncludingWMDCells:];
-[_UIDatePickerView _selectedMinuteForColumn:];
-[_UIDatePickerView setFrame:];
-[_UIDatePickerView hasDefaultSize];
-[_UIDatePickerView passthroughInteractionEnabled];
-[_UIDatePickerView _allowsZeroTimeInterval];
-[_UIDatePickerView _allowsZeroCountDownDuration];
-[_UIDatePickerView _dayPeriodValue];
-[_UIDatePickerView displaySelectedDateAnimated:];
-[_UIDatePickerView _removeUnitLabels];
-[_UIDatePickerView contentWidth];
-[_UIDatePickerView _tableRowHeight];
-[_UIDatePickerView timeLabelDidFailToBecomeFirstResponder:];
-[_UIDatePickerView _updateTimeInputLabelConfiguration];
-[_UIDatePickerView setTimeInterval:];
-[_UIDatePickerView _hardwareKeyboardAvailabilityChanged:];
-[_UIDatePickerView _showingDate];
-[_UIDatePickerView _hidePickerViewSelectionBarForTimeInputLabel:];
-[_UIDatePickerView didChangeToday];
-[_UIDatePickerView _disableCustomKeyboardIfNecessary];
-[_UIDatePickerView _setLabel:forCalendarUnit:animated:];
-[_UIDatePickerView pickerTableView:didChangeSelectionBarRowFrom:to:];
-[_UIDatePickerView _selectedHourForColumn:];
-[_UIDatePickerView _contentViewForSizingLabelForPositioningInComponent:];
-[_UIDatePickerView didChangeMaximumDate];
-[_UIDatePickerView wheelsTimeLabel:didChangeVisibility:];
-[_UIDatePickerView _updateWheelsLabelForCurrentDateComponents];
-[_UIDatePickerView initWithFrame:];
-[_UIDatePickerView controlEventsGestureRecognizer:recognizedControlEvent:withEvent:];
-[_UIDatePickerView primaryFirstResponder];
-[_UIDatePickerView _updateTimeInputLabelPosition];
-[_UIDatePickerView datePickerMode];
-[_UIDatePickerView _updateLabels:];
-[_UIDatePickerView _hoursStringForHour:];
-[_UIDatePickerView _updatedLastSelectedComponentsByValidatingSelectedDateWithLastManipulatedComponent:];
-[_UIDatePickerView highlightsToday];
-[_UIDatePickerView _doneLoadingDateOrTime];
-[_UIDatePickerView datePicker];
-[_UIDatePickerView didChangeMode];
-[_UIDatePickerView _contentHuggingDefault_isUsuallyFixedWidth];
-[_UIDatePickerView didReset];
-[_UIDatePickerView _UIAppearance_setTextColor:];
-[_UIDatePickerView timeLabel:didUpdateText:];
```
