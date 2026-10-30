# `_UIDatePickerCompactDateLabel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`
- 8 instance variables, 17 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _enabled;
B _tapInteractionControlledExternally;
B _highlightedForTouch;
@"<_UIDatePickerCompactDateLabelDelegate>" _delegate;
@"_UIDatePickerOverlayPresentation" _overlayPresentation;
@"UIButton" _backgroundView;
@"_UIDatePickerStyle" _visualStyle;
@"_UIDatePickerLinkedLabel" _textLabel;
```

## Properties

```
@property (T@"_UIDatePickerStyle",&,N,V_visualStyle) visualStyle;
@property (T@"UIButton",&,N,V_backgroundView) backgroundView;
@property (T@"_UIDatePickerLinkedLabel",&,N,V_textLabel) textLabel;
@property (TB,N,V_highlightedForTouch) highlightedForTouch;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TB,N,V_tapInteractionControlledExternally) tapInteractionControlledExternally;
@property (TB,N) adjustsFontSizeToFitWidth;
@property (Td,N) minimumScaleFactor;
@property (T@"NSArray",&,N) titles;
@property (T@"NSDictionary",&,N) overrideAttributes;
@property (T@"<_UIDatePickerCompactDateLabelDelegate>",W,N,V_delegate) delegate;
@property (T@"_UIDatePickerOverlayPresentation",W,N,V_overlayPresentation) overlayPresentation;
@property (Tq,N) textAlignment;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDatePickerCompactDateLabel setTextAlignment:];
-[_UIDatePickerCompactDateLabel setTextLabel:];
-[_UIDatePickerCompactDateLabel setVisualStyle:];
-[_UIDatePickerCompactDateLabel textAlignment];
-[_UIDatePickerCompactDateLabel pointerInteraction:styleForRegion:];
-[_UIDatePickerCompactDateLabel visualStyle];
-[_UIDatePickerCompactDateLabel textLabel];
-[_UIDatePickerCompactDateLabel setAdjustsFontSizeToFitWidth:];
-[_UIDatePickerCompactDateLabel isEnabled];
-[_UIDatePickerCompactDateLabel setDelegate:];
-[_UIDatePickerCompactDateLabel setHighlightedForTouch:];
-[_UIDatePickerCompactDateLabel minimumScaleFactor];
-[_UIDatePickerCompactDateLabel setEnabled:];
-[_UIDatePickerCompactDateLabel adjustsFontSizeToFitWidth];
-[_UIDatePickerCompactDateLabel pointerInteraction:regionForRequest:defaultRegion:];
-[_UIDatePickerCompactDateLabel delegate];
-[_UIDatePickerCompactDateLabel backgroundView];
-[_UIDatePickerCompactDateLabel setMinimumScaleFactor:];
-[_UIDatePickerCompactDateLabel initWithFrame:];
-[_UIDatePickerCompactDateLabel setBackgroundView:];
-[_UIDatePickerCompactDateLabel activateLabel];
-[_UIDatePickerCompactDateLabel highlightedForTouch];
-[_UIDatePickerCompactDateLabel overlayPresentation];
-[_UIDatePickerCompactDateLabel overrideAttributes];
-[_UIDatePickerCompactDateLabel setOverlayPresentation:];
-[_UIDatePickerCompactDateLabel setOverrideAttributes:];
-[_UIDatePickerCompactDateLabel setTapInteractionControlledExternally:];
-[_UIDatePickerCompactDateLabel setTitles:];
-[_UIDatePickerCompactDateLabel tapInteractionControlledExternally];
-[_UIDatePickerCompactDateLabel titles];
```
