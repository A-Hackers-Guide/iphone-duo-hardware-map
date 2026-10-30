# `AVAudioSessionManager`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 4 instance methods, 1 class methods

## Instance variables

```
{synchronized<(anonymous namespace)::ManagerState, caulk::mach::unfair_lock, caulk::empty_atomic_interface<(anonymous namespace)::ManagerState>>="mMutex"{unfair_lock="m_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}}"mObject"{ManagerState="mServerPIDs"{circular_buffer<int, std::allocator<int>>="m_buff"^i"m_end"^i"m_first"^i"m_last"^i"m_size"Q}}} _state;
B _processAudioMuted;
```

## Properties

```
@property (TB,R,N,GisProcessAudioMuted,V_processAudioMuted) processAudioMuted;
```

## Class methods

```
+[AVAudioSessionManager defaultManager];
```

## Instance methods

```
-[AVAudioSessionManager init];
-[AVAudioSessionManager triggerMediaServicesResetNotifications:daemonName:];
-[AVAudioSessionManager trackDaemonPID:];
-[AVAudioSessionManager isProcessAudioMuted];
```
