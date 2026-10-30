# `CBDisplayModuleiOS`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBDisplayModule`
- Protocols: `CBHIDServiceProtocol`, `CBDisplayModeProtocol`, `CBAODProtocol`, `RTPLCRampRunner`
- 47 instance variables, 11 properties, 47 instance methods, 0 class methods

## Instance variables

```
f _trustedLux;
@"<CBBrightnessProxy>" _brtCtl;
@"CBDisplayContext" _context;
@"CBAurora" _aurora;
@"CBTwilight" _twilight;
@"CBAmmolite" _ammolite;
@"CBGammaContrastPreservation" _gcp;
@"CBIndicatorBrightnessModule" _indicatorBrightnessModule;
@"NSMutableArray" _subModules;
f _minNits;
f _midNits;
f _maxNits;
f _maxNitsEDR;
f _maxNitsPanel;
f _nitsSDR;
f _dynSliderCap;
f _currentCapToCA;
@"CBCPMSModule" _cpmsModule;
B _blrEnabled;
B _harmonyEnabled;
@"CBEDR" _edr;
@"CBSBIM" _sbim;
@"CBBrightDotMitigation" _bdm;
B _referenceModeIsActive;
@ _lastEDRHeadroomRequestFromCA;
Q _edrState;
B _brightnessControlEnabled;
@"CBAppliedCompensations" _appliedCompensations;
B _ecoMode;
B _dominoMode;
B _autoDimActive;
@"<CBPowerManagementClient>" _cbpm;
Q _transactionID;
@"NSMutableDictionary" _pendingCommitedTransactions;
@"CBFrameInfoProvider" _frameInfoProvider;
@"CBFrameStats" _frameStats;
@"CBRTPLCModule" _rtplc;
@"CBRampManager" _rampManager;
@"NSMutableArray" _cachedProperties;
@"NSMutableArray" _cachedKeys;
B _brightnessIsUnderAutoDimThresholdCurrentValue;
B _aliasingMitigationActive;
@"AABCHistograms" _analyticsHist;
q _analyticsPeriodicSender;
^{__Display=} _displayInternal;
q _displayMode;
@"<CBPrimitiveConfigurationProvider><CBBacklightConfigurationProvider>" _backlightParams;
```

## Properties

```
@property (TB,R,GisAODActive) AODActive;
@property (TB,R) useModernCPMS;
@property (T@"<CBPrimitiveConfigurationProvider><CBBacklightConfigurationProvider>",R,V_backlightParams) backlightParams;
@property (T^{__Display=},R,V_displayInternal) displayInternal;
@property (Tf,R,N) compensatedSDRNits;
@property (Tf,R,N) appliedCompensation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,V_displayMode) displayMode;
```

## Instance methods

```
-[CBDisplayModuleiOS handleCPMSNotification:withValue:];
-[CBDisplayModuleiOS copyPropertyForKey:];
-[CBDisplayModuleiOS handleDisplayModeUpdate:withDuration:callback:];
-[CBDisplayModuleiOS setProperty:forKey:];
-[CBDisplayModuleiOS handleEvent:];
-[CBDisplayModuleiOS addHIDServiceClient:];
-[CBDisplayModuleiOS className];
-[CBDisplayModuleiOS copyIdentifiers];
-[CBDisplayModuleiOS removeHIDServiceClient:];
-[CBDisplayModuleiOS copyPropertyInternalForKey:];
-[CBDisplayModuleiOS isAODActive];
-[CBDisplayModuleiOS backlightParams];
-[CBDisplayModuleiOS handleDisplayBrightnessUpdate:];
-[CBDisplayModuleiOS handleEDRHeadroomRequest:];
-[CBDisplayModuleiOS setDisplayMode:];
-[CBDisplayModuleiOS getAppliedHeadroom];
-[CBDisplayModuleiOS stop];
-[CBDisplayModuleiOS dealloc];
-[CBDisplayModuleiOS displayMode];
-[CBDisplayModuleiOS handleAttachedNotification];
-[CBDisplayModuleiOS start];
-[CBDisplayModuleiOS edrStateToString:];
-[CBDisplayModuleiOS sendNotificationForKey:withValue:];
-[CBDisplayModuleiOS updateBDMWithLux:];
-[CBDisplayModuleiOS startRTPLCRampFrom:to:withSpeed:];
-[CBDisplayModuleiOS updateEDRStateForEvent:andHeadroom:];
-[CBDisplayModuleiOS getCurrentHeadroom];
-[CBDisplayModuleiOS handleNotificationForKey:withProperty:];
-[CBDisplayModuleiOS setDisplayFactor:withPeriod:completion:];
-[CBDisplayModuleiOS edrIsEngaged];
-[CBDisplayModuleiOS newFrameStats];
-[CBDisplayModuleiOS updateSDRLimits:];
-[CBDisplayModuleiOS updatePanelLimit:];
-[CBDisplayModuleiOS initWithBacklight:display:andContext:];
-[CBDisplayModuleiOS initialiseSDR];
-[CBDisplayModuleiOS initialiseBrightDotMitigation];
-[CBDisplayModuleiOS handleAODStateUpdate:transitionTime:context:];
-[CBDisplayModuleiOS compensatedSDRNits];
-[CBDisplayModuleiOS initialiseEDR];
-[CBDisplayModuleiOS displayInternal];
-[CBDisplayModuleiOS copyPropertyForKey:withParameter:];
-[CBDisplayModuleiOS initialiseAurora];
-[CBDisplayModuleiOS useModernCPMS];
-[CBDisplayModuleiOS initWithBacklight:andContext:];
-[CBDisplayModuleiOS updatePresetState:];
-[CBDisplayModuleiOS getRequestedHeadroom];
-[CBDisplayModuleiOS appliedCompensation];
```
