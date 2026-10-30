# `SBHostedScenePolicyHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`
- 4 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _assertions;
@"NSHashTable" _observers;
@"SBWindowScene" _hostWindowScene;
q _suspensionUnderLockPolicy;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_hostWindowScene) hostWindowScene;
@property (Tq,N,V_suspensionUnderLockPolicy) suspensionUnderLockPolicy;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHostedScenePolicyHostComponent setSuspensionUnderLockPolicy:];
-[SBHostedScenePolicyHostComponent removeObserver:];
-[SBHostedScenePolicyHostComponent setScene:];
-[SBHostedScenePolicyHostComponent hostWindowScene];
-[SBHostedScenePolicyHostComponent scene:willUpdateSettings:];
-[SBHostedScenePolicyHostComponent _assertionStateDidChange:];
-[SBHostedScenePolicyHostComponent addObserver:];
-[SBHostedScenePolicyHostComponent invalidate];
-[SBHostedScenePolicyHostComponent acquireHostingAssertionWithPolicy:reason:];
-[SBHostedScenePolicyHostComponent _notifyObserversOfSuspensionUnderLockPolicyChange];
-[SBHostedScenePolicyHostComponent _notifyObserversOfHostWindowSceneChange];
-[SBHostedScenePolicyHostComponent _updateWindowSceneFromSettings:];
-[SBHostedScenePolicyHostComponent suspensionUnderLockPolicy];
-[SBHostedScenePolicyHostComponent setHostWindowScene:];
```
