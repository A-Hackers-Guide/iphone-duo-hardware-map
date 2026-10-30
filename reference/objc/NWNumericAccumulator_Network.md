# `NWNumericAccumulator`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _kvo_lock;
@"NSString" _name;
@"NSMutableDictionary" _accumulations;
@"NSMutableArray" _kvoWatchers;
@"NSMutableArray" _overriddenStates;
```

## Properties

```
@property (T@"NSString",&,N,V_name) name;
@property (T@"NSMutableArray",&,N,V_kvoWatchers) kvoWatchers;
@property (T@"NSMutableArray",&,N,V_overriddenStates) overriddenStates;
@property (T@"NSMutableDictionary",&,N,V_accumulations) accumulations;
```

## Instance methods

```
-[NWNumericAccumulator addCount:toAccumulation:];
-[NWNumericAccumulator addAccumulation:forKey:stateCallback:];
-[NWNumericAccumulator observeValueForKeyPath:ofObject:change:context:];
-[NWNumericAccumulator dealloc];
-[NWNumericAccumulator overrideStateWithName:];
-[NWNumericAccumulator reset];
-[NWNumericAccumulator setKvoWatchers:];
-[NWNumericAccumulator kvoWatchers];
-[NWNumericAccumulator overriddenStates];
-[NWNumericAccumulator accumulations];
-[NWNumericAccumulator setOverriddenStates:];
-[NWNumericAccumulator aggregatedStates];
-[NWNumericAccumulator setAccumulations:];
-[NWNumericAccumulator description];
-[NWNumericAccumulator setName:];
-[NWNumericAccumulator updateState:forName:];
-[NWNumericAccumulator watcherForObject:andKeyPath:];
-[NWNumericAccumulator registerObserverForKeyPath:ofObject:alreadyRegistered:];
-[NWNumericAccumulator name];
-[NWNumericAccumulator addAccumulation:withName:forKey:stateCallback:];
-[NWNumericAccumulator initWithName:];
-[NWNumericAccumulator dictionaryRepresentation];
```
