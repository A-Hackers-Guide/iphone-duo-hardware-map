# `_UIHIDPathCollection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _pathsById;
{CGPoint="x"d"y"d} _position;
I _buttonMask;
Q _machTimestamp;
C _locus;
^{__IOHIDEvent=} _hidEvent;
I _fallbackContextId;
Q _digitizerSenderID;
```

## Properties

```
@property (TQ,N,V_digitizerSenderID) digitizerSenderID;
@property (TQ,R,N) pathCount;
@property (TI,N,V_fallbackContextId) fallbackContextId;
```

## Instance methods

```
-[_UIHIDPathCollection init];
-[_UIHIDPathCollection dealloc];
-[_UIHIDPathCollection _collectionMask];
-[_UIHIDPathCollection _createCollectionEventForEvent:];
-[_UIHIDPathCollection addPath:];
-[_UIHIDPathCollection digitizerSenderID];
-[_UIHIDPathCollection fallbackContextId];
-[_UIHIDPathCollection hasPathWithId:];
-[_UIHIDPathCollection hidEventFromCurrentState];
-[_UIHIDPathCollection pathCount];
-[_UIHIDPathCollection pathWithId:];
-[_UIHIDPathCollection pathsInPhase:];
-[_UIHIDPathCollection pathsTouching];
-[_UIHIDPathCollection removePath:];
-[_UIHIDPathCollection setDigitizerSenderID:];
-[_UIHIDPathCollection setFallbackContextId:];
-[_UIHIDPathCollection updateEventTimestamp:];
-[_UIHIDPathCollection updateWithHIDEvent:];
```
