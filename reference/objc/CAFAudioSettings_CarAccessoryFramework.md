# `CAFAudioSettings`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 10 properties, 14 instance methods, 2 class methods

## Properties

```
@property (T@"NSArray",R,N) volumeServices;
@property (T@"NSArray",R,N) equalizerServices;
@property (T@"CAFSoundDistribution",R,N) soundDistributionService;
@property (T@"CAFSoundDistributionPresets",R,N) soundDistributionPresetsService;
@property (T@"CAFEqualizerPresets",R,N) equalizerPresetsService;
@property (T@"NSArray",R,N) volumes;
@property (T@"NSArray",R,N) equalizers;
@property (T@"CAFSoundDistribution",R,N) soundDistribution;
@property (T@"CAFSoundDistributionPresets",R,N) soundDistributionPresets;
@property (T@"CAFEqualizerPresets",R,N) equalizerPresets;
```

## Class methods

```
+[CAFAudioSettings accessoryIdentifier];
+[CAFAudioSettings observerProtocol];
```

## Instance methods

```
-[CAFAudioSettings removeObserver:];
-[CAFAudioSettings addObserver:];
-[CAFAudioSettings volumes];
-[CAFAudioSettings volumeServices];
-[CAFAudioSettings registerObserver:];
-[CAFAudioSettings unregisterObserver:];
-[CAFAudioSettings equalizerPresets];
-[CAFAudioSettings equalizers];
-[CAFAudioSettings soundDistribution];
-[CAFAudioSettings soundDistributionPresets];
-[CAFAudioSettings soundDistributionPresetsService];
-[CAFAudioSettings equalizerPresetsService];
-[CAFAudioSettings equalizerServices];
-[CAFAudioSettings soundDistributionService];
```
