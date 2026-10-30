# `_UIKBRTDecayingObject`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _resetBlocks;
B _isDecaying;
B _isHolding;
d _lastUpdate;
d _timeoutDuration;
```

## Properties

```
@property (Td,R,N,V_lastUpdate) lastUpdate;
@property (Td,N,V_timeoutDuration) timeoutDuration;
@property (TB,R,N,V_isDecaying) isDecaying;
@property (TB,R,N,V_isHolding) isHolding;
@property (TB,R,N) isActive;
```

## Instance methods

```
-[_UIKBRTDecayingObject reset];
-[_UIKBRTDecayingObject lastUpdate];
-[_UIKBRTDecayingObject isActive];
-[_UIKBRTDecayingObject timeoutDuration];
-[_UIKBRTDecayingObject initWithTimeoutDuration:];
-[_UIKBRTDecayingObject isDecaying];
-[_UIKBRTDecayingObject isHolding];
-[_UIKBRTDecayingObject onResetDo:];
-[_UIKBRTDecayingObject resetActiveDecayTo:];
-[_UIKBRTDecayingObject resetDecayTo:];
-[_UIKBRTDecayingObject setTimeoutDuration:];
-[_UIKBRTDecayingObject startDecaying];
-[_UIKBRTDecayingObject startOrUpdateDecay];
-[_UIKBRTDecayingObject updateDecay];
```
