# `LAUIAuthenticationView`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `LAUIAuthenticationCoreDelegate`, `LAUIAuthentication`
- 8 instance variables, 11 properties, 38 instance methods, 1 class methods

## Instance variables

```
q _lastState;
B _idleWhenDone;
B _fastAnimations;
@"<LAUIAuthenticationDelegate>" _delegate;
q _glyphStyle;
q _style;
@"LAUIAuthenticationCore" _authenticationCore;
@"LAUIPKGlyphWrapper" _glyphWrapper;
```

## Properties

```
@property (T@"LAUIAuthenticationCore",R,N,V_authenticationCore) authenticationCore;
@property (T@"LAUIPKGlyphWrapper",R,N,V_glyphWrapper) glyphWrapper;
@property (T@"<LAUIAuthenticationDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_glyphStyle) glyphStyle;
@property (Tq,N,V_style) style;
@property (TB,N,V_idleWhenDone) idleWhenDone;
@property (TB,N,V_fastAnimations) fastAnimations;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LAUIAuthenticationView defaultRect];
```

## Instance methods

```
-[LAUIAuthenticationView localizedCallerName];
-[LAUIAuthenticationView callerIconBundlePath];
-[LAUIAuthenticationView didMoveToWindow];
-[LAUIAuthenticationView willMoveToSuperview:];
-[LAUIAuthenticationView style];
-[LAUIAuthenticationView setStyle:];
-[LAUIAuthenticationView setDelegate:];
-[LAUIAuthenticationView delegate];
-[LAUIAuthenticationView initWithCoder:];
-[LAUIAuthenticationView didMoveToSuperview];
-[LAUIAuthenticationView initWithFrame:];
-[LAUIAuthenticationView _setupView];
-[LAUIAuthenticationView authenticationResult:error:context:];
-[LAUIAuthenticationView biometricNoMatch];
-[LAUIAuthenticationView callerIconPath];
-[LAUIAuthenticationView disableMechanism:error:];
-[LAUIAuthenticationView enableMechanism:error:];
-[LAUIAuthenticationView initWithFrame:mechanisms:];
-[LAUIAuthenticationView isMechanismEnabled:];
-[LAUIAuthenticationView setFastAnimations:];
-[LAUIAuthenticationView _stateOfSuccess];
-[LAUIAuthenticationView _biometryIdle];
-[LAUIAuthenticationView _setupMechanisms:context:];
-[LAUIAuthenticationView authenticationCore];
-[LAUIAuthenticationView biometryState:completionHandler:];
-[LAUIAuthenticationView fastAnimations];
-[LAUIAuthenticationView glyphStyle];
-[LAUIAuthenticationView glyphWrapper];
-[LAUIAuthenticationView idleWhenDone];
-[LAUIAuthenticationView initWithFrame:mechanisms:context:];
-[LAUIAuthenticationView initWithMechanisms:];
-[LAUIAuthenticationView initWithMechanisms:context:];
-[LAUIAuthenticationView isMechanismActive:];
-[LAUIAuthenticationView isMechanismAvailable:error:];
-[LAUIAuthenticationView notification:original:mechanism:];
-[LAUIAuthenticationView setGlyphStyle:];
-[LAUIAuthenticationView setIdleWhenDone:];
-[LAUIAuthenticationView tappedFaceID:];
```
