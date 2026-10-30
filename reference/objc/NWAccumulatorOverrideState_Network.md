# `NWAccumulatorOverrideState`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSString" _state;
@"NSString" _name;
```

## Properties

```
@property (T@"NSString",&,N,V_state) state;
@property (T@"NSString",&,N,V_name) name;
```

## Instance methods

```
-[NWAccumulatorOverrideState setState:];
-[NWAccumulatorOverrideState init];
-[NWAccumulatorOverrideState description];
-[NWAccumulatorOverrideState setName:];
-[NWAccumulatorOverrideState name];
-[NWAccumulatorOverrideState state];
-[NWAccumulatorOverrideState updateWithState:];
```
