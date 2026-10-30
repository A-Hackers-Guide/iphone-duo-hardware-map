# `AVAudioNodeLock`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{optional<std::pair<std::unique_lock<std::recursive_mutex>, std::unique_lock<std::recursive_mutex>>>=""(?="__null_state_"c"__val_"{pair<std::unique_lock<std::recursive_mutex>, std::unique_lock<std::recursive_mutex>>="first"{unique_lock<std::recursive_mutex>="__m_"^{recursive_mutex}"__owns_"B}"second"{unique_lock<std::recursive_mutex>="__m_"^{recursive_mutex}"__owns_"B}})"__engaged_"B} _lock;
```

## Instance methods

```
-[AVAudioNodeLock dealloc];
-[AVAudioNodeLock unlock];
-[AVAudioNodeLock initWithLock:];
```
