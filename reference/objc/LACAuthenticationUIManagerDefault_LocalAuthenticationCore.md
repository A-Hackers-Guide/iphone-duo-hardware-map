# `LACAuthenticationUIManagerDefault`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACAuthenticationUIManaging`, `LACEvaluationEventHandling`, `LACRemoteUIHost`, `LACUIMechanism`
- 15 instance variables, 15 properties, 37 instance methods, 0 class methods

## Instance variables

```
I instanceId;
@"<LACEvaluationRequest>" request;
q type;
? authenticationHints;
? uiEventDelegate;
? anonymousListeners;
? activeMechanisms;
B isActive;
@"<LACAuthenticationUINotifying>" notificationCenter;
presentedController;
@"<LACRemoteUI>" remoteUI;
@"<LACRemoteUIManaging>" remoteUIManager;
B uiDisappeared;
B ignoreUIDisappearance;
B uiTransitioning;
```

## Properties

```
@property (TI,N,R,VinstanceId) instanceId;
@property (TB,N,R) isRunning;
@property (T@"<LACEvaluationRequest>",N,R,Vrequest) request;
@property (Tq,N,R,Vtype) type;
@property (T@"NSDictionary",N,C) authenticationHints;
@property (T@"<LACAuthenticationUIProxy>",N,W,VuiEventDelegate) uiEventDelegate;
@property (T@"NSArray",N,C) anonymousListeners;
@property (T@"NSSet",N,C) activeMechanisms;
@property (TB,N,VisActive) isActive;
@property (T@"<LACAuthenticationUINotifying>",N,&,VnotificationCenter) notificationCenter;
@property (T@"<LACRemoteUI>",N,&,VremoteUI) remoteUI;
@property (T@"<LACRemoteUIManaging>",N,R,VremoteUIManager) remoteUIManager;
@property (TB,N,VuiDisappeared) uiDisappeared;
@property (TB,N,VignoreUIDisappearance) ignoreUIDisappearance;
@property (TB,N,VuiTransitioning) uiTransitioning;
```

## Instance methods

```
-[LACAuthenticationUIManagerDefault setIsActive:];
-[LACAuthenticationUIManagerDefault isRunning];
-[LACAuthenticationUIManagerDefault notificationCenter];
-[LACAuthenticationUIManagerDefault setNotificationCenter:];
-[LACAuthenticationUIManagerDefault init];
-[LACAuthenticationUIManagerDefault dealloc];
-[LACAuthenticationUIManagerDefault request];
-[LACAuthenticationUIManagerDefault instanceId];
-[LACAuthenticationUIManagerDefault type];
-[LACAuthenticationUIManagerDefault isActive];
-[LACAuthenticationUIManagerDefault remoteUIManager];
-[LACAuthenticationUIManagerDefault uiTransitioning];
-[LACAuthenticationUIManagerDefault uiEventDelegate];
-[LACAuthenticationUIManagerDefault activeMechanisms];
-[LACAuthenticationUIManagerDefault anonymousListeners];
-[LACAuthenticationUIManagerDefault authenticationHints];
-[LACAuthenticationUIManagerDefault checkHasPendingUIRequestsForRemoteUI:completion:];
-[LACAuthenticationUIManagerDefault connectRemoteUI:requestID:reply:];
-[LACAuthenticationUIManagerDefault disconnectRemoteUI];
-[LACAuthenticationUIManagerDefault failAuthenticationWithError:];
-[LACAuthenticationUIManagerDefault handleEvaluationEvent:completion:];
-[LACAuthenticationUIManagerDefault ignoreUIDisappearance];
-[LACAuthenticationUIManagerDefault initWithRequest:remoteUIManager:];
-[LACAuthenticationUIManagerDefault internalInfoWithReply:];
-[LACAuthenticationUIManagerDefault remoteUI];
-[LACAuthenticationUIManagerDefault setActiveMechanisms:];
-[LACAuthenticationUIManagerDefault setAnonymousListeners:];
-[LACAuthenticationUIManagerDefault setAuthenticationHints:];
-[LACAuthenticationUIManagerDefault setIgnoreUIDisappearance:];
-[LACAuthenticationUIManagerDefault setRemoteUI:];
-[LACAuthenticationUIManagerDefault setUiDisappeared:];
-[LACAuthenticationUIManagerDefault setUiEventDelegate:];
-[LACAuthenticationUIManagerDefault setUiTransitioning:];
-[LACAuthenticationUIManagerDefault uiDisappeared];
-[LACAuthenticationUIManagerDefault uiEvent:options:];
-[LACAuthenticationUIManagerDefault uiFailureWithError:];
-[LACAuthenticationUIManagerDefault uiSuccessWithResult:];
```
