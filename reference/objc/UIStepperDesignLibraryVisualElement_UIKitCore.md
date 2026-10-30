# `UIStepperDesignLibraryVisualElement`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIStepperVisualElement`
- 22 instance variables, 9 properties, 38 instance methods, 5 class methods

## Instance variables

```
@"<UIStepperControl>" stepperControl;
B isEnabled;
d value;
d minimumValue;
d maximumValue;
d stepValue;
B isContinuous;
B wraps;
B autorepeat;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 isRTL;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 coreHostingView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 minusPressed;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 plusPressed;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 minusEnabled;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 plusEnabled;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 repeatTimer;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 timerDelay;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 fastTimerDelay;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 superFastTimerDelay;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 fastStartRepeatCount;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 superFastStartRepeatCount;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 repeatCount;
```

## Properties

```
@property (T@"<UIStepperControl>",N,&,VstepperControl) stepperControl;
@property (TB,N,VisEnabled) enabled;
@property (Td,N,Vvalue) value;
@property (Td,N,VminimumValue) minimumValue;
@property (Td,N,VmaximumValue) maximumValue;
@property (Td,N,VstepValue) stepValue;
@property (TB,N,VisContinuous) continuous;
@property (TB,N,Vwraps) wraps;
@property (TB,N,Vautorepeat) autorepeat;
```

## Class methods

```
+[UIStepperDesignLibraryVisualElement setInitialSize:];
+[UIStepperDesignLibraryVisualElement initialAlignmentRectInsets];
+[UIStepperDesignLibraryVisualElement initialIntrinsicSize];
+[UIStepperDesignLibraryVisualElement initialSize];
+[UIStepperDesignLibraryVisualElement setInitialAlignmentRectInsets:];
```

## Instance methods

```
-[UIStepperDesignLibraryVisualElement setMaximumValue:];
-[UIStepperDesignLibraryVisualElement init];
-[UIStepperDesignLibraryVisualElement cancelTrackingWithEvent:];
-[UIStepperDesignLibraryVisualElement setContinuous:];
-[UIStepperDesignLibraryVisualElement endTrackingWithTouch:withEvent:];
-[UIStepperDesignLibraryVisualElement continueTrackingWithTouch:withEvent:];
-[UIStepperDesignLibraryVisualElement value];
-[UIStepperDesignLibraryVisualElement layoutSubviews];
-[UIStepperDesignLibraryVisualElement beginTrackingWithTouch:withEvent:];
-[UIStepperDesignLibraryVisualElement isContinuous];
-[UIStepperDesignLibraryVisualElement isEnabled];
-[UIStepperDesignLibraryVisualElement backgroundImageForState:];
-[UIStepperDesignLibraryVisualElement setValue:];
-[UIStepperDesignLibraryVisualElement setMinimumValue:];
-[UIStepperDesignLibraryVisualElement setEnabled:];
-[UIStepperDesignLibraryVisualElement initWithCoder:];
-[UIStepperDesignLibraryVisualElement minimumValue];
-[UIStepperDesignLibraryVisualElement initWithFrame:];
-[UIStepperDesignLibraryVisualElement maximumValue];
-[UIStepperDesignLibraryVisualElement setBackgroundImage:forState:];
-[UIStepperDesignLibraryVisualElement alignmentRectInsetsForControl:];
-[UIStepperDesignLibraryVisualElement autorepeat];
-[UIStepperDesignLibraryVisualElement decrementImageForState:];
-[UIStepperDesignLibraryVisualElement dividerImageForLeftSegmentState:rightSegmentState:];
-[UIStepperDesignLibraryVisualElement incrementImageForState:];
-[UIStepperDesignLibraryVisualElement intrinsicSizeWithinSize:forControl:];
-[UIStepperDesignLibraryVisualElement setAutorepeat:];
-[UIStepperDesignLibraryVisualElement setDecrementImage:forState:];
-[UIStepperDesignLibraryVisualElement setDividerImage:forLeftSegmentState:rightSegmentState:];
-[UIStepperDesignLibraryVisualElement setIncrementImage:forState:];
-[UIStepperDesignLibraryVisualElement setStepValue:];
-[UIStepperDesignLibraryVisualElement setStepperControl:];
-[UIStepperDesignLibraryVisualElement setWraps:];
-[UIStepperDesignLibraryVisualElement sizeThatFits:forControl:];
-[UIStepperDesignLibraryVisualElement stepValue];
-[UIStepperDesignLibraryVisualElement stepperControl];
-[UIStepperDesignLibraryVisualElement updateCount:];
-[UIStepperDesignLibraryVisualElement wraps];
```
