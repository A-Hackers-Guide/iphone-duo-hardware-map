# `SBRestToOpenSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
d _restToOpenDuration;
d _freshTouchDisabledRestToOpenDuration;
d _liftFingerCoachingDelay;
```

## Properties

```
@property (Td,V_restToOpenDuration) restToOpenDuration;
@property (Td,V_freshTouchDisabledRestToOpenDuration) freshTouchDisabledRestToOpenDuration;
@property (Td,V_liftFingerCoachingDelay) liftFingerCoachingDelay;
```

## Class methods

```
+[SBRestToOpenSettings settingsControllerModule];
```

## Instance methods

```
-[SBRestToOpenSettings setDefaultValues];
-[SBRestToOpenSettings freshTouchDisabledRestToOpenDuration];
-[SBRestToOpenSettings liftFingerCoachingDelay];
-[SBRestToOpenSettings restToOpenDuration];
-[SBRestToOpenSettings setFreshTouchDisabledRestToOpenDuration:];
-[SBRestToOpenSettings setLiftFingerCoachingDelay:];
-[SBRestToOpenSettings setRestToOpenDuration:];
```
