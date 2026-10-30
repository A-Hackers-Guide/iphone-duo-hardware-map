# `BWNodeInputMediaConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSString" _associatedAttachedMediaKey;
@"BWFormatRequirements" _formatRequirements;
i _passthroughMode;
B _conversionToPassthroughModeNeverAllowed;
i _retainedBufferCount;
i _delayedBufferCount;
i _indefinitelyHeldBufferCount;
```

## Properties

```
@property (T@"BWFormatRequirements",&,N,V_formatRequirements) formatRequirements;
@property (Ti,N,V_passthroughMode) passthroughMode;
@property (TB,N,V_conversionToPassthroughModeNeverAllowed) conversionToPassthroughModeNeverAllowed;
@property (Ti,N,V_retainedBufferCount) retainedBufferCount;
@property (Ti,N,V_delayedBufferCount) delayedBufferCount;
@property (Ti,N,V_indefinitelyHeldBufferCount) indefinitelyHeldBufferCount;
```

## Instance methods

```
-[BWNodeInputMediaConfiguration setFormatRequirements:];
-[BWNodeInputMediaConfiguration formatRequirements];
-[BWNodeInputMediaConfiguration setConversionToPassthroughModeNeverAllowed:];
-[BWNodeInputMediaConfiguration setPassthroughMode:];
-[BWNodeInputMediaConfiguration passthroughMode];
-[BWNodeInputMediaConfiguration conversionToPassthroughModeNeverAllowed];
-[BWNodeInputMediaConfiguration init];
-[BWNodeInputMediaConfiguration setRetainedBufferCount:];
-[BWNodeInputMediaConfiguration delayedBufferCount];
-[BWNodeInputMediaConfiguration dealloc];
-[BWNodeInputMediaConfiguration retainedBufferCount];
-[BWNodeInputMediaConfiguration setIndefinitelyHeldBufferCount:];
-[BWNodeInputMediaConfiguration indefinitelyHeldBufferCount];
-[BWNodeInputMediaConfiguration _setAssociatedAttachedMediaKey:];
-[BWNodeInputMediaConfiguration setDelayedBufferCount:];
```
