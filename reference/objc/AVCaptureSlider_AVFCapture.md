# `AVCaptureSlider`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureControl`
- 14 instance variables, 8 properties, 24 instance methods, 1 class methods

## Instance variables

```
f _value;
@"NSString" _localizedValueFormat;
@"NSArray" _prominentValues;
f _minValue;
f _maxValue;
@"CAMOverlayDiscreteFloatRange" _discreteRange;
@"CAMOverlayContinuousFloatRange" _continuousRange;
@"NSString" _localizedTitle;
@"NSString" _symbolName;
@"NSString" _accessibilityIdentifier;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _actionLock;
@"NSObject<OS_dispatch_queue>" _actionQueue;
@? _action;
@"CAMOverlayServiceSlider" _overlayControl;
```

## Properties

```
@property (T@?,C,N,V_action) action;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_actionQueue) actionQueue;
@property (Tf,N,V_value) value;
@property (T@"NSString",C,N,V_localizedValueFormat) localizedValueFormat;
@property (T@"NSArray",C,N,V_prominentValues) prominentValues;
@property (T@"NSString",R,C,N,V_localizedTitle) localizedTitle;
@property (T@"NSString",R,C,N,V_symbolName) symbolName;
@property (T@"NSString",C,N,V_accessibilityIdentifier) accessibilityIdentifier;
```

## Class methods

```
+[AVCaptureSlider initialize];
```

## Instance methods

```
-[AVCaptureSlider localizedTitle];
-[AVCaptureSlider setLocalizedValueValueFormat:];
-[AVCaptureSlider setLocalizedValueFormat:];
-[AVCaptureSlider symbolName];
-[AVCaptureSlider actionQueue];
-[AVCaptureSlider dealloc];
-[AVCaptureSlider enqueueActionWithUpdate:];
-[AVCaptureSlider value];
-[AVCaptureSlider initWithLocalizedTitle:symbolName:minValue:maxValue:step:];
-[AVCaptureSlider setAction:];
-[AVCaptureSlider action];
-[AVCaptureSlider initWithLocalizedTitle:symbolName:values:];
-[AVCaptureSlider setAccessibilityIdentifier:];
-[AVCaptureSlider setActionQueue:];
-[AVCaptureSlider initWithLocalizedTitle:symbolName:minValue:maxValue:];
-[AVCaptureSlider accessibilityIdentifier];
-[AVCaptureSlider setValue:];
-[AVCaptureSlider overlayUpdate];
-[AVCaptureSlider prominentValues];
-[AVCaptureSlider setActionQueue:action:];
-[AVCaptureSlider description];
-[AVCaptureSlider overlayControl];
-[AVCaptureSlider setProminentValues:];
-[AVCaptureSlider localizedValueFormat];
```
