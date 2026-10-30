# `SBBootDefaults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractSpringBoardDefaultDomain`
- 0 instance variables, 8 properties, 1 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",&,D,N) lastSystemBuildVersion;
@property (T@"NSString",&,D,N) lastRestoreIdentifier;
@property (TB,D,N) hasCompletedSynchronizingCloudCriticalData;
@property (T@"NSDictionary",D,N) bootTransitionContext;
@property (T@"NSData",&,D,N) lastActiveLockPoster;
@property (T@"NSData",&,D,N) lastActiveHomePoster;
@property (TB,R,D,N) dontLockAfterCrash;
@property (TB,R,D,N) recordBootTimeUntilStartupComplete;
```

## Instance methods

```
-[SBBootDefaults _bindAndRegisterDefaults];
```
