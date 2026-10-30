# `MockPropertySet`

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
{function<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>="__f_"{__value_func<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>="__buf_"(type="__data"[24C])"__f_"^v}} _propertyValueHook;
```

## Properties

```
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propAvailableOffloadsInput) propAvailableOffloadsInput;
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propVoiceActivityState) propVoiceActivityState;
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propDSPGraphParam) propDSPGraphParam;
@property (T^{DSP_HAL_Mock_Property=^^?},N,V_propHasDSPGraphParam) propHasDSPGraphParam;
@property (T{function<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>={__value_func<unsigned int (const AudioObjectPropertyAddress &, unsigned int)>=(type=[24C])^v}},N,V_propertyValueHook) propertyValueHook;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MockPropertySet init];
-[MockPropertySet hasHostedDSPPropertyAtAddress:];
-[MockPropertySet getHostedDSPPropertyInfoArray];
-[MockPropertySet dealloc];
-[MockPropertySet getHostedDSPPropertyAtAddress:withQualifierData:];
-[MockPropertySet setHostedDSPPropertyAtAddress:withData:withQualifier:error:];
-[MockPropertySet configureForFeatureFlag:];
-[MockPropertySet configureForProcessor:];
-[MockPropertySet getVoiceActivityState];
-[MockPropertySet propAvailableOffloadsInput];
-[MockPropertySet propDSPGraphParam];
-[MockPropertySet propHasDSPGraphParam];
-[MockPropertySet propVoiceActivityState];
-[MockPropertySet propertyValueHook];
-[MockPropertySet setPropAvailableOffloadsInput:];
-[MockPropertySet setPropDSPGraphParam:];
-[MockPropertySet setPropHasDSPGraphParam:];
-[MockPropertySet setPropVoiceActivityState:];
-[MockPropertySet setPropertyValueHook:];
-[MockPropertySet toggleVoiceActivityAndNotify];
```
