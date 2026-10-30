# `LACDTOPolicyEvaluationController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACDTOPolicyEvaluationController`
- 5 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<LACDTOEnvironmentProviding>" _environment;
@"<LACDTOPolicyEvaluationIdentifierFactory>" _evaluationIdentifierFactory;
@"<LACDTODeviceInfoProvider>" _device;
@"NSHashTable" _observers;
@"NSMutableDictionary" _pendingRequests;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACDTOPolicyEvaluationController processRequest:configuration:completion:];
-[LACDTOPolicyEvaluationController removeObserver:];
-[LACDTOPolicyEvaluationController addObserver:];
-[LACDTOPolicyEvaluationController postProcessRequest:result:completion:];
-[LACDTOPolicyEvaluationController canProcessRequest:];
-[LACDTOPolicyEvaluationController _forEachObserver:];
-[LACDTOPolicyEvaluationController _checkDeviceHasBeenUnlockedSinceBoot];
-[LACDTOPolicyEvaluationController _errorCodesToFilterForOptions:];
-[LACDTOPolicyEvaluationController _evaluateRequest:completion:];
-[LACDTOPolicyEvaluationController _evaluateRequest:environment:completion:];
-[LACDTOPolicyEvaluationController _mapResult:filterCodes:];
-[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:];
-[LACDTOPolicyEvaluationController _notifyObserversAboutEvaluation:result:];
-[LACDTOPolicyEvaluationController _updateEvaluationOptions:forPolicy:environment:];
-[LACDTOPolicyEvaluationController _verifyHasRequiredOptions:forPolicy:error:];
-[LACDTOPolicyEvaluationController initWithEnvironment:evaluationIdentifierFactory:device:];
```
