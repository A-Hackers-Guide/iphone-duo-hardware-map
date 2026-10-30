# `FBSystemShellInitializationOptions`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 7 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _initializeReadyForInteraction;
B _shouldWaitForMigrator;
B _resetDarkBootState;
B _initializeDisplayManager;
@"NSString" _independentWatchdogPortName;
d _systemSleepInterval;
@? _registerServicesBlock;
```

## Properties

```
@property (TB,R,N,V_initializeReadyForInteraction) initializeReadyForInteraction;
@property (TB,R,N,V_resetDarkBootState) resetDarkBootState;
@property (TB,R,N,V_shouldWaitForMigrator) shouldWaitForMigrator;
@property (Td,R,N,V_systemSleepInterval) systemSleepInterval;
@property (T@?,R,C,N,V_registerServicesBlock) registerAdditionalServicesBlock;
@property (TB,R,N,V_initializeDisplayManager) initializeDisplayManager;
@property (T@"NSString",R,C,N,V_independentWatchdogPortName) independentWatchdogPortName;
```

## Instance methods

```
-[FBSystemShellInitializationOptions _initWithOptions:];
-[FBSystemShellInitializationOptions mutableCopyWithZone:];
-[FBSystemShellInitializationOptions init];
-[FBSystemShellInitializationOptions hash];
-[FBSystemShellInitializationOptions copyWithZone:];
-[FBSystemShellInitializationOptions isEqual:];
-[FBSystemShellInitializationOptions registerAdditionalServicesBlock];
-[FBSystemShellInitializationOptions independentWatchdogPortName];
-[FBSystemShellInitializationOptions initializeDisplayManager];
-[FBSystemShellInitializationOptions initializeReadyForInteraction];
-[FBSystemShellInitializationOptions resetDarkBootState];
-[FBSystemShellInitializationOptions shouldWaitForMigrator];
-[FBSystemShellInitializationOptions systemSleepInterval];
```
