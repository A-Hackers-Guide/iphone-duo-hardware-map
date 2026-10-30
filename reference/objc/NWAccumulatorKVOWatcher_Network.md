# `NWAccumulatorKVOWatcher`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSString" _state;
@"NSString" _name;
@"NSObject" _object;
@"NSString" _keyPath;
@? _callback;
```

## Properties

```
@property (T@"NSString",&,V_state) state;
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSObject",&,N,V_object) object;
@property (T@"NSString",&,N,V_keyPath) keyPath;
@property (T@?,C,N,V_callback) callback;
```

## Instance methods

```
-[NWAccumulatorKVOWatcher keyPath];
-[NWAccumulatorKVOWatcher setKeyPath:];
-[NWAccumulatorKVOWatcher callback];
-[NWAccumulatorKVOWatcher setCallback:];
-[NWAccumulatorKVOWatcher setState:];
-[NWAccumulatorKVOWatcher init];
-[NWAccumulatorKVOWatcher setObject:];
-[NWAccumulatorKVOWatcher description];
-[NWAccumulatorKVOWatcher setName:];
-[NWAccumulatorKVOWatcher object];
-[NWAccumulatorKVOWatcher name];
-[NWAccumulatorKVOWatcher state];
-[NWAccumulatorKVOWatcher updateWithState:];
```
