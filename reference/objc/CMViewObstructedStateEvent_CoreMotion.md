# `CMViewObstructedStateEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _shouldSuppress;
C _currentState;
f _lux;
f _pocketProbability;
@"NSString" _orientation;
@"NSString" _motionType;
@"NSArray" _meanProbabilities;
```

## Properties

```
@property (TB,N,V_shouldSuppress) shouldSuppress;
@property (TC,N,V_currentState) currentState;
@property (T@"NSString",C,N,V_orientation) orientation;
@property (T@"NSString",C,N,V_motionType) motionType;
@property (Tf,N,V_lux) lux;
@property (Tf,N,V_pocketProbability) pocketProbability;
@property (T@"NSArray",&,N,V_meanProbabilities) meanProbabilities;
```

## Instance methods

```
-[CMViewObstructedStateEvent setOrientation:];
-[CMViewObstructedStateEvent setMotionType:];
-[CMViewObstructedStateEvent orientation];
-[CMViewObstructedStateEvent dealloc];
-[CMViewObstructedStateEvent motionType];
-[CMViewObstructedStateEvent setLux:];
-[CMViewObstructedStateEvent setCurrentState:];
-[CMViewObstructedStateEvent description];
-[CMViewObstructedStateEvent lux];
-[CMViewObstructedStateEvent currentState];
-[CMViewObstructedStateEvent initWithShouldSupress:currentState:orientation:motionType:lux:pocketProbability:meanProbabilitiesFloatArray:];
-[CMViewObstructedStateEvent meanProbabilities];
-[CMViewObstructedStateEvent pocketProbability];
-[CMViewObstructedStateEvent setMeanProbabilities:];
-[CMViewObstructedStateEvent setPocketProbability:];
-[CMViewObstructedStateEvent setShouldSuppress:];
-[CMViewObstructedStateEvent shouldSuppress];
```
