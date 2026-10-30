# `TUSoundPlayer`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _currentPlaying;
I _soundID;
@"NSObject<OS_dispatch_queue>" _queue;
@"TURepeatingActor" _repeatingActor;
@"TUConfigurationProvider" _configurationProvider;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"TURepeatingActor",R,N,V_repeatingActor) repeatingActor;
@property (TI,N,V_soundID) soundID;
@property (TB,N,V_currentPlaying) currentPlaying;
@property (T@"TUConfigurationProvider",R,N,V_configurationProvider) configurationProvider;
@property (TB,R,N,GisPlaying) playing;
```

## Instance methods

```
-[TUSoundPlayer soundID];
-[TUSoundPlayer init];
-[TUSoundPlayer isPlaying];
-[TUSoundPlayer queue];
-[TUSoundPlayer configurationProvider];
-[TUSoundPlayer setSoundID:];
-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:completion:];
-[TUSoundPlayer currentPlaying];
-[TUSoundPlayer isCurrentPlaying];
-[TUSoundPlayer isRepeatingActorPlaying];
-[TUSoundPlayer playSound:];
-[TUSoundPlayer playSound:iterations:pauseDurationBetweenIterations:];
-[TUSoundPlayer playSoundIndefinitely:pauseDurationBetweenIterations:];
-[TUSoundPlayer repeatingActor];
-[TUSoundPlayer setCurrentPlaying:];
-[TUSoundPlayer setIsCurrentPlaying:];
-[TUSoundPlayer stopPlaying];
```
