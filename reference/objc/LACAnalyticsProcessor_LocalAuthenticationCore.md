# `LACAnalyticsProcessor`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACEvaluationRequestProcessor`
- 2 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"LACAnalyticsSession" _analyticsSession;
@"NSObject<OS_dispatch_queue>" _workQueue;
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
-[LACAnalyticsProcessor processRequest:configuration:completion:];
-[LACAnalyticsProcessor postProcessRequest:result:completion:];
-[LACAnalyticsProcessor canProcessRequest:];
-[LACAnalyticsProcessor _donateDialogEvent:request:];
-[LACAnalyticsProcessor initWithAnalyticsSession:];
```
