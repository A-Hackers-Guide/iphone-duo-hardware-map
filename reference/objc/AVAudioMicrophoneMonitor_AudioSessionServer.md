# `AVAudioMicrophoneMonitor`

- Image: [`/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`](../userland/System__Library__PrivateFrameworks__AudioSessionServer.framework__AudioSessionServer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVAudioMicrophoneMonitor`
- 2 instance variables, 4 properties, 2 instance methods, 1 class methods

## Instance variables

```
{set<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>, std::less<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>, std::allocator<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>>="__tree_"{__tree<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>, std::less<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>, std::allocator<std::pair<AVAudioMicrophoneMonitorClientType, unsigned long long>>>="__begin_node_"^v""{?="__end_node_"{__tree_end_node<std::__tree_node_base<void *> *>="__left_"^v}}""{?="__size_"Q}}} _clientsWithMicEnabled;
{mutex="__m_"{_opaque_pthread_mutex_t="__sig"q"__opaque"[56c]}} _monitorMutex;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVAudioMicrophoneMonitor sharedInstance];
```

## Instance methods

```
-[AVAudioMicrophoneMonitor init];
-[AVAudioMicrophoneMonitor setState:clientType:clientID:clientDescription:];
```
