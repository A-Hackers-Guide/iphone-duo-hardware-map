# `SBSceneRelevancyResult`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 6 instance variables, 9 properties, 14 instance methods, 1 class methods

## Instance variables

```
Q _cachedHash;
c _activityMode;
c _jetsamMode;
c _resourceElevation;
B _resignActive;
B _disableFlattening;
```

## Properties

```
@property (Tc,R,N,V_activityMode) activityMode;
@property (Tc,R,N,V_jetsamMode) jetsamMode;
@property (Tc,R,N,V_resourceElevation) resourceElevation;
@property (TB,R,N,V_resignActive) resignActive;
@property (TB,R,N,V_disableFlattening) disableFlattening;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSceneRelevancyResult defaultResult];
```

## Instance methods

```
-[SBSceneRelevancyResult resignActive];
-[SBSceneRelevancyResult succinctDescriptionBuilder];
-[SBSceneRelevancyResult descriptionWithMultilinePrefix:];
-[SBSceneRelevancyResult succinctDescription];
-[SBSceneRelevancyResult disableFlattening];
-[SBSceneRelevancyResult activityMode];
-[SBSceneRelevancyResult hash];
-[SBSceneRelevancyResult description];
-[SBSceneRelevancyResult resourceElevation];
-[SBSceneRelevancyResult isEqual:];
-[SBSceneRelevancyResult descriptionBuilderWithMultilinePrefix:];
-[SBSceneRelevancyResult jetsamMode];
-[SBSceneRelevancyResult hasSameAssertions:];
-[SBSceneRelevancyResult initWithActivityMode:jetsamMode:resourceElevation:resignActive:disableFlattening:];
```
