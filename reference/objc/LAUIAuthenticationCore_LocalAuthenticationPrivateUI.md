# `LAUIAuthenticationCore`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LAUIDelegate`, `LAUIAuthentication`
- 16 instance variables, 10 properties, 43 instance methods, 1 class methods

## Instance variables

```
B _doneMatching;
B _doneWatch;
B _usesInternalContext;
B _mirroringToDefaultUI;
q _lastState;
B _supportsConcurrentEvaluations;
B _applicationActive;
B _keyWindow;
B _uiActive;
@"NSObject<LAUIAuthenticationCoreDelegate>" _delegate;
@"UIView" _view;
q _biometryType;
Q _enabledMechanisms;
Q _activeMechanisms;
@"LAContext" _context;
@"NSDictionary" _faceIdResult;
```

## Properties

```
@property (TQ,N,V_enabledMechanisms) enabledMechanisms;
@property (TQ,N,V_activeMechanisms) activeMechanisms;
@property (TB,N,GisApplicationActive,V_applicationActive) applicationActive;
@property (TB,N,GisKeyWindow,V_keyWindow) keyWindow;
@property (TB,N,GisUiActive,V_uiActive) uiActive;
@property (T@"LAContext",&,N,V_context) context;
@property (T@"NSDictionary",R,N,V_faceIdResult) faceIdResult;
@property (T@"NSObject<LAUIAuthenticationCoreDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",W,N,V_view) view;
@property (Tq,R,N,V_biometryType) biometryType;
```

## Class methods

```
+[LAUIAuthenticationCore performBlockOnMainThread:];
```

## Instance methods

```
-[LAUIAuthenticationCore isApplicationActive];
-[LAUIAuthenticationCore setView:];
-[LAUIAuthenticationCore view];
-[LAUIAuthenticationCore setDelegate:];
-[LAUIAuthenticationCore setContext:];
-[LAUIAuthenticationCore delegate];
-[LAUIAuthenticationCore biometryType];
-[LAUIAuthenticationCore context];
-[LAUIAuthenticationCore setApplicationActive:];
-[LAUIAuthenticationCore isKeyWindow];
-[LAUIAuthenticationCore _notification:];
-[LAUIAuthenticationCore disableMechanism:error:];
-[LAUIAuthenticationCore enableMechanism:error:];
-[LAUIAuthenticationCore isMechanismEnabled:];
-[LAUIAuthenticationCore event:params:reply:];
-[LAUIAuthenticationCore checkView];
-[LAUIAuthenticationCore activeMechanisms];
-[LAUIAuthenticationCore setActiveMechanisms:];
-[LAUIAuthenticationCore startOrStopBackgroundMechanisms];
-[LAUIAuthenticationCore _biometryState:];
-[LAUIAuthenticationCore _biometricNoMatchWithBiolockoutError:];
-[LAUIAuthenticationCore _enableAvailableMechanisms:];
-[LAUIAuthenticationCore _handleBackgroundMechanismsResult:error:context:];
-[LAUIAuthenticationCore _mechanism:enable:error:];
-[LAUIAuthenticationCore _optionsForBackgroundMechanism];
-[LAUIAuthenticationCore _policyForBackgroundMechanisms];
-[LAUIAuthenticationCore _processActivityChangeForNotification:block:];
-[LAUIAuthenticationCore _setupMechanisms:];
-[LAUIAuthenticationCore _setupNotifications:];
-[LAUIAuthenticationCore _simpleStatusInParams:touchId:faceId:];
-[LAUIAuthenticationCore _startBackgroundMechanisms];
-[LAUIAuthenticationCore _stopBackgroundMechanisms];
-[LAUIAuthenticationCore enabledMechanisms];
-[LAUIAuthenticationCore faceIdResult];
-[LAUIAuthenticationCore initWithMechanisms:];
-[LAUIAuthenticationCore initWithMechanisms:context:];
-[LAUIAuthenticationCore isMechanismActive:];
-[LAUIAuthenticationCore isMechanismAvailable:error:];
-[LAUIAuthenticationCore isUiActive];
-[LAUIAuthenticationCore notificationNames];
-[LAUIAuthenticationCore setEnabledMechanisms:];
-[LAUIAuthenticationCore setKeyWindow:];
-[LAUIAuthenticationCore setUiActive:];
```
