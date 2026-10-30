# `SBDynamicMemoryLimitApplicationSceneHostComponent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneComponent`, `SBDynamicMemoryControllingHost`
- 3 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"RBSAssertion" _memoryLimitAssertion;
@"NSString" _domainName;
B _isManagingApplicationSceneAssertion;
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
-[SBDynamicMemoryLimitApplicationSceneHostComponent _acquireAssertionWithName:];
-[SBDynamicMemoryLimitApplicationSceneHostComponent _reconcileApplicationSceneAssertionForForegroundStateChange:upcomingSettingsUpdate:];
-[SBDynamicMemoryLimitApplicationSceneHostComponent setScene:];
-[SBDynamicMemoryLimitApplicationSceneHostComponent scene:willUpdateSettings:];
-[SBDynamicMemoryLimitApplicationSceneHostComponent invalidate];
-[SBDynamicMemoryLimitApplicationSceneHostComponent _invalidateMemoryLimitAssertionForUpcomingSettingsUpdate:];
-[SBDynamicMemoryLimitApplicationSceneHostComponent acquireMemoryLimitAssertionWithName:];
-[SBDynamicMemoryLimitApplicationSceneHostComponent invalidateMemoryLimitAssertion];
```
