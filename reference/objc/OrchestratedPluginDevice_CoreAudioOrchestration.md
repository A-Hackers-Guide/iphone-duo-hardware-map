# `OrchestratedPluginDevice`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `OrchestratedDSPObject`
- 6 instance variables, 10 properties, 10 instance methods, 0 class methods

## Instance variables

```
I _mDeviceID;
I _mPluginID;
I _mChannelCount;
I _mFramesPerBuffer;
@"DSPController" _mDSPController;
{shared_ptr<ADMIO>="__ptr_"^{ADMIO}"__cntrl_"^{__shared_weak_count}} _mADMIO;
```

## Properties

```
@property (TI,R,N,V_mDeviceID) mDeviceID;
@property (TI,R,N,V_mPluginID) mPluginID;
@property (T@"DSPController",R,N,V_mDSPController) mDSPController;
@property (T{shared_ptr<ADMIO>=^{ADMIO}^{__shared_weak_count}},R,N,V_mADMIO) mADMIO;
@property (TI,R,N,V_mChannelCount) mChannelCount;
@property (TI,R,N,V_mFramesPerBuffer) mFramesPerBuffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[OrchestratedPluginDevice stopDSP];
-[OrchestratedPluginDevice initWithDeviceID:andPluginID:andDSPController:andChannelCount:andFramesPerBuffer:];
-[OrchestratedPluginDevice mADMIO];
-[OrchestratedPluginDevice mChannelCount];
-[OrchestratedPluginDevice mDSPController];
-[OrchestratedPluginDevice mDeviceID];
-[OrchestratedPluginDevice mFramesPerBuffer];
-[OrchestratedPluginDevice mPluginID];
-[OrchestratedPluginDevice processDSPWithNow:inInputData:inInputTime:inOutputData:inOutputTime:];
-[OrchestratedPluginDevice startDSP];
```
