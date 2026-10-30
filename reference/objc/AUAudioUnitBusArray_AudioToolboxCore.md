# `AUAudioUnitBusArray`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 5 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _busses;
B _countChangeable;
@"AUAudioUnit" _ownerAudioUnit;
q _busType;
{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>="__begin_"^{BusPropertyObserver}"__end_"^{BusPropertyObserver}""{?="__cap_"^{BusPropertyObserver}}} _observers;
```

## Properties

```
@property (T{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}{?=^{BusPropertyObserver}}},N,V_observers) observers;
@property (TQ,R,N) count;
@property (TB,R,N,GisCountChangeable,V_countChangeable) countChangeable;
@property (T@"AUAudioUnit",R,N,V_ownerAudioUnit) ownerAudioUnit;
@property (Tq,R,N,V_busType) busType;
```

## Instance methods

```
-[AUAudioUnitBusArray init];
-[AUAudioUnitBusArray objectAtIndexedSubscript:];
-[AUAudioUnitBusArray dealloc];
-[AUAudioUnitBusArray count];
-[AUAudioUnitBusArray countByEnumeratingWithState:objects:count:];
-[AUAudioUnitBusArray setObservers:];
-[AUAudioUnitBusArray observers];
-[AUAudioUnitBusArray busType];
-[AUAudioUnitBusArray addObserverToAllBusses:forKeyPath:options:context:];
-[AUAudioUnitBusArray indexBusses];
-[AUAudioUnitBusArray initWithAudioUnit:busType:];
-[AUAudioUnitBusArray initWithAudioUnit:busType:busses:];
-[AUAudioUnitBusArray isCountChangeable];
-[AUAudioUnitBusArray ownerAudioUnit];
-[AUAudioUnitBusArray removeObserverFromAllBusses:forKeyPath:context:];
-[AUAudioUnitBusArray replaceBusses:];
-[AUAudioUnitBusArray setBusCount:error:];
```
