# `AVAudioIONodeSession`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<caulk::synchronized<avas::client::AVAudioIONodeSessionImpl>, std::default_delete<caulk::synchronized<avas::client::AVAudioIONodeSessionImpl>>>=""{?="__ptr_"^v}} _impl;
@"AVAudioIONodePlayState" _playState;
{atomic_flag="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _invalidated;
B _explicitSimulationEnabled;
```

## Properties

```
@property (TI,R,N) nodeSessionID;
@property (T@"NSUUID",R,N) nodeSessionUUID;
@property (TI,R,N) sourceSessionID;
@property (Ti,R,N) sessionOwnerPID;
@property (TI,R,N) playerType;
@property (TB,N,GisInputMuted) inputMuted;
@property (TB,N,GisOutputMuted) outputMuted;
@property (T@"AVAudioIONodePlayState",C,N) playState;
@property (TB,R,N,GisExplicitSimulationEnabled,V_explicitSimulationEnabled) explicitSimulationEnabled;
```

## Instance methods

```
-[AVAudioIONodeSession playState];
-[AVAudioIONodeSession dealloc];
-[AVAudioIONodeSession sourceSessionID];
-[AVAudioIONodeSession invalidate];
-[AVAudioIONodeSession description];
-[AVAudioIONodeSession setPlayState:];
-[AVAudioIONodeSession isOutputMuted];
-[AVAudioIONodeSession playerType];
-[AVAudioIONodeSession initWithDescription:];
-[AVAudioIONodeSession getMXProperties:propertyErrors:];
-[AVAudioIONodeSession getMXSessionProperty:error:];
-[AVAudioIONodeSession setMXSessionProperty:value:error:];
-[AVAudioIONodeSession nodeSessionUUID];
-[AVAudioIONodeSession sessionOwnerPID];
-[AVAudioIONodeSession setOutputMuted:];
-[AVAudioIONodeSession _setMXProperties:properties:error:];
-[AVAudioIONodeSession initWithDescription:server:];
-[AVAudioIONodeSession isExplicitSimulationEnabled];
-[AVAudioIONodeSession isInputMuted];
-[AVAudioIONodeSession nodeSessionID];
-[AVAudioIONodeSession privateCreateIONodeSession:server:];
-[AVAudioIONodeSession reconfigure:error:];
-[AVAudioIONodeSession setInputMuted:];
-[AVAudioIONodeSession setMXProperties:error:];
```
