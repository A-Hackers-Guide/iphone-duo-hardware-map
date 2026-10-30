# `ATIOBinding`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 1 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
{shared_ptr<const AT::IOBinding::Impl>="__ptr_"^{Impl}"__cntrl_"^{__shared_weak_count}} mImpl;
```

## Properties

```
@property (T@"AVAudioSession",R,&,N) session;
@property (TI,R,N) sessionID;
@property (T@"NSString",R,&,N) deviceUID;
@property (TI,R,N) deviceID;
@property (T{ATIsolatedAudioUseCaseID=I},R,N) useCaseID;
```

## Class methods

```
+[ATIOBinding supportsSecureCoding];
```

## Instance methods

```
-[ATIOBinding deviceUID];
-[ATIOBinding initWithImpl:];
-[ATIOBinding sessionID];
-[ATIOBinding initWithDeviceID:];
-[ATIOBinding deviceID];
-[ATIOBinding encodeWithCoder:];
-[ATIOBinding description];
-[ATIOBinding initWithCoder:];
-[ATIOBinding session];
-[ATIOBinding isEqual:];
-[ATIOBinding initWithAudioSession:];
-[ATIOBinding initWithAudioSessionID:];
-[ATIOBinding initWithDeviceUID:];
-[ATIOBinding initWithUseCaseID:];
-[ATIOBinding useCaseID];
```
