# `AVAudioSharedBufferToken`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
{mach_port="m_mach_port"I} taskToken;
{ObjectRef<__IOSurface *>="mCFObject"^{__IOSurface}} surface;
```

## Class methods

```
+[AVAudioSharedBufferToken supportsSecureCoding];
```

## Instance methods

```
-[AVAudioSharedBufferToken surface];
-[AVAudioSharedBufferToken encodeWithCoder:];
-[AVAudioSharedBufferToken initWithCoder:];
-[AVAudioSharedBufferToken initWithSurface:taskToken:];
-[AVAudioSharedBufferToken surfaceXPCType];
-[AVAudioSharedBufferToken taskToken];
-[AVAudioSharedBufferToken taskTokenXPCType];
```
