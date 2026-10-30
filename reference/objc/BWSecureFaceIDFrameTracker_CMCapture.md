# `BWSecureFaceIDFrameTracker`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _frameIdentifiers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _frameIdentifiersLock;
```

## Instance methods

```
-[BWSecureFaceIDFrameTracker init];
-[BWSecureFaceIDFrameTracker dealloc];
-[BWSecureFaceIDFrameTracker addFrameIdentifiersForFaceIDResult:];
-[BWSecureFaceIDFrameTracker removeFrameIdentifier:];
```
