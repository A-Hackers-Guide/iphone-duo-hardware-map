# `BLSHBacklightAggregateState`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightTransitionStateMachineState`
- 2 instance variables, 7 properties, 11 instance methods, 5 class methods

## Instance variables

```
@"BLSHBacklightDisplayStateMachine" _displayModeSource;
@"BLSHBacklightEnvironmentStateMachine" _presentationSource;
```

## Properties

```
@property (T@"BLSHBacklightEnvironmentStateMachine",&,V_presentationSource) presentationSource;
@property (Tq,R) displayMode;
@property (T@"BLSHBacklightEnvironmentPresentation",R) presentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHBacklightAggregateState bls_shortLoggingStringForState:];
+[BLSHBacklightAggregateState bls_debugLoggingDescriptionForState:];
+[BLSHBacklightAggregateState bls_loggingStringForState:];
+[BLSHBacklightAggregateState isState:equalToObject:];
+[BLSHBacklightAggregateState stateHash:];
```

## Instance methods

```
-[BLSHBacklightAggregateState bls_loggingString];
-[BLSHBacklightAggregateState presentation];
-[BLSHBacklightAggregateState bls_shortLoggingString];
-[BLSHBacklightAggregateState debugDescription];
-[BLSHBacklightAggregateState presentationSource];
-[BLSHBacklightAggregateState setPresentationSource:];
-[BLSHBacklightAggregateState displayMode];
-[BLSHBacklightAggregateState hash];
-[BLSHBacklightAggregateState description];
-[BLSHBacklightAggregateState isEqual:];
-[BLSHBacklightAggregateState initWithDisplayModeSource:];
```
