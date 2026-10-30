# `CBRampProfileSpring`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBRampProfile`
- 5 instance variables, 8 properties, 12 instance methods, 1 class methods

## Instance variables

```
f _normalizer;
f _mass;
f _stiffness;
f _damping;
f _initialVelocity;
```

## Properties

```
@property (Tf,N,V_mass) mass;
@property (Tf,N,V_stiffness) stiffness;
@property (Tf,N,V_damping) damping;
@property (Tf,N,V_initialVelocity) initialVelocity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBRampProfileSpring defaultSpringProfile];
```

## Instance methods

```
-[CBRampProfileSpring setDamping:];
-[CBRampProfileSpring setInitialVelocity:];
-[CBRampProfileSpring setMass:];
-[CBRampProfileSpring init];
-[CBRampProfileSpring damping];
-[CBRampProfileSpring setStiffness:];
-[CBRampProfileSpring initialVelocity];
-[CBRampProfileSpring stiffness];
-[CBRampProfileSpring mass];
-[CBRampProfileSpring _cacheNormalizer];
-[CBRampProfileSpring _springValAtT:];
-[CBRampProfileSpring normalizedOutputForProgress:];
```
