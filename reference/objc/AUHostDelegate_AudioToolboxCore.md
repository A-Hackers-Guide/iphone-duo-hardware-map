# `AUHostDelegate`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AUAudioUnitHostProtocol`
- 2 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" mParameterQueue;
@"AUAudioUnit" _audioUnit;
```

## Properties

```
@property (T@"AUAudioUnit",W,N,V_audioUnit) audioUnit;
```

## Instance methods

```
-[AUHostDelegate init];
-[AUHostDelegate MIDICIProfileChanged:channel:profile:enabled:];
-[AUHostDelegate audioUnit];
-[AUHostDelegate propertiesChanged:];
-[AUHostDelegate setAudioUnit:];
-[AUHostDelegate speechSynthesisMetadataAvailable:speechRequest:];
-[AUHostDelegate syncParameter:value:extOriginator:hostTime:eventType:];
```
