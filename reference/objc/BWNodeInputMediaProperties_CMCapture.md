# `BWNodeInputMediaProperties`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSString" _associatedAttachedMediaKey;
@"BWNodeInput" _owningNodeInput;
@"BWFormat" _resolvedFormat;
@"BWFormat" _liveFormat;
```

## Properties

```
@property (T@"BWFormat",&,N) resolvedFormat;
@property (T@"BWVideoFormat",R,N) resolvedVideoFormat;
@property (T@"BWFormat",R,N,V_liveFormat) liveFormat;
@property (T@"BWVideoFormat",R,N) liveVideoFormat;
```

## Instance methods

```
-[BWNodeInputMediaProperties liveFormat];
-[BWNodeInputMediaProperties dealloc];
-[BWNodeInputMediaProperties resolvedFormat];
-[BWNodeInputMediaProperties setResolvedFormat:];
-[BWNodeInputMediaProperties liveVideoFormat];
-[BWNodeInputMediaProperties setLiveFormat:];
-[BWNodeInputMediaProperties resolvedVideoFormat];
-[BWNodeInputMediaProperties _setOwningNodeInput:associatedAttachedMediaKey:];
```
