# `_UIDatePickerCompactTimeLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIDatePickerCalendarTimeLabel`
- Protocols: `UIPointerInteractionDelegate`, `_UIDatePickerCalendarTimeLabelDelegate`, `_UIPassthroughScrollInteractionDelegate`, `_UIControlEventsGestureRecognizerDelegate`, `UIGestureRecognizerDelegateInternal`
- 25 instance variables, 23 properties, 78 instance methods, 0 class methods

## Instance variables

```
{?="needsLabelUpdateOnResignFirstResponder"b1"deferringHoverStateUpdate"b1"highlightedForTouch"b1} _flags;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _hourRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _minuteRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _timeOfDayRect;
@"NSDateFormatter" _formatter;
@"_UITextLayoutControllerBase<_UITextLayoutController>" _textLayoutController;
@"NSTextContentStorage" _textContentStorage;
q _highlightedScope;
@"UIView" _touchHighlightedView;
B _enabled;
B _tapInteractionControlledExternally;
@"<_UIDatePickerCompactTimeLabelDelegate>" _selectionDelegate;
@"_UIDatePickerOverlayPresentation" _overlayPresentation;
@"_UIDatePickerCalendarTime" _selectedTime;
@"NSDictionary" _overrideAttributes;
@"UIPointerInteraction" _pointerInteraction;
@"UILabel" _label;
@"UILabel" _hourLabel;
@"UILabel" _minuteLabel;
@"UILabel" _timeOfDayLabel;
@"UIButton" _backgroundView;
@"UIView" _inputBackgroundView;
Q _currentState;
@"_UIPassthroughScrollInteraction" _passthroughInteraction;
@"_UIDatePickerStyle" _datePickerStyle;
```

## Properties

```
@property (T@"UIPointerInteraction",R,N,V_pointerInteraction) pointerInteraction;
@property (T@"UILabel",R,N,V_label) label;
@property (T@"UILabel",R,N,V_hourLabel) hourLabel;
@property (T@"UILabel",R,N,V_minuteLabel) minuteLabel;
@property (T@"UILabel",R,N,V_timeOfDayLabel) timeOfDayLabel;
@property (T@"UIButton",R,N,V_backgroundView) backgroundView;
@property (T@"UIView",R,N,V_inputBackgroundView) inputBackgroundView;
@property (TQ,R,N,V_currentState) currentState;
@property (T@"_UIPassthroughScrollInteraction",R,N,V_passthroughInteraction) passthroughInteraction;
@property (T@"_UIDatePickerStyle",R,N,V_datePickerStyle) datePickerStyle;
@property (TB,N,GisPassthroughInteractionEnabled) passthroughInteractionEnabled;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (T@"<_UIDatePickerCompactTimeLabelDelegate>",W,N,V_selectionDelegate) selectionDelegate;
@property (T@"_UIDatePickerOverlayPresentation",W,N,V_overlayPresentation) overlayPresentation;
@property (T@"_UIDatePickerCalendarTime",R,N,V_selectedTime) selectedTime;
@property (Td,N) minimumScaleFactor;
@property (TB,N) adjustsFontSizeToFitWidth;
@property (TB,N,V_tapInteractionControlledExternally) tapInteractionControlledExternally;
@property (T@"NSDictionary",&,N,V_overrideAttributes) overrideAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDatePickerCompactTimeLabel _gestureRecognizerFailed:];
-[_UIDatePickerCompactTimeLabel keyboardTypeForTimeLabel:];
-[_UIDatePickerCompactTimeLabel hourRect];
-[_UIDatePickerCompactTimeLabel intrinsicContentSize];
-[_UIDatePickerCompactTimeLabel timeLabelDidBecomeFirstResponder:];
-[_UIDatePickerCompactTimeLabel timeLabelDidEndEditing:];
-[_UIDatePickerCompactTimeLabel pointerInteraction:styleForRegion:];
-[_UIDatePickerCompactTimeLabel label];
-[_UIDatePickerCompactTimeLabel pointerInteraction:willEnterRegion:animator:];
-[_UIDatePickerCompactTimeLabel pointerInteraction:willExitRegion:animator:];
-[_UIDatePickerCompactTimeLabel timeLabelDidResignFirstResponder:];
-[_UIDatePickerCompactTimeLabel datePickerStyle];
-[_UIDatePickerCompactTimeLabel setAdjustsFontSizeToFitWidth:];
-[_UIDatePickerCompactTimeLabel passthroughScrollInteractionDidRecognize:atLocation:];
-[_UIDatePickerCompactTimeLabel isEnabled];
-[_UIDatePickerCompactTimeLabel sizeThatFits:];
-[_UIDatePickerCompactTimeLabel passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_UIDatePickerCompactTimeLabel stateMachineUpdateFromState:toState:];
-[_UIDatePickerCompactTimeLabel setHighlightedForTouch:];
-[_UIDatePickerCompactTimeLabel initWithTimeFormat:minuteInterval:];
-[_UIDatePickerCompactTimeLabel setPassthroughInteractionEnabled:];
-[_UIDatePickerCompactTimeLabel minimumScaleFactor];
-[_UIDatePickerCompactTimeLabel timeLabel:didReceiveText:];
-[_UIDatePickerCompactTimeLabel pointerInteraction];
-[_UIDatePickerCompactTimeLabel setEnabled:];
-[_UIDatePickerCompactTimeLabel adjustsFontSizeToFitWidth];
-[_UIDatePickerCompactTimeLabel timeLabelDidBeginEditing:];
-[_UIDatePickerCompactTimeLabel pointerInteraction:regionForRequest:defaultRegion:];
-[_UIDatePickerCompactTimeLabel timeLabelShouldSuppressSoftwareKeyboard:];
-[_UIDatePickerCompactTimeLabel timeLabelWillBecomeFirstResponder:];
-[_UIDatePickerCompactTimeLabel timeLabelCanBecomeFirstResponder:];
-[_UIDatePickerCompactTimeLabel backgroundView];
-[_UIDatePickerCompactTimeLabel minuteRect];
-[_UIDatePickerCompactTimeLabel hourLabel];
-[_UIDatePickerCompactTimeLabel timeLabelDidFailToBecomeFirstResponder:];
-[_UIDatePickerCompactTimeLabel willBeginWritingInScribbleInteraction];
-[_UIDatePickerCompactTimeLabel font];
-[_UIDatePickerCompactTimeLabel pushCurrentStateIntoUI];
-[_UIDatePickerCompactTimeLabel minuteLabel];
-[_UIDatePickerCompactTimeLabel setMinimumScaleFactor:];
-[_UIDatePickerCompactTimeLabel currentState];
-[_UIDatePickerCompactTimeLabel controlEventsGestureRecognizer:recognizedControlEvent:withEvent:];
-[_UIDatePickerCompactTimeLabel setFont:];
-[_UIDatePickerCompactTimeLabel timeLabel:didUpdateText:];
-[_UIDatePickerCompactTimeLabel pushCurrentStateIntoUIAndNotify];
-[_UIDatePickerCompactTimeLabel reloadWithDate:];
-[_UIDatePickerCompactTimeLabel _updateHoverStateLabelsIfNeeded];
-[_UIDatePickerCompactTimeLabel isPassthroughInteractionEnabled];
-[_UIDatePickerCompactTimeLabel _activateCompactLabelForGestureRecognizer:];
-[_UIDatePickerCompactTimeLabel _currentDateForInput];
-[_UIDatePickerCompactTimeLabel _expandedComponentRectForHours:minuteRect:timeOfDayRect:];
-[_UIDatePickerCompactTimeLabel _inputScopeForPointerLocation:];
-[_UIDatePickerCompactTimeLabel _reloadWithDate:notify:];
-[_UIDatePickerCompactTimeLabel _updateEnabledStyling];
-[_UIDatePickerCompactTimeLabel _updateInputFieldFromSelectedDateComponents];
-[_UIDatePickerCompactTimeLabel _updateInputFieldLayoutForCurrentState];
-[_UIDatePickerCompactTimeLabel _updateLayoutRectsForRanges:];
-[_UIDatePickerCompactTimeLabel _updateSelectedDateComponentsFromInput];
-[_UIDatePickerCompactTimeLabel _updateTextContentStorage];
-[_UIDatePickerCompactTimeLabel _updateTimeFormatIfNeeded];
-[_UIDatePickerCompactTimeLabel _viewForInputScope:];
-[_UIDatePickerCompactTimeLabel activateLabel];
-[_UIDatePickerCompactTimeLabel applyTextAttributesForState:inputScope:updater:];
-[_UIDatePickerCompactTimeLabel inputBackgroundView];
-[_UIDatePickerCompactTimeLabel overlayPresentation];
-[_UIDatePickerCompactTimeLabel overrideAttributes];
-[_UIDatePickerCompactTimeLabel passthroughInteraction];
-[_UIDatePickerCompactTimeLabel reloadWithCalendar:locale:followsSystemHourCycle:displaysTimeZone:];
-[_UIDatePickerCompactTimeLabel selectedTime];
-[_UIDatePickerCompactTimeLabel selectionDelegate];
-[_UIDatePickerCompactTimeLabel setOverlayPresentation:];
-[_UIDatePickerCompactTimeLabel setOverrideAttributes:];
-[_UIDatePickerCompactTimeLabel setSelectionDelegate:];
-[_UIDatePickerCompactTimeLabel setTapInteractionControlledExternally:];
-[_UIDatePickerCompactTimeLabel tapInteractionControlledExternally];
-[_UIDatePickerCompactTimeLabel timeOfDayLabel];
-[_UIDatePickerCompactTimeLabel timeOfDayRect];
-[_UIDatePickerCompactTimeLabel updateHoverLabelForAttributedString:ranges:];
```
