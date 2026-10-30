# `_UIFocusActiveSceneObserver_Classic`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIFocusActiveSceneObserver`
- Protocols: `BKSHIDEventDeliveryPolicyObserving`
- 2 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _hidObserverMapTable;
{?="supportsHIDUpdates"b1} _flags;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusActiveSceneObserver_Classic observerDeliveryPolicyDidChange:];
-[_UIFocusActiveSceneObserver_Classic _keyWindowDidChangeNotification:];
-[_UIFocusActiveSceneObserver_Classic _initWithScene:];
-[_UIFocusActiveSceneObserver_Classic _resolvedDisplayForWindow:];
-[_UIFocusActiveSceneObserver_Classic _addDeliveryObserverForWindow:];
-[_UIFocusActiveSceneObserver_Classic dealloc];
-[_UIFocusActiveSceneObserver_Classic stopMonitoringContextChangesForWindow:];
-[_UIFocusActiveSceneObserver_Classic _windowDidDetachContext:];
-[_UIFocusActiveSceneObserver_Classic _removeDeliverObserverForWindow:];
-[_UIFocusActiveSceneObserver_Classic beginMonitoringContextChangesForWindow:];
-[_UIFocusActiveSceneObserver_Classic isActive];
-[_UIFocusActiveSceneObserver_Classic descriptionBuilder];
-[_UIFocusActiveSceneObserver_Classic _windowDidAttachContext:];
-[_UIFocusActiveSceneObserver_Classic _screenUUIDDidChangeNotification:];
```
