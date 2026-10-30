# `LLVUserDefaults`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 18 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _bufferDumpEnable;
B _opticalFlowEnable;
B _hybridWarperEnable;
B _tripodNetworkTuningEnable;
B _gpuProcessingEnable;
B _guidedFilterEnable;
B _computeHybridWarperStatsUsingGPU;
B _useGPUGammaCalculation;
B _ane1HintEnable;
f _historyBlendingFactor;
f _denoisedBlendingFactor;
f _guidedFilterEpsilon;
i _guidedFilterSubsampleFactor;
@"NSString" _resolution;
@"NSString" _opticalFlowResolution;
q _opticalFlowLKTPreset;
q _guidedFilterKernelDiameter;
@"NSUserDefaults" _userDefaults;
```

## Properties

```
@property (T@"NSUserDefaults",&,N,V_userDefaults) userDefaults;
@property (Tf,R,N,V_historyBlendingFactor) historyBlendingFactor;
@property (Tf,R,N,V_denoisedBlendingFactor) denoisedBlendingFactor;
@property (T@"NSString",R,C,N,V_resolution) resolution;
@property (T@"NSString",R,C,N,V_opticalFlowResolution) opticalFlowResolution;
@property (Tq,R,N,V_opticalFlowLKTPreset) opticalFlowLKTPreset;
@property (TB,R,N,V_bufferDumpEnable) bufferDumpEnable;
@property (TB,R,N,V_opticalFlowEnable) opticalFlowEnable;
@property (TB,R,N,V_hybridWarperEnable) hybridWarperEnable;
@property (TB,R,N,V_tripodNetworkTuningEnable) tripodNetworkTuningEnable;
@property (TB,R,N,V_gpuProcessingEnable) gpuProcessingEnable;
@property (TB,R,N,V_guidedFilterEnable) guidedFilterEnable;
@property (Tf,R,N,V_guidedFilterEpsilon) guidedFilterEpsilon;
@property (Tq,R,N,V_guidedFilterKernelDiameter) guidedFilterKernelDiameter;
@property (Ti,R,N,V_guidedFilterSubsampleFactor) guidedFilterSubsampleFactor;
@property (TB,R,N,V_computeHybridWarperStatsUsingGPU) computeHybridWarperStatsUsingGPU;
@property (TB,R,N,V_useGPUGammaCalculation) useGPUGammaCalculation;
@property (TB,R,N,V_ane1HintEnable) ane1HintEnable;
```

## Class methods

```
+[LLVUserDefaults sharedInstance];
```

## Instance methods

```
-[LLVUserDefaults userDefaults];
-[LLVUserDefaults init];
-[LLVUserDefaults resolution];
-[LLVUserDefaults setUserDefaults:];
-[LLVUserDefaults dictionaryRepresentation];
-[LLVUserDefaults loadSettings];
-[LLVUserDefaults ane1HintEnable];
-[LLVUserDefaults bufferDumpEnable];
-[LLVUserDefaults clampFloat:min:max:];
-[LLVUserDefaults clampInteger:min:max:];
-[LLVUserDefaults computeHybridWarperStatsUsingGPU];
-[LLVUserDefaults denoisedBlendingFactor];
-[LLVUserDefaults gpuProcessingEnable];
-[LLVUserDefaults guidedFilterEnable];
-[LLVUserDefaults guidedFilterEpsilon];
-[LLVUserDefaults guidedFilterKernelDiameter];
-[LLVUserDefaults guidedFilterSubsampleFactor];
-[LLVUserDefaults historyBlendingFactor];
-[LLVUserDefaults hybridWarperEnable];
-[LLVUserDefaults opticalFlowEnable];
-[LLVUserDefaults opticalFlowLKTPreset];
-[LLVUserDefaults opticalFlowResolution];
-[LLVUserDefaults tripodNetworkTuningEnable];
-[LLVUserDefaults useGPUGammaCalculation];
```
