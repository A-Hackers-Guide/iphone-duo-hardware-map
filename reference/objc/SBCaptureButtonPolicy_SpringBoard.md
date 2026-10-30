# `SBCaptureButtonPolicy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDictionaryRepresentable`
- 14 instance variables, 18 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _consoleModeMitigationEnabled;
B _wakeEnabled;
B _directLaunchAfterUnsuppressEnabled;
B _deviceStationaryDetectionEnabled;
B _deviceStationaryDetectionEnabledWhenUnlocked;
B _suppressionEnabled;
B _launchIfUnobstructedWhileButtonDownEnabled;
B _launchIfUnobstructedPromptlyAfterButtonUpEnabled;
B _visionIntelligenceEnabled;
@"NSArray" _wakingBacklightStates;
d _directLaunchAfterUnsuppressGracePeriod;
d _deviceStationaryDetectionStationaryThreshold;
d _deviceStationaryDetectionStationaryPickUpBuffer;
d _deviceStationaryDetectionStationaryDebounceInterval;
```

## Properties

```
@property (TB,R,N,V_consoleModeMitigationEnabled) consoleModeMitigationEnabled;
@property (TB,R,N,V_wakeEnabled) wakeEnabled;
@property (T@"NSArray",R,C,N,V_wakingBacklightStates) wakingBacklightStates;
@property (TB,R,N,V_directLaunchAfterUnsuppressEnabled) directLaunchAfterUnsuppressEnabled;
@property (Td,R,N,V_directLaunchAfterUnsuppressGracePeriod) directLaunchAfterUnsuppressGracePeriod;
@property (TB,R,N,V_deviceStationaryDetectionEnabled) deviceStationaryDetectionEnabled;
@property (TB,R,N,V_deviceStationaryDetectionEnabledWhenUnlocked) deviceStationaryDetectionEnabledWhenUnlocked;
@property (Td,R,N,V_deviceStationaryDetectionStationaryThreshold) deviceStationaryDetectionStationaryThreshold;
@property (Td,R,N,V_deviceStationaryDetectionStationaryPickUpBuffer) deviceStationaryDetectionStationaryPickUpBuffer;
@property (Td,R,N,V_deviceStationaryDetectionStationaryDebounceInterval) deviceStationaryDetectionStationaryDebounceInterval;
@property (TB,R,N,V_suppressionEnabled) suppressionEnabled;
@property (TB,R,N,V_launchIfUnobstructedWhileButtonDownEnabled) launchIfUnobstructedWhileButtonDownEnabled;
@property (TB,R,N,V_launchIfUnobstructedPromptlyAfterButtonUpEnabled) launchIfUnobstructedPromptlyAfterButtonUpEnabled;
@property (TB,R,N,GisVisionIntelligenceEnabled,V_visionIntelligenceEnabled) visionIntelligenceEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureButtonPolicy initWithDictionary:];
-[SBCaptureButtonPolicy succinctDescriptionBuilder];
-[SBCaptureButtonPolicy descriptionWithMultilinePrefix:];
-[SBCaptureButtonPolicy succinctDescription];
-[SBCaptureButtonPolicy hash];
-[SBCaptureButtonPolicy description];
-[SBCaptureButtonPolicy isEqual:];
-[SBCaptureButtonPolicy descriptionBuilderWithMultilinePrefix:];
-[SBCaptureButtonPolicy dictionaryRepresentation];
-[SBCaptureButtonPolicy consoleModeMitigationEnabled];
-[SBCaptureButtonPolicy deviceStationaryDetectionEnabled];
-[SBCaptureButtonPolicy deviceStationaryDetectionEnabledWhenUnlocked];
-[SBCaptureButtonPolicy deviceStationaryDetectionStationaryDebounceInterval];
-[SBCaptureButtonPolicy deviceStationaryDetectionStationaryPickUpBuffer];
-[SBCaptureButtonPolicy deviceStationaryDetectionStationaryThreshold];
-[SBCaptureButtonPolicy directLaunchAfterUnsuppressEnabled];
-[SBCaptureButtonPolicy directLaunchAfterUnsuppressGracePeriod];
-[SBCaptureButtonPolicy initWithConsoleModeEnabled:wakeEnabled:directLaunchAfterUnsuppressEnabled:directLaunchAfterUnsuppressGracePeriod:deviceStationaryDetectionEnabled:deviceStationaryDetectionEnabledWhenUnlocked:deviceStationaryDetectionStationaryThreshold:deviceStationaryDetectionStationaryPickUpBuffer:deviceStationaryDetectionStationaryDebounceInterval:suppressionEnabled:launchIfUnobstructedWhileButtonDownEnabled:launchIfUnobstructedPromptlyAfterButtonUpEnabled:wakingBacklightStates:visionIntelligenceEnabled:];
-[SBCaptureButtonPolicy isVisionIntelligenceEnabled];
-[SBCaptureButtonPolicy launchIfUnobstructedPromptlyAfterButtonUpEnabled];
-[SBCaptureButtonPolicy launchIfUnobstructedWhileButtonDownEnabled];
-[SBCaptureButtonPolicy suppressionEnabled];
-[SBCaptureButtonPolicy wakeEnabled];
-[SBCaptureButtonPolicy wakingBacklightStates];
```
