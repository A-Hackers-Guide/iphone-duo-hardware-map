# `UICubicTimingParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITimingCurveProvider`
- 4 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
q _timingCurveType;
@"_UIViewCubicTimingFunction" _timingFunction;
q _animationCurve;
@"UISpringTimingParameters" _springTimingParameters;
```

## Properties

```
@property (T@"_UIViewCubicTimingFunction",R,N,V_timingFunction) timingFunction;
@property (T@"UISpringTimingParameters",&,N,V_springTimingParameters) springTimingParameters;
@property (Tq,R,N,V_animationCurve) animationCurve;
@property (T{CGPoint=dd},R,N) controlPoint1;
@property (T{CGPoint=dd},R,N) controlPoint2;
@property (Tq,R,N,V_timingCurveType) timingCurveType;
@property (T@"UICubicTimingParameters",R,N) cubicTimingParameters;
```

## Instance methods

```
-[UICubicTimingParameters controlPoint2];
-[UICubicTimingParameters animationCurve];
-[UICubicTimingParameters init];
-[UICubicTimingParameters cubicTimingParameters];
-[UICubicTimingParameters timingFunction];
-[UICubicTimingParameters timingCurveType];
-[UICubicTimingParameters _setAnimationCurve:];
-[UICubicTimingParameters _mediaTimingFunction];
-[UICubicTimingParameters initWithAnimationCurve:];
-[UICubicTimingParameters encodeWithCoder:];
-[UICubicTimingParameters initWithCustomCurve:];
-[UICubicTimingParameters controlPoint1];
-[UICubicTimingParameters description];
-[UICubicTimingParameters initWithCoder:];
-[UICubicTimingParameters initWithControlPoint1:controlPoint2:];
-[UICubicTimingParameters copyWithZone:];
-[UICubicTimingParameters isEqual:];
-[UICubicTimingParameters springTimingParameters];
-[UICubicTimingParameters effectiveTimingFunction];
-[UICubicTimingParameters setSpringTimingParameters:];
```
