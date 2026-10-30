# `TUAudioController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _modifyingStateLock;
```

## Properties

```
@property (T{os_unfair_lock_s=I},N,V_modifyingStateLock) modifyingStateLock;
```

## Instance methods

```
-[TUAudioController init];
-[TUAudioController _acquireLock];
-[TUAudioController _releaseLock];
-[TUAudioController _requestUpdatedValueWithBlock:object:isRequestingPointer:forceNewRequest:scheduleTimePointer:notificationString:notificationUserInfo:queue:];
-[TUAudioController _requestUpdatedValueWithBlock:object:isRequestingPointer:forceNewRequest:scheduleTimePointer:notificationString:queue:];
-[TUAudioController modifyingStateLock];
-[TUAudioController setModifyingStateLock:];
```
