# `DBSDeviceDisplayZoomAnimationView`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _animating;
f _duration;
d _scale;
Q _displayZoomOption;
@"CALayer" _packageLayer;
@"CAPackage" _package;
@"CAStateController" _stateController;
Q _state;
```

## Properties

```
@property (TQ,N,V_displayZoomOption) displayZoomOption;
@property (T@"CALayer",&,N,V_packageLayer) packageLayer;
@property (T@"CAPackage",&,N,V_package) package;
@property (T@"CAStateController",&,N,V_stateController) stateController;
@property (TQ,N,V_state) state;
@property (Tf,N,V_duration) duration;
@property (TB,N,GisAnimating,V_animating) animating;
@property (T{CGSize=dd},R,N) preferredSize;
@property (Td,N,V_scale) scale;
```

## Instance methods

```
-[DBSDeviceDisplayZoomAnimationView package];
-[DBSDeviceDisplayZoomAnimationView startAnimation];
-[DBSDeviceDisplayZoomAnimationView setState:];
-[DBSDeviceDisplayZoomAnimationView intrinsicContentSize];
-[DBSDeviceDisplayZoomAnimationView drawRect:];
-[DBSDeviceDisplayZoomAnimationView setScale:];
-[DBSDeviceDisplayZoomAnimationView duration];
-[DBSDeviceDisplayZoomAnimationView scale];
-[DBSDeviceDisplayZoomAnimationView setPackage:];
-[DBSDeviceDisplayZoomAnimationView stateController];
-[DBSDeviceDisplayZoomAnimationView _setPackage:];
-[DBSDeviceDisplayZoomAnimationView traitCollectionDidChange:];
-[DBSDeviceDisplayZoomAnimationView setPackageLayer:];
-[DBSDeviceDisplayZoomAnimationView setDuration:];
-[DBSDeviceDisplayZoomAnimationView setStateController:];
-[DBSDeviceDisplayZoomAnimationView isAnimating];
-[DBSDeviceDisplayZoomAnimationView setAnimating:];
-[DBSDeviceDisplayZoomAnimationView preferredSize];
-[DBSDeviceDisplayZoomAnimationView state];
-[DBSDeviceDisplayZoomAnimationView packageLayer];
-[DBSDeviceDisplayZoomAnimationView _configureView];
-[DBSDeviceDisplayZoomAnimationView stopAnimation];
-[DBSDeviceDisplayZoomAnimationView _startAnimationForLayer:];
-[DBSDeviceDisplayZoomAnimationView setDisplayZoomOption:];
-[DBSDeviceDisplayZoomAnimationView displayZoomOption];
-[DBSDeviceDisplayZoomAnimationView _stepAnimamtionForLayer:];
-[DBSDeviceDisplayZoomAnimationView initWithDisplayZoomOption:];
```
