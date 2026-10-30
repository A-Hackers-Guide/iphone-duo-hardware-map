# `SecExperimentConfig`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
I _fleetSampleRate;
I _deviceSampleRate;
@"NSString" _identifier;
@"NSDictionary" _configurationData;
@"NSDictionary" _config;
```

## Properties

```
@property (T@"NSString",&,V_identifier) identifier;
@property (T@"NSDictionary",&,V_config) config;
@property (TI,V_fleetSampleRate) fleetSampleRate;
@property (TI,V_deviceSampleRate) deviceSampleRate;
@property (T@"NSDictionary",&,V_configurationData) configurationData;
@property (TB,R) isSampled;
```

## Instance methods

```
-[SecExperimentConfig config];
-[SecExperimentConfig setConfig:];
-[SecExperimentConfig identifier];
-[SecExperimentConfig initWithConfiguration:];
-[SecExperimentConfig setIdentifier:];
-[SecExperimentConfig configurationData];
-[SecExperimentConfig fleetSampleRate];
-[SecExperimentConfig deviceSampleRate];
-[SecExperimentConfig hostHash];
-[SecExperimentConfig isSampled];
-[SecExperimentConfig setConfigurationData:];
-[SecExperimentConfig setDeviceSampleRate:];
-[SecExperimentConfig setFleetSampleRate:];
-[SecExperimentConfig shouldRunWithSamplingRate:];
```
