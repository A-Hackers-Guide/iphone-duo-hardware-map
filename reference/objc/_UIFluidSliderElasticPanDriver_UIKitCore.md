# `_UIFluidSliderElasticPanDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIFluidSliderDirectDriving`
- 15 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 animatedValue;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 previousTranslation;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 previousTarget;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 state;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 initialStretchAmount;
? drivable;
@"UIPanGestureRecognizer" panGestureRecognizer;
Q trackAxis;
d stretchAmount;
d velocityMultiplier;
? delegate;
? name;
? view;
B enabled;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 currentDetent;
```

## Properties

```
@property (T@"<_UIFluidSliderDrivable>",N,W,Vdrivable) drivable;
@property (T@"UIPanGestureRecognizer",N,&,VpanGestureRecognizer) panGestureRecognizer;
@property (TQ,N,VtrackAxis) trackAxis;
@property (Td,N,VstretchAmount) stretchAmount;
@property (Td,N,VvelocityMultiplier) velocityMultiplier;
@property (T@"<_UIFluidSliderDirectDrivingDelegate>",N,W,Vdelegate) delegate;
@property (T@"NSString",N,C) name;
@property (T@"UIView",N,W,Vview) view;
@property (TB,N,Venabled) enabled;
```

## Instance methods

```
-[_UIFluidSliderElasticPanDriver panGestureRecognizer];
-[_UIFluidSliderElasticPanDriver handleGesture:];
-[_UIFluidSliderElasticPanDriver stretchAmount];
-[_UIFluidSliderElasticPanDriver velocityMultiplier];
-[_UIFluidSliderElasticPanDriver setPanGestureRecognizer:];
-[_UIFluidSliderElasticPanDriver drivable];
-[_UIFluidSliderElasticPanDriver setStretchAmount:];
-[_UIFluidSliderElasticPanDriver enabled];
-[_UIFluidSliderElasticPanDriver init];
-[_UIFluidSliderElasticPanDriver stop];
-[_UIFluidSliderElasticPanDriver setView:];
-[_UIFluidSliderElasticPanDriver view];
-[_UIFluidSliderElasticPanDriver setTrackAxis:];
-[_UIFluidSliderElasticPanDriver setDelegate:];
-[_UIFluidSliderElasticPanDriver gestureRecognizerShouldBegin:];
-[_UIFluidSliderElasticPanDriver setEnabled:];
-[_UIFluidSliderElasticPanDriver delegate];
-[_UIFluidSliderElasticPanDriver setName:];
-[_UIFluidSliderElasticPanDriver setVelocityMultiplier:];
-[_UIFluidSliderElasticPanDriver cancel];
-[_UIFluidSliderElasticPanDriver trackAxis];
-[_UIFluidSliderElasticPanDriver name];
-[_UIFluidSliderElasticPanDriver setDrivable:];
```
