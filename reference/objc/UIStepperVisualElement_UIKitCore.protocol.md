# `UIStepperVisualElement` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 34 instance methods, 3 class methods

## Properties

```
@property (TB,N,GisEnabled) enabled;
@property (Td,N) value;
@property (Td,N) minimumValue;
@property (Td,N) maximumValue;
@property (Td,N) stepValue;
@property (TB,N,GisContinuous) continuous;
@property (TB,N) wraps;
@property (TB,N) autorepeat;
@property (T@"<UIStepperControl>",W,N) stepperControl;
@property (class, T{CGSize=dd},R) initialSize;
@property (class, T{CGSize=dd},R) initialIntrinsicSize;
@property (class, T{UIEdgeInsets=dddd},R) initialAlignmentRectInsets;
```

## Class methods

```
+[UIStepperVisualElement initialAlignmentRectInsets];
+[UIStepperVisualElement initialIntrinsicSize];
+[UIStepperVisualElement initialSize];
```

## Instance methods

```
-[UIStepperVisualElement setMaximumValue:];
-[UIStepperVisualElement init];
-[UIStepperVisualElement cancelTrackingWithEvent:];
-[UIStepperVisualElement setContinuous:];
-[UIStepperVisualElement endTrackingWithTouch:withEvent:];
-[UIStepperVisualElement continueTrackingWithTouch:withEvent:];
-[UIStepperVisualElement value];
-[UIStepperVisualElement beginTrackingWithTouch:withEvent:];
-[UIStepperVisualElement isContinuous];
-[UIStepperVisualElement isEnabled];
-[UIStepperVisualElement backgroundImageForState:];
-[UIStepperVisualElement setValue:];
-[UIStepperVisualElement setMinimumValue:];
-[UIStepperVisualElement setEnabled:];
-[UIStepperVisualElement minimumValue];
-[UIStepperVisualElement maximumValue];
-[UIStepperVisualElement setBackgroundImage:forState:];
-[UIStepperVisualElement alignmentRectInsetsForControl:];
-[UIStepperVisualElement autorepeat];
-[UIStepperVisualElement decrementImageForState:];
-[UIStepperVisualElement dividerImageForLeftSegmentState:rightSegmentState:];
-[UIStepperVisualElement incrementImageForState:];
-[UIStepperVisualElement intrinsicSizeWithinSize:forControl:];
-[UIStepperVisualElement setAutorepeat:];
-[UIStepperVisualElement setDecrementImage:forState:];
-[UIStepperVisualElement setDividerImage:forLeftSegmentState:rightSegmentState:];
-[UIStepperVisualElement setIncrementImage:forState:];
-[UIStepperVisualElement setStepValue:];
-[UIStepperVisualElement setStepperControl:];
-[UIStepperVisualElement setWraps:];
-[UIStepperVisualElement sizeThatFits:forControl:];
-[UIStepperVisualElement stepValue];
-[UIStepperVisualElement stepperControl];
-[UIStepperVisualElement wraps];
```
