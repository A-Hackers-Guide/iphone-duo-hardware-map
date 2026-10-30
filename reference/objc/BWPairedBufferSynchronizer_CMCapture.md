# `BWPairedBufferSynchronizer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 8 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
^{opaqueCMSimpleQueue=} _primarySampleBufferQueue;
^{opaqueCMSimpleQueue=} _secondarySampleBufferQueue;
^{opaqueCMSampleBuffer=} _secondaryFallbackSampleBuffer;
B _secondaryStreamComplete;
```

## Properties

```
@property (TB,N,V_secondaryStreamComplete) secondaryStreamComplete;
```

## Class methods

```
+[BWPairedBufferSynchronizer initialize];
```

## Instance methods

```
-[BWPairedBufferSynchronizer flush];
-[BWPairedBufferSynchronizer dealloc];
-[BWPairedBufferSynchronizer initWithCapacity:];
-[BWPairedBufferSynchronizer addPrimaryBuffer:];
-[BWPairedBufferSynchronizer addSecondaryBuffer:];
-[BWPairedBufferSynchronizer getSynchronizedBufferPair];
-[BWPairedBufferSynchronizer secondaryStreamComplete];
-[BWPairedBufferSynchronizer setSecondaryStreamComplete:];
```
