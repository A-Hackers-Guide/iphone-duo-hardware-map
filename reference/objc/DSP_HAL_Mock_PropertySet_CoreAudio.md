# `DSP_HAL_Mock_PropertySet`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_PropertySet`
- 5 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
^{DSP_HAL_Mock_Property=^^?} _propAvailableOffloadsInput;
^{DSP_HAL_Mock_Property=^^?} _propVoiceActivityState;
^{DSP_HAL_Mock_Property=^^?} _propDSPGraphParam;
^{DSP_HAL_Mock_Property=^^?} _propHasDSPGraphParam;
{function<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>="__f_"{__value_func<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>="__buf_"(type="__data"[24C])"__f_"^v}} _propertyUpdater;
```

## Properties

```
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propAvailableOffloadsInput) propAvailableOffloadsInput;
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propVoiceActivityState) propVoiceActivityState;
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propDSPGraphParam) propDSPGraphParam;
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propHasDSPGraphParam) propHasDSPGraphParam;
@property (T{function<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>={__value_func<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>=(type=[24C])^v}},N,V_propertyUpdater) propertyUpdater;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSP_HAL_Mock_PropertySet init];
-[DSP_HAL_Mock_PropertySet hasHostedDSPPropertyAtAddress:];
-[DSP_HAL_Mock_PropertySet getHostedDSPPropertyInfoArray];
-[DSP_HAL_Mock_PropertySet dealloc];
-[DSP_HAL_Mock_PropertySet getHostedDSPPropertyAtAddress:withQualifierData:];
-[DSP_HAL_Mock_PropertySet setHostedDSPPropertyAtAddress:withData:withQualifier:error:];
-[DSP_HAL_Mock_PropertySet propertyUpdater];
-[DSP_HAL_Mock_PropertySet configureForFeatureFlag:];
-[DSP_HAL_Mock_PropertySet configureForProcessor:];
-[DSP_HAL_Mock_PropertySet getVoiceActivityState];
-[DSP_HAL_Mock_PropertySet propAvailableOffloadsInput];
-[DSP_HAL_Mock_PropertySet propDSPGraphParam];
-[DSP_HAL_Mock_PropertySet propHasDSPGraphParam];
-[DSP_HAL_Mock_PropertySet propVoiceActivityState];
-[DSP_HAL_Mock_PropertySet setPropAvailableOffloadsInput:];
-[DSP_HAL_Mock_PropertySet setPropDSPGraphParam:];
-[DSP_HAL_Mock_PropertySet setPropHasDSPGraphParam:];
-[DSP_HAL_Mock_PropertySet setPropVoiceActivityState:];
-[DSP_HAL_Mock_PropertySet setPropertyUpdater:];
-[DSP_HAL_Mock_PropertySet toggleVoiceActivityAndNotify];
```
