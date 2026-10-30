# `UISpringTimingParameters`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `UITimingCurveProvider`
- 6 instance variables, 10 properties, 32 instance methods, 4 class methods

## Instance variables

```
B _implicitDuration;
d _dampingRatio;
d _mass;
d _stiffness;
d _damping;
{CGVector="dx"d"dy"d} _initialVelocity;
```

## Properties

```
@property (Td,R,N,V_dampingRatio) dampingRatio;
@property (TB,N,V_implicitDuration) implicitDuration;
@property (Td,N,V_mass) mass;
@property (Td,N,V_stiffness) stiffness;
@property (Td,N,V_damping) damping;
@property (Td,R,N) settlingDuration;
@property (T{CGVector=dd},R,N,V_initialVelocity) initialVelocity;
@property (Tq,R,N) timingCurveType;
@property (T@"UICubicTimingParameters",R,N) cubicTimingParameters;
@property (T@"UISpringTimingParameters",R,N) springTimingParameters;
```

## Class methods

```
+[UISpringTimingParameters supportsSecureCoding];
+[UISpringTimingParameters _convertDampingRatio:response:toMass:stiffness:damping:];
+[UISpringTimingParameters _convertBounce:toDampingRatio:];
+[UISpringTimingParameters _convertMass:stiffness:damping:toDampingRatio:response:];
```

## Instance methods

```
-[UISpringTimingParameters initWithDampingRatio:response:];
-[UISpringTimingParameters setDamping:];
-[UISpringTimingParameters initWithParameters:];
-[UISpringTimingParameters implicitDuration];
-[UISpringTimingParameters setMass:];
-[UISpringTimingParameters init];
-[UISpringTimingParameters cubicTimingParameters];
-[UISpringTimingParameters damping];
-[UISpringTimingParameters dampingRatio];
-[UISpringTimingParameters setStiffness:];
-[UISpringTimingParameters initWithParameters:initialVelocity:];
-[UISpringTimingParameters initWithMass:stiffness:damping:initialVelocity:];
-[UISpringTimingParameters setImplicitDuration:];
-[UISpringTimingParameters timingCurveType];
-[UISpringTimingParameters initialVelocity];
-[UISpringTimingParameters stiffness];
-[UISpringTimingParameters _mediaTimingFunction];
-[UISpringTimingParameters settlingDuration];
-[UISpringTimingParameters encodeWithCoder:];
-[UISpringTimingParameters initWithDuration:bounce:initialVelocity:];
-[UISpringTimingParameters initWithDampingRatio:initialVelocity:];
-[UISpringTimingParameters description];
-[UISpringTimingParameters initWithCoder:];
-[UISpringTimingParameters initWithDampingRatio:response:initialVelocity:];
-[UISpringTimingParameters mass];
-[UISpringTimingParameters initWithDuration:bounce:];
-[UISpringTimingParameters copyWithZone:];
-[UISpringTimingParameters isEqual:];
-[UISpringTimingParameters springTimingParameters];
-[UISpringTimingParameters effectiveTimingFunction];
-[UISpringTimingParameters initWithVelocity:];
-[UISpringTimingParameters initWithDampingRatio:];
```
