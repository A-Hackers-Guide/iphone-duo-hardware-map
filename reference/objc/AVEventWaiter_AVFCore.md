# `AVEventWaiter`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSCondition" _condition;
B _eventCompleted;
```

## Instance methods

```
-[AVEventWaiter init];
-[AVEventWaiter dealloc];
-[AVEventWaiter markEventAsCompleted];
-[AVEventWaiter waitUntilEventIsCompleted];
```
