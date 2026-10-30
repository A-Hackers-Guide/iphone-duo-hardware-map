# `AVAudioIOController_iOS`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioIOController`
- 2 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
{optional<(anonymous namespace)::IOControllerImpl>=""(?="__null_state_"c"__val_"{IOControllerImpl="mSession"@"AVAudioSession""mIsDecoupledInput"B"mXPCConnection"{weak_ptr<avas::client::XPCConnection>="__ptr_"^{XPCConnection}"__cntrl_"^{__shared_weak_count}}"mTimingStateSlot"{atomic<unsigned int>="__a_"{__cxx_atomic_impl<unsigned int, std::__cxx_atomic_base_impl<unsigned int>>="__a_value"AI}}"mListenerMgr"{synchronized<(anonymous namespace)::ListenerMgr, caulk::mach::unfair_lock, caulk::empty_atomic_interface<(anonymous namespace)::ListenerMgr>>="mMutex"{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}"mObject"{ListenerMgr="mOuter"^{IOControllerImpl}"mListeners"{vector<std::pair<long, void (^)(AVAudioIOControllerEvent)>, std::allocator<std::pair<long, void (^)(AVAudioIOControllerEvent)>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}}}}})"__engaged_"B} impl;
{shared_ptr<avas::client::DeviceTimeClient>="__ptr_"^{DeviceTimeClient}"__cntrl_"^{__shared_weak_count}} _deviceTimeClient;
```

## Properties

```
@property (T{AVAudioIOPeriod=ddQf},R,N) IOPeriod;
@property (TB,R,N,GisRunning) running;
@property (TB,R,N) supportsDynamicLatency;
@property (T{AVAudioTimeInterval=ddQ},R,N) dynamicLatency;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioIOController_iOS isRunning];
-[AVAudioIOController_iOS currentTime];
-[AVAudioIOController_iOS presentationTime];
-[AVAudioIOController_iOS IOPeriod];
-[AVAudioIOController_iOS createIOEventBlock:];
-[AVAudioIOController_iOS destroyIOEventBlock:];
-[AVAudioIOController_iOS dynamicLatency];
-[AVAudioIOController_iOS initWithSession:xpcConnection:deviceTimeClient:timingSlot:isDecoupledInput:];
-[AVAudioIOController_iOS privateDispatchIOControllerEvent:];
-[AVAudioIOController_iOS setTimingSlot:];
-[AVAudioIOController_iOS supportsDynamicLatency];
```
