# `LACEvaluationEvent`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
q mechanism;
q eventType;
q evaluationMode;
@"<LACEvaluationEventValue>" mutableValue;
```

## Properties

```
@property (Tq,N,R,Vmechanism) mechanism;
@property (Tq,N,R,VeventType) eventType;
@property (Tq,N,R,VevaluationMode) evaluationMode;
@property (T@"<LACEvaluationEventValue>",N,R) value;
@property (T@"<LACEvaluationEventValue>",N,&,VmutableValue) mutableValue;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[LACEvaluationEvent eventType];
-[LACEvaluationEvent evaluationMode];
-[LACEvaluationEvent init];
-[LACEvaluationEvent value];
-[LACEvaluationEvent mechanism];
-[LACEvaluationEvent description];
-[LACEvaluationEvent updateValue:];
-[LACEvaluationEvent initWithMechanism:evaluationMode:eventType:value:];
-[LACEvaluationEvent mutableValue];
-[LACEvaluationEvent setMutableValue:];
-[LACEvaluationEvent uiDelegateEvaluationParametersWithEventProcessing:];
```
