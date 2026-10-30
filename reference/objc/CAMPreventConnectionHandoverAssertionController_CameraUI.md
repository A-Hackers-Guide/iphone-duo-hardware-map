# `CAMPreventConnectionHandoverAssertionController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NFAssertion" __preventConnectionHandoverAssertion;
@"NSObject<OS_dispatch_queue>" __accessQueue;
```

## Properties

```
@property (T@"NFAssertion",&,N,S_setPreventConnectionHandoverAssertion:,V__preventConnectionHandoverAssertion) _preventConnectionHandoverAssertion;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__accessQueue) _accessQueue;
```

## Instance methods

```
-[CAMPreventConnectionHandoverAssertionController init];
-[CAMPreventConnectionHandoverAssertionController dealloc];
-[CAMPreventConnectionHandoverAssertionController _accessQueue];
-[CAMPreventConnectionHandoverAssertionController _preventConnectionHandoverAssertion];
-[CAMPreventConnectionHandoverAssertionController _releaseAssertionIfHeld];
-[CAMPreventConnectionHandoverAssertionController _requestAssertionIfUnheld];
-[CAMPreventConnectionHandoverAssertionController _setPreventConnectionHandoverAssertion:];
-[CAMPreventConnectionHandoverAssertionController releaseAssertionIfHeld];
-[CAMPreventConnectionHandoverAssertionController requestAssertionIfUnheld];
```
