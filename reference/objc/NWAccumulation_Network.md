# `NWAccumulation`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _isSnapshot;
@"NSString" _name;
@"NSMutableDictionary" _durations;
@"NSString" _currentState;
d _lastUpdateTime;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSMutableDictionary",&,N,V_durations) durations;
@property (T@"NSString",&,N,V_currentState) currentState;
@property (Td,N,V_lastUpdateTime) lastUpdateTime;
@property (TB,N,V_isSnapshot) isSnapshot;
```

## Instance methods

```
-[NWAccumulation lastUpdateTime];
-[NWAccumulation isSnapshot];
-[NWAccumulation snapshot];
-[NWAccumulation setLastUpdateTime:];
-[NWAccumulation dealloc];
-[NWAccumulation setIsSnapshot:];
-[NWAccumulation reset];
-[NWAccumulation setCurrentState:];
-[NWAccumulation updateWithState:atTime:];
-[NWAccumulation setDurations:];
-[NWAccumulation description];
-[NWAccumulation durations];
-[NWAccumulation setName:];
-[NWAccumulation currentState];
-[NWAccumulation name];
-[NWAccumulation initWithName:];
```
