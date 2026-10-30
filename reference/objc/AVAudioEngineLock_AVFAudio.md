# `AVAudioEngineLock`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{optional<std::unique_lock<std::recursive_mutex>>=""(?="__null_state_"c"__val_"{unique_lock<std::recursive_mutex>="__m_"^{recursive_mutex}"__owns_"B})"__engaged_"B} _lock;
```

## Instance methods

```
-[AVAudioEngineLock dealloc];
-[AVAudioEngineLock unlock];
-[AVAudioEngineLock initWithLock:];
```
