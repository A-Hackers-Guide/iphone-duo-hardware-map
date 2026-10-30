# `AVAudioTimeObserverImpl`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioTimeObserver`
- 1 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<avas::client::DeviceTimeClient>="__ptr_"^{DeviceTimeClient}"__cntrl_"^{__shared_weak_count}} _deviceTimeClient;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AVAudioTimeObserverImpl currentTime];
-[AVAudioTimeObserverImpl currentPresentationTime];
-[AVAudioTimeObserverImpl currentLatency];
-[AVAudioTimeObserverImpl deviceTimeClient];
-[AVAudioTimeObserverImpl initWithDeviceTimeClient:];
-[AVAudioTimeObserverImpl isLatencyDynamic];
```
