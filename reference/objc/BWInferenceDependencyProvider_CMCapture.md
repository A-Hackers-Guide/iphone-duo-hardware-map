# `BWInferenceDependencyProvider`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _dependenciesByInputVideoRequirements;
@"NSMapTable" _dependenciesByOutputVideoRequirements;
@"NSDictionary" _providedVideoRequirementsByAttachedMediaKey;
@"NSSet" _consumedVideoAttachedMediaKeys;
i _supportedPixelBufferCompressionType;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_dependenciesByInputVideoRequirements) dependenciesByInputVideoRequirements;
@property (T@"NSMapTable",&,N,V_dependenciesByOutputVideoRequirements) dependenciesByOutputVideoRequirements;
@property (T@"NSDictionary",&,N,V_providedVideoRequirementsByAttachedMediaKey) providedVideoRequirementsByAttachedMediaKey;
@property (T@"NSSet",&,N,V_consumedVideoAttachedMediaKeys) consumedVideoAttachedMediaKeys;
@property (T@"NSArray",R,C,N) allInputVideoDependencies;
@property (T@"NSArray",R,C,N) allOutputVideoDependencies;
@property (Ti,N,V_supportedPixelBufferCompressionType) supportedPixelBufferCompressionType;
```

## Instance methods

```
-[BWInferenceDependencyProvider init];
-[BWInferenceDependencyProvider dealloc];
-[BWInferenceDependencyProvider providedVideoRequirementsByAttachedMediaKey];
-[BWInferenceDependencyProvider description];
-[BWInferenceDependencyProvider allInputVideoDependencies];
-[BWInferenceDependencyProvider allOutputVideoDependencies];
-[BWInferenceDependencyProvider consumedVideoAttachedMediaKeys];
-[BWInferenceDependencyProvider dependenciesByInputVideoRequirements];
-[BWInferenceDependencyProvider dependenciesByOutputVideoRequirements];
-[BWInferenceDependencyProvider dependenciesForInputVideoRequirement:];
-[BWInferenceDependencyProvider dependenciesForOutputVideoRequirement:];
-[BWInferenceDependencyProvider setConsumedVideoAttachedMediaKeys:];
-[BWInferenceDependencyProvider setDependenciesByInputVideoRequirements:];
-[BWInferenceDependencyProvider setDependenciesByOutputVideoRequirements:];
-[BWInferenceDependencyProvider setProvidedVideoRequirementsByAttachedMediaKey:];
-[BWInferenceDependencyProvider setSupportedPixelBufferCompressionType:];
-[BWInferenceDependencyProvider supportedPixelBufferCompressionType];
```
