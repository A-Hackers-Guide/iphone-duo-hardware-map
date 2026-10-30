# `SBSecureIndicatorMinimumOnTimeCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBSecureIndicatorMinimumOnTimeCoordinatedBlockRegistrationDelegate`
- 4 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"<SBSecureIndicatorMinimumOnTimeProvider>" _minimumOnTimeProvider;
@"NSMutableDictionary" _blockRegistrationsByIndicatorMask;
@"NSMutableDictionary" _minimumOnTimeTimersByIndicatorMask;
@"SBSensorAccessMinimumOnTimeProvider" _secureDisplayProvider;
```

## Properties

```
@property (T@"SBSensorAccessMinimumOnTimeProvider",R,N,V_secureDisplayProvider) secureDisplayProvider;
```

## Instance methods

```
-[SBSecureIndicatorMinimumOnTimeCoordinator init];
-[SBSecureIndicatorMinimumOnTimeCoordinator dealloc];
-[SBSecureIndicatorMinimumOnTimeCoordinator initWithDevicePoseProvider:];
-[SBSecureIndicatorMinimumOnTimeCoordinator initWithMinimumOnTimeProvider:];
-[SBSecureIndicatorMinimumOnTimeCoordinator isMinimumOnTimeSatisfiedForIndicators:];
-[SBSecureIndicatorMinimumOnTimeCoordinator performWhenMinimumOnTimeIsSatisfiedForIndicators:block:];
-[SBSecureIndicatorMinimumOnTimeCoordinator registrationDidInvalidate:];
-[SBSecureIndicatorMinimumOnTimeCoordinator secureDisplayProvider];
-[SBSecureIndicatorMinimumOnTimeCoordinator secureIndicatorTimeToSteadyForLayer:display:];
```
