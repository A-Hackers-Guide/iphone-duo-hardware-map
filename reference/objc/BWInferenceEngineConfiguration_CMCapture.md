# `BWInferenceEngineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
Q _connection;
B _configurationReconfigured;
@"BWInferenceDependencyProvider" _dependencyProvider;
@"NSMutableArray" _inferenceRequirements;
@"NSMutableArray" _videoRequirementsPossiblyReceivingAttachedMedia;
@"NSMutableArray" _videoRequirementsPossiblyProvidingAttachedMedia;
@"NSMutableDictionary" _lazyInputVideoRequirementsByAttachedMediaKey;
@"NSMutableDictionary" _lazyOutputVideoRequirementsByAttachedMediaKey;
@"NSMutableSet" _unresolvedAttachedMediaKeysPreventingProvidedVideoRequirements;
```

## Properties

```
@property (TQ,N,V_connection) connection;
@property (TB,N,V_configurationReconfigured) configurationReconfigured;
@property (T@"BWInferenceDependencyProvider",&,N,V_dependencyProvider) dependencyProvider;
@property (T@"NSMutableArray",&,N) inferenceRequirements;
@property (T@"NSMutableArray",&,N,V_videoRequirementsPossiblyReceivingAttachedMedia) videoRequirementsPossiblyReceivingAttachedMedia;
@property (T@"NSMutableArray",&,N,V_videoRequirementsPossiblyProvidingAttachedMedia) videoRequirementsPossiblyProvidingAttachedMedia;
@property (T@"NSMutableDictionary",&,N,V_lazyInputVideoRequirementsByAttachedMediaKey) lazyInputVideoRequirementsByAttachedMediaKey;
@property (T@"NSMutableDictionary",&,N,V_lazyOutputVideoRequirementsByAttachedMediaKey) lazyOutputVideoRequirementsByAttachedMediaKey;
@property (T@"NSMutableSet",&,N,V_unresolvedAttachedMediaKeysPreventingProvidedVideoRequirements) unresolvedAttachedMediaKeysPreventingProvidedVideoRequirements;
```

## Instance methods

```
-[BWInferenceEngineConfiguration init];
-[BWInferenceEngineConfiguration dealloc];
-[BWInferenceEngineConfiguration connection];
-[BWInferenceEngineConfiguration setConnection:];
-[BWInferenceEngineConfiguration configurationReconfigured];
-[BWInferenceEngineConfiguration dependencyProvider];
-[BWInferenceEngineConfiguration inferenceRequirements];
-[BWInferenceEngineConfiguration lazyInputVideoRequirementsByAttachedMediaKey];
-[BWInferenceEngineConfiguration lazyOutputVideoRequirementsByAttachedMediaKey];
-[BWInferenceEngineConfiguration setConfigurationReconfigured:];
-[BWInferenceEngineConfiguration setDependencyProvider:];
-[BWInferenceEngineConfiguration setInferenceRequirements:];
-[BWInferenceEngineConfiguration setLazyInputVideoRequirementsByAttachedMediaKey:];
-[BWInferenceEngineConfiguration setLazyOutputVideoRequirementsByAttachedMediaKey:];
-[BWInferenceEngineConfiguration setUnresolvedAttachedMediaKeysPreventingProvidedVideoRequirements:];
-[BWInferenceEngineConfiguration setVideoRequirementsPossiblyProvidingAttachedMedia:];
-[BWInferenceEngineConfiguration setVideoRequirementsPossiblyReceivingAttachedMedia:];
-[BWInferenceEngineConfiguration unresolvedAttachedMediaKeysPreventingProvidedVideoRequirements];
-[BWInferenceEngineConfiguration videoRequirementsPossiblyProvidingAttachedMedia];
-[BWInferenceEngineConfiguration videoRequirementsPossiblyReceivingAttachedMedia];
```
