# `_UIDeepPressAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"_UIVelocityIntegrator" _touchForceIntegrator;
@"_UIVelocityIntegrator" _locationIntegrator;
```

## Properties

```
@property (T@"_UIVelocityIntegrator",&,N,V_touchForceIntegrator) touchForceIntegrator;
@property (T@"_UIVelocityIntegrator",&,N,V_locationIntegrator) locationIntegrator;
@property (TB,R,N,GisDeepPressLikely) deepPressLikely;
```

## Instance methods

```
-[_UIDeepPressAnalyzer init];
-[_UIDeepPressAnalyzer analyzeTouches:];
-[_UIDeepPressAnalyzer _touchForceFromTouches:];
-[_UIDeepPressAnalyzer analyzeTouchForce:centroidAtLocation:];
-[_UIDeepPressAnalyzer isDeepPressLikely];
-[_UIDeepPressAnalyzer locationIntegrator];
-[_UIDeepPressAnalyzer setLocationIntegrator:];
-[_UIDeepPressAnalyzer setTouchForceIntegrator:];
-[_UIDeepPressAnalyzer touchForceIntegrator];
```
