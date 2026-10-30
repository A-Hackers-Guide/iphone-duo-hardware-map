# `DSP_HostCallbacks`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_HostCallbacks`
- 3 instance variables, 7 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{DSP_Host_IOProcessor=^^?} _owner;
{function<void (const DSP_Host_Types::MutationRequestConfiguration &)>="__f_"{__value_func<void (const DSP_Host_Types::MutationRequestConfiguration &)>="__buf_"(type="__data"[24C])"__f_"^v}} _mutationRequestListener;
{function<void (const AudioObjectPropertyAddress &)>="__f_"{__value_func<void (const AudioObjectPropertyAddress &)>="__buf_"(type="__data"[24C])"__f_"^v}} _propertyChangeListener;
```

## Properties

```
@property (T{function<void (const DSP_Host_Types::MutationRequestConfiguration &)>={__value_func<void (const DSP_Host_Types::MutationRequestConfiguration &)>=(type=[24C])^v}},N,V_mutationRequestListener) mutationRequestListener;
@property (T{function<void (const AudioObjectPropertyAddress &)>={__value_func<void (const AudioObjectPropertyAddress &)>=(type=[24C])^v}},N,V_propertyChangeListener) propertyChangeListener;
@property (T^{DSP_Host_IOProcessor=^^?},N,V_owner) owner;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSP_HostCallbacks owner];
-[DSP_HostCallbacks setOwner:];
-[DSP_HostCallbacks mutationRequestListener];
-[DSP_HostCallbacks notifyClientsOfCustomPropertyChange:];
-[DSP_HostCallbacks propertyChangeListener];
-[DSP_HostCallbacks setMutationRequestListener:];
-[DSP_HostCallbacks setPropertyChangeListener:];
```
