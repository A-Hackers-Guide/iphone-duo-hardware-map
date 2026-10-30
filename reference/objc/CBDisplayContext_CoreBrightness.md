# `CBDisplayContext`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<CBSystemContext>" _systemContext;
@"CBGammaContrastPreservation" _gcp;
@"CBTwilight" _twilight;
@"CBAmmolite" _ammolite;
@"<CBPrimitiveConfigurationProvider><CBBacklightConfigurationProvider>" _configuration;
@"<CBBrightnessProxy>" _brtCtl;
@"<CBPowerManagementClient>" _cbpm;
@"CBAODState" _AODState;
@"CBSILState" _SILState;
@"CBRingLight" _ringLight;
@"CADisplay" _display;
@"NSObject<OS_dispatch_queue>" _displayQueue;
```

## Properties

```
@property (T@"<CBSystemContext>",R,V_systemContext) systemContext;
@property (T@"CBGammaContrastPreservation",R,V_gcp) gcp;
@property (T@"CBTwilight",R,V_twilight) twilight;
@property (T@"CBAmmolite",R,V_ammolite) ammolite;
@property (T@"<CBPrimitiveConfigurationProvider><CBBacklightConfigurationProvider>",R,V_configuration) configuration;
@property (T@"<CBBrightnessProxy>",R,V_brtCtl) brtCtl;
@property (T@"<CBPowerManagementClient>",R,V_cbpm) cbpm;
@property (T@"CBAODState",R,V_AODState) AODState;
@property (T@"CBSILState",R,V_SILState) SILState;
@property (T@"CBRingLight",R,V_ringLight) ringLight;
@property (T@"CADisplay",R,V_display) display;
@property (T@"NSObject<OS_dispatch_queue>",R,V_displayQueue) displayQueue;
```

## Instance methods

```
-[CBDisplayContext AODState];
-[CBDisplayContext display];
-[CBDisplayContext systemContext];
-[CBDisplayContext dealloc];
-[CBDisplayContext SILState];
-[CBDisplayContext configuration];
-[CBDisplayContext description];
-[CBDisplayContext gcp];
-[CBDisplayContext ammolite];
-[CBDisplayContext brtCtl];
-[CBDisplayContext cbpm];
-[CBDisplayContext displayQueue];
-[CBDisplayContext initWithQueue:andSystemContext:andBrtCtl:andConfig:andTwilight:andAmmolite:andGCP:andCADisplay:andCBPM:andAODState:andSILState:andRingLight:];
-[CBDisplayContext ringLight];
-[CBDisplayContext twilight];
```
