# `NeuralNetCache`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/libAudioDSP.dylib`](../userland/System__Library__Frameworks__AudioToolbox.framework__libAudioDSP.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
{unique_ptr<NeuralNetImpl, std::default_delete<NeuralNetImpl>>=""{?="__ptr_"^{NeuralNetImpl}}} _impl;
I _batchSize;
```

## Class methods

```
+[NeuralNetCache sharedCache];
```

## Instance methods

```
-[NeuralNetCache batchSize];
-[NeuralNetCache impl];
-[NeuralNetCache initWithImpl:batchSize:];
```
