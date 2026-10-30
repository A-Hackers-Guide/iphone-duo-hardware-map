# `_UIMotionEffectEventProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 7 instance methods, 4 class methods

## Instance variables

```
@"<_UIMotionEffectEventConsumer>" _consumer;
```

## Properties

```
@property (T@"<_UIMotionEffectEventConsumer>",V_consumer) consumer;
```

## Class methods

```
+[_UIMotionEffectEventProvider _supportsPerScreenInstantiation];
+[_UIMotionEffectEventProvider shouldLogEvents];
+[_UIMotionEffectEventProvider fastUpdateIntervalForLogs];
+[_UIMotionEffectEventProvider slowUpdateIntervalForLogs];
```

## Instance methods

```
-[_UIMotionEffectEventProvider currentEvent];
-[_UIMotionEffectEventProvider setConsumer:];
-[_UIMotionEffectEventProvider consumer];
-[_UIMotionEffectEventProvider setSlowUpdatesEnabled:];
-[_UIMotionEffectEventProvider startGeneratingEvents];
-[_UIMotionEffectEventProvider stopGeneratingEvents];
-[_UIMotionEffectEventProvider wantsSynchronizedUpdates];
```
