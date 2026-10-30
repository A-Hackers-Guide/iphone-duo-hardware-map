# `OrchestratorClientIOProc`

- Image: [`/System/Library/PrivateFrameworks/CoreAudioOrchestration.framework/CoreAudioOrchestration`](../userland/System__Library__PrivateFrameworks__CoreAudioOrchestration.framework__CoreAudioOrchestration.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ADMConfigurationProtocol`
- 3 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
I mDeviceID;
^? mIOProcID;
{IOProcBrain="_vptr$IOProcCallable"^^?"_vptr$ADMIOConfigurable"^^?"mClientIOProc"{ClientIOProc="mProvidedCallback"^?"mProvidedClientData"^v}"admIOProc"{ADMIO="_vptr$IOProcCallable"^^?"_vptr$ADMIOConfigurable"^^?"ioInfo"{ADMIOConfiguration="contextID"I"frameBufferSize"Q"admCallback"{function<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>="__f_"{__value_func<void (unsigned int, const AMCP::Proc_Cycle_Info &, unsigned long, AMCP::Proc_Stream *, unsigned long, AMCP::Proc_Stream *)>="__buf_"(type="__data"[24C])"__f_"^v}}"inputStreamIndicesInIOProc"{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}}"outputStreamIndicesInIOProc"{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}}}"admInputs"{ADMStreamsAndABLs="streams"{vector<AMCP::Proc_Stream, std::allocator<AMCP::Proc_Stream>>="__begin_"^{Proc_Stream}"__end_"^{Proc_Stream}""{?="__cap_"^{Proc_Stream}}}"abls"{vector<AudioBufferList, std::allocator<AudioBufferList>>="__begin_"^{AudioBufferList}"__end_"^{AudioBufferList}""{?="__cap_"^{AudioBufferList}}}}"admOutputs"{ADMStreamsAndABLs="streams"{vector<AMCP::Proc_Stream, std::allocator<AMCP::Proc_Stream>>="__begin_"^{Proc_Stream}"__end_"^{Proc_Stream}""{?="__cap_"^{Proc_Stream}}}"abls"{vector<AudioBufferList, std::allocator<AudioBufferList>>="__begin_"^{AudioBufferList}"__end_"^{AudioBufferList}""{?="__cap_"^{AudioBufferList}}}}}} mIOBrain;
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
-[OrchestratorClientIOProc configure:];
-[OrchestratorClientIOProc init];
-[OrchestratorClientIOProc createHALIOProc:];
-[OrchestratorClientIOProc destroyHALIOProc];
-[OrchestratorClientIOProc installClientIOProc:data:];
-[OrchestratorClientIOProc startHALIOProc];
-[OrchestratorClientIOProc startHALIOProcAtTime:];
-[OrchestratorClientIOProc stopHALIOProc];
-[OrchestratorClientIOProc uninstallClientIOProc];
```
