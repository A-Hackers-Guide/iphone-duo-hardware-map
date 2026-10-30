# `LACCompanionAuthenticationController`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACCompanionAuthenticationSessionMonitorObserver`, `LACCompanionAuthenticationControlling`, `LACEvaluationRequestProcessor`, `LACDomainStateProviding`
- 6 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<LACCompanionAuthenticationCoordinating>" authenticator;
@"<LACCompanionAuthenticationEnvironmentProviding>" environmentProvider;
@"<LACCompanionAuthenticationSessionMonitoring>" sessionMonitor;
@"OS_dispatch_queue" replyQueue;
q companion;
pendingRequests;
```

## Properties

```
@property (T@"<LACCompanionAuthenticationCoordinating>",N,R,Vauthenticator) authenticator;
@property (T@"<LACCompanionAuthenticationEnvironmentProviding>",N,R,VenvironmentProvider) environmentProvider;
@property (T@"<LACCompanionAuthenticationSessionMonitoring>",N,R,VsessionMonitor) sessionMonitor;
@property (T@"OS_dispatch_queue",N,R,VreplyQueue) replyQueue;
@property (Tq,N,R,Vcompanion) companion;
@property (TB,N,R) isFeatureSupported;
@property (TB,N,R) isSessionActive;
```

## Instance methods

```
-[LACCompanionAuthenticationController canAuthenticateRequest:availabilityError:error:];
-[LACCompanionAuthenticationController companion];
-[LACCompanionAuthenticationController isSessionActive];
-[LACCompanionAuthenticationController processRequest:configuration:completion:];
-[LACCompanionAuthenticationController init];
-[LACCompanionAuthenticationController cancelAllRequests];
-[LACCompanionAuthenticationController sessionMonitor];
-[LACCompanionAuthenticationController isFeatureSupported];
-[LACCompanionAuthenticationController replyQueue];
-[LACCompanionAuthenticationController initWithAuthenticator:environmentProvider:sessionMonitor:replyQueue:];
-[LACCompanionAuthenticationController postProcessRequest:result:completion:];
-[LACCompanionAuthenticationController canProcessRequest:];
-[LACCompanionAuthenticationController mapError:];
-[LACCompanionAuthenticationController authenticator];
-[LACCompanionAuthenticationController cancelRequestsForContextID:];
-[LACCompanionAuthenticationController companionAuthenticationSessionMonitorDidUpdate:];
-[LACCompanionAuthenticationController domainStateForRequest:completion:];
-[LACCompanionAuthenticationController environmentProvider];
```
