# `_UIPencilEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- Protocols: `BSDescriptionStreaming`
- 12 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
Q _senderID;
q _subtype;
@"<BSInvalidatable>" _stateCaptureToken;
@"UINotificationFeedbackGenerator" _doubleTapNotificationGenerator;
{?="requestedSystemFocusForUpdatedFallbackInteraction"b1} _eventFlags;
Q _phase;
d _normalizedForceVelocity;
@"NSHashTable" _registeredInteractions;
@"NSCountedSet" _countedWindowPointersWithInteractionsAffectingSystemFocus;
@"NSMapTable" _deliveryRecordsByDescriptor;
@"_UIGenericGestureHIDEventDescriptor" _continuousEventDescriptorForDispatch;
@"NSArray" _interactionsForDispatch;
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
-[_UIPencilEvent _cleanupAfterDispatch];
-[_UIPencilEvent _setHIDEvent:];
-[_UIPencilEvent subtype];
-[_UIPencilEvent _cloneEvent];
-[_UIPencilEvent debugDescription];
-[_UIPencilEvent dealloc];
-[_UIPencilEvent _init];
-[_UIPencilEvent succinctDescription];
-[_UIPencilEvent type];
-[_UIPencilEvent description];
-[_UIPencilEvent appendDescriptionToStream:];
```
