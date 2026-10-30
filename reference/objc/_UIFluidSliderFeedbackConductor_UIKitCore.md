# `_UIFluidSliderFeedbackConductor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
d _epsilon;
@"<_UIFluidSliderFeedbackPlayer>" __directFeedbackPlayer;
@"<_UIFluidSliderFeedbackPlayer>" __indirectFeedbackPlayer;
d __lastValue;
d __lastSnappingTarget;
Q __detentCount;
q __currentRegion;
```

## Properties

```
@property (T@"<_UIFluidSliderFeedbackPlayer>",&,N,V__directFeedbackPlayer) _directFeedbackPlayer;
@property (T@"<_UIFluidSliderFeedbackPlayer>",&,N,V__indirectFeedbackPlayer) _indirectFeedbackPlayer;
@property (Td,N,V__lastValue) _lastValue;
@property (Td,N,V__lastSnappingTarget) _lastSnappingTarget;
@property (TQ,N,V__detentCount) _detentCount;
@property (Tq,N,V__currentRegion) _currentRegion;
@property (Td,N,V_epsilon) epsilon;
```

## Instance methods

```
-[_UIFluidSliderFeedbackConductor _indirectFeedbackPlayer];
-[_UIFluidSliderFeedbackConductor _lastSnappingTarget];
-[_UIFluidSliderFeedbackConductor set_detentCount:];
-[_UIFluidSliderFeedbackConductor set_lastValue:];
-[_UIFluidSliderFeedbackConductor _lastValue];
-[_UIFluidSliderFeedbackConductor initWithDetentCount:view:indirectFeedbackPlayer:];
-[_UIFluidSliderFeedbackConductor moveToValue:snappingTarget:withUpdateType:atLocation:forced:];
-[_UIFluidSliderFeedbackConductor _playFeedback:forUpdateType:value:atLocation:];
-[_UIFluidSliderFeedbackConductor _detentCount];
-[_UIFluidSliderFeedbackConductor set_currentRegion:];
-[_UIFluidSliderFeedbackConductor set_indirectFeedbackPlayer:];
-[_UIFluidSliderFeedbackConductor set_lastSnappingTarget:];
-[_UIFluidSliderFeedbackConductor _directFeedbackPlayer];
-[_UIFluidSliderFeedbackConductor setEpsilon:];
-[_UIFluidSliderFeedbackConductor epsilon];
-[_UIFluidSliderFeedbackConductor set_directFeedbackPlayer:];
-[_UIFluidSliderFeedbackConductor _currentRegion];
```
