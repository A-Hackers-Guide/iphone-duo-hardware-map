# `HapticServerConfig`

- Image: [`/System/Library/Frameworks/CoreHaptics.framework/CoreHaptics`](../userland/System__Library__Frameworks__CoreHaptics.framework__CoreHaptics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 14 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _currentLocality;
B _usingInternalHaptics;
B _supportsAudioPlayback;
B _supportsHapticPlayback;
B _supportsAdvancedPatternPlayers;
f _hapticContinuousTimeLimit;
f _defaultHapticTransientEventSharpness;
f _defaultHapticContinuousEventSharpness;
f _defaultHapticTransientEventIntensity;
f _defaultHapticContinuousEventIntensity;
@"NSDictionary" _builtInAudioEventIDs;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _hapticTransientIDs;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _hapticContinuousSustainedIDs;
{vector<unsigned long, std::allocator<unsigned long>>="__begin_"^Q"__end_"^Q""{?="__cap_"^Q}} _hapticContinuousNonsustainedIDs;
```

## Properties

```
@property (TB,R,V_usingInternalHaptics) usingInternalHaptics;
@property (TB,R,V_supportsAudioPlayback) supportsAudioPlayback;
@property (TB,R,V_supportsHapticPlayback) supportsHapticPlayback;
@property (TB,R,V_supportsAdvancedPatternPlayers) supportsAdvancedPatternPlayers;
@property (Tf,R,V_hapticContinuousTimeLimit) hapticContinuousTimeLimit;
@property (T@"NSString",R,V_currentLocality) currentLocality;
@property (Tf,R,V_defaultHapticTransientEventSharpness) defaultHapticTransientEventSharpness;
@property (Tf,R,V_defaultHapticContinuousEventSharpness) defaultHapticContinuousEventSharpness;
@property (Tf,R,V_defaultHapticTransientEventIntensity) defaultHapticTransientEventIntensity;
@property (Tf,R,V_defaultHapticContinuousEventIntensity) defaultHapticContinuousEventIntensity;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticTransientIDs) hapticTransientIDs;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticContinuousSustainedIDs) hapticContinuousSustainedIDs;
@property (T{vector<unsigned long, std::allocator<unsigned long>>=^Q^Q{?=^Q}},R,V_hapticContinuousNonsustainedIDs) hapticContinuousNonsustainedIDs;
@property (T@"NSDictionary",R,V_builtInAudioEventIDs) builtInAudioEventIDs;
```

## Instance methods

```
-[HapticServerConfig usingInternalHaptics];
-[HapticServerConfig defaultHapticTransientEventIntensity];
-[HapticServerConfig currentLocality];
-[HapticServerConfig hapticContinuousSustainedIDs];
-[HapticServerConfig defaultHapticTransientEventSharpness];
-[HapticServerConfig defaultHapticContinuousEventIntensity];
-[HapticServerConfig hapticContinuousTimeLimit];
-[HapticServerConfig hapticTransientIDs];
-[HapticServerConfig builtInAudioEventIDs];
-[HapticServerConfig supportsAdvancedPatternPlayers];
-[HapticServerConfig defaultHapticContinuousEventSharpness];
-[HapticServerConfig supportsHapticPlayback];
-[HapticServerConfig hapticContinuousNonsustainedIDs];
-[HapticServerConfig supportsAudioPlayback];
-[HapticServerConfig initWithHapticPlayer:withOptions:error:];
```
