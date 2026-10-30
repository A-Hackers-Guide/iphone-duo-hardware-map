# `UIStepper`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIStepperControl`
- 12 instance variables, 8 properties, 54 instance methods, 6 class methods

## Instance variables

```
@"NSMutableDictionary" _dividerImages;
@"NSMutableDictionary" _incrementImages;
@"NSMutableDictionary" _decrementImages;
@"NSMutableDictionary" _backgroundImages;
B _continuous;
B _autorepeat;
B _wraps;
d _value;
d _minimumValue;
d _maximumValue;
d _stepValue;
@"UIView<UIStepperVisualElement>" _visualElement;
```

## Properties

```
@property (T@"UIView<UIStepperVisualElement>",&,N,V_visualElement) visualElement;
@property (TB,N,GisContinuous,V_continuous) continuous;
@property (TB,N,V_autorepeat) autorepeat;
@property (TB,N,V_wraps) wraps;
@property (Td,N,V_value) value;
@property (Td,N,V_minimumValue) minimumValue;
@property (Td,N,V_maximumValue) maximumValue;
@property (Td,N,V_stepValue) stepValue;
```

## Class methods

```
+[UIStepper _setAllowsUnsupportedMacIdiomBehavior:];
+[UIStepper _allowsUnsupportedMacIdiomBehavior];
+[UIStepper _fallbackVisualElementClass];
+[UIStepper _registerVisualElementClass:forIdiom:];
+[UIStepper visualElementClassForTraitCollection:usingImageCustomization:];
+[UIStepper visualElementForTraitCollection:usingImageCustomization:];
```

## Instance methods

```
-[UIStepper _controlEventsForActionTriggered];
-[UIStepper setMaximumValue:];
-[UIStepper pointerInteraction:styleForRegion:];
-[UIStepper _intrinsicSizeWithinSize:];
-[UIStepper alignmentRectInsets];
-[UIStepper pointerInteraction:willEnterRegion:animator:];
-[UIStepper cancelTrackingWithEvent:];
-[UIStepper pointerInteraction:willExitRegion:animator:];
-[UIStepper setContinuous:];
-[UIStepper endTrackingWithTouch:withEvent:];
-[UIStepper continueTrackingWithTouch:withEvent:];
-[UIStepper value];
-[UIStepper hitTest:withEvent:];
-[UIStepper beginTrackingWithTouch:withEvent:];
-[UIStepper isContinuous];
-[UIStepper sizeThatFits:];
-[UIStepper _contentHuggingDefault_isUsuallyFixedHeight];
-[UIStepper tintColorDidChange];
-[UIStepper backgroundImageForState:];
-[UIStepper gestureRecognizerShouldBegin:];
-[UIStepper setValue:];
-[UIStepper setTintColor:];
-[UIStepper setMinimumValue:];
-[UIStepper setEnabled:];
-[UIStepper encodeWithCoder:];
-[UIStepper pointerInteraction:regionForRequest:defaultRegion:];
-[UIStepper setFrame:];
-[UIStepper initWithCoder:];
-[UIStepper _populateArchivedSubviews:];
-[UIStepper minimumValue];
-[UIStepper initWithFrame:];
-[UIStepper maximumValue];
-[UIStepper _contentHuggingDefault_isUsuallyFixedWidth];
-[UIStepper setBackgroundImage:forState:];
-[UIStepper _commonStepperInit];
-[UIStepper _emitValueChanged];
-[UIStepper _refreshVisualElement];
-[UIStepper _refreshVisualElementForTraitCollection:populatingAPIProperties:];
-[UIStepper autorepeat];
-[UIStepper decrementImageForState:];
-[UIStepper dividerImageForLeftSegmentState:rightSegmentState:];
-[UIStepper incrementImageForState:];
-[UIStepper setAutorepeat:];
-[UIStepper setDecrementImage:forState:];
-[UIStepper setDividerImage:forLeftSegmentState:rightSegmentState:];
-[UIStepper setIncrementImage:forState:];
-[UIStepper setStepValue:];
-[UIStepper setVisualElement:];
-[UIStepper setWraps:];
-[UIStepper stepValue];
-[UIStepper visualElement];
-[UIStepper visualElementDidSetValue:];
-[UIStepper visualElementSendValueChangedEvent:];
-[UIStepper wraps];
```
