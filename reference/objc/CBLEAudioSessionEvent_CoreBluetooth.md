# `CBLEAudioSessionEvent`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _eventType;
@"CBLEAudioSessionInfo" _sessionInfo;
@"NSNumber" _updatedValue;
@"NSError" _error;
```

## Properties

```
@property (T@"CBLEAudioSessionInfo",C,N,V_sessionInfo) sessionInfo;
@property (T@"NSNumber",C,N,V_updatedValue) updatedValue;
@property (T@"NSError",C,N,V_error) error;
@property (Tq,R,N,V_eventType) eventType;
```

## Instance methods

```
-[CBLEAudioSessionEvent setError:];
-[CBLEAudioSessionEvent eventType];
-[CBLEAudioSessionEvent sessionInfo];
-[CBLEAudioSessionEvent setSessionInfo:];
-[CBLEAudioSessionEvent error];
-[CBLEAudioSessionEvent setUpdatedValue:];
-[CBLEAudioSessionEvent updatedValue];
-[CBLEAudioSessionEvent initWithEventType:withError:];
```
