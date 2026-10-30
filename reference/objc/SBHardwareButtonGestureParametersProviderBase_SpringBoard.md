# `SBHardwareButtonGestureParametersProviderBase`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHardwareButtonGestureParametersProvider`, `BSDescriptionProviding`
- 1 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _observers;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_observers) observers;
@property (T@"SBHardwareButtonGestureParameters",R,N) hardwareButtonGestureParameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHardwareButtonGestureParametersProviderBase succinctDescriptionBuilder];
-[SBHardwareButtonGestureParametersProviderBase descriptionWithMultilinePrefix:];
-[SBHardwareButtonGestureParametersProviderBase hardwareButtonGestureParameters];
-[SBHardwareButtonGestureParametersProviderBase succinctDescription];
-[SBHardwareButtonGestureParametersProviderBase description];
-[SBHardwareButtonGestureParametersProviderBase setObservers:];
-[SBHardwareButtonGestureParametersProviderBase observers];
-[SBHardwareButtonGestureParametersProviderBase descriptionBuilderWithMultilinePrefix:];
-[SBHardwareButtonGestureParametersProviderBase addHardwareButtonGestureParametersObserver:];
-[SBHardwareButtonGestureParametersProviderBase publishUpdatedParameters:];
-[SBHardwareButtonGestureParametersProviderBase removeHardwareButtonGestureParametersObserver:];
```
