# `_UIMotionEffectCoreMotionEventProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIMotionEffectEventProvider`
- 2 instance variables, 0 properties, 6 instance methods, 4 class methods

## Instance variables

```
@"CMMotionManager" _motionManager;
@"NSOperationQueue" _handlerQueue;
```

## Class methods

```
+[_UIMotionEffectCoreMotionEventProvider _supportsPerScreenInstantiation];
+[_UIMotionEffectCoreMotionEventProvider shouldLogEvents];
+[_UIMotionEffectCoreMotionEventProvider fastUpdateIntervalForLogs];
+[_UIMotionEffectCoreMotionEventProvider slowUpdateIntervalForLogs];
```

## Instance methods

```
-[_UIMotionEffectCoreMotionEventProvider currentEvent];
-[_UIMotionEffectCoreMotionEventProvider dealloc];
-[_UIMotionEffectCoreMotionEventProvider initWithMotionManager:];
-[_UIMotionEffectCoreMotionEventProvider setSlowUpdatesEnabled:];
-[_UIMotionEffectCoreMotionEventProvider startGeneratingEvents];
-[_UIMotionEffectCoreMotionEventProvider stopGeneratingEvents];
```
