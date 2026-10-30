# `/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`

iOS 27.2 dyld shared cache image. Version `2300.52.5.0.0`. **[DSC]**

## Linked libraries (15)

- `/System/Library/PrivateFrameworks/AFKUser.framework/AFKUser`
- `/System/Library/PrivateFrameworks/HID.framework/HID`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/usr/lib/libMobileGestalt.dylib`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`

## Objective-C: 29 classes, 6 protocols, 363 methods, 98 properties

### Class pages

Every class and protocol, with its methods: [`APToDCPEndpoint`](../objc/APToDCPEndpoint_BrightnessControl.md), [`BCAABConstraintsParser`](../objc/BCAABConstraintsParser_BrightnessControl.md), [`BCAppleBacklightBrtControl`](../objc/BCAppleBacklightBrtControl_BrightnessControl.md), [`BCAuroraParser`](../objc/BCAuroraParser_BrightnessControl.md), [`BCBrtControl`](../objc/BCBrtControl_BrightnessControl.md), [`BCBrtMonitor`](../objc/BCBrtMonitor_BrightnessControl.md), [`BCCPMSParser`](../objc/BCCPMSParser_BrightnessControl.md), [`BCDynamicSliderParser`](../objc/BCDynamicSliderParser_BrightnessControl.md), [`BCHIDBrtControl`](../objc/BCHIDBrtControl_BrightnessControl.md), [`BCNativeBrtControl`](../objc/BCNativeBrtControl_BrightnessControl.md), [`BCParserPlugin`](../objc/BCParserPlugin_BrightnessControl.protocol.md), [`BCRTPLCParser`](../objc/BCRTPLCParser_BrightnessControl.md), [`BCVirtualBrtControl`](../objc/BCVirtualBrtControl_BrightnessControl.md), [`CBAPEndpoint`](../objc/CBAPEndpoint_BrightnessControl.md), [`CBBootArgsConfigProvider`](../objc/CBBootArgsConfigProvider_BrightnessControl.md), [`CBChromaticCorectionParamsProtocol`](../objc/CBChromaticCorectionParamsProtocol_BrightnessControl.protocol.md), [`CBChromaticCorrectionParams`](../objc/CBChromaticCorrectionParams_BrightnessControl.md), [`CBCombinedConfigProvider`](../objc/CBCombinedConfigProvider_BrightnessControl.md), [`CBDictConfigProvider`](../objc/CBDictConfigProvider_BrightnessControl.md), [`CBDictSerializer`](../objc/CBDictSerializer_BrightnessControl.md), [`CBFloatArray`](../objc/CBFloatArray_BrightnessControl.md), [`CBFloatArray2D`](../objc/CBFloatArray2D_BrightnessControl.md), [`CBGammaContrastPreservationParams`](../objc/CBGammaContrastPreservationParams_BrightnessControl.md), [`CBIORegInterface`](../objc/CBIORegInterface_BrightnessControl.protocol.md), [`CBIORegistryParser`](../objc/CBIORegistryParser_BrightnessControl.md), [`CBIORegistryReader`](../objc/CBIORegistryReader_BrightnessControl.md), [`CBNopConfigurationProvider`](../objc/CBNopConfigurationProvider_BrightnessControl.md), [`CBPrimitiveConfigurationProvider`](../objc/CBPrimitiveConfigurationProvider_BrightnessControl.protocol.md), [`CBSerializable`](../objc/CBSerializable_BrightnessControl.protocol.md), [`CBUserDefaultsProvider`](../objc/CBUserDefaultsProvider_BrightnessControl.md), [`NSObject`](../objc/NSObject_BrightnessControl.protocol.md), [`VMBrtControl`](../objc/VMBrtControl_BrightnessControl.md)

### Classes

`APToDCPEndpoint`, `BCAABConstraintsParser`, `BCAppleBacklightBrtControl`, `BCAuroraParser`, `BCBrtControl`, `BCBrtMonitor`, `BCCPMSParser`, `BCDynamicSliderParser`, `BCHIDBrtControl`, `BCNativeBrtControl`, `BCRTPLCParser`, `BCVirtualBrtControl`, `CBAPEndpoint`, `CBBootArgsConfigProvider`, `CBChromaticCorrectionParams`, `CBCombinedConfigProvider`, `CBDictConfigProvider`, `CBDictSerializer`, `CBFloatArray`, `CBFloatArray2D`, `CBGammaContrastPreservationParams`, `CBIORegistryParser`, `CBIORegistryReader`, `CBNopConfigurationProvider`, `CBUserDefaultsProvider`, `NSArray`, `NSError`, `NSSet`, `VMBrtControl`

### Protocols

`BCParserPlugin`, `CBChromaticCorectionParamsProtocol`, `CBIORegInterface`, `CBPrimitiveConfigurationProvider`, `CBSerializable`, `NSObject`

### Properties

```
@property (T@"NSString",R,N) capabilitiesKey;
@property (Tf,R) luxActivationThreshold;
@property (Tf,R) nitsActivationThreshold;
@property (Tf,R) rampUpdateRate;
@property (Tf,R) rampUpDuration;
@property (Tf,R) rampUpLuxDeltaThreshold;
@property (Tf,R) rampDownDuration;
@property (Tf,R) rampDownLuxDeltaThreshold;
@property (Tf,R) aodRampDuration;
@property (TI,R) supported;
@property (T@"NSObject<OS_os_log>",&) logHandle;
@property (T@"NSDictionary",R) codingKeys;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",N,R) capabilitiesKey;
@property (TQ,R) registryID;
@property (T@"NSObject<OS_os_log>",R) logHandle;
@property (T@"NSObject<OS_dispatch_queue>",R) queue;
@property (T^{__CFUUID=},R) cfContainerID;
@property (T@"NSUUID",R,V_containerID) containerID;
@property (Td,R,V_maxNits) maxNits;
@property (Td,R,V_minNits) minNits;
@property (T@,R,C) ID;
@property (T@"NSDictionary",R,V_capabilities) capabilities;
@property (TB,V_multipleControlEnabled) multipleControlEnabled;
@property (TQ,R) hash;
@property (TB,R,V_isValid) isValid;
@property (T@?,C,V_displayInvalidHandler) displayInvalidHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,V_callbackQueue) callbackQueue;
@property (T@"NSString",N,R) capabilitiesKey;
@property (TQ,R,V_registryID) registryID;
@property (T@"NSString",R,V_bootargs) bootargs;
@property (T@"NSArray",R,V_luxTable) luxTable;
@property (T@"NSArray",R,V_nitsTable) nitsTable;
@property (T@"NSArray",R,V_strengthTable) strengthTable;
@property (T@"NSArray",R,V_rampBezierAnchors) rampBezierAnchors;
@property (Tf,R,V_luxActivationThreshold) luxActivationThreshold;
@property (Tf,R,V_nitsActivationThreshold) nitsActivationThreshold;
@property (Tf,R,V_rampUpdateRate) rampUpdateRate;
@property (Tf,R,V_rampUpDuration) rampUpDuration;
@property (Tf,R,V_rampUpLuxDeltaThreshold) rampUpLuxDeltaThreshold;
@property (Tf,R,V_rampDownDuration) rampDownDuration;
@property (Tf,R,V_rampDownLuxDeltaThreshold) rampDownLuxDeltaThreshold;
@property (Tf,R,V_aodRampDuration) aodRampDuration;
@property (TI,R,V_supported) supported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,V_codingKeys) codingKeys;
@property (T@"NSArray",R,V_providers) providers;
@property (T@"NSObject<OS_os_log>",&,VlogHandle) logHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,V_dict) dict;
@property (Tf,R,V_referenceWhiteBrightness) referenceWhiteBrightness;
@property (Tf,R,V_referenceLux) referenceLux;
@property (Tf,R,V_Lmin) Lmin;
@property (Tf,R,V_Lmax) Lmax;
@property (Tf,R,V_ambientFactor) ambientFactor;
@property (Tf,R,V_Bmin) Bmin;
@property (Tf,R,V_Bmax) Bmax;
@property (Tf,R,V_gammaMin) gammaMin;
@property (Tf,R,V_gammaMax) gammaMax;
@property (Tf,R,V_gcpFactorLow) gcpFactorLow;
@property (Tf,R,V_gcpFactorHigh) gcpFactorHigh;
@property (Tf,R,V_ASb) ASb;
@property (Tf,R,V_Kb) Kb;
@property (Tf,R,V_Kl) Kl;
@property (Tf,R,V_luxActivationThreshold) luxActivationThreshold;
@property (Tf,R,V_nitsActivationThreshold) nitsActivationThreshold;
@property (Tf,R,V_rampUpdateRate) rampUpdateRate;
@property (Tf,R,V_rampUpDuration) rampUpDuration;
@property (Tf,R,V_rampUpLuxDeltaThreshold) rampUpLuxDeltaThreshold;
@property (Tf,R,V_rampDownDuration) rampDownDuration;
@property (Tf,R,V_rampDownLuxDeltaThreshold) rampDownLuxDeltaThreshold;
@property (Tf,R,V_aodRampDuration) aodRampDuration;
@property (TI,R,V_supported) supported;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,V_codingKeys) codingKeys;
@property (T@"<CBIORegInterface>",R,V_reader) reader;
@property (TI,R,V_service) service;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_os_log>",&,V_logHandle) logHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (608)

```
lMinPanel
hw.targettype
Virtualization
aab-constraint-l0b
This class doesn't support setProperty
aurora-saturation-lux
CPMSNitSize
bdm-nits2
min_thresholds
pcc-table
blr-cct-warning
AuroraAllowEDR
callbackQueue is nil. Cannot call user supplied callback.
aab-constraint-emax-threshold
MinE2
min_fall_time
ds-max-rise-time
MaxNits
PAAMaxGain
aab-constraint-e2
aab-constraint-dark-light-thr
ds-max-factor-aab-off
 %f%s
aurora-upo-enter-multiplier
EDRExitSecondsPerStop
ProductID
IOGeneralInterest
This class doesn't support setting brightness
%@-lux-table
strengthTable
IOServiceTerminate
com.apple.BCHIDBrtControl.global
%@-ramp-update-rate
lmid-calibration-ignore
edm-supported
IOKitCode
min_factors_charger
BuiltIn
EDRReferenceHeadroom
IOPropertyMatch
luxActivationThreshold
gs-pab-index
Lmax
Unable to talk to hardware
ds-max-fall-time
_maxUser >= _minUser
use-cabal
PCCRampTime
brightness-nits
gs-b-min
Invalid Type
max_rise_time
BCAppleBacklightBrtControl(BuiltIn: %@)
com.apple.CoreBrightness
com.apple.BCBrtControl.HID
NotSupported
DeviceUsage
rampBezierAnchors
gs-i-threshold
grimaldi-lux-cap
%@-ramp-up-duration
PAARampDownMaxAPCEPoints
power-lut-data-xindex
gs-i-nominal
rtplc-nits-table-ref
gcp-ambient-max
referenceLux
AABConstraints
BCAppleBacklightBrtControl(DFR)
AmmlTableFactor
v16@?0@\"NSTimer\"8
aurora-cltm-threshold
aurora-exit-lux
rtplc-supported
gcpFactorHigh
multi_point
LmaxProduct
PCCTable
AmmlRelLux
BLRCCTWarning
backlight-control
paa-sdr-lut
CPMSAPLTable
gcp-gamma-min
%@-ramp-bezier-anchors
AuroraRampDownSpeed
ramp-down-min-tap-point
edr-aurora-seconds-per-stop
gcp-ramp-up-lux-threshold
gcp-reference-ambient-lux
E0a
v12@?0I8
E
CBAFKEndpointQueue
This class doesn't support create monitor with handler
vbatt-current
gcp-nits-min
ds-min-thresholds-charger
ds-min-factors-charger
truetone-strength
aurora-ramp-up-tap-points
ammolite
gcp-gamma-factor-high
gcp-gamma-max
gcp-ramp-down-duration
ambientFactor
Kb
EDRSecondsPerStopDefault
IOService
Invalid queue
AuroraUPOThreshold
Brightness_Scale
com.apple.BrightnessControl
nitsActivationThreshold
CPMSNitTable
i
luxTable
lMaxPanel
com.apple.BCBrtControl.Native
rtplc-apce-table
gcp-k-l
pivoting_L
max_thresholds_charger
edr-max-nits
aab-cap-l
[%@]
rampUpDuration
lMaxProduct
/System/Library/Display/%@/%d-rtplc.bin
rtplc-nits-table
utilites.mm
max
DCP
aab-cap-e
supports-cltm-aware-aurora
bdm-nits1
aab-constraint-max-slope
MinSlope
ds-min-fall-time
BCAppleBacklightBrtControl(DCP: \"%@\", BuiltIn: %@)
BatterySavingFeatures
thermal-mitigation-min-cap
Aurora
DeviceUsagePage
AuroraSessionLimit
SupportCLTMAwareAurora
PowerAwareAAB
HarmonyStrength
CBGammaContrastPreservation
bdm-lux1
block
v16@?0@\"BCBrtControl\"8
min_rise_time
ds-max-thresholds-charger
use-lut
pab-scaler-index
aml-rel-lux-thresh
role
BCBrtControl.m
%@-ramp-aod-duration
gcp-supported
gammaMin
aab-constraint-l2
com.apple.BCBrtControl.HID.BrtUpdate
MinNitsPanel
pcc-ramp-time
truetone-shift-a
com.apple.CoreBrightness.ChromaticCorrection
power-lut-vbatt-cur-nominal
luminance-ratio
B_input
DisplayVendorIndex
rampUpdateRate
 
CPMSAPLTarget
B_min
CBTwilight
gcp-ramp-up-duration
max_thresholds
lMidPanel
%@-strength-table
ramp-up-min-tap-point
power-lut-use-iofixed
CPMSVbattCurrentNominal
-[BCNativeBrtControl parseCapabilities:withDCPEndpoint:andError:]
lMaxReachable
aab-constraint-lmax
backlight-calibration-parameters
MinNits
AuroraIgnoreAPCE
-[CBAPEndpoint setProperty:property:]
%@-lux-activation-threshold
supported
rampDownDuration
lMinReachable
aml-table-factor
kern.bootargs
aurora-ramp-down-tap-points
min_factors
gcp-ambient-min
max_factors_charger
default
%@-supported
max_factors
pivoting_L_max
EDRSecondsPerStopRapid
aurora-enter-lux
aurora-allow-edr
Slope
gcp-ambient-factor
supports-gcp
Bmin
com.apple.BCBrtControl
power-lut-data-lut
CPMSWattNitConversion
IODeviceTree:/core-brightness
IODeviceTree
I_nominal
ds-max-rise-time-fast-thr
NitsToUserBrightnessTableForce
min
rampUpLuxDeltaThreshold
nitsTable
aurora-ramp-down-speed
CPMSAPLSize
aab-constraint-emax
ds-max-rise-time-fast
v8@?0
milliAmps2NitsScaleFactor
HarmonyShiftB
IOProviderClass
PAAEnergyConsumptionTarget
BCNativeBrtControl.mm
error != nil
max_rise_time_fast_threshold
com.apple.BCBrtControl.AppleBacklight
BrightnessMicroAmps
com.apple.CoreBrightness.CBAPEndpoint
v16@?0@\"NSError\"8
ds-max-thresholds
MidNits
IOHIDDevice
%@-%@
vector
edr-potential-headroom
ASb
IOKit error
max_factor_aab_off
backlight-marketing-table
-[BCBrtControl queue]
use-cpms-lut
I_threshold
plt-logic-version
Unknown error
aab-constraint-min-e2
energy-saving
AmmlAbsLux
Resource unavailable
AuroraRampDownTapAPCEPoints
IONameMatch
PowerAwareAuroraSDRLUT
Unable to copy the backlight calibration from the DCP
ds-min-thresholds
main
%@-ramp-down-lux-threshold
aurora-ignore-peak-apce
AuroraCLTMEnterMultiplier
Lmin
IOServiceFirstMatch
NitsToUserBrightnessTable
Default
DisplayID
pre-strobe-nit
aab-constraint-e0b
DynamicSlider
aurora-session-limit
dfr-brightness-control
ThermalMitigation
force-brightness-control
RTPLC
CBAmmolite
com.apple.VMBrtControl.global
gammaMax
%@-nits-table
rampDownLuxDeltaThreshold
dcpexpert-service
gcp-nits-max
aab-constraint-e0a
CBUserDefaultsProvider(%@)
PAARampUpMinAPCEPoints
com.apple.BCBrtControl.VirtualMachine
ds-max-factors-charger
DFR
CapabilitiesVersion
,
aurora-ignore-session-limit
edr-exit-seconds-per-stop
gcp-ramp-update-rate
aab-constraint-min-slope
thermal-mitigation
LmidProduct
aml-only-support
aurora-upo-threshold
AuroraAverageAPCESamplingRate
supports-rtplc
twilight
MaxSlope
user-accessible-max-nits
kUSBContainerID
This class doesn't support copy available controls
Could not construct
%@-nits-activation-threshold
pab_scaler_index
supports-edm
bdm-supported
aml-abs-lux-thresh
AmmlTable
This class doesn't support display service.
aurora-supported
aurora-ignore-apce
tw
_newBlockWrapper
ParavirtBrightnessCaps
dcp-brightness-node
MaxNitsEDR
DefaultWPType
%s-%d
supports-aurora
aurora-avrg-apce-sampling-rate
BDM
gcpFactorLow
BCAppleBacklightBrtControl.m
color-accuracy-index
aml-period
display-id
aml
gcp-ramp-down-lux-threshold
Bmax
aab-constraint-l0a
BrightnessMilliNits
LminProduct
value
_queue && \"Cannot proceed without dispatch queue\"
PAARampUpMaxAPCEPoints
PAARampDownMinAPCEPoints
semantic-lux-levels
Kl
MaxNitsPanel
%@-%llu
Returned calibration dictionary is of invalid type
lMinProduct
HarmonyShiftA
aml-table
VendorID
AuroraMaxNits
power-lut-data-y
RTPLCNitsTable
min_thresholds_charger
default-whitepoint-type
AuroraExitLux
AuroraSaturationLux
aodRampDuration
aurora-maximum-nits
gcp-as-b
Device doesn't support current operation
pre-strobe-dim-period
max-aurora-gain
v24@?0I8I12^v16
gcp-k-b
gcp-reference-white-nits
L0a
L
AuroraRampUpSpeed
edr-seconds-per-stop-rapid
CBGammaContrastPreservationParams.mm
EDRAuroraSecondsPerStop
-[CBAPEndpoint copyProperty:]
This class doesn't support setting brightness with this unit
loaded
com.apple.BCAppleBacklightBrtControl.global
AuroraEnterLux
AuroraIgnoreSessionLimit
ramp-up-max-tap-point
power-lut-data-x
RTPLCAPCETable
rtplc-apce-table-ref
IODisplayParameters
brightness
truetone-shift-b
AuroraCLTMThreshold
IsVirtualDevice
 %f%s 
aurora-ramp-up-speed
slider-mapping
-[BCAppleBacklightBrtControl initWithService:]
BCNativeBrtControl(DCP: \"%@\")
edr-seconds-per-stop
_newInterestBlockWrapper
AppleParavirtDisplay
gcp
referenceWhiteBrightness
max_rise_time_fast
%@-ramp-down-duration
AuroraMinNits
power-lut-data-yindex
bdm-lux2
CPMS
AmmlPeriod
AuroraRampUpTapAPCEPoints
CBAPToDCPService
RegistryID
ring-light-supported
%@-ramp-up-lux-threshold
AuroraUPOEnterMultiplier
gs-slope
I_input
DisplayContainerID
gcp-gamma-factor-low
ForcedAmmoliteSupport
DarkLightThreshold
ds-min-rise-time
AFKEndpointInterface
cpms-apl-column
AABCurveCap
-[CBGammaContrastPreservationParams initWithProvider:]
max_fall_time
_maxNits >= _minNits
ThermalMitigationMinCap
AuroraIgnorePeakAPCE
aurora-cltm-enter-multiplier
ramp-down-max-tap-point
use-modern-cpms
lMidProduct
edr-reference-headroom
backlight-marketing-table-force
EDRPotentialHeadroom
supports-%@
energy-consumption-target
Unable to setup IO notifications (error = %d)
Unable to read properties from backlight service.
weakSelf.displayInvalidHandler = %@
ERROR initializing CBAPEndpoint for service: %s
ERROR: unable to serialize outputBuffer: %@
Loaded %@ = %d from %@
RampAODDuration=%f
NitArray has invalid size: %lu (expected %d)
IOKit error registering for termination notification: %d
error: can't find brightness element - abort
%s:%s called for key: %s
Nits table is not monotonically increasing
NitsTableSize=%lu
StrengthTable[%lu]={%s}
cpmsparams = %{public}@
Successfully created DCP endpoint for role %@
BCAppleBacklightBrtControl: cleaning up monitor
Loaded %@ = %f from %@
RampUpLuxDeltaThreshold=%f
APL Array has wrong size: %lu (expected %d)
Received IOMFB service %d
Cannot obtain luminance-ratio
Failed to get registry ID
BCAppleBacklightBrtControl: got back service %u
capabilities = %{public}@
failed to retrieve registry ID for brightness service (%u)
Unable to load ramp up lux delta threshold
Failed to init DCP endpoint for role %@
EDR APT seconds per stop overridden in Defaults %@ = %@ \n
Display disconnected
Unable to load lux table
WattNitsConversion table has wrong size: %lu (expected %d)
VMBrtControl: Could not init for service %u
Unable to find display service.
Nits activation threshold is negative
Cannot get ParavirtBrightnessCaps
EDR POTENTIAL headroom retrieved from brightness node (%@)
Setting nits to %f
device removed
nits = %f, maxNits = %f, minNits = %f, nitsScaler = %f, exponent = %ld
0x%x, status: %d
The length of the plane name is >= %zu
LuxTable={%s}
Cannot load color accuracy index. Did the property name changed?
EDR seconds per stop default override to %f
Loading RTPLC from file. color-accuracy-index: %d
Could not encode value for setting property %s, value: %@\n
LuxActivationThreshold=%f
RampBezierAnchors={ %f, %f, %f }
Loading RTPLC from file
Cannot obtain vbatt-current
Disabling due to invalid config: %@(%f) >= %@(%f)
EDR REFERENCE headroom not found in brightness node - use default (%f)
Invalid queue
Unable to load strength table
Disabling due to invalid config: %@(%f) out of sensible range [1,2]
Display service found. Initializing dispService related properties
failed to set %f nits (%{public}@)
power-lut-data-x not found
Unable to find AppleParavirtDisplay service.
matching dictionary = %@
Property name is too long, %s\n
ERROR! enqueueCommandSync failed result:0x%x
Third ramp Bezier anchor is out of valid [0, 1] range
Ramp down lux delta threshold is negative
Unable to load nits table
Aurora ramp down tap points - unexpected number of values(%lu), expected 2
Error: failed to create port for display notifications
EDR APT seconds per stop default override to %f
First ramp Bezier anchor is out of valid [0, 1] range
Lux table has less than one element
VMBrtControl: changed capabilities for service %u (%@)
Disabling due to invalid config: %@(%f) out of sensible range [0.5,2]
EDR seconds per stop overridden in Defaults %@ = %@ \n
EDR EXIT seconds per stop overridden in Defaults %@ = %@ \n
Ramp up lux delta threshold is negative
Unable to register for property change notification (error = %d)
failed to create HID brightness device
dealloc
error: value (%f) out of bounds (%f-%f)
Data for setting property %s is too long, max payload %lu, needed size %lu\n
Lux activation threshold is negative
Unable to load ramp down duration
Nits table has less than one element
Not loading CPMS config because use-cpms-lut=%d
Unable to set CF properties (err = 0x%X)
Loaded %@ = %u from %@
NitsActivationThreshold=%f
BCNativeBrtControl: got back service %u (%@)
Cannot determine the associated DCP role
error: failed to retrieve backlight services (%u)
Parsed AAB cap curve: (e: %@, l: %@)
Unable to load AOD ramp duration
Strength table has wrong size %lu for lux table size %lu and nits table size %lu
Failed to get child iterator err = %#x (%s)
RampUpdateRate=%f
[GS] Index array size != nominal current array (%zu != %zu)
0x%x
Unable to create log handle
Incorrect number of ramp Bezier anchors
RampDownDuration=%f
StrengthTableSize=%lu
Lux table is not monotonically increasing
NitsTable={%s}
[GS] Index array size != Bmin array size (%zu != %zu)
VMBrtControl: failed to find matching AppleParavirtDisplay services
Unable to load ramp down lux delta threshold
Unable to find backlight service.
EDR EXIT seconds per stop default override to %f
error: %@ isn't IOKit compatible (string, number, array, dictionary)
failed to commit elements %{public}@
[GS] PAB index array not found
VMBrtControl: cleaning up monitor
Ramp down duration is negative
RampDownLuxDeltaThreshold=%f
[GS] Index array size != Ithr array size (%zu != %zu)
EDR Aurora seconds per stop overridden in Defaults %@ = %@ \n
retrying commit attempt No.%d
enqueueCommandSync
Ramp up duration is negative
LuxTableSize=%lu
[GS] Index array size != slope array size (%zu != %zu)
VMBrtControl: got back service %u (%@)
Disabling due to invalid config: %@(%f) <= 0
error: failed to retrieve current nits - defaulting to 150 nits
Failed to read brightness capabilities
Disabling due to invalid config: %@(%f) out of sensible range [0.5,1.5]
copyProperty(%@) = %@ (error: %@)
adding display service (0x%X)
error: invalid boost factor retrieved from IOMFB (%@)
Unable to load nits activation threshold
driver params = %{public}@
EDR Aurora seconds per stop default override to %f
Mismatched lengths of AAB cap curve arrays (e.count = %lu, l.count = %lu)
Unable to load lux activation threshold
power-lut-data-y not found
missing container ID. Defaulting to nil
Send command = 0x%x
Aurora ramp up tap points - unexpected number of values(%lu), expected 2
Cancelling BCNativeBrtMonitor...
BCNativeBrtControl: Could not init for service %u
display service message type 0x%X from service 0x%X
updated boost factor: %f
Unable to load ramp Bezier anchors
Second ramp Bezier anchor is out of valid [0, 1] range
Strength table element #%lu with value %f is out of the valid [0, 1] range
Failed to read brightness capabilities: %@
%s:%s called for key: %s, property: %@
Unable to load ramp update rate
Successfully loaded display-id: %u for role %@
IOMFB gave us NULL service
VMBrtControl: failed to get iterator err = %#x (%s)
Loading RTPLC from ioreg
Invalid service
setting nits %f X %f boost factor
WARNING: Property name is too long it will be truncated, %s -> %s\n
Response received from DCP: %@
AOD ramp duration is negative
Parser is null
RampUpDuration=%f
slider mapping retrieved from the backlight driver
EDR REFERENCE headroom retrieved from brightness node (%@)
Failed to create CoreBrightness default log
ERROR: %s sevice not found
Unable to load ramp up duration
%@ is not supported
artificial slider mapping
successfully created HID device (%{public}@) for service %ul
Send OOB command = 0x%x
Loaded %@ from %@
```
