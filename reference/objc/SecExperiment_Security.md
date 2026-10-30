# `SecExperiment`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _samplingDisabled;
@"NSString" _name;
@"SecExperimentConfig" _cachedConfig;
```

## Properties

```
@property (T@"NSString",&,V_name) name;
@property (TB,N,V_samplingDisabled) samplingDisabled;
@property (T@"SecExperimentConfig",&,V_cachedConfig) cachedConfig;
@property (T@"NSString",R) identifier;
```

## Instance methods

```
-[SecExperiment identifier];
-[SecExperiment setName:];
-[SecExperiment name];
-[SecExperiment initWithName:];
-[SecExperiment cachedConfig];
-[SecExperiment copyExperimentConfiguration];
-[SecExperiment copyExperimentConfigurationFromUserDefaults];
-[SecExperiment copyRandomExperimentConfigurationFromAsset:];
-[SecExperiment copyRemoteExperimentAsset];
-[SecExperiment experimentIsAllowedForProcess];
-[SecExperiment isSamplingDisabled];
-[SecExperiment isSamplingDisabledWithDefault:];
-[SecExperiment samplingDisabled];
-[SecExperiment setCachedConfig:];
-[SecExperiment setSamplingDisabled:];
```
