# `SBInitialRestartState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 10 instance variables, 14 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isAuthenticated;
B _isInLostMode;
B _isBlocked;
B _hasPasscodeSet;
B _requiresSetup;
B _shouldNeverLock;
B _forSimulator;
B _isLoginSession;
q _homeButtonType;
@"SBBootDefaults" _bootDefaults;
```

## Properties

```
@property (TB,N,GisAuthenticated,V_isAuthenticated) authenticated;
@property (TB,N,GisInLostMode,V_isInLostMode) inLostMode;
@property (TB,N,GisBlocked,V_isBlocked) blocked;
@property (TB,N,V_hasPasscodeSet) hasPasscodeSet;
@property (TB,N,V_requiresSetup) requiresSetup;
@property (TB,N,V_shouldNeverLock) shouldNeverLock;
@property (TB,N,GisLoginSession,V_isLoginSession) loginSession;
@property (T@"SBBootDefaults",&,N,V_bootDefaults) bootDefaults;
@property (TB,N,GisForSimulator,V_forSimulator) forSimulator;
@property (Tq,N,V_homeButtonType) homeButtonType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBInitialRestartState isAuthenticated];
-[SBInitialRestartState isInLostMode];
-[SBInitialRestartState setAuthenticated:];
-[SBInitialRestartState setRequiresSetup:];
-[SBInitialRestartState succinctDescriptionBuilder];
-[SBInitialRestartState bootDefaults];
-[SBInitialRestartState descriptionWithMultilinePrefix:];
-[SBInitialRestartState setBlocked:];
-[SBInitialRestartState succinctDescription];
-[SBInitialRestartState hasPasscodeSet];
-[SBInitialRestartState requiresSetup];
-[SBInitialRestartState homeButtonType];
-[SBInitialRestartState isBlocked];
-[SBInitialRestartState description];
-[SBInitialRestartState setHomeButtonType:];
-[SBInitialRestartState descriptionBuilderWithMultilinePrefix:];
-[SBInitialRestartState isLoginSession];
-[SBInitialRestartState shouldNeverLock];
-[SBInitialRestartState isForSimulator];
-[SBInitialRestartState setBootDefaults:];
-[SBInitialRestartState setForSimulator:];
-[SBInitialRestartState setHasPasscodeSet:];
-[SBInitialRestartState setInLostMode:];
-[SBInitialRestartState setLoginSession:];
-[SBInitialRestartState setShouldNeverLock:];
```
