# `BWSubjectRelightingCalculatorResult`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _relightingRequired;
f _curveParameter;
@"NSObject<OS_dispatch_group>" _group;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (TB,R) relightingRequired;
@property (Tf,R) curveParameter;
```

## Instance methods

```
-[BWSubjectRelightingCalculatorResult init];
-[BWSubjectRelightingCalculatorResult dealloc];
-[BWSubjectRelightingCalculatorResult _completeWithRelightingRequired:curveParameter:];
-[BWSubjectRelightingCalculatorResult curveParameter];
-[BWSubjectRelightingCalculatorResult relightingRequired];
-[BWSubjectRelightingCalculatorResult waitForResult];
```
