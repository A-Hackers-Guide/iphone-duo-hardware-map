# `LACDTOPolicyProcessorEmptyPasscode`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEvaluationRequestProcessor`
- 2 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"<LACCredentialStore>" _store;
@"<LACDTODeviceInfoProvider>" _device;
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
-[LACDTOPolicyProcessorEmptyPasscode processRequest:configuration:completion:];
-[LACDTOPolicyProcessorEmptyPasscode canProcessRequest:];
-[LACDTOPolicyProcessorEmptyPasscode initWithCredentialStore:device:];
-[LACDTOPolicyProcessorEmptyPasscode _processAndEvaluateRequest:completion:];
```
