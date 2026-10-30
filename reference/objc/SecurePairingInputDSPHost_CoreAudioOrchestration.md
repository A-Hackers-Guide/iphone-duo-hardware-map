# `SecurePairingInputDSPHost`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OrchestratedDSPObject`
- 6 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
{IOClutch="isEngaged"{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}}"transmissionIsBusy"{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}}"freewheeler"{jthread="__stop_source_"{stop_source="__state_"{__intrusive_shared_ptr<std::__stop_state>="__raw_ptr_"^{__stop_state}}}"__thread_"{thread="__t_"^{_opaque_pthread_t}}}"semaphore"{semaphore="mImpl"{semaphore="mMachSem"I"mOwned"B}"mCounter"{atomic<int>="__a_"{__cxx_atomic_impl<int, std::__cxx_atomic_base_impl<int>>="__a_value"Ai}}"mOriginalCounter"i}} mIOClutch;
@ mADMFactory;
@"DSPController" mDSPController;
{shared_ptr<ADMIO>="__ptr_"^{ADMIO}"__cntrl_"^{__shared_weak_count}} mADMIO;
^? mReadyForStartCallback;
^v mRecruiterData;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SecurePairingInputDSPHost stopDSP];
-[SecurePairingInputDSPHost getOrchestratedDSPObjects];
-[SecurePairingInputDSPHost initWithCallback:inRecruiterData:inADMFactory:outStatus:];
-[SecurePairingInputDSPHost processDSPWithNow:inInputData:inInputTime:inOutputData:inOutputTime:];
-[SecurePairingInputDSPHost startDSP];
```
