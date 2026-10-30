# `AABCHistograms`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 19 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _EPerAls;
@"NSArray" _eBins;
B _firstBrightnessUpdate;
B _autoBrightnessOn;
B _ecoModeOn;
B _builtInDisplay;
f _lastBrightnessUpdateNits;
f _lastBrightnessUpdateNitsEDR;
@"CBHistogramBuilder" _L;
@"CBHistogramBuilder" _LOff;
@"CBHistogramBuilder" _LDevice;
@"CBHistogramBuilder" _LDeviceOff;
@"CBHistogramBuilder" _LLPM;
@"CBHistogramBuilder" _L_EDR;
@"CBHistogramBuilder" _LOff_EDR;
@"CBHistogramBuilder" _LDevice_EDR;
@"CBHistogramBuilder" _LDeviceOff_EDR;
@"CBHistogramBuilder" _LLPM_EDR;
@"CBHistogramBuilder" _E;
@"NSString" _displayID;
d _lastBrightnessUpdateTimestamp;
```

## Properties

```
@property (T@"CBHistogramBuilder",R,V_L) L;
@property (T@"CBHistogramBuilder",R,V_LOff) LOff;
@property (T@"CBHistogramBuilder",R,V_LDevice) LDevice;
@property (T@"CBHistogramBuilder",R,V_LDeviceOff) LDeviceOff;
@property (T@"CBHistogramBuilder",R,V_LLPM) LLPM;
@property (T@"CBHistogramBuilder",R,V_L_EDR) L_EDR;
@property (T@"CBHistogramBuilder",R,V_LOff_EDR) LOff_EDR;
@property (T@"CBHistogramBuilder",R,V_LDevice_EDR) LDevice_EDR;
@property (T@"CBHistogramBuilder",R,V_LDeviceOff_EDR) LDeviceOff_EDR;
@property (T@"CBHistogramBuilder",R,V_LLPM_EDR) LLPM_EDR;
@property (T@"CBHistogramBuilder",R,V_E) E;
@property (T@"NSString",C,V_displayID) displayID;
@property (Td,V_lastBrightnessUpdateTimestamp) lastBrightnessUpdateTimestamp;
@property (Tf,V_lastBrightnessUpdateNits) lastBrightnessUpdateNits;
@property (Tf,V_lastBrightnessUpdateNitsEDR) lastBrightnessUpdateNitsEDR;
@property (TB,V_firstBrightnessUpdate) firstBrightnessUpdate;
@property (TB,V_autoBrightnessOn) autoBrightnessOn;
@property (TB,V_ecoModeOn) ecoModeOn;
@property (TB,V_builtInDisplay) builtInDisplay;
```

## Instance methods

```
-[AABCHistograms setDisplayID:];
-[AABCHistograms init];
-[AABCHistograms submit];
-[AABCHistograms dealloc];
-[AABCHistograms displayID];
-[AABCHistograms E];
-[AABCHistograms LDevice];
-[AABCHistograms LDeviceOff];
-[AABCHistograms LDevice_EDR];
-[AABCHistograms LLPM_EDR];
-[AABCHistograms LOff_EDR];
-[AABCHistograms L_EDR];
-[AABCHistograms L];
-[AABCHistograms LDeviceOff_EDR];
-[AABCHistograms LLPM];
-[AABCHistograms LOff];
-[AABCHistograms setLastBrightnessUpdateNitsEDR:];
-[AABCHistograms autoBrightnessOn];
-[AABCHistograms builtInDisplay];
-[AABCHistograms ecoModeOn];
-[AABCHistograms firstBrightnessUpdate];
-[AABCHistograms flushPendingWithNitsSDR:andNitsEDR:];
-[AABCHistograms lastBrightnessUpdateNits];
-[AABCHistograms lastBrightnessUpdateNitsEDR];
-[AABCHistograms lastBrightnessUpdateTimestamp];
-[AABCHistograms luminanceHistLogNitsSDR:andNitsEDR:];
-[AABCHistograms pushIlluminance:weight:forAlsID:];
-[AABCHistograms setAutoBrightnessOn:];
-[AABCHistograms setBuiltInDisplay:];
-[AABCHistograms setEcoModeOn:];
-[AABCHistograms setFirstBrightnessUpdate:];
-[AABCHistograms setLastBrightnessUpdateNits:];
-[AABCHistograms setLastBrightnessUpdateTimestamp:];
```
