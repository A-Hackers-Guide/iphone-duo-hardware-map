# `BWAudioFormat`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFormat`
- 2 instance variables, 2 properties, 7 instance methods, 5 class methods

## Instance variables

```
^{opaqueCMFormatDescription=} _audioFormatDescription;
@"NSDictionary" _avAudioSettings;
```

## Properties

```
@property (T^{opaqueCMFormatDescription=},R) audioFormatDescription;
@property (T@"NSDictionary",R) audioCompressionSBPOptions;
```

## Class methods

```
+[BWAudioFormat initialize];
+[BWAudioFormat compressionOptionTrimSampleBufferDurationsIsRequiredForAudioSettings:];
+[BWAudioFormat formatForAVAudioSettings:inputFormat:];
+[BWAudioFormat formatForAVAudioSettings:inputFormat:formatExtensions:];
+[BWAudioFormat formatWithAudioFormatDescription:];
```

## Instance methods

```
-[BWAudioFormat formatDescription];
-[BWAudioFormat debugDescription];
-[BWAudioFormat dealloc];
-[BWAudioFormat audioFormatDescription];
-[BWAudioFormat description];
-[BWAudioFormat mediaType];
-[BWAudioFormat audioCompressionSBPOptions];
```
