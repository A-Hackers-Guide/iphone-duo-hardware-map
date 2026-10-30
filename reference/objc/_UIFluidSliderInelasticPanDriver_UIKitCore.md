# `_UIFluidSliderInelasticPanDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIFluidSliderDirectDriving`
- 10 instance variables, 15 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _enabled;
@"<_UIFluidSliderDrivable>" _drivable;
@"UIView" _view;
d _stretchAmount;
d _velocityMultiplier;
Q _trackAxis;
@"<_UIFluidSliderDirectDrivingDelegate>" _delegate;
@"UIPanGestureRecognizer" _panGestureRecognizer;
d __previousTranslation;
d __previousValue;
```

## Properties

```
@property (Td,N,V__previousTranslation) _previousTranslation;
@property (Td,N,V__previousValue) _previousValue;
@property (T@"UIPanGestureRecognizer",R,N,V_panGestureRecognizer) panGestureRecognizer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UIFluidSliderDirectDrivingDelegate>",W,N,V_delegate) delegate;
@property (T@"<_UIFluidSliderDrivable>",W,N,V_drivable) drivable;
@property (T@"UIView",W,N,V_view) view;
@property (TB,N,V_enabled) enabled;
@property (TQ,N,V_trackAxis) trackAxis;
@property (Td,N,V_stretchAmount) stretchAmount;
@property (Td,N,V_velocityMultiplier) velocityMultiplier;
@property (T@"NSString",R,N) name;
```

## Instance methods

```
-[_UIFluidSliderInelasticPanDriver panGestureRecognizer];
-[_UIFluidSliderInelasticPanDriver stretchAmount];
-[_UIFluidSliderInelasticPanDriver velocityMultiplier];
-[_UIFluidSliderInelasticPanDriver _previousValue];
-[_UIFluidSliderInelasticPanDriver drivable];
-[_UIFluidSliderInelasticPanDriver setStretchAmount:];
-[_UIFluidSliderInelasticPanDriver enabled];
-[_UIFluidSliderInelasticPanDriver init];
-[_UIFluidSliderInelasticPanDriver stop];
-[_UIFluidSliderInelasticPanDriver _trackLength];
-[_UIFluidSliderInelasticPanDriver setView:];
-[_UIFluidSliderInelasticPanDriver view];
-[_UIFluidSliderInelasticPanDriver setTrackAxis:];
-[_UIFluidSliderInelasticPanDriver setDelegate:];
-[_UIFluidSliderInelasticPanDriver gestureRecognizerShouldBegin:];
-[_UIFluidSliderInelasticPanDriver setEnabled:];
-[_UIFluidSliderInelasticPanDriver delegate];
-[_UIFluidSliderInelasticPanDriver setVelocityMultiplier:];
-[_UIFluidSliderInelasticPanDriver cancel];
-[_UIFluidSliderInelasticPanDriver trackAxis];
-[_UIFluidSliderInelasticPanDriver name];
-[_UIFluidSliderInelasticPanDriver setDrivable:];
-[_UIFluidSliderInelasticPanDriver _handleGesture:];
-[_UIFluidSliderInelasticPanDriver _issueUpdateWithValue:isActive:];
-[_UIFluidSliderInelasticPanDriver _previousTranslation];
-[_UIFluidSliderInelasticPanDriver set_previousTranslation:];
-[_UIFluidSliderInelasticPanDriver set_previousValue:];
```
