# `NWAccumulator`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _kvo_lock;
@"NSString" _name;
@"NWAccumulator" _lastSnapshot;
@"NSMutableArray" _accumulatedValues;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSMutableArray",&,N,V_accumulatedValues) accumulatedValues;
@property (T@"NSArray",R,N) accumulations;
@property (T@"NWAccumulator",&,N,V_lastSnapshot) lastSnapshot;
```

## Instance methods

```
-[NWAccumulator addAccumulation:forKey:stateCallback:];
-[NWAccumulator accumulatedValues];
-[NWAccumulator observeValueForKeyPath:ofObject:change:context:];
-[NWAccumulator snapshot];
-[NWAccumulator dealloc];
-[NWAccumulator reset];
-[NWAccumulator lastSnapshot];
-[NWAccumulator setAccumulatedValues:];
-[NWAccumulator accumulations];
-[NWAccumulator description];
-[NWAccumulator setName:];
-[NWAccumulator accumulatedValueForObject:andKeyPath:];
-[NWAccumulator registerObserverForKeyPath:ofObject:alreadyRegistered:];
-[NWAccumulator name];
-[NWAccumulator addAccumulation:withName:forKey:stateCallback:];
-[NWAccumulator setLastSnapshot:];
-[NWAccumulator initWithName:];
-[NWAccumulator dictionaryRepresentation];
```
