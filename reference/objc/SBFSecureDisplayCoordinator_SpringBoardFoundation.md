# `SBFSecureDisplayCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSSecureRenderingServiceDelegate`
- 5 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"BKSSecureRenderingService" _secureRenderingService;
@"NSMutableSet" _activatedDisplayUUIDs;
B _activatedNilDisplay;
B _inSecureMode;
@"<SBFSecureRenderingViolationHandling>" _secureRenderingViolationHandler;
```

## Properties

```
@property (TB,N,GinSecureMode,V_inSecureMode) secureMode;
@property (T@"<SBFSecureRenderingViolationHandling>",W,N,V_secureRenderingViolationHandler) secureRenderingViolationHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFSecureDisplayCoordinator init];
-[SBFSecureDisplayCoordinator secureRenderingService:receivedSecureRenderingViolations:];
-[SBFSecureDisplayCoordinator secureRenderingViolationHandler];
-[SBFSecureDisplayCoordinator setSecureMode:postNotification:];
-[SBFSecureDisplayCoordinator _setSecureRenderingEnabled:];
-[SBFSecureDisplayCoordinator activateForDisplayUUID:];
-[SBFSecureDisplayCoordinator inSecureMode];
-[SBFSecureDisplayCoordinator setSecureMode:];
-[SBFSecureDisplayCoordinator setSecureRenderingViolationHandler:];
```
