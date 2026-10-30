# `_UIKBRTTouchHistory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _history;
{CGPoint="x"d"y"d} _historyOffset;
d _lastDecayTime;
B _isLeftHand;
```

## Properties

```
@property (T{CGPoint=dd},R,N) historyOffset;
@property (TB,N,V_isLeftHand) isLeftHand;
@property (TB,R,N) hasHistory;
@property (Td,R,N) lastTime;
```

## Instance methods

```
-[_UIKBRTTouchHistory dealloc];
-[_UIKBRTTouchHistory reset];
-[_UIKBRTTouchHistory copyWithZone:];
-[_UIKBRTTouchHistory _decayHistoryToSize:];
-[_UIKBRTTouchHistory _sortHistory];
-[_UIKBRTTouchHistory _updateOffset];
-[_UIKBRTTouchHistory addInfo:];
-[_UIKBRTTouchHistory adjustHistoryOffset:];
-[_UIKBRTTouchHistory clearHistory];
-[_UIKBRTTouchHistory containsInfo:];
-[_UIKBRTTouchHistory decayHistory];
-[_UIKBRTTouchHistory hasHistory];
-[_UIKBRTTouchHistory historyOffset];
-[_UIKBRTTouchHistory initWithIsLeftHand:];
-[_UIKBRTTouchHistory isLeftHand];
-[_UIKBRTTouchHistory lastTime];
-[_UIKBRTTouchHistory removeInfo:];
-[_UIKBRTTouchHistory setIsLeftHand:];
```
