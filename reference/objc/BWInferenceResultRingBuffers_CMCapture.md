# `BWInferenceResultRingBuffers`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _lock;
@"NSMutableDictionary" _rings;
```

## Instance methods

```
-[BWInferenceResultRingBuffers init];
-[BWInferenceResultRingBuffers dealloc];
-[BWInferenceResultRingBuffers bufferingStatsForType:firstOut:lastOut:countOut:];
-[BWInferenceResultRingBuffers insertInferenceResultsFromSampleBuffer:];
-[BWInferenceResultRingBuffers retrieveInferencesForType:beginning:until:];
-[BWInferenceResultRingBuffers setupRingBuffer:inferencesOfType:];
```
