# `DSP_HostCallbacks_ADM`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_HostCallbacks`
- 3 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
^v _owner;
{shared_ptr<std::shared_mutex>="__ptr_"^{shared_mutex}"__cntrl_"^{__shared_weak_count}} _mxCallbacks;
{HostCallbacks="propertyChangeCallback_"{function<void (AudioObjectPropertyAddress)>="__f_"{__value_func<void (AudioObjectPropertyAddress)>="__buf_"(type="__data"[24C])"__f_"^v}}} _hostCallbacks;
```

## Properties

```
@property (T{HostCallbacks={function<void (AudioObjectPropertyAddress)>={__value_func<void (AudioObjectPropertyAddress)>=(type=[24C])^v}}},N,V_hostCallbacks) hostCallbacks;
@property (T^v,N,V_owner) owner;
@property (T{shared_ptr<std::shared_mutex>=^{shared_mutex}^{__shared_weak_count}},N,V_mxCallbacks) mxCallbacks;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSP_HostCallbacks_ADM owner];
-[DSP_HostCallbacks_ADM setOwner:];
-[DSP_HostCallbacks_ADM setMxCallbacks:];
-[DSP_HostCallbacks_ADM clearCallbacks];
-[DSP_HostCallbacks_ADM hostCallbacks];
-[DSP_HostCallbacks_ADM mxCallbacks];
-[DSP_HostCallbacks_ADM notifyClientsOfCustomPropertyChange:];
-[DSP_HostCallbacks_ADM setHostCallbacks:];
```
