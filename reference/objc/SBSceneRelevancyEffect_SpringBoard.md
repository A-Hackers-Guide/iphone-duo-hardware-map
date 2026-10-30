# `SBSceneRelevancyEffect`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 1 class methods

## Instance variables

```
c _jetsamMode;
c _resourceElevation;
c _activityMode;
B _resignActive;
B _freeze;
@"NSString" _flattenMode;
```

## Properties

```
@property (T@"NSString",R,C,N,V_flattenMode) flattenMode;
@property (Tc,R,N,V_jetsamMode) jetsamMode;
@property (Tc,R,N,V_resourceElevation) resourceElevation;
@property (Tc,R,N,V_activityMode) activityMode;
@property (TB,R,N,V_resignActive) resignActive;
@property (TB,R,N,V_freeze) freeze;
```

## Class methods

```
+[SBSceneRelevancyEffect effectWithFlattenMode:jetsamMode:resourceElevation:activityMode:resignActive:freeze:];
```

## Instance methods

```
-[SBSceneRelevancyEffect resignActive];
-[SBSceneRelevancyEffect activityMode];
-[SBSceneRelevancyEffect freeze];
-[SBSceneRelevancyEffect resourceElevation];
-[SBSceneRelevancyEffect flattenMode];
-[SBSceneRelevancyEffect jetsamMode];
-[SBSceneRelevancyEffect initWithFlattenMode:jetsamMode:resourceElevation:activityMode:resignActive:freeze:];
```
