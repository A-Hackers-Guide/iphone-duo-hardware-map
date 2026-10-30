# `LAAuthenticationBiometricMethod`

- Image: [`/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`](../userland/System__Library__Frameworks__LocalAuthentication.framework__LocalAuthentication.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `LAAuthenticationMethod`
- Protocols: `LAUIDelegate`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isDevicePresent;
B _isEnrolled;
B _isAllowed;
@"LAContext" _context;
@"LAAuthenticationBiometricMethodState" _currentState;
```

## Properties

```
@property (T@"LAContext",R,N,V_context) context;
@property (T@"LAAuthenticationBiometricMethodState",&,N,V_currentState) currentState;
@property (TB,R,N,V_isDevicePresent) isDevicePresent;
@property (TB,R,N,V_isEnrolled) isEnrolled;
@property (TB,R,N,V_isAllowed) isAllowed;
```

## Instance methods

```
-[LAAuthenticationBiometricMethod terminate];
-[LAAuthenticationBiometricMethod start];
-[LAAuthenticationBiometricMethod initWithConfiguration:];
-[LAAuthenticationBiometricMethod setCurrentState:];
-[LAAuthenticationBiometricMethod isAllowed];
-[LAAuthenticationBiometricMethod context];
-[LAAuthenticationBiometricMethod currentState];
-[LAAuthenticationBiometricMethod isEnrolled];
-[LAAuthenticationBiometricMethod event:params:reply:];
-[LAAuthenticationBiometricMethod isDevicePresent];
-[LAAuthenticationBiometricMethod distributeBiometricFeedback:];
-[LAAuthenticationBiometricMethod distributeStateChange];
-[LAAuthenticationBiometricMethod lockoutStateFromError:];
-[LAAuthenticationBiometricMethod runBiometricOperation];
```
