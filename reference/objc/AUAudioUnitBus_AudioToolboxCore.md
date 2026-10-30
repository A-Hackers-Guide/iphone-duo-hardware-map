# `AUAudioUnitBus`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 10 properties, 28 instance methods, 0 class methods

## Instance variables

```
B _removingObserverWithContext;
@"AVAudioFormat" _format;
@"NSArray" _supportedChannelCounts;
I _maximumChannelCount;
B _enabled;
B _shouldAllocateBuffer;
@"NSString" _name;
Q _index;
q _busType;
@"AUAudioUnit" _ownerAudioUnit;
@"NSArray" _supportedChannelLayoutTags;
d _contextPresentationLatency;
{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>="__begin_"^{BusPropertyObserver}"__end_"^{BusPropertyObserver}""{?="__cap_"^{BusPropertyObserver}}} _observers;
```

## Properties

```
@property (T{vector<BusPropertyObserver, std::allocator<BusPropertyObserver>>=^{BusPropertyObserver}^{BusPropertyObserver}{?=^{BusPropertyObserver}}},N,V_observers) observers;
@property (T@"AVAudioFormat",R,N) format;
@property (TB,N,V_shouldAllocateBuffer) shouldAllocateBuffer;
@property (TB,N,GisEnabled) enabled;
@property (T@"NSString",C,N,V_name) name;
@property (TQ,R,N,V_index) index;
@property (Tq,R,N,V_busType) busType;
@property (T@"AUAudioUnit",R,N,V_ownerAudioUnit) ownerAudioUnit;
@property (T@"NSArray",R,C,N,V_supportedChannelLayoutTags) supportedChannelLayoutTags;
@property (Td,N,V_contextPresentationLatency) contextPresentationLatency;
```

## Instance methods

```
-[AUAudioUnitBus addObserver:forKeyPath:options:context:];
-[AUAudioUnitBus removeObserver:forKeyPath:];
-[AUAudioUnitBus dealloc];
-[AUAudioUnitBus index];
-[AUAudioUnitBus setIndex:];
-[AUAudioUnitBus isEnabled];
-[AUAudioUnitBus setEnabled:];
-[AUAudioUnitBus setName:];
-[AUAudioUnitBus setObservers:];
-[AUAudioUnitBus observers];
-[AUAudioUnitBus removeObserver:forKeyPath:context:];
-[AUAudioUnitBus format];
-[AUAudioUnitBus name];
-[AUAudioUnitBus busType];
-[AUAudioUnitBus contextPresentationLatency];
-[AUAudioUnitBus initWithFormat:error:];
-[AUAudioUnitBus maximumChannelCount];
-[AUAudioUnitBus ownerAudioUnit];
-[AUAudioUnitBus setBusType:];
-[AUAudioUnitBus setContextPresentationLatency:];
-[AUAudioUnitBus setFormat:error:];
-[AUAudioUnitBus setMaximumChannelCount:];
-[AUAudioUnitBus setOwnerAudioUnit:];
-[AUAudioUnitBus setShouldAllocateBuffer:];
-[AUAudioUnitBus setSupportedChannelCounts:];
-[AUAudioUnitBus shouldAllocateBuffer];
-[AUAudioUnitBus supportedChannelCounts];
-[AUAudioUnitBus supportedChannelLayoutTags];
```
