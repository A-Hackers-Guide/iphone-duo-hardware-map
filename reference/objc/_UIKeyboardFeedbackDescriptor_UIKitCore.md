# `_UIKeyboardFeedbackDescriptor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
f _hapticIntensity;
f _hapticSharpness;
f _audioVolume;
@"NSString" _audioFile;
```

## Properties

```
@property (Tf,N,V_hapticIntensity) hapticIntensity;
@property (Tf,N,V_hapticSharpness) hapticSharpness;
@property (T@"NSString",C,N,V_audioFile) audioFile;
@property (Tf,N,V_audioVolume) audioVolume;
```

## Class methods

```
+[_UIKeyboardFeedbackDescriptor descriptorWithIntensity:sharpness:audio:volume:];
```

## Instance methods

```
-[_UIKeyboardFeedbackDescriptor audioVolume];
-[_UIKeyboardFeedbackDescriptor setAudioVolume:];
-[_UIKeyboardFeedbackDescriptor hapticIntensity];
-[_UIKeyboardFeedbackDescriptor hapticSharpness];
-[_UIKeyboardFeedbackDescriptor audioFile];
-[_UIKeyboardFeedbackDescriptor setAudioFile:];
-[_UIKeyboardFeedbackDescriptor setHapticIntensity:];
-[_UIKeyboardFeedbackDescriptor setHapticSharpness:];
```
