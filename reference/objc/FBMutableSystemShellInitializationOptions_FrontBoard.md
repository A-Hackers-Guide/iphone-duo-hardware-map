# `FBMutableSystemShellInitializationOptions`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSystemShellInitializationOptions`
- 0 instance variables, 7 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TB,D,N) initializeReadyForInteraction;
@property (TB,D,N) resetDarkBootState;
@property (TB,D,N) shouldWaitForMigrator;
@property (Td,D,N) systemSleepInterval;
@property (T@?,C,D,N) registerAdditionalServicesBlock;
@property (TB,D,N) initializeDisplayManager;
@property (T@"NSString",C,D,N) independentWatchdogPortName;
```

## Instance methods

```
-[FBMutableSystemShellInitializationOptions copyWithZone:];
-[FBMutableSystemShellInitializationOptions setIndependentWatchdogPortName:];
-[FBMutableSystemShellInitializationOptions setInitializeDisplayManager:];
-[FBMutableSystemShellInitializationOptions setInitializeReadyForInteraction:];
-[FBMutableSystemShellInitializationOptions setRegisterAdditionalServicesBlock:];
-[FBMutableSystemShellInitializationOptions setResetDarkBootState:];
-[FBMutableSystemShellInitializationOptions setShouldWaitForMigrator:];
-[FBMutableSystemShellInitializationOptions setSystemSleepInterval:];
```
