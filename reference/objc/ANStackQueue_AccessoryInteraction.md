# `ANStackQueue`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _inbox;
@"NSMutableArray" _outbox;
```

## Instance methods

```
-[ANStackQueue init];
-[ANStackQueue dealloc];
-[ANStackQueue dequeue];
-[ANStackQueue isEmpty];
-[ANStackQueue peek];
-[ANStackQueue enqueue:];
-[ANStackQueue _transferInboxToOutboxIfNeeded];
```
