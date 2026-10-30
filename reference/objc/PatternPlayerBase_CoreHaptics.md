# `PatternPlayerBase`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PatternPlayerDetails`
- 6 instance variables, 3 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"CHHapticEngine" _engine;
@"NSArray" _events;
@"NSString" _patternID;
d _patternDuration;
{atomic<MuteState>="__a_"{__cxx_atomic_impl<MuteState, std::__cxx_atomic_base_impl<MuteState>>="__a_value"Ai}} _muteState;
C _previousAction;
```

## Properties

```
@property (T@"CHHapticEngine",W,V_engine) engine;
@property (T@"NSString",R,V_patternID) patternID;
@property (Td,R,V_patternDuration) patternDuration;
```

## Instance methods

```
-[PatternPlayerBase needsResetForAction:];
-[PatternPlayerBase setEngine:];
-[PatternPlayerBase engine];
-[PatternPlayerBase patternDuration];
-[PatternPlayerBase patternID];
```
